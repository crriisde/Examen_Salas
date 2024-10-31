print (" ") #esta linea da el espacio para el nombre 
print ("Cristian David Salas De La O 3-W") #esta linea muestra el nombre del programador 
print (" ") #esta linea da el espacio para el nombre 

asignaturas = { #esta linea define el diccionario 
    'Matematicas': 6,
    'Fisica': 4,
    'Quimica': 5
}


total_creditos = 0 #esta linea define el total de creditos 


for asignatura, creditos in asignaturas.items(): #esta linea define los creditos de cada asignatura 
    print(f"{asignatura} tiene {creditos} creditos") #esta linea muestra los creditos de cada asignatura
    total_creditos += creditos  #esta linea suma el total de creditos


print(f"El numero total de créditos del curso es: {total_creditos}") #esta linea muestra todos los creditos
