print (" ") #esta linea da el espacio para el nombre 
print (" Cristian David Sals De La O 3-W") #esta linea muestra el nombre del programador 
print (" ") #esta linea da el espacio para el nombre

materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"] #Esta linea define la lista de las materias 

for asignatura in materias[:]: #Esta linea define la asignatura dentro de las materias 
    nota = float(input(f"Introduce la nota en {asignatura}: ")) #Esta linea solicita la nota de la asignatura
    
    if nota >= 5:  #Esta linea define como saber si pasaste una asignatura 
        materias.remove(asignatura) #Esta linea especifica el elemento 

if materias: #Esta linea define que hacer si se cumple la peticion 
    print("Tienes que repetir las siguientes materias:") #Esta linea muestra las materias que tienes que repetir 
    for asignatura in materias: #Esta linea muestra las materias que tienes que repetir 
        print(asignatura) #Esta linea muestras las materias que tienes que repetir 
else: #Esta linea define que hacer si no se cumple con la condiccion 
    print("aprobaste todas las materias.") #Esta linea muestra que no tienes que reprtir ninguna materia
