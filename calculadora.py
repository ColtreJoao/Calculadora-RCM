import numpy as np
import matplotlib.pyplot as plt

def menuPrincipal():
    while True: 
        print("Calculadora RCM")
        print("1. Conjuntos Numéricos")
        print("2. Funções do 2º grau")
        print("3. Funções exponenciais")
        print("4. Matrizes")
        print("5. Saida")
        opcao = int(input("Escolha um opção: "))
        
        if opcao == 1:
            conjuntosNumericos()
        elif opcao == 2:
            funcoesSegundoGrau()
        elif opcao == 3:
            funcoesExponenciais()
        elif opcao == 4:
            matrizes()
        elif opcao == 5:
            print("Saindo...")
            break 
        else:
            print("Opção inválida, tente novamente.")

def conjuntosNumericos():
    def subconjuntos(a, b):
        return set(a).issubset(set(b)) and set(a) != set(b)

    def uniao(a, b):
        return list(set(a).union(set(b)))

    def interseccao(a, b):
        return list(set(a).intersection(set(b)))

    def diferenca(a, b):
        return list(set(a).difference(set(b)))

    while True:
        print("Conjuntos Numéricos")
        a = input("Informe os elementos do conjunto A separados por espaço: ").split()
        b = input("Informe os elementos do conjunto B separados por espaço: ").split()
        print("1. Verificar se A é subconjunto próprio de B")
        print("2. Realizar operação de União")
        print("3. Calcular intersecção")
        print("4. Calcular diferença")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            result = subconjuntos(a, b)
            print("A é subconjunto próprio de B" if result else "A não é subconjunto próprio de B")
        elif opcao == '2':
            result = uniao(a, b)
            print(f"União: {result}")
        elif opcao == '3':
            result = interseccao(a, b)
            print(f"Intersecção: {result}")
        elif opcao == '4':
            result = diferenca(a, b)
            print(f"Diferença: {result}")
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def funcoesSegundoGrau():
    import math

    def calcularRaizes(a, b, c):
        delta = b**2 - 4*a*c
        if delta > 0:
            num1 = (-b + math.sqrt(delta)) / (2*a)
            num2 = (-b - math.sqrt(delta)) / (2*a)
            return (num1, num2)
        elif delta == 0:
            x = -b / (2*a)
            return (x,)
        else:
            real = -b / (2*a)
            imag = math.sqrt(-delta) / (2*a)
            return (f"{real} + {imag}i", f"{real} - {imag}i")

    def calcularFuncao(a, b, c, x):
        return a*x**2 + b*x + c

    def calcularVertice(a, b, c):
        xv = -b / (2*a)
        yv = a*xv**2 + b*xv + c
        tipo = "mínimo" if a > 0 else "máximo"
        return (xv, yv, tipo)

    def gerarGrafico(a, b, c):
        
        x = np.linspace(-10, 10, 400)
        y = a*x**2 + b*x + c
        
        plt.plot(x, y)
        plt.title(f"f(x) = {a}x² + {b}x + {c}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.show()

    while True:
        print("Funções do 2º")
        print("1. Calcular raízes")
        print("2. Calcular função em x pedido")
        print("3. Calcular Vértice")
        print("4. Gerar gráfico")
        print("5. Voltar ao menu principal")
        a = float(input("Informe o coeficiente a: "))
        b = float(input("Informe o coeficiente b: "))
        c = float(input("Informe o coeficiente c: "))
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            raizes = calcularRaizes(a, b, c)
            print(f"Raízes: {raizes}")
        elif opcao == 2:
            x = float(input("Informe o valor de x: "))
            resultado = calcularFuncao(a, b, c, x)
            print(f"f({x}) = {resultado}")
        elif opcao == 3:
            xv, yv, tipo = calcularVertice(a, b, c)
            print(f"Vértice: ({xv}, {yv}), tipo: {tipo}")
        elif opcao == 4:
            gerarGrafico(a, b, c)
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")

def funcoesExponenciais():

    def verificarCrescimento(a, b):
        return "crescente" if b > 1 else "decrescente"

    def calcularFuncao(a, b, x):
        return a * (b ** x)

    def gerarGrafico(a, b):
        
        x = np.linspace(-10, 10, 400)
        y = a * (b ** x)
        
        plt.plot(x, y)
        plt.title(f"f(x) = {a} * ({b} ** x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.show()

    while True:
        print("Funções Exponenciais")
        print("1. Verificar se é crescente ou decrescente")
        print("2. Calcular função em x pedido")
        print("3. Gerar gráfico")
        print("4. Voltar ao menu principal")
        a = float(input("Informe o coeficiente a: "))
        b = float(input("Informe a base b: "))
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            crescimento = verificarCrescimento(a, b)
            print(f"A função é {crescimento}")
        elif opcao == 2:
            x = float(input("Informe o valor de x: "))
            resultado = calcularFuncao(a, b, x)
            print(f"f({x}) = {resultado}")
        elif opcao == 3:
            gerarGrafico(a, b)
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

def matrizes():
    while True:
        print("Operações com Matrizes")
        print("1. Soma de Matrizes")
        print("2. Subtração de Matrizes")
        print("3. Multiplicação de Matrizes")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            matrizA = np.array(eval(input("Digite a matriz A no formato [[a11, a12, ...], [a21, a22, ...], ...]: ")))
            matrizB = np.array(eval(input("Digite a matriz B no formato [[b11, b12, ...], [b21, b22, ...], ...]: ")))
            if matrizA.shape == matrizB.shape:
                print("Resultado da soma:\n", matrizA + matrizB)
            else:
                print("As matrizes devem ter as mesmas dimensões para realizar a soma.")
        elif opcao == 2:
            matrizA = np.array(eval(input("Digite a matriz A no formato [[a11, a12, ...], [a21, a22, ...], ...]: ")))
            matrizB = np.array(eval(input("Digite a matriz B no formato [[b11, b12, ...], [b21, b22, ...], ...]: ")))
            if matrizA.shape == matrizB.shape:
                print("Resultado da subtração:\n", matrizA - matrizB)
            else:
                print("As matrizes devem ter as mesmas dimensões para realizar a subtração.")
        elif opcao == 3:
            matrizA = np.array(eval(input("Digite a matriz A no formato [[a11, a12, ...], [a21, a22, ...], ...]: ")))
            matrizB = np.array(eval(input("Digite a matriz B no formato [[b11, b12, ...], [b21, b22, ...], ...]: ")))
            if matrizA.shape[1] == matrizB.shape[0]:
                print("Resultado da multiplicação:\n", np.dot(matrizA, matrizB))
            else:
                print("O número de colunas da matriz A deve ser igual ao número de linhas da matriz B para realizar a multiplicação.")
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")
menuPrincipal()
