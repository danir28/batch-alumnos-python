"""Agregar alumno a una colección
Calcular promedio
Contar aprobados y desaprobados"""
#Usa modelos + utils para hacer lógica de negocio.

def agregar_alumno(diccionario, nombre, nota):
    if nombre in diccionario:
        return {
            'ok': False,
            'error': 'alumno_existente'
        }
    diccionario[nombre] = nota
    return {
        'ok': True
    }
    
def calcular_estadisticas(diccionario):
    if not diccionario:
        return {}
    
    cantidad = 0
    suma = 0
    aprobados = 0
    desaprobados = 0
    nota_maxima = -1
    nota_minima = 11
    
    for nota in diccionario.values():
        cantidad += 1
        suma += nota
        
        if nota >= 7:
            aprobados += 1
        else:
            desaprobados += 1
            
        if nota > nota_maxima:
            nota_maxima = nota
        if nota < nota_minima:
            nota_minima = nota
            
    return {
        'promedio': suma / cantidad,
        'aprobados': aprobados,
        'desaprobados': desaprobados,
        'maximo': nota_maxima,
        'minimo': nota_minima
    }