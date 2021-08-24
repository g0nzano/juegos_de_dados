import random
valor_minimo = 1
valor_maximo = 6

juego_otra_vez = "si"
while juego_otra_vez =="si" or juego_otra_vez == "s":
    print("Tirando los dados...")
    print("Los numeros son ...")
    print(random.randint(valor_minimo, valor_maximo))
    print(random.randint(valor_minimo, valor_maximo))
    juego_otra_vez = input("tira los dados otra vez")
