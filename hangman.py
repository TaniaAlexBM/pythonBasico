# Importar el archivo
import hangman_art as art
import random

# palabras para jugar
words = ['Python','Ruby','JavaScript', 'Java', 'Rust']

# cuántos stage tiene
n_stage = len(art.stages) # 7
lives = 7

# Elegir una palabra la azar
word = random.choice(words).lower()

# mostrar sólo los espacios que ocuparía la palabra
word_hidden = list('_' * len(word))
print(''.join(word_hidden))


# Muestra el logo
print(art.logo)

game_on = True

# Preguntarle al usuario una palabra
while game_on:
    letter = input('Gues a letter: ').lower()
    print(f'You said guessed {letter}')

    # Si la letra no está en la palabra
    if letter not in word:
        lives -= 1
        print(f"You guessed {letter}, that's not in the word. You lose a life!")
        if lives == 1:
            print('The game is over!')
            print(f'The word was {word}')
            game_on = False
    # Cuando la letra está en la palabra oculta
    elif letter in word:
        print(f'You already guessed {letter}')

    # Sustituir la palabra en los guiones
    for i in range(len(word)):
        if word[i] == letter:
            word_hidden[i] = letter

    # Comprobar si la palabra oculta tiene guiones sin llenar
    if '_' not in word_hidden:
        print('You win!')
        game_on = False

    # Estado de la palabra
    print(" ".join(word_hidden))
    print(art.stages[n_stage - lives])

    # Opción para salir del juego
    if letter == 'exit':
        game_on = False
        print('The game is over!')