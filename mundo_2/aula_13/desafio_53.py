''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona

frase = str(input("Palíndromo: \n"))
frase = "".join(frase.split(" "))

if frase == frase[::-1]:
    print("A palavra {} é um palíndromo.".format(frase))
else:
    print("A palavra {} não é um palíndromo.".format(frase))
