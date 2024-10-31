print (" ") #esta linea da el espacio para el nombre 
print (" Cristian David Sals De La O 3-W") #esta linea muestra el nombre del programador 
print (" ") #esta linea da el espacio para el nombre

materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"] #Esta linea define la lista de las materias 

for asignatura in materias[:]: #Esta linea define la asignatura dentro de las materias 
    nota = float(input(f"Introduce la nota en {asignatura}: ")) #Esta linea solicita la nota de la asignatura

for asignatura in materias:
    print (f"sacaste en {asignatura} {nota}")
    