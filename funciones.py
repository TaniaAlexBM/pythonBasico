# Función
def imprimirMensaje():
    # Bloque de código
    print('Mensaje especial: ')
    print('Estoy aprendiendo funciones')

imprimirMensaje()
imprimirMensaje()
imprimirMensaje()


# Funciones con parámetros
opcion = input('Elige un opción (1,2,3): ')
if opcion == '1':
    print('Hola')
    print('¿Cómo estás?')
    print('Elegiste la opción 1')
    print('Adiós')
elif opcion == '2':
    print('Hola')
    print('¿Cómo estás?')
    print('Elegiste la opción 2')
    print('Adiós')
elif opcion == '3':
    print('Hola')
    print('¿Cómo estás?')
    print('Elegiste la opción 3')
    print('Adiós')
else:
    print('Opción inválida')

# función con parámetros
def conversacion(mensaje):
    print('Hola')
    print('¿Cómo estás?')
    print(mensaje)
    print('Adiós')
opcion1 = input('Elige una opción (1,2,3): ')
if opcion1 == '1':
    conversacion('Elegiste la opción 1')
elif opcion1 == '2':
    conversacion('Elegiste la opción 2')
elif opcion1 == '3':
    conversacion('Elegiste la opción 3')
else:
    conversacion('Opción inválida')


# Return
def suma(a,b):
    print('Se suman dos números')
    resultado = a + b
    # devuelve el resultado
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)