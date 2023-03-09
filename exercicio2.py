def main():
    num = int(input("Digite um número: "))
    print_fibonacci(num)


def print_fibonacci(num):
    fibonacci = [0, 1]

    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    if num in fibonacci:
        print(str(num) + " pertence à sequência de Fibonacci!")
    else:
        print(str(num) + " não pertence à sequência de Fibonacci!")


main()
