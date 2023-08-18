#Solcitar un nombre y apellido y luego mostrar el nombre completo.
#Para este ejercicio definiremos 3 variables (nombre,apellido, nombre_completo)
#Solicitar para esas variables los valores usando el metodo input()
#luego mediante el print mostraremos el nombre completo

nombre =  input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
nombre_completo = nombre + ' - ' + apellido
print(nombre_completo)
