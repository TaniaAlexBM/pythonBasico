def palindromo(palabra):
    # quitar los espacios
    palabra = palabra.replace(' ', '')
    # pasar la palabra minúsculas
    palabra = palabra.lower()
    # guardar la palabra invertida
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return True
    else:
        return False


# función principal; también se puee llamar MAIN
def run():
    palabra = input('Escribe una palabra: ')
    esPalindromo = palindromo(palabra)
    if esPalindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


# Es un punto de entrada. Es buena práctica tenerlo
if __name__ == '__main__':
    run()