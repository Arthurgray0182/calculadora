import math


def suma(a, b):
    """Retorna la suma de dos números."""
    return a + b


def resta(a, b):
    """Retorna la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Retorna la multiplicación de dos números."""
    return a * b


def division(a, b):
    """Retorna la división de dos números."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def potencia(base, exponente):
    """Retorna la potencia de una base elevada a un exponente."""
    return base ** exponente


def raiz_cuadrada(numero):
    """Retorna la raíz cuadrada de un número."""
    if numero < 0:
        raise ValueError(
            "No se puede calcular la raíz cuadrada de un número negativo."
        )
    return math.sqrt(numero)
