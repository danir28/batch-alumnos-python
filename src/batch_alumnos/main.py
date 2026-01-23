"""Menú
Inputs
Prints
Llama funciones"""
from batch_alumnos.core.logic import agregar_alumno, calcular_estadisticas
from utils.formato import mostrar_estadisticas

alumnos = {}
while True:
    print("\nMenú de opciones:")
    print("1. Agregar alumno")
    print("2. Mostrar estadisticas")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nombre = input('ingrese nombre del alumno: ')
        
        try:
            nota = float(input('ingrese nota del alumno: '))
        except ValueError:
            print('la nota debe ser un número')
            continue
        resultado = agregar_alumno(alumnos, nombre, nota)
        print(resultado)
        
    elif opcion == '2':
        estadisticas = calcular_estadisticas(alumnos)
        salida = mostrar_estadisticas(estadisticas)
        print(salida)
                    
    elif opcion == '3':
        print('saliendo...')
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")
