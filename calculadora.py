import numpy as np 
import matplotlib as plt 

#Menu para escolher 
def menu_principal():
    while True: 
        print("Calculadora RCM")
        print("1. Conjuntos Numéricos")
        print("2. Funções do 2º grau")
        print("3. Funções exponenciais")
        print("4. Matrizes")
        print("5. Saida")
        opcao = int(input("Escolha um opção: "))
        
        if opcao == "1":
            conjuntos_numericos()
        elif opcao == "2":
            funcoes_segundo_grau()
        elif opcao == "3":
            funcoes_exponenciais()
        elif opcao == "4":
            matrizes()
        elif opcao == "5":
            print("Saindo ...")
            break 
        else:
            print("Opção inválida, tente novamente.")

def conjuntos_numericos():
    def subconjuntos(a,b):
        #A função retorna verdadeira somente se "a" for subconjunto de "b" e se "a" for diferente de "b".
        #.issubset é a função para o subconjunto.
        return set(a). issubset(set(b)) and set(a) != set(b)
    def uniao(a,b):
        #Remove os números duplicados e ignora a ordem dos elementos.
        #.union retorna um conjunto com os elementos de "a" e "b"
        #list converte o conjunto em lista.
        return list(set(a).union(set(b)))
    def interseccao(a,b):
        #Remove os números duplicados e ignora a ordem dos elementos.
        #.intersection retorna um conjunto que possui apenas os elementos presentes tanto em "a" quanto em "b".
        #list converte o conjunto em lista.
         return list(set(a).intersection(set(b)))
    def diferenca(a, b):
        #.difference retorna um novo conjunto contendo os elementos que estão presentes em "a", mas não em "b".
        #list converte o conjunto em lista.
        return list(set(a).difference(set(b)))
    while True:
        # A função "split" em Python divide uma string em uma lista de substrings usando um delimitador especificado (ou espaços em branco por padrão).
        
        print("Conjuntos Numéricos")
        a = input("Informe os elementos do conjunto A separados por espaço: ").split()
        b = input("Informe os elementos do conjunto B separados por espaço: ").split()
        print("1. Verificar se A é subconjunto próprio de B")
        print("2. Realizar operação de União")
        print("3. Calcular intersecção")
        print("4. Calcular diferença")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")
        
        # "result" é usada em uma expressão condicional para determinar qual mensagem imprimir
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
            

def funcoes_segundo_grau():
    import math
    
    def calcular_raizes(a, b, c):
        delta = b**2 - 4*a*c
        if delta > 0:
            #"math.sqrt" é uma função do módulo "math" em Python que retorna a raiz quadrada de um número.
            num1 = (-b + math.sqrt(delta)) / (2*a)
            num2 = (-b - math.sqrt(delta)) / (2*a)
            return (num1, num2)
        elif delta == 0:
            x = -b / (2*a)
            return (x,)
        else:
            #Parte real.
            real = -b / (2*a)
            #Parte imaginaria
            imag = math.sqrt(-delta) / (2*a)
            return (f"{real} + {imag}i", f"{real} - {imag}i")
        
    def calcular_funcao(a, b, c, x):
        return a*x**2 + b*x + c
    
    def calcular_vertice(a, b, c):
        #xv = vertice x / yv = vertice y
        xv = -b / (2*a)
        yv = a*xv**2 + b*xv + c
        tipo = "mínimo" if a > 0 else "máximo"
        return (xv, yv, tipo)
    
     def gerar_grafico(a, b, c):
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(-10, 10, 400)#Esta função cria um array de números uniformemente espaçados em um intervalo especificado.
        y = a*x**2 + b*x + c
        
        plt.plot(x, y) #Esta função é usada para plotar o gráfico da função quadrática. 
        plt.title(f"f(x) = {a}x² + {b}x + {c}")#Esta função define o título do gráfico.
        plt.xlabel("x")# Esta função define o rótulo do eixo x do gráfico.
        plt.ylabel("f(x)")# Esta função define o rótulo do eixo y do gráfico.
        plt.grid(True)# Esta função ativa as linhas de grade no gráfico, facilitando a leitura dos valores.
        plt.axhline(0, color='black',linewidth=0.5)#Esta função adiciona uma linha horizontal (horizontal line) no gráfico no valor y=0. Ela é usada para representar o eixo y.
        plt.axvline(0, color='black',linewidth=0.5)#Esta função adiciona uma linha vertical (vertical line) no gráfico no valor x=0. Ela é usada para representar o eixo x.
        plt.show()#Esta função é usada para exibir o gráfico na tela. Ela mostra o gráfico que você criou usando as várias funções de plotagem do "matplotlib.pyplot".

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
        
        if opcao == '1':
            raizes = calcular_raizes(a, b, c)
            print(f"Raízes: {raizes}")
        elif opcao == '2':
            x = float(input("Informe o valor de x: "))
            resultado = calcular_funcao(a, b, c, x)
            print(f"f({x}) = {resultado}")
        elif opcao == '3':
            xv, yv, tipo = calcular_vertice(a, b, c)
            print(f"Vértice: ({xv}, {yv}), tipo: {tipo}")
        elif opcao == '4':
            gerar_grafico(a, b, c)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def funcoes_exponenciais():
    import math
    
    def verificar_crescimento(a, b):
        return "crescente" if b > 1 else "decrescente"
    
    def calcular_funcao(a, b, x):
        return a * (b ** x)
    
     def gerar_grafico(a, b):
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(-10, 10, 400)#Esta função cria um array de números uniformemente espaçados em um intervalo especificado.
        y = a*x**2 + b*x + c
        
        plt.plot(x, y) #Esta função é usada para plotar o gráfico da função quadrática. 
        plt.title(f"f(x) = {a}x² + {b}x + {c}")#Esta função define o título do gráfico.
        plt.xlabel("x")# Esta função define o rótulo do eixo x do gráfico.
        plt.ylabel("f(x)")# Esta função define o rótulo do eixo y do gráfico.
        plt.grid(True)# Esta função ativa as linhas de grade no gráfico, facilitando a leitura dos valores.
        plt.axhline(0, color='black',linewidth=0.5)#Esta função adiciona uma linha horizontal (horizontal line) no gráfico no valor y=0. Ela é usada para representar o eixo y.
        plt.axvline(0, color='black',linewidth=0.5)#Esta função adiciona uma linha vertical (vertical line) no gráfico no valor x=0. Ela é usada para representar o eixo x.
        plt.show()#Esta função é usada para exibir o gráfico na tela. Ela mostra o gráfico que você criou usando as várias funções de plotagem do "matplotlib.pyplot".

    while True:
        print("Funções Exponenciais")
        print("1. Verificar se é crescente ou decrescente")
        print("2. Calcular função em x pedido")
        print("3. Gerar gráfico")
        print("4. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")
        a = float(input("Informe o coeficiente a: "))
        b = float(input("Informe a base b: "))
        
        if opcao == '1':
            crescimento = verificar_crescimento(a, b)
            print(f"A função é {crescimento}")
        elif opcao == '2':
            x = float(input("Informe o valor de x: "))
            resultado = calcular_funcao(a, b, x)
            print(f"f({x}) = {resultado}")
        elif opcao == '3':
            gerar_grafico(a, b)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")