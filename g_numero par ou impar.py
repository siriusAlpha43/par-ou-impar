while True:
    try:
        num = int(input("Digite um número: "))
        if num % 2 == 0:
            print("O número digitado é par.")
            break

        else:
            print("O numero digitado é impar.")
            break

    except ValueError:
        print("Digite um número válido.")    