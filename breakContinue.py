def run():
    # CONTINUE
    for contador in range(100):
        if contador % 2 != 0:
            continue
            # Lo que está después de CONTINUE no se realiza si el condicional de If es verdadero
        print(contador)

    # BREAK
    for i in range(100):
        print(i)
        if i == 45:
            break
        # Break corta el ciclo cuando el condicional de if es verdadero

    # Break con Strings
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

    # Break, Continue con While
    LIMITE = 200
    contador = 0
    print(contador)
    while contador < LIMITE:
        contador += 1
        if contador == 60:
            continue
        elif contador == 70:
            break
        print(contador)

    
if __name__ == '__main__':
    run()