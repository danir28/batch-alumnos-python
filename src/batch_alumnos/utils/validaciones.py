"""Funciones booleanas
Validar nota
Validar texto
Nada de lógica de negocio"""
#Solo valida cosas simples.

def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_nota(nota):
    return 0 <= nota <= 10

def existe_nombre(nombre, alumnos):
    return nombre in alumnos
