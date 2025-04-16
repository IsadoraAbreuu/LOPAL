# LISTA MÁRCIA 09/04

#EXERCICIO1
quantidade = 0
for numero in range(1,11):
    numeros = int(input("Digite um número: "))
    if numeros % 3 == 0:
        quantidade += 1
print("A quantidade de números múltiplos de 3, dentro desses 10, são", quantidade)

#EXERCICIO2
senha = "isadoradiva"
while True:
    tentativa = input("Digite a senha (apenas letras): ")
    if tentativa == senha:
        print("Arrasou, senha correta! Acesso Liberado.")
        break

#EXERCICIO3
menu = int(input("Escolha uma das operações abaixo: \n"
                 "[1] ADIÇÃO\n"
                 "[2] SUBTRAÇÃO\n"
                 "[3] MULTIPLICAÇÃO\n"
                 "[4] DIVISÃO\n"
                 "[5] SAIR\n"
                 "Opção escolhida: "))
while menu != 5:
    menu = int(input("Escolha uma das operações abaixo: \n"
                 "[1] ADIÇÃO\n"
                 "[2] SUBTRAÇÃO\n"
                 "[3] MULTIPLICAÇÃO\n"
                 "[4] DIVISÃO\n"
                 "[5] SAIR\n"
                 "Opção escolhida: "))
    if menu == 5:
        print("Você saiu do menu. Volte sempre!")
        break

#EXERCICIO4
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

for numero in range(numero1,numero2+1):
    if numero <= 1:
        continue
    for num in range(2, numero):
        if numero % num == 0:
            break
    else:
        print(f"{numero} é primo.")

#EXERCICIO5
senha_correta = "isadoradiva"
tentativas = 3
while tentativas > 0:
    senha = input("Digite a senha (apenas letras): ")
    tentativas -= 1
    if senha == senha_correta:
        print("Arrasou, senha correta! Acesso Liberado.")
        break
    elif tentativas > 0:
        print(f"Ixi, senha incorreta. Você ainda tem {tentativas} tentativas.")
    elif senha != senha_correta:
        print("Senha incorreta nas 3 tentativas. Acesso bloqueado.")
        break

#EXERCICIO6
impares = []
pares = []
for i in range(1,11):
    numero = int(input(f"{i} - Digite um número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"\nOs números ímpares são: {impares}")
print(f"Os números pares são: {pares}")

#EXERCICIO7
frase = input("Digite uma frase: ").lower()
vogais = ["a", "e", "i", "o", "u"]
a = 0
e = 0
i = 0
o = 0
u = 0
for letra in frase:
    if letra == "a":
        a += 1
    if letra == "e":
        e += 1
    if letra == "i":
       i += 1
    if letra == "o":
        o += 1
    if letra == "u":
        u += 1
print(f"A frase {frase} tem: ")
print(f"{a} letras 'a'\n")
print(f"{e} letras 'e'\n")
print(f"{i} letras 'i'\n")
print(f"{o} letras 'o'\n")
print(f"{u} letras 'u'\n")

#EXERCICIO 8
import random
jogo = ['cara', 'coroa']
condicao = 'cara'
contador = 0
while contador < 3:
    cara_ou_coroa = random.choice(jogo)
    print(f"A moeda caiu em {cara_ou_coroa} nesse lançamento.")
    if cara_ou_coroa == condicao:
        contador += 1
    if contador == 3:
        print(f"A moeda caiu na {condicao} 3 vezes seguidas.")
        break

#EXERCICIO9
numeros = []
menores_media = 0
tamanho_lista = int(input("Digite a quantidade de números que deseja na lista: "))
for i in range(tamanho_lista):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

if numeros:
    media = sum(numeros) / len(numeros)
else:
    media = 0

for n in numeros:
    if n < media:
        menores_media += 1
print(f"A média dos números é: {media}")
print(f"A quantidade de números menores que a média de {media} é: {menores_media}")

#EXERCICIO10
numeros = []
menor = float('inf')
segundo_menor = float('inf')
tamanho_lista = int(input("Digite a quantidade de números que deseja na lista: "))
for i in range(1,tamanho_lista+1):
    numero = int(input("Digite um número inteiro positivo: "))
    numeros.append(numero)

for numero in numeros:
    if numero < menor:
        segundo_menor = menor
        menor = numero
    elif numero < segundo_menor and numero != menor:
        segundo_menor = numero
print("O segundo menor número da lista é: ",segundo_menor)

#DESAFIO 1
populacao_inicial = int(input("Digite o número inicial de coelhos: "))
taxa_reproducao = float(input("Digite a taxa de reprodução (ex: 0.2 para 20%): "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade (ex: 0.1 para 10%): "))
numero_geracoes = int(input("Digite o número de gerações que deseja simular: "))
populacao = populacao_inicial
for geracao in range(1, numero_geracoes+1):
    nascimentos = populacao * taxa_reproducao
    mortes = populacao * taxa_mortalidade
    populacao = populacao + nascimentos - mortes
    populacao = max(0,int(populacao)) #deixa em número inteiro e garante que a população nao fique negativa
    print(f"Geração {geracao}: {populacao} coelhos")

#DESAFIO 2
import random

palavras = ['banana', 'maça', 'amora', 'goiaba', 'pera', 'melancia', 'abacaxi', 'mamão', 'kiwi', 'laranja', 'mexerica', 'jaca']
palavra_oculta = random.choice(palavras)
tentativas = 6
letras_erradas = []
letras_corretas = ['_'] * len(palavra_oculta)

while tentativas > 0 and '_' in letras_corretas:
    print("FORCA - TEMA FRUTAS")
    print("-------------------------------")
    print(f"Palavra: {' '.join(letras_corretas)}")
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")
    letra = input("Digite uma letra: ").lower()

    if letra in letras_erradas or letra in letras_corretas:
        print(f"Você já tentou a letra '{letra}'. Tente outra.\n")
        continue
    if letra in palavra_oculta:
        print(f"Boa! A letra '{letra}' está na palavra.\n")
        for i in range(len(palavra_oculta)):
            if palavra_oculta[i] == letra:
                letras_corretas[i] = letra
    else:
        print(f"A letra '{letra}' não está na palavra.\n")
        letras_erradas.append(letra)
        tentativas -= 1
if '_' not in letras_corretas:
    print("-------------------------------")
    print(f"Parabéns! Você adivinhou a palavra: {palavra_oculta}")
else:
    print("-------------------------------")
    print(f"Você perdeu! A palavra era: {palavra_oculta}")

