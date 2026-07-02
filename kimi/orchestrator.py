#!/usr/bin/env python3
"""
Orquestador de dos agentes Kimi para escribir un paper de investigación matemática.

Roles:
- investigador: escribe y corrige el paper.
- jefe_research: audita el borrador y genera sub-tareas concretas.

El orquestador alterna entre ambos roles, guarda el estado en mailbox/state.json
y frena a los 40 loops o cuando el jefe emite veredicto APROBADO.
"""

import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROLES = BASE / "roles"
MAILBOX = BASE / "mailbox"
PAPER = BASE / "paper"
LOGS = BASE / "logs"

PROMPT_INICIADOR = BASE / "PROMPT_INICIADOR.md"
CONFIG = BASE / "config.json"
STATE = MAILBOX / "state.json"
DRAFT = PAPER / "draft.md"
JEFE_RESPONSE = MAILBOX / "jefe_response.md"
INVESTIGADOR_RESPONSE = MAILBOX / "investigador_response.md"


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def save_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def load_config() -> dict:
    default = {
        "max_loops": 40,
        "model": None,
        "work_dir": str(BASE),
        "yolo": True,
        "quiet": True,
        "thinking": False,
        "dry_run": False,
        "use_sessions": True,
        "session_investigador": None,
        "session_jefe": None,
        "subprocess_timeout": 600,
    }
    if CONFIG.exists():
        default.update(json.loads(CONFIG.read_text(encoding="utf-8")))

    # Generar IDs de sesión persistentes por rol si no existen.
    if default.get("use_sessions"):
        updated = False
        for key in ("session_investigador", "session_jefe"):
            if not default.get(key):
                default[key] = str(uuid.uuid4())
                updated = True
        if updated:
            CONFIG.write_text(
                json.dumps(default, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
    return default


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {
        "loop": 1,
        "turno": "investigador",
        "tareas": ["Escribí el abstract, la introducción y el modelo/resultado principal."],
        "veredicto": None,
        "historial": [],
    }


def save_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def log_path(role: str) -> Path:
    stamp = datetime.now().isoformat(timespec="seconds").replace(":", "-")
    return LOGS / f"{stamp}_{role}.log"


def run_kimi(prompt: str, role: str, session_id: str | None, config: dict) -> str:
    """Llama a la CLI de Kimi en modo no interactivo pasando el prompt por stdin."""
    if config.get("dry_run"):
        return f"[DRY-RUN] Respuesta simulada para {role}.\n\nVeredicto: REVISAR\nTareas:\n- Continuar desarrollo."

    cmd = ["kimi", "--input-format", "text"]
    if config.get("quiet"):
        cmd.append("--quiet")
    if config.get("yolo"):
        cmd.append("--yolo")
    if config.get("thinking"):
        cmd.append("--thinking")
    if config.get("model"):
        cmd.extend(["--model", str(config["model"])])

    if session_id:
        cmd.extend(["--session", session_id])

    work_dir = config.get("work_dir", str(BASE))
    cmd.extend(["--work-dir", work_dir])

    log = log_path(role)
    try:
        result = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            timeout=int(config.get("subprocess_timeout", 600)),
        )
    except subprocess.TimeoutExpired as exc:
        log.write_text(
            f"TIMEOUT after 600s\nSTDOUT:\n{exc.stdout or ''}\n\nSTDERR:\n{exc.stderr or ''}",
            encoding="utf-8",
        )
        raise RuntimeError(f"Timeout llamando a Kimi para {role}")

    log.write_text(
        f"CMD: {' '.join(cmd)}\n\n"
        f"--- PROMPT ({len(prompt)} chars) ---\n{prompt}\n\n"
        f"--- STDOUT ---\n{result.stdout}\n\n"
        f"--- STDERR ---\n{result.stderr}\n\n"
        f"RETURN CODE: {result.returncode}",
        encoding="utf-8",
    )

    if result.returncode != 0:
        raise RuntimeError(f"Kimi falló para {role} (ver {log}): {result.stderr[:500]}")

    # La CLI a veces agrega una línea de resumen de sesión incluso en modo quiet.
    lines = [
        ln for ln in result.stdout.splitlines()
        if not ln.strip().startswith("To resume this session")
    ]
    return "\n".join(lines).strip()


def build_investigador_prompt(iniciador: str, draft: str, tareas: list, historial: list) -> str:
    rol = load_text(ROLES / "investigador.md")
    hist = "\n\n".join(
        f"--- Turno {h['loop']} ({h['turno']}) ---\n{h['resumen']}"
        for h in historial[-6:]
    )
    tareas_txt = "\n".join(f"- {t}" for t in tareas)

    return f"""{rol}

=== PROMPT INICIADOR DEL PAPER ===
{iniciador}

=== BORRADOR ACTUAL ===
{draft}

=== HISTORIAL RECIENTE ===
{hist}

=== TAREAS PENDIENTES DEL JEFE ===
{tareas_txt}

INSTRUCCIONES PARA ESTE TURNO:
1. Escribí, corregí o expandí el paper según las tareas pendientes.
2. Mantené estilo académico, riguroso y notación consistente.
3. Devolvé únicamente el texto completo del paper actualizado.
4. No incluyas saludos ni metacomentarios fuera del cuerpo del paper.
"""


def build_jefe_prompt(iniciador: str, draft: str, tareas_previas: list, loop: int) -> str:
    rol = load_text(ROLES / "jefe_research.md")
    tareas_txt = "\n".join(f"- {t}" for t in tareas_previas)

    return f"""{rol}

=== PROMPT INICIADOR DEL PAPER ===
{iniciador}

=== BORRADOR ACTUAL (loop {loop}) ===
{draft}

=== TAREAS PREVIAS ===
{tareas_txt}

INSTRUCCIONES PARA ESTE TURNO:
1. Audita el borrador como revisor de un journal matemático.
2. Devolvé tu respuesta en el formato exacto indicado en tu rol: ANALISIS, TAREAS, VEREDICTO.
3. Cada tarea debe ser concreta y accionable para el investigador.
4. Usá APROBADO solo si el paper está realmente listo para envío.
"""


def parse_jefe_response(text: str) -> tuple:
    """Extrae veredicto, lista de tareas y el texto completo."""
    m = re.search(r"VEREDICTO:\s*(APROBADO|REVISAR)", text, re.IGNORECASE)
    veredicto = m.group(1).upper() if m else "REVISAR"

    tareas = []
    m_tareas = re.search(r"TAREAS:\s*(.*?)(?=VEREDICTO:|$)", text, re.DOTALL | re.IGNORECASE)
    if m_tareas:
        bloque = m_tareas.group(1)
        for linea in bloque.splitlines():
            linea = linea.strip()
            if linea.startswith(("-", "*")):
                tareas.append(linea.lstrip("-* ").strip())
            elif re.match(r"^\d+\.", linea):
                tareas.append(re.sub(r"^\d+\.\s*", "", linea).strip())

    if not tareas:
        tareas = ["Revisar el paper según el análisis del jefe."]

    return veredicto, tareas, text


def main():
    iniciador = load_text(PROMPT_INICIADOR).strip()
    if not iniciador:
        print(f"❌ Escribí el prompt iniciador en {PROMPT_INICIADOR}")
        sys.exit(1)

    config = load_config()
    state = load_state()
    max_loops = int(config.get("max_loops", 40))

    # Asegurar directorios
    for d in (MAILBOX, PAPER, LOGS):
        d.mkdir(parents=True, exist_ok=True)

    print(f"🚀 Orquestador iniciado")
    print(f"   Max loops: {max_loops}")
    print(f"   Modelo: {config.get('model') or 'default'}")
    print(f"   Work dir: {config.get('work_dir')}")
    print(f"   Dry run: {config.get('dry_run')}")
    print(f"   Estado: loop {state['loop']}, turno {state['turno']}")

    while state["loop"] <= max_loops:
        print(f"\n--- Loop {state['loop']}/{max_loops} | Turno: {state['turno']} ---")
        draft = load_text(DRAFT)

        if state["turno"] == "investigador":
            prompt = build_investigador_prompt(
                iniciador, draft, state["tareas"], state["historial"]
            )
            session_id = config.get("session_investigador")
            print("   Llamando a investigador...")
            respuesta = run_kimi(prompt, "investigador", session_id, config)
            save_text(INVESTIGADOR_RESPONSE, respuesta)
            save_text(DRAFT, respuesta)

            state["historial"].append({
                "loop": state["loop"],
                "turno": "investigador",
                "resumen": f"Actualizó borrador ({len(respuesta)} caracteres).",
            })
            state["turno"] = "jefe"
            save_state(state)

        else:
            prompt = build_jefe_prompt(
                iniciador, draft, state["tareas"], state["loop"]
            )
            session_id = config.get("session_jefe")
            print("   Llamando a jefe de research...")
            respuesta = run_kimi(prompt, "jefe_research", session_id, config)
            save_text(JEFE_RESPONSE, respuesta)

            veredicto, tareas, _ = parse_jefe_response(respuesta)
            state["veredicto"] = veredicto
            state["tareas"] = tareas
            state["historial"].append({
                "loop": state["loop"],
                "turno": "jefe",
                "resumen": f"Veredicto: {veredicto}; Tareas: {', '.join(tareas[:3])}",
            })
            save_state(state)
            print(f"   Veredicto: {veredicto}")
            print(f"   Próximas tareas: {tareas}")

            if veredicto == "APROBADO":
                print(f"\n✅ Paper aprobado en el loop {state['loop']}.")
                print(f"   Borrador final: {DRAFT}")
                print(f"   Estado: {STATE}")
                break

            state["loop"] += 1
            state["turno"] = "investigador"
            save_state(state)
    else:
        print(f"\n⛔ Se alcanzó el límite de {max_loops} loops sin aprobación.")
        print(f"   Revisá el borrador en {DRAFT}")
        print(f"   Estado guardado en {STATE}")


if __name__ == "__main__":
    main()
