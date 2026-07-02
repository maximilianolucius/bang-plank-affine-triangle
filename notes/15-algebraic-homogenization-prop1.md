# [REFUTADA DEFINITIVAMENTE] La Vía Algebraica: Un Callejón Sin Salida
> Documento histórico de la investigación algebraica. CERRADO tras la Segunda Auditoría de Fundamentos.
> Date: 2026-06-29.

## 1. El Falso Espejismo de los Gradientes Tóricos
En un intento desesperado por salvar la vía algebraica, se propuso que el sistema de gradientes logarítmicos $E_k = x_k \frac{\partial \Phi}{\partial x_k}$ evaluaba a $-1$ en los bordes del símplex, sugiriendo que el sistema no tenía raíces en el infinito tórico.

## 2. La Segunda Auditoría: El Error Categorial
Una segunda auditoría estricta de fundamentos algebraicos (`experiments/audit_algebra_2.py`) destrozó esta afirmación por un error de categoría matemática:

1. El Teorema de Euler-Jacobi Tórico de Khovanskii (y la teoría BKK) aplica **estrictamente a polinomios de Laurent**.
2. Un polinomio de Laurent pertenece al anillo $\mathbb{C}[x^{\pm 1}, y^{\pm 1}]$, lo que significa que sus *únicos* polos permitidos son los hiperplanos coordenados ($x=0, y=0$).
3. Nuestro sistema de gradientes contiene términos como $\frac{x}{u_i x + v_i y - m_i}$ y $\frac{x}{1-x-y}$. Estos denominadores **no son monomios**.
4. Por lo tanto, nuestro sistema de gradientes es una red de **funciones racionales**, no de polinomios de Laurent.
5. Para aplicar cualquier teorema de intersección geométrica (Bézout, BKK, Euler-Jacobi), es matemáticamente obligatorio limpiar los denominadores no-monomiales para volver el sistema algebraico. 
6. Al limpiar los denominadores multiplicando por $L_i$ y $(1-x-y)$, el sistema regresa exactamente a los polinomios densos analizados en la Primera Auditoría.

## 3. Conclusión Final e Inapelable
La Primera Auditoría ya demostró que los polinomios densos tienen una resultante idénticamente nula (comparten curvas enteras de raíces en el infinito proyectivo). La Segunda Auditoría demuestra que no hay forma de eludir esos denominadores usando atajos tóricos sin caer en un error de categoría.

La vía algebraica está matemáticamente muerta para el caso de planchas asimétricas ($m \ge 4$) a menos que se desarrolle una teoría masiva de desingularización geométrica (blow-ups). La investigación se traslada al 100% a la Topología Combinatoria y a la Geometría Computacional de Fuerza Bruta.