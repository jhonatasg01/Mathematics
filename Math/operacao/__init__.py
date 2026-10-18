from random import randint

def simb(opera):
    match opera:
        case 1: return "+"
        case 2: return "-"
        case 3: return "x"
        case 4: return "/"
        case 5: return ","
        case _: return "?"

def nivel_tabuadas(valor):
    match valor:
        case 1:
            return randint(1, 10)
        case 2:
            return randint(11, 50)
        case 3:
            return randint(51, 100)
        case _:
            return None

def opcao(opera, tabuadas=0, num=0):
    """
    -> Função para calcular a resposta e lógica do programa
    :param opera: Resposta da escolha no menu inicial.
    :param tabuadas: Número aleatório gerado pelo nível de dificuldade escolhido pelo usuário.
    :param num: Esse e um valor aleatório de 1 a 10 sem repetição (No programa principal e
    gerado 10 vezes para as questões).
    :return: Retorna a resposta do calculo.
    """
    match opera:
        case 1:
            return num + tabuadas
        case 2:
            return num - tabuadas
        case 3:
            return num * tabuadas
        case 4:
            if tabuadas == 0:
                return 0 #evitando divisão por 0
            return round(num / tabuadas, 2)
        case 5:
            #Resposta das sequências lógicas da função sequencias_log()
            seq = sequencias_log()
            resposta = seq[7]
            return resposta
        case _:
            return None

def sequencias_log():
    logica = randint(2, 4)
    n1 = 3
    n2 = n1 + logica
    sequencia = []

    #Coloca a sequência dentro da lista
    ## 3, 7, 11, 15, 19, ...
    for _ in range(8):
        sequencia.append(n1)
        #Faz a soma pela variável "logica"
        n1, n2 = n2, n2 + logica
    #Mostra na tela a sequência
    for i, valor in enumerate(sequencia[:5]):
        print(f"\033[0;41m{valor},", end=" ")
    print("...\033[m")
    return sequencia
