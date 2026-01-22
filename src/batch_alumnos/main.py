"""Menú
Inputs
Prints
Llama funciones"""
from batch_alumnos.core.logic import agregar_alumno, calcular_estadisticas

alumnos = {}
while True:
    print("\nMenú de opciones:")
    print("1. Agregar alumno")
    print("2. Mostrar estadisticas")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nombre = input('ingrese nombre del alumno: ')
        nota = float(input('ingrese nota del alumno: '))
        alumno_agregado = agregar_alumno(alumnos, nombre, nota)
        print(alumno_agregado)
    elif opcion == '2':
        estadisticas = calcular_estadisticas(alumnos)
        if estadisticas == 0:
            print("No hay alumnos cargados.")
        else:
            print("\n📊 Estadísticas:")
            print(f"Promedio de notas: {estadisticas['promedio']}")
            print(f"Aprobados: {estadisticas['aprobados']}")
            print(f"Desaprobados: {estadisticas['desaprobados']}")
            print(f"Nota más alta: {estadisticas['maximo']}")
            print(f"Nota más baja: {estadisticas['minimo']}")
    elif opcion == '3':
        print('saliendo...')
        break
    else:
        print("Opción no válida. Intente de nuevo.")
