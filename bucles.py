def run():
    # Para definir las constantes, se escriben en mayúsculas
    LIMITE = 1000
    
    contador = 0
    potencia2 = 2**contador
    # Mientras la potencia sea menor al límite, se va a ejecutar el bloque de código que sigue al WHILE
    while potencia2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a ' + str(potencia2))
        # Si no se pone un límite, el While sera infinito
        contador = contador + 1
        potencia2 = 2**contador


if __name__ == '__main__':
    run()