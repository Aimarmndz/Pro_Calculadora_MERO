"""Operaciones aritmeticas basicas."""


def suma(a, b, *resto):
    return a + b + sum(resto)


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b
