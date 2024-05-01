import random

# ===== FUNÇÃO QUE DEFINE UM DICIONARIO QUE ARMAZENA TODOS OS STATUS DO PLAYER =====
def criarPlayer():
    return {'posicao': 0, 'filhos': 0, 'casado': False, 'formado': False, 'dinheiro': 0, 'famoso': False, 'vivo': True}

# ===== FUNÇÃO QUE DEFINE O DADO DO JOGO =====
def dice(player): 
    result = random.randint(1, 6)
    print(f"Você lançou o dado! Resultado: {result}")
    return result

# ===== FUNÇÃO PARA DEFINIR TER UM FILHO =====
def terFilho(player):
    print('')
    print("Wow! Você terá um filho!")
    print('')
    resultado = dice(player)
    if resultado != 5:
        player['filhos'] += 2
        print('')
        print("Parabéns! Você teve um filho.")
        print('')
    else:
        player['filhos'] += 1
        print('')
        print("Parabéns! Você teve gêmeos.")
        print('')

# ===== FUNÇÃO PARA DEFINIR FICAR FAMOSO =====
def ficarFamoso(player):
    if player['famoso'] == False:
        player['famoso'] = True
        print("Olha só! Você ficou famoso!")
    else:
        print('Mais fama? Você já é famoso!')

# ===== FUNÇÃO PARA DEFINIR O NOVO AMOR =====
def novoAmor(player):
    if player['casado'] == False:
        print("Que sorte! Você encontrou um novo amor.")
        player['casado'] = True
    else:
        pass

# ===== FUNÇÃO PARA DEFINIR A MAQUINA DO TEMPO =====
def maquinaDoTempo(player):
    print("Você caiu na máquina do tempo!")
    print("Que azar! Você voltou para o início.")
    player['posicao'] = 0

# ===== FUNÇÃO PARA DEFINIR O CASAMENTO =====
def casamento(player):
    print('')
    print('Wow! Você irá se casar. Meu parabéns!')
    print('')
    if player['casado'] == False:
        print('')
        print("Incrível! Você se casou!")
        print('')
    else:
        print('Você já está casado!')



# ===== FUNÇÃO PARA DEFINIR FORMATURA E NO QUE O PLAYER IRÁ SE FORMAR =====    
def formatura(player): 
    print("Se formou!!! Gire a roleta e decida cursos para os 6 seguintes valores:\n1 - Medicia\n2 - Direito\n3 - História\n4 - Arquitetura\n5 - Engenharia\n6 - Segurança da informação\n")
    result = dice(player)
    if result == 1:
        if player['formado'] == False:
            print('Parabens! Você se formou em Medicina.')
            player['formado'] == True
        else:
            print("Você já está formado!")
    if result == 2:
        if player['formado'] == False:
            print('Parabens! Você se formou em Direito.')
            player['formado'] == True
        else:
            print("Você já está formado!")
    if result == 3:
        if player['formado'] == False:
            print('Parabens! Você se formou em História.')
            player['formado'] == True
        else:
            print("Você já está formado!")
    if result == 4:
        if player['formado'] == False:
            print('Parabens! Você se formou em Arquitetura.')
            player['formado'] == True
        else:
            print("Você já está formado!")
    if result == 5:
        if player['formado'] == False:
            print('Parabens! Você se formou em Engenharia.')
            player['formado'] == True
        else:
            print("Você já está formado!")
    if result == 6:
        if player['formado'] == False:
            print('Parabens! Você se formou em Segurança da Informação (a melhor).')
            player['formado'] == True
        else:
            print("Você já está formado!")

# ===== DESAFIO MATEMATICO =====
def desafioMatematico(player):
    print("Legal!\nVocê caiu no desafio matemático!")
    result = dice(player)
    if result == 1:
        print("1) Mostrar na tela os números primos até 100:")
        print('')
        imprimirPrimos()
    elif result == 2:
        print("2) Fazer o somatório dos números de 1 a 10:")
        print('')
        resultado = somatorio1a10()
        print("O somatório dos números de 1 a 10 é:",resultado)
    elif result == 3:
        print("3) Imprimir a série de Fibonacci até o décimo elemento:")
        print('')
        fibo(10)
        print('')
    elif result == 4:
        print("4) Calcular a área de um círculo com raio 2.5:")
        print('')
        raio = 2.5
        area = 3.14 * raio ** 2
        print("A área de um circulo equivale a:",area)
    elif result == 5:
        print("5. Imprimir o fatorial de 5:")
        print('')
        fat = fatorial(5)
        print("O fatorial de 5 é:",fat)
    elif result == 6:
        print("6) Imprimir os 5 primeiros números divisíveis por 2 e por 5")
        print('')
        divisiveisPor2e5()       
        print('')

def somatorio1a10(): # Função para executar o somatório dos números de 1 a 10; usado no desafio matemático
    soma = 0
    for numero in range(1, 11):
        soma += numero
    return soma

def fibo(n, a=0, b=1): # Função para executar a serie de Fibonacci; usado no desafio matematico
    if n == 0:
        return
    print(a, end=" ")
    fibo(n-1, b, a+b)

def fatorial(n): # Função que realiza o fatorial de 5; usado no desafio matematico
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def divisiveisPor2e5(): # Função que imprime os 5 primerios numeros divisiveis por 2 e 5; usado no desafio matematico
    i = 0
    num = 1
    while i < 5:
        if num % 2 == 0 and num % 5 == 0:
            print(num)
            i += 1
        num += 1

def primo(num): # Função para definir se um numero é primo ou não; complemento de "Mostrar na tela os números primos até 100"
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def imprimirPrimos(): # Função que mostra na tela todos os numeros primos até 100; usado no desafio matematico
    for numero in range(2, 101):
        if primo(numero):
            print("Os números primos até 100 são:")
            print(numero, end=" ")



# ===== FUNÇÃO PARA DEFINIR GANHAR NA LOTERIA E QUANTO QUE ELE GANHOU DE DINHEIRO =====
def loteria(player):       
    print("Você vai apostar na loteria!")
    print('')
    result = dice(player)
    if result == 1:
        print('Você ganhou R$2.50!!')
        player['dinheiro'] += 2.50
    if result == 2:
        print('Você ganhou R$5.000!!')
        player['dinheiro'] + 5000
    if result == 3:
        print('Você ganhou R$50.000!!')
        player['dinheiro'] + 50000
    if result == 4:
        print('Você ganhou R$500.000!!')
        player['dinheiro'] + 500000
    if result == 5:
        print('Você ganhou R$5.000.000!!')
        player['dinheiro'] + 5000000
    if result == 6:
        print('Você ganhou R$100.000.000!!')
        player['dinheiro'] + 100000000
    


#===== FUNÇÃO PARA MOSTRAR OS SATUS DO JOGADOR ASSIM QUE GANHAR =====
def fim(player):
    print("----------------------------------")
    print("       STATUS DO JOGADOR")
    print("----------------------------------")
    print(f"Quantidade de filhos: {player['filhos']}")
    print(f"Casado: {player['casado']}")
    print(f"Total de dinheiro: {player['dinheiro']}")
    print(f"Famoso: {player['famoso']}")
    print(f"Formado:{player['formado']}")
    print("----------------------------------")

#===== FUNÇÃO PARA DEFINIR O FLUXO DE JOGO =====
def pos(player):
    posPlayer = player['posicao']
    if posPlayer == 1:
        print("Role o dado novamente!.")
    elif posPlayer == 2:
        print("===============")
        print(" VOCÊ MORREU :(")
        print("===============")
        player['vivo'] = False
    elif posPlayer == 3:
        print("Role o dado novamente.")
    elif posPlayer == 4:
        desafioMatematico(player)
    elif posPlayer == 5:
        formatura(player)
    elif posPlayer == 6:
        terFilho(player)
    elif posPlayer == 7:
        casamento(player)
    elif posPlayer == 8:
        print("===============")
        print(" VOCÊ MORREU :(")
        print("===============")
        player['vivo'] = False
    elif posPlayer == 9:
        terFilho(player)
    elif posPlayer == 10:
        print("Role o dado novamente.")
    elif posPlayer == 11:
        desafioMatematico(player)
    elif posPlayer == 12:
        print("Que triste! Você se divorciou :(")
        player['casado'] = False
    elif posPlayer == 13:
        terFilho(player)
    elif posPlayer == 14:
        loteria(player)    
    elif posPlayer == 15:
        ficarFamoso(player)
    elif posPlayer == 16:
        novoAmor(player)
    elif posPlayer == 17:
        print("Role o dado novamente.")
    elif posPlayer == 18:
        print("===============")
        print(" VOCÊ MORREU :(")
        print("===============")
        player['vivo']= False
    elif posPlayer == 19:
        desafioMatematico(player)
    elif posPlayer == 20:
        maquinaDoTempo(player)    

#===== FUNÇÃO PARA INICIAR O JOGO E DETECTAR SE ALGUM JOGADOR MORREU =====
def game():
    Player1 = criarPlayer()
    Player2 = criarPlayer()
    print('========================')
    print('     JOGO DA VIDA')     
    print('========================')    

    # ===== LOOP PRINCIPAL DO JOGO =====
    while Player1['vivo'] == True or Player2['vivo'] == True:
        print('')
        input(f"Player |1| (Casa: {Player1['posicao']}):\n Pressione 'ENTER' para jogar:")
        print('')
        Player1['posicao'] += dice(Player1)
        pos(Player1)
        if Player1['posicao'] >= 21 or Player2['vivo'] == False:
            print("====================")
            print("       FIM!")
            print("====================") 
            print(" Você teve uma vida longa e próspera!")
            fim(Player1)
            break
        
        print('')
        input(f"Player |2| (Casa {Player2['posicao']}):\n Pressione 'ENTER' para jogar:")
        print('')
        Player2['posicao'] += dice(Player2)
        pos(Player2)
        if Player2['posicao'] >= 21 or Player1['vivo'] == False:
            print("====================")
            print("       FIM!")
            print("====================") 
            print(" Você teve uma vida longa e próspera!")
            fim(Player2)
            break

################ PROGRAMA PRINCIPAL ###############
game()


