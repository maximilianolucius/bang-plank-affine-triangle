# Prompt iniciador del paper

Este prompt es el contrato compartido por el tandem de agentes Kimi:

- **Investigador matematico:** redacta y corrige el paper completo.
- **Jefe de research:** audita como referee hostil y devuelve tareas accionables hasta aprobar.

El objetivo no es inventar un paper desde cero, sino convertir el corpus del proyecto en un
manuscrito matematico honesto, autocontenido y listo para envio.

## Proyecto y fuentes

Repositorio raiz:

`/home/maxim/PycharmProjects/bang-plank-euler-jacobi`

Aunque el orquestador corre desde `kimi/`, ambos agentes deben usar rutas absolutas para leer
el contexto fuera de `kimi/`. Prioridad de lectura:

1. `drafts/affine-plank-triangle.tex` como borrador base si existe.
2. `notes/46-R2-4-esqueleto-paper.md` como estructura aprobada del paper.
3. `auditorias/48-ronda4.md` como ultimo dictamen: el paper esta referee-clean y el deliverable
   seguro esta cumplido.
4. `notes/36-bang-medianas-PROBADO.md`, `notes/45-R2-2-rigidez-medianas-COMPLETA.md`,
   `notes/48-R4-4-suficiencia-concurrencia.md`, `notes/47-R3-2-medianas-dim-general.md`.
5. `notes/30-tier1-reenfoque-hallazgos.md`, `notes/37-familia-marginal-uniforme-transporte.md`,
   `notes/44-R2-1-bang-Nc-nogo.md`, `notes/43-P2-ambrus-dimension.md`,
   `notes/43-P3-gardner-suficiencia.md`, `notes/42-refs-papers-resumen.md`.
6. `AUDITORIA_CLAUDE_30Jn.md` y `auditorias/*.md` para advertencias de alcance y rutas refutadas.

Si una afirmacion de una nota temprana contradice una auditoria posterior, prevalece la auditoria
posterior. No uses resultados etiquetados como `[OPEN]`, `[EVIDENCE]`, `[CANDIDATE]`,
`[REFUTADA]` o "grid" como teoremas.

## Tema

Bang's affine plank problem on the triangle, with transport and tiling methods:
new sharp cases, a tight non-facet median theorem with rigidity, a necessary concurrence
condition for uniform-marginal transport, and a normalizer obstruction for the Bang
sign/chord method.

Titulo sugerido:

`Transport and tiling bounds for the affine plank problem on the triangle`

## Objetivo principal

Generar un paper matematico en **ingles**, en formato **LaTeX completo**, basado en los
resultados firmes del proyecto:

1. Presentar el problema afin de Bang y el estado honesto: abierto para cuerpos no simetricos,
   abierto ya en el plano para 3 planks; Ball resuelve el caso simetrico; Bakaev-Yehudayoff
   da la mejor cota general conocida.
2. Estudiar el triangulo como cuerpo concreto, no como reduccion de la conjetura general.
3. Probar los teoremas firmes A-G del esqueleto.
4. Explicar con precision que queda abierto y que rutas fueron descartadas.

## Tesis y alcance obligatorio

El paper debe decir explicitamente:

- No se prueba la conjetura afin de Bang.
- No se mejora la cota de Bakaev-Yehudayoff.
- No se usa el triangulo como target de la reduccion de Ambrus; Ambrus produce simplices de
  dimension `2N-1` para una cobertura por `N` planks, por lo que el triangulo no es target.
- La contribucion es un conjunto de casos sharp y herramientas para el triangulo como cuerpo
  concreto.
- El resultado central es el caso de las tres medianas: `sum rw >= 1`, con igualdad si y solo si
  cada intervalo es `[1/3, 2/3]`.

## Resultados que SI pueden enunciarse como teoremas

Usar solo estos como resultados propios probados:

1. **Cota de medida unica:** si `K subset R^d` esta cubierto por planks, entonces
   `sum rw_K(P_i) >= 1/d`; sharp en el simplex.
2. **Dos direcciones:** en el triangulo, planks en a lo sumo dos direcciones cumplen
   `sum rw >= 1`; citar Gardner 1988 Theorem 1 para la medida de ancho relativo en dos
   direcciones.
3. **Faceta-paralelo:** en el simplex de cualquier dimension, planks paralelos a facetas
   cumplen `sum rw >= 1`; prueba por sumset/Minkowski 1D, no por una arista.
4. **Tres facetas mas un plank arbitrario:** en el triangulo, tres familias faceta-paralelas
   mas un plank arbitrario cumplen `sum rw >= 1`; usar la prueba por fibras de `notes/30`.
5. **Medianas:** tres planks paralelos a las medianas del triangulo cumplen `sum rw >= 1`;
   igualdad, con planks esenciales, si y solo si `I_i=[1/3,2/3]` para todo `i`.
   La cota usa la medida uniforme del perimetro; la rigidez usa particion del perimetro,
   enumeracion exacta de edge-tilings y el centroide como testigo interior.
6. **Condicion necesaria de transporte:** para `d+1` formas afines normalizadas en `Delta^d`,
   si existe una medida con marginales uniformes, entonces los hiperplanos `{u_i=1/2}`
   concurren en un punto del simplex; algebraicamente `1^T V^{-1} 1 = 2` y
   `V^{-1}1 >= 0`.
7. **Perimetro solo en medianas:** para una forma con valores de vertices `{0,tau,1}`,
   la medida uniforme del perimetro tiene marginal uniforme si y solo si `tau=1/2`.
8. **No-go del normalizador por Bang:** el argumento de signos de Bang/Verreault que produce
   `sum width_i/ell_K(u_i) >= 1` esta atado a la cuerda mas larga `ell`; no puede reemplazarse
   por `N_c=(1-c)ell+c w` con `c>0` dentro de ese metodo. Esto es no-go de metodo, no una
   refutacion de `S_c >= 1`.

## Resultados que NO deben afirmarse

No afirmar ni insinuar como teorema:

- La conjetura afin de Bang para el triangulo general.
- El caso de 3 planks tilted del triangulo.
- Una mejora de Bakaev-Yehudayoff.
- Suficiencia general de la condicion de concurrencia `1^T V^{-1}1=2`.
- Que las medianas del simplex regular en toda dimension satisfacen Bang por la misma medida.
- Que la via toric/Euler-Jacobi resuelve el problema afin.
- Que Hunter resolvio la desigualdad de 3 planks en el triangulo; Hunter solo da 2 planks y
  caracterizacion de igualdad en un contexto especifico, segun las auditorias.
- Cualquier resultado basado solo en grilla, LP discreto o evidencia numerica.

## Estructura deseada del manuscrito

Producir una fuente LaTeX completa estilo `amsart`, con abstract, introduccion, teoremas,
pruebas y bibliografia.

Estructura recomendada:

1. Abstract.
2. Introduction: Bang affine plank problem, estado del arte, alcance, contribuciones.
3. Preliminaries and triangle model: relative width, normalized affine coordinates,
   planks as slabs `{f in I}`.
4. Single-measure bound `1/d`.
5. Sharp cases: two directions and facet-parallel families.
6. Three facets plus one arbitrary plank.
7. Median theorem and rigidity.
8. Uniform-marginal transport and concurrence obstruction.
9. Normalizer obstruction: chord vs width.
10. Final remarks and open problems.
11. References.

## Estilo y rigor

- Idioma del paper: ingles.
- Estilo: matematico, sobrio, referee-clean. Sin marketing ni lenguaje grandilocuente.
- Cada theorem/lemma/proposition debe estar probado en el texto o citado con fuente primaria.
- Usar `Conjecture`, `Problem` o `Remark` para lo abierto.
- Separar claramente "proved", "open", "evidence" y "method no-go".
- Mantener notacion consistente: `K`, `Delta`, `P_i`, `u_i`, `I_i`, `rw_K(P)`, `w_K(u)`,
  `ell_K(u)`, `Leb`, `V`, `p`.
- Evitar dependencias de scripts salvo el lema de rigidez mediana, que puede declararse
  computer-assisted con scripts archivados:
  `experiments/median_rigidity_enumeration.py` y
  `experiments/median_edgetilings_independent.py`.

## Reglas para el tandem de agentes

### Investigador

- En el primer turno, si `drafts/affine-plank-triangle.tex` existe, usarlo como base y producir
  una version LaTeX completa actualizada en el borrador del orquestador.
- Si el borrador actual ya contiene una version del paper, corregirlo incrementalmente segun las
  tareas del jefe, sin degradar resultados correctos.
- No incluir comentarios fuera del paper: devolver solo la fuente LaTeX completa.
- Cuando haya duda entre una afirmacion fuerte y una formulacion conservadora, usar la conservadora.

### Jefe de research

Auditar como referee matematico adversarial. En particular bloquear:

- sobreclaims sobre Bang, B-Y, Ambrus, Hunter o concurrencia;
- pruebas que usen una nota refutada;
- argumentos de grilla como prueba;
- prueba faceta-paralela por "una arista" en vez del argumento sumset/BM-1D;
- uso de la medida del perimetro fuera del caso `tau=1/2`;
- bibliografia vaga o citas que no soportan la afirmacion.

El veredicto `APROBADO` solo corresponde si el paper esta completo, autocontenido, sin
contradicciones de alcance y con todas las afirmaciones fuertes justificadas.

## Referencias minimas esperadas

Incluir al menos:

- T. Bang, original plank problem paper.
- K. Ball, *The plank problem for symmetric bodies*, Invent. Math. 104 (1991).
- R. J. Gardner, *Relative width measures and the plank problem*, Pacific J. Math. 135 (1988).
- E. Bakaev and A. Yehudayoff, *A Note on the Affine Plank Conjecture*, arXiv:2602.20290.
- G. Ambrus, *Appendix: Plank problems*.
- Verreault survey, *Plank theorems and their applications: a survey*, arXiv:2203.05540v2.

## Entregable final

El entregable del orquestador es `kimi/paper/draft.md`, pero su contenido debe ser una fuente
LaTeX completa y coherente del paper. El paper debe poder copiarse a un `.tex` y compilar tras
ajustar autor/acknowledgements si hiciera falta.
