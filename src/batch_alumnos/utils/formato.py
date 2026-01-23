def mostrar_estadisticas(estadisticas):
    if estadisticas is None:
        return "No hay alumnos cargados."
    return (
        f'Cantidad de alumnos: {estadisticas["cantidad"]}\n'
        f'Promedio: {estadisticas["promedio"]:.2f}\n'
        f'Nota maxima: {estadisticas["maximo"]}\n'
        f'Nota minima: {estadisticas["minimo"]}'
    )