
# José Auyón
# Matemática Discreta
# Ejercicio 6
# Agosto 16, 2024
def generar_numeros_pseudoaleatorios(m, a, c, s, n):
    """
    Genera una sucesión de números pseudoaleatorios usando el método de congruencial lineal.

    Parámetros:
    - m: módulo
    - a: multiplicador
    - c: incremento
    - s: semilla inicial
    - n: cantidad de números a generar

    Retorna:
    - Una lista con la sucesión de números pseudoaleatorios generados.
    """

    # Validación de los parámetros
    if not (isinstance(m, int) and isinstance(a, int) and isinstance(c, int) and isinstance(s, int) and isinstance(n, int)):
        raise TypeError("Todos los parámetros deben ser enteros.")

    if not (2 <= a < m):
        raise ValueError("El multiplicador 'a' debe cumplir 2 ≤ a < m.")
    if not (0 <= c < m):
        raise ValueError("El incremento 'c' debe cumplir 0 ≤ c < m.")
    if not (0 <= s < m):
        raise ValueError("La semilla 's' debe cumplir 0 ≤ s < m.")
    if not (n > 0):
        raise ValueError(
            "La cantidad de números a generar 'n' debe ser un entero positivo.")

    # Inicializar la lista con la semilla
    numeros = [s]

    # Generar la secuencia de números pseudoaleatorios
    for _ in range(n - 1):
        nuevo_numero = (a * numeros[-1] + c) % m
        numeros.append(nuevo_numero)

    return numeros

# Pruebas del algoritmo


def pruebas():
    casos_de_prueba = [
        {"m": 16, "a": 5, "c": 3, "s": 7, "n": 10},
        {"m": 20, "a": 7, "c": 5, "s": 12, "n": 5},
        {"m": 10, "a": 3, "c": 1, "s": 1, "n": 7},
        {"m": 8, "a": 4, "c": 2, "s": 3, "n": 6},
    ]

    for caso in casos_de_prueba:
        try:
            resultado = generar_numeros_pseudoaleatorios(
                caso["m"], caso["a"], caso["c"], caso["s"], caso["n"])
            print(f"Para m={caso['m']}, a={caso['a']}, c={
                  caso['c']}, s={caso['s']}, n={caso['n']}:")
            print(resultado)
        except Exception as e:
            print(f"Error en el caso m={caso['m']}, a={caso['a']}, c={
                  caso['c']}, s={caso['s']}, n={caso['n']}: {e}")


# Ejecutar pruebas
pruebas()
