import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Guardar en una lista las opciones
options = [rock, paper, scissors]

# Pedir la opción al usuario
option = int(input('What do you choose?\n0: rock\n1: paper\n2: scissors\n'))

# Asegurarnos de que el valor que dé el usuario es una opción válida
if -1 < option < 3:
    print('You choose\n')
    # Imprimir la opción del usuario
    print(options[option])

    # El programa elegirá una opción
    com_option = random.randint(0, 2) # incluye al cero y al dos en el rango
    print('Computer chose:\n')
    print(options[com_option])

    # Ajustar las opciones, para saber quién gana
    adjusted_option = (option + 1) % 3
    adjusted_com_option = (com_option + 1) % 3

    if option == com_option:
        print('Draw!')
    elif adjusted_option == com_option:
        print('Computer wins!')
    elif adjusted_com_option == option:
        print('You win!')
else:
    print('Invalid option, you lose')