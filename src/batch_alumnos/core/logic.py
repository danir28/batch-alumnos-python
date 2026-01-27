"""Agregar alumno a una colección
Calcular promedio
Contar aprobados y desaprobados"""
#Usa modelos + utils para hacer lógica de negocio.
from utils.validaciones import validar_nombre, validar_nota, existe_nombre
from models.alumnos import Alumno

OK = 0
NOMBRE_INVALIDO = 1
NOTA_INVALIDA = 2
ALUMNO_EXISTE = 3

def agregar_alumno(alumnos, nombre, nota):
    alumno = Alumno(nombre, nota)
    alumnos[nombre] = alumno
    return 0
    
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