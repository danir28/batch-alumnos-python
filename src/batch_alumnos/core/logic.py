"""Agregar alumno a una colección
Calcular promedio
Contar aprobados y desaprobados"""
#Usa modelos + utils para hacer lógica de negocio.

def agregar_alumno(diccionario, nombre, nota):
    if nombre in diccionario:
        return 'alumno existente'
    else:
        diccionario[nombre] = nota
        return 'alumno agregado'
    
def calcular_estadisticas(diccionario):
    if not diccionario:
        return {
            'promedio': 0,
            'aprobados': 0,
            'desaprobados': 0,
            'maximo': 0,
            'minimo': 0
        }
    cantidad = 0
    suma = 0
    aprobados = 0
    desaprobados = 0
    nota_maxima = -1
    nota_minima = 11
    
    for nota in diccionario.values():
        cantidad += 1
        suma += nota
        
        if nota >= 6:
            aprobados += 1
        else:
            desaprobados += 1
            
        if nota > nota_maxima:
            nota_maxima = nota
        if nota < nota_minima:
            nota_minima = nota
            
    promedio = suma / cantidad
    
    return {
        'promedio': promedio,
        'aprobados': aprobados,
        'desaprobados': desaprobados,
        'maximo': nota_maxima,
        'minimo': nota_minima
    }