"""Agregar alumno a una colección
Calcular promedio
Contar aprobados y desaprobados"""
#Usa modelos + utils para hacer lógica de negocio.
from core.logic import validar_nombre, validar_nota, existe_nombre

def agregar_alumno(alumnos, nombre, nota):
    if not validar_nombre(nombre):
        return 'nombre inválido'
    
    if existe_nombre(nombre, alumnos):
        return 'alumno existente'
    
    if not validar_nota(nota):
        return 'nota invalida'
    
    alumnos[nombre] = nota
    return 'alumno agregado'
    
def calcular_estadisticas(alumnos):
    if not alumnos:
        return None
    
    notas = alumnos.values()
    
    return {
        'cantidad': len(alumnos),
        'promedio': sum(notas) / len(alumnos),
        'maximo': max(notas),
        'minimo': min(notas),
    }