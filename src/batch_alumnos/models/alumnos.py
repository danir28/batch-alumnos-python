"""Representa un alumno
Tiene nombre y nota
No pide input
No imprime nada"""
#Representa el concepto de alumno o alumnos.

class Alumno:
    def __init__(self, nombre: str, nota: float):
        self.nombre = nombre
        self.nota = nota
    
    def esta_aprobado(self):
        return self.nota >= 6
    
    def __str__(self):
        return f"{self.nombre} - Nota: {self.nota}"
    