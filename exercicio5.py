def main():
    string = input("Digite uma string: ")
    inverter_string(string)


def inverter_string(string):
    # Usando o operador de slicing [::-1] para inverter a string
    string_invertida = string[::-1]

    print("A string invertida é:", string_invertida)


main()
