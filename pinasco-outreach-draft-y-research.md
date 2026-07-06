# Outreach a Damián Pinasco — research verificado + draft de email
> Fecha: 2026-07-05. Estado: **BORRADOR — NO ENVIADO** (pendiente de OK del usuario).
> Fuente del research: deep-research workflow (101 agentes; cada claim verificado por
> panel adversarial de 3 votantes contra fuentes primarias, 2026-07-04).
> JSON completo del research: scratchpad de la sesión "bang" (`pinasco_full.json`).

---

## 1. Perfil verificado (todo 3-0 salvo indicación)

**Identidad y cargo**
- Damián Pinasco — **Director del Departamento de Matemática y Estadística, UTDT**
  (verificado en la página viva de UTDT el 2026-07-04); Profesor Investigador
  Asociado; Doctor en Ciencias Matemáticas, UBA (2008).
- **CONICET Investigador Independiente**, especialidad Análisis Funcional; lugar de
  trabajo registrado: Depto. de Matemáticas y Estadística, UTDT, Miñones 2177,
  C1428ATG, CABA. (Dirección: voto 2-1, verificada contra ficha primaria.)
- **Email profesional: dpinasco@utdt.edu** (página de facultad UTDT + footer de
  arXiv:2208.05584).
- NO se verificó ORCID ni Google Scholar (ausencia de evidencia, no confirmación
  de ausencia).
- Distinción institucional: premio UTDT **"La Dicha de los Comunes"** (26-jun-2025,
  anunciado por Juan José Cruces).
- Desambiguación confirmada en cada paso: NO es Juan Pablo Pinasco (PDEs, UBA).

**Identidad de research**
- Tema CONICET: "Polinomios, operadores y medidas en espacios de Banach"; programa
  SIGEVA: representación integral de funciones holomorfas en espacios de Banach,
  desigualdades polinomiales determinísticas y probabilísticas, polinomios
  aleatorios. Tesis UBA 2008: "Representación integral de funciones holomorfas en
  espacios de Banach".
- Papers de geometría convexa con MSC íntegramente en el bloque 52A (convexidad).

**Publicaciones clave (verificadas)**
- *On the n-th linear polarization constant of R^n* — **autor único**,
  arXiv:2208.05584, Math. Nachr. 296(8) (2023) 3593-3605,
  DOI 10.1002/mana.202200026. Prueba la conjetura Benítez–Sarantopoulos–Tonge
  (c_n(R^n)=n^{n/2}) para **n≤14**, igualdad sii sistema ortonormal.
  ⚠️ El claim "la prueba n≤14 es puramente a mano (sin computadora)" fue
  **votado abajo 1-2**: no caracterizar la prueba como computacional NI como
  no-computacional sin leer el paper.
- *On the linear polarization constants of finite dimensional spaces* — con
  Carando y J. T. Rodríguez, Math. Nachr. 290 (2017) 2547-2559 (precursor directo
  del paper 2023; confirma el nodo Carando de su red).
- Volume ratio: Galicer–Merzbacher–Pinasco, Rev. Mat. Iberoam. 37(6) (2021)
  2347-2372; y Galicer–Litvak–Merzbacher–Pinasco, J. Funct. Anal. 286 (2024)
  110242. (Litvak NO está en el de 2021 — son dos trabajos distintos.)
- **2026, el timing**: Martínez–Ortega-Moreno (arXiv:2605.28744, mayo 2026)
  resuelven la polarización fuerte de Ball–Frenkel — el problema que Pinasco
  verificó para n≤14; un mes después Pinasco co-firma el follow-up
  **"Strong Polarization and Entropy"** (arXiv:2606.02567, con Galicer y
  Ortega-Moreno). Está adentro y activo en el círculo polarización↔planks AHORA.

**Caveats operativos del research**
- 2605.28744 y 2606.02567 son **preprints** (llamarlos "solución reciente /
  preprint", no teorema establecido — aunque los insiders, Pinasco incluido, ya
  construyen sobre ellos).
- **Cero evidencia** de interés público en matemática computer-assisted / IA /
  experimental → el email NO debe asumir ese interés; pitch como invitación
  abierta, no como alineación documentada.
- Nada verificado sobre editorial boards, seminarios, carga docente.
- Cargo de Director y categoría CONICET verificados vivos al 2026-07-04;
  re-chequear si el envío se demora.

---

## 2. Draft del email (v1, 2026-07-04 — pendiente de aprobación)

**Para:** dpinasco@utdt.edu
**Asunto:** El problema del plank afín en el triángulo — transporte, rigidez y una pregunta de Gardner

Estimado Profesor Pinasco:

Le escribo porque acabo de completar un manuscrito sobre la conjetura afín de
planks de Bang (la de anchos relativos, abierta desde 1951) y creo que pocos
lugares del mundo leen ese problema con más contexto que su grupo, especialmente
después de la resolución de la polarización fuerte por Martínez y Ortega-Moreno y
de su trabajo con Galicer y Ortega-Moreno sobre polarización y entropía.

El paper (35 pp., adjunto) estudia el triángulo como cuerpo concreto. En una
línea: introducimos el *transport defect* D_K(u) — el menor D tal que existe una
probabilidad sobre K con todas las marginales u_i acotadas por D·Leb — con
dualidad minimax y certificados exactos en ambos lados, y sobre el triángulo
determinamos exactamente cuándo el método de transporte certifica la constante
sharp 1: para tres direcciones, una medida testigo de marginales uniformes existe
**si y sólo si** las tres rectas de nivel medio concurren — lo que responde, para
tres direcciones sobre el triángulo, la pregunta de existencia de Gardner (1988).
La familia concurrente cíclica resulta además rígida: exhibimos el cubrimiento
tight único de cada miembro, una familia biparamétrica que extiende el caso de
las medianas. Como calibración, las facetas del d-símplice tienen defecto
exactamente (d+1)/2, y en una terna inclinada no concurrente determinamos la
constante de cubrimiento un-plank-por-dirección mediante un certificado racional
exacto verificado por un checker independiente, al estándar de las pruebas
computer-assisted modernas.

Hay una segunda razón, más inusual, para escribirle. Este manuscrito es el piloto
de una plataforma de investigación que estoy construyendo — la llamo
*bourbaki-engine*: ensambles de agentes de IA organizados sobre un grafo de
objetivos AND-OR, con paneles adversariales de refutación con poder de veto,
disciplina estricta de etiquetas ([PROVED]/[EVIDENCE]/[OPEN]) y certificados con
checkers independientes para todo paso computacional. El paper de planks salió de
dieciséis rondas auditadas de ese proceso. No le pido que le interese la
ingeniería: le pido que juzgue el output matemático — si el teorema de
caracterización y la rigidez le parecen correctos e interesantes, la plataforma
que los produjo se vuelve, creo, una conversación que vale la pena tener.

Concretamente: me encantaría conocer su opinión sobre el manuscrito (toda crítica
es bienvenida — el proceso está diseñado para absorberlas), y explorar si le
interesaría involucrarse en la siguiente fase, al nivel que usted elija: los
próximos objetivos naturales son la agregación de certificados de Farkas para las
ternas no concurrentes y la adaptación de la identidad de Euler–Jacobi de
Martínez–Ortega-Moreno a anchos relativos — territorio donde su experiencia sería
decisiva.

Con gusto le comparto el repositorio completo (notas, auditorías, certificados)
si quiere ver el proceso por dentro.

Cordialmente,
Maximiliano Lucius
Investigador independiente
maximiliano.lucius@gmail.com

---

## 3. Decisiones de redacción (racional)

1. **La matemática abre; la plataforma entra tarde y en un solo párrafo** — el
   research confirmó cero señal de interés suyo en IA; el gancho es Gardner +
   rigidez + el momento M–OM (su casa).
2. **"Juzgue el output, no la ingeniería"** — frase pivote: le da rol de autoridad
   (referee natural) en vez de pedirle fe en agentes.
3. **Invitación de nivel variable** ("al nivel que usted elija").
4. Sin mención de Alraddadi ni de funding — primer contacto, puramente científico.
5. Registro formal rioplatense ("usted"). Variante en inglés disponible si se
   pide.
6. Pendientes al aprobar: decidir adjunto (PDF via cliente de mail del usuario vs
   extender el helper SMTP para attachments); re-chequear cargo si pasa tiempo.

## 4. Fuentes principales
- UTDT: ver_contenido.php?id_contenido=1895 / 13422; ver_novedad.php?id_novedad=6276
- CONICET: new_scp/detalle.php?id=31274; bicyt.conicet.gov.ar/fichas/persona/scp/31274; ri.conicet.gov.ar/author/18846
- arXiv: 2208.05584, 1703.06316, 2211.06094, 2605.28744, 2606.02567, 1901.00771
- EMS Press RMI 37(6):2347-2372; JFA 286 (2024) 110242 (lista de Litvak)
