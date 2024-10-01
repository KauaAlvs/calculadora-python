import math

def calcular_sqrt(num):
    try:
        return math.sqrt(num)
    except ValueError:
        return "Erro: Não é possível calcular a raiz quadrada de um número negativo."

def calcular_log(num):
    return math.log10(num)

def calcular_fatorial(num):
    return math.factorial(num)

reiniciar = True

while reiniciar:
    print("Escolha uma operação:")
    print("1. Raiz Quadrada")
    print("2. Logaritmo na base 10")
    print("3. Fatorial")

    escolha = int(input("Digite o número correspondente à operação desejada: "))

    if escolha == 1:
        num = float(input("Digite um número: "))
        resultado = calcular_sqrt(num)
        print(f"A raiz quadrada de {num} é: {resultado}")
    elif escolha == 2:
        num = float(input("Digite um número: "))
        resultado = calcular_log(num)
        print(f"O logaritmo de {num} na base 10 é: {resultado}")
    elif escolha == 3:
        num = int(input("Digite um número inteiro: "))
        resultado = calcular_fatorial(num)
        print(f"O fatorial de {num} é: {resultado}")
    else:
        print("Escolha inválida. Por favor, digite um número válido correspondente à operação desejada.")

    opcao = input("Deseja reiniciar o programa? (s/n): ")
    if opcao.lower() != 's':
        reiniciar = False
    else:
        print("\n" * 3)

print("Programa encerrado.")