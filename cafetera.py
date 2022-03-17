# Función para los reportes
def print_report():
    print(f'''
    The maquine have:
    water:  {water} [ml]
    milk:   {milk} [ml]
    sugar:  {sugar} [g]
    coffee: {coffee} [g]
    ''')

# Función para rellenar la máquina
def fill_machine():
    # Indicar que vamos a utilizar las variables globales
    global water, milk, sugar, coffee
    
    water_ml = int(input('How much water do you want to add? '))
    milk_ml = int(input('How much milk do you want to add? '))
    sugar_g = int(input('How much sugar do you want to add? '))
    coffee_g = int(input('How much coffee do you want to add? '))

    water += water_ml
    milk += milk_ml
    sugar += sugar_g
    coffee += coffee_g

    # Mostrar los nuevos valores
    print_report()

# Función que monitorea los ingredientes
def enough_resourses(drink_name):
    if drink_name == 'latte':
        return water >= 150 and milk >= 50 and sugar >= 15 and coffee >= 5
    elif drink_name == 'espresso':
        return water >= 200 and coffee >= 10
    elif drink_name == 'macchiatto':
        return water >= 150 and milk >= 80 and sugar >= 20 and coffee >= 8
 
# Función para preparar el café
def make_coffe(drink_name):
    global water, milk, sugar, coffee
    
    if enough_resourses(drink_name):
        if drink_name == 'latte':
            water -= 150
            milk -= 50
            sugar -= 15
            coffee -= 5
        elif drink_name == 'espresso':
            water -= 200
            coffee -= 10
        elif drink_name == 'macchiatto':
            water -= 150
            milk -= 80
            sugar -= 20
            coffee -= 8
        print(f"Here is your {drink_name}, enjoy!")
    else:
        print("There isn't enough recourses to make your coffee, sorry!")


coffee_machine = True

# Ingredientes que contiene el café
water = 500
milk = 300
sugar = 100
coffee = 40

# Bebidas
drinks = ['latte', 'espresso','macchiatto']

while coffee_machine:
    option = input('What would you like to have? (latte, espresso, macchiatto; e for exit) ')
    if option == 'e':
        print('Thank you, come again!')
        coffee_machine = False
    # Preparar la bebida
    elif option in drinks:
        make_coffe(option)
    # Agregar ingredientes
    elif option == 'fill':
        fill_machine()
    # Estado de los recursos de la máquina
    elif option == 'report':
        print_report()
    else:
        print('Try again!')