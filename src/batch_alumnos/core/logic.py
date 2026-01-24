"""Agregar alumno a una colección
Calcular promedio
Contar aprobados y desaprobados"""
#Usa modelos + utils para hacer lógica de negocio.
from core.logic import validar_nombre, validar_nota, existe_nombre

OK = 0
NOMBRE_INVALIDO = 1
NOTA_INVALIDA = 2
ALUMNO_EXISTE = 3

def agregar_alumno(alumnos, nombre, nota):
    if not validar_nombre(nombre):
        return NOMBRE_INVALIDO
    
    if existe_nombre(nombre, alumnos):
        return ALUMNO_EXISTE
    
    if not validar_nota(nota):
        return NOTA_INVALIDA
    
    alumnos[nombre] = nota
    return OK
    
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