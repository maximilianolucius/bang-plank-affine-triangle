# Orquestador de paper matemático con dos agentes Kimi

Automatiza la comunicación entre dos roles:
- **Investigador matemático**: escribe y corrige el paper.
- **Jefe de research**: audita el borrador y genera sub-tareas concretas.

El orquestador alterna entre ambos, guarda todo el estado en disco y se detiene cuando el jefe aprueba o cuando se alcanzan **40 loops**.

---

## Estructura

```
kimi/
├── PROMPT_INICIADOR.md          # ← Editá esto primero
├── config.json                  # ← Config (loops, modelo, sesiones, dry-run)
├── orchestrator.py              # ← Script principal
├── roles/
│   ├── investigador.md          # System prompt del investigador
│   └── jefe_research.md         # System prompt del jefe/auditor
├── mailbox/
│   ├── state.json               # Estado del loop
│   ├── investigador_response.md # Última respuesta del investigador
│   └── jefe_response.md         # Última respuesta del jefe
├── paper/
│   └── draft.md                 # Borrador acumulado del paper
└── logs/                        # Logs de cada llamada a Kimi
```

---

## Cómo usar

### 1. Escribí el prompt iniciador

Abrí `PROMPT_INICIADOR.md` y completá:
- Tema y título provisional
- Objetivo principal
- Audiencia y nivel de rigor
- Estructura deseada
- Restricciones y preferencias

> Este es **el único archivo que tenés que editar** para arrancar un paper nuevo.

### 2. (Opcional) Ajustá la configuración

En `config.json`:

```json
{
  "max_loops": 40,
  "model": null,
  "work_dir": "/home/maxim/PycharmProjects/bang-plank-euler-jacobi/kimi",
  "yolo": true,
  "quiet": true,
  "thinking": false,
  "dry_run": false,
  "use_sessions": true,
  "session_investigador": null,
  "session_jefe": null,
  "subprocess_timeout": 600
}
```

- `max_loops`: cantidad máxima de ciclos investigador→jefe.
- `model`: modelo de Kimi (ej. `kimi-k2-0711-preview`). `null` usa el default.
- `work_dir`: directorio de trabajo que ven los agentes. Por defecto es `kimi/` para evitar escanear todo el proyecto.
- `use_sessions`: si es `true`, cada rol usa una sesión persistente de Kimi (`--session`), por lo que conserva su propio historial interno.
- `session_investigador` / `session_jefe`: IDs de sesión. Si son `null`, el orquestador los genera automáticamente y los guarda en `config.json`.
- `dry_run`: si es `true`, simula las respuestas sin llamar a la API (útil para testear el flujo).

### 3. Ejecutá el orquestador

```bash
cd /home/maxim/PycharmProjects/bang-plank-euler-jacobi/kimi
python3 orchestrator.py
```

### 4. Revisá los resultados

- Borrador: `paper/draft.md`
- Estado del loop: `mailbox/state.json`
- Logs: `logs/`

---

## Cómo funciona el loop

```
Loop 1:
  1. Investigador escribe/corrige el paper (guarda en paper/draft.md)
  2. Jefe audita y devuelve ANALISIS / TAREAS / VEREDICTO
     - Si VEREDICTO == APROBADO → fin
     - Si VEREDICTO == REVISAR  → loop 2 comienza con las nuevas tareas
```

Cada loop implica **dos llamadas a Kimi** (investigador + jefe), así que 40 loops = hasta 80 llamadas.

---

## Conservación del contexto (importante)

El sistema usa **dos mecanismos simultáneos** para que los agentes no pierdan el hilo:

1. **Sesiones persistentes por rol**  
   Cada agente tiene su propio ID de sesión de Kimi (`--session`). Eso significa que, además del prompt actual, Kimi mantiene el historial interno de cada conversación. El investigador recuerda lo que escribió antes; el jefe recuerda lo que pidió antes.

2. **Contexto explícito en cada prompt**  
   El orquestador siempre incluye en el prompt:
   - el prompt iniciador completo,
   - el borrador actual (`paper/draft.md`),
   - las tareas pendientes del jefe,
   - los últimos 6 turnos de historial.

   Esto garantiza que, incluso si una sesión se reinicia o hay un fallo, el agente reciba todo lo necesario para continuar coherentemente.

Si querés forzar un "reset" de contexto, borrá `config.json` (se regenerará) o cambiá los IDs de sesión manualmente.

---

## Reanudar un paper

El orquestador lee `mailbox/state.json` al arrancar. Si querés retomar desde donde quedó, simplemente volvé a ejecutar:

```bash
python3 orchestrator.py
```

Si querés reiniciar de cero, borrá el estado y el borrador:

```bash
rm mailbox/state.json paper/draft.md mailbox/*.md
```

Y si querés nuevas sesiones:

```bash
rm config.json
```

(el orquestador lo regenerará con IDs nuevos).

---

## Notas

- El orquestador usa `kimi --quiet --yolo --input-format text` para correr sin interacción humana.
- Los prompts de los roles están en `roles/`: podés ajustar el tono, el rigor o el formato de salida.
- El jefe debe devolver exactamente `VEREDICTO: APROBADO` o `VEREDICTO: REVISAR`; el parser lo detecta automáticamente.
- Si ves un error `429 rate limit reached`, es porque llegaste al límite de uso de Kimi. Esperá a que se refresque la cuota o usá `dry_run: true` para testear el flujo sin consumir API.
