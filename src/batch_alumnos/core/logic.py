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
    if not validar_nombre(nombre):
        return False, NOMBRE_INVALIDO
    if not validar_nota(nota):
        return False, NOTA_INVALIDA
    if existe_nombre(nombre, alumnos):
        return False, ALUMNO_EXISTE
    
    alumno = Alumno(nombre, nota)
    alumnos[nombre] = alumno.nota
    return True, OK
    
def calcular_estadisticas(alumnos):
    if not alumnos:
        return None

    notas = [alumno.nota for alumno in alumnos.values()]

    return {
        'cantidad': len(notas),
        'promedio': sum(notas) / len(notas),
        'maximo': max(notas),
        'minimo': min(notas),
    }
