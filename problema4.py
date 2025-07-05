alumnos = []

n = int(input("¿Cuántos alumnos desea registrar?: "))

for i in range(n):
    print(f"\nAlumno {i + 1}")
    nombre = input("Nombre del alumno: ")
    
    notas = [] 
    for j in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {j}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    
    alumnos.append(alumno)

print("\nListado de alumnos registrados:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")