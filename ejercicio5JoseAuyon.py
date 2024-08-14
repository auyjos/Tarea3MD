
# José Auyón
# Matemática Discreta
# Ejercicio 5
# Agosto 16, 2024
def almacenar_datos(datos, tamano_celdas):
    """
    Almacena un array de datos en celdas de memoria usando una función de dispersión.

    Parámetros:
    - datos: lista de enteros que se desea almacenar
    - tamano_celdas: número de celdas en la memoria

    Retorna:
    - Un array con los datos almacenados en las posiciones calculadas.
    """

    # Validación de entrada
    if not isinstance(datos, list):
        raise TypeError(
            "La entrada 'datos' debe ser una lista de números enteros.")

    if not all(isinstance(x, int) for x in datos):
        raise ValueError("Todos los elementos de 'datos' deben ser enteros.")

    if not isinstance(tamano_celdas, int) or tamano_celdas <= 0:
        raise ValueError(
            "El tamaño de las celdas de memoria debe ser un entero positivo.")

    if tamano_celdas < 1:
        raise ValueError(
            "El tamaño de las celdas de memoria debe ser al menos 1.")

    # Inicializar el array de celdas de memoria con valores None
    celdas = [None] * tamano_celdas

    def funcion_dispersion(n):
        # Función de dispersión H(n) = n mod tamano_celdas
        return n % tamano_celdas

    def insertar_en_memoria(n):
        pos = funcion_dispersion(n)
        intentos = 0

        while celdas[pos] is not None and intentos < tamano_celdas:
            pos = (pos + 1) % tamano_celdas
            intentos += 1

        if intentos >= tamano_celdas:
            raise OverflowError(
                "No se puede insertar el dato, la tabla de hash está llena.")

        celdas[pos] = n

    # Insertar todos los datos en la memoria
    for numero in datos:
        insertar_en_memoria(numero)

    return celdas


def pruebas():
    casos_de_prueba = [
        {"datos": [15, 558, 32, 132, 102, 5, 257], "tamano_celdas": 11},
        {"datos": [10, 20, 30, 40, 50], "tamano_celdas": 5},
        {"datos": [1, 2, 3, 4, 5], "tamano_celdas": 3},
        {"datos": [6, 12, 18, 24, 30], "tamano_celdas": 7},
        {"datos": [], "tamano_celdas": 5},  # Caso con lista vacía
    ]

    for caso in casos_de_prueba:
        try:
            resultado = almacenar_datos(caso["datos"], caso["tamano_celdas"])
            print(f"Para datos={caso['datos']} y tamaño de celdas={
                  caso['tamano_celdas']}:")
            print(resultado)
        except (TypeError, ValueError, OverflowError) as e:
            print(f"Error en el caso datos={caso['datos']} y tamaño de celdas={
                  caso['tamano_celdas']}: {e}")


pruebas()
