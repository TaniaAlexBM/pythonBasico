def conversor(tipoPesos, valorDolar):
    pesos = input('¿Cuántos pesos ' + tipoPesos + ' tienes? ')
    pesos = float(pesos)

    # convertir dolares a pesos colombianos
    dolares = pesos / valorDolar
    # reducir a dos decimales
    dolares = round(dolares, 2)

    # convertir los dolares a strings
    dolares = str(dolares)

    print('Tienes $' + dolares + ' dólares')

# Menú para que elija que moneda está utilizando
# Cadena de caracteres que toma en cuenta los saltos de línea
menu = """
Bienvenido al conversor de monedas 💰

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos

Elige una opción: 
"""

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 3875)
elif opcion == '2':
    conversor('argentinos', 65)
elif opcion == '3':
    conversor('mexicanos', 24)
else:
    print('Íngrsa una opción válida')



# dolar = input('¿Cuántos dólares tienes? ')
# dolar = float(dolar)

# valor_peso = 1 / valor_dolar

# peso = dolar / valor_peso
# peso = str(peso)

# print('Tienes $' + peso + ' pesos')