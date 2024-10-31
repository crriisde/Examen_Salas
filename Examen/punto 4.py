print (" ") #esta linea da el espacio para el nombre 
print (" Cristian David Sals De La O 3-W") #esta linea muestra el nombre del programador 
print (" ") #esta linea da el espacio para el nombre


usuario = {} #esta linea define al diccionario 

usuario['nombre'] = input("Introduce tu nombre: ") #esta linea solicita el nombre 
usuario['edad'] = input("Introduce tu edad: ") #esta linea solicita la edad 
usuario['direccion'] = input("Introduce tu dirección: ") #esta linea solicita la direccion 
usuario['telefono'] = input("Introduce tu número de teléfono: ") #esta linea solicita el telefono 

print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.") 

