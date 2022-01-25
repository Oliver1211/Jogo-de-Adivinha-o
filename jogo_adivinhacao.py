palavra_secreta = 'inconstitucionalidade'.upper()
lista = []
rodada = 1
tentativas = 6

print('Jogo da Forca')
print()

while rodada <= tentativas:

    letra = input('Digite uma palvra ').upper().strip()
    lista.append(letra)

    if letra in palavra_secreta:
        print(f'Parabéns, a letra "{letra}" faz parte da palavra secreta, você está na {rodada} tentativa e possui {tentativas}')
    else:
        print(f'Que pena, a letra não faz parte da palavra secreta, você está na {rodada} tentativa e possui {tentativas}')
        lista.pop()

    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in lista:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == palavra_secreta:
        print(f'Parabéns você GANHOU!!! a palavra secreta é "{palavra_secreta}"')
        break
    else:
        print(secreto_temporario)

    if letra not in palavra_secreta:
        rodada += 1

    if rodada > tentativas:
        print(f'Suas chances acabaram, a palavra secreta era "{palavra_secreta}"')
        break
