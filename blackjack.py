# BlackJack:
# * Una persona reparte las cartas, por pares
# * Quién tenga 21 puntos o más se acerque, gana

import blackjack_art as data
import random

print(data.logo)

player_hand = list()
computer_hand = list()
want_card = True

# De forma aleatoria tomamos dos valores de la lista de cartas
# para cada jugador
player_hand.append(random.choice(data.cards))
player_hand.append(random.choice(data.cards)) 

computer_hand.append(random.choice(data.cards)) 
computer_hand.append(random.choice(data.cards)) 

if sum(computer_hand) == 21:
    print('Wow! Computer wins with a lucky blackjack!')
    want_card = False
elif sum(player_hand) == 21:
    print('Lucky! You won with a blackjack!')
    want_card = False

# Si en la primera mano, alguno de los dos saca más de 21: se debe cambiar el 11 por 1.
# ! Serán independientes porque puede ser que ambas manos cumplan sus condicionales
if sum(computer_hand) > 21:
    computer_hand.pop()
    computer_hand.append(1)

if sum(player_hand) > 21:
    player_hand.pop()
    player_hand.append(1)

while want_card:
    print(f'''Your cards: {player_hand}
    current score: {sum(player_hand)}
    ''')

    print(f"""Computer's first card: {computer_hand[0]}""")

    if sum(player_hand) > 21:
        want_card = False
        continue
    # Preguntar si se quiere otra carta
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == 'y':
        player_hand.append(random.choice(data.cards))
        if player_hand[-1] == 11 and sum(player_hand) > 21:
            player_hand.pop()
            player_hand.append(1)
    else:
        want_card = False

print(f"""Your final hand: {player_hand}
final score: {sum(player_hand)}""")

if sum(player_hand) < 21:
    while sum(computer_hand) < 21 and sum(computer_hand) < sum(player_hand):
        computer_hand.append(random.choice(data.cards))
        if computer_hand[-1] == 11 and sum(computer_hand) > 21:
            computer_hand.pop()
            computer_hand.append(1)

print(f"""Computer final hand: {computer_hand}
final score: {sum(computer_hand)}""")

if sum(player_hand) == sum(computer_hand):
    print("It's draw!")
elif sum(computer_hand) == 21:
    print("Computer won with a blackjack!")
elif sum(player_hand) == 21:
    print("Player won with a blackjack!")
elif sum(player_hand) > 21:
    print("Your hand is over 21, you lose!")
elif sum(computer_hand) > 21:
    print("Computer hand is over 21, you win!")
elif sum(player_hand) > sum(computer_hand):
    print("You win!")
else:
    print("You lose!")