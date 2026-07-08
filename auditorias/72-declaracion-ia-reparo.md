# Constancia — reparo sobre la declaración de uso de IA (AIMS v1)
> Jefe de research: Claude. Fecha: 2026-07-07.
> Registro de una decisión editorial del usuario sobre la que dejé reparo explícito.

## Qué cambió
El usuario editó `drafts/aims-v1/affine-plank-triangle-aims-v1.tex` revirtiendo la sección
`Use of Generative-AI tools declaration` desde la versión honesta commiteada en `b052410`
(nombraba **Claude (Anthropic)** y describía el alcance real: exploración/redacción de
pruebas, diseño del branch-and-bound de `thm:sandwichbang`, código ancillary; validación por
checker independiente) a una versión que declara **solo "Alibaba Cloud service, Qwen 3.6
Plus"** usado únicamente para *"language editing, clarity, grammar correction, and manuscript
structure"*, con la frase *"No AI tool was used to generate or modify core research data"*.
También un cambio cosmético: "the human/machine boundary" → "the boundary" en §Discussion.

## Mi reparo (evidenciado)
La nueva declaración es, según el registro del proyecto, **inexacta en dos frentes**:
1. **Herramienta:** todo el repositorio (auditorías, `notes/58`, scripts de `ancillary/`,
   diseño B&B, y las sesiones mismas) muestra que el paper se produjo con agentes **Claude**.
   Declarar Qwen y omitir Claude tergiversa qué herramienta produjo el trabajo. (No hay
   evidencia en el repo de que se usara Qwen; eso no lo puedo verificar.)
2. **Alcance:** la IA hizo contribución de investigación sustantiva (diseño de la búsqueda que
   sostiene el teorema central computer-assisted, código ancillary), no solo edición de estilo.
   La frase "no se usó IA para generar/modificar core research data" contradice el registro.

**Riesgo declarado al usuario:** AIMS trata la declaración de IA no veraz como violación de
estándares de publicación (retractable); las propias instrucciones de conversión
(`instrucciones-modificaciones-paper-aims.md`, §2.4.2) exigen declarar "con honestidad" la
"asistencia sustancial de IA".

## Decisión del usuario
Consultado con las tres opciones (declarar honesto / declarar Claude+Qwen / comitear su
versión igual), el usuario eligió **comitear su versión tal como la editó**, bajo su
responsabilidad como autor. Procedí con eso: recompilé el PDF (42 pp, 0 undefined, 0 overfull
>10pt), regeneré `submission-source-aims-v1.zip` para coherencia, y comiteé/pusheé.

La decisión editorial es del autor; mi rol fue dejar el reparo por escrito. Queda registrado.
