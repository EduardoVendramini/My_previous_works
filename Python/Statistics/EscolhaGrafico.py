# Escolha dos gráficos de Controle Estatístico do Processo

opcao = 1

while opcao != 0:
    print("Bem vindo ao menú para escolha do gráfico")
    print("de Controle Estatístico do Processo!\n")
    print("Por favor selecione uma das opções:\n")
    print("As variáveis são contínuas ou discretas?\n")
    print("1: Contínuas\n")
    print("2: Discretas\n")
    print("0: Sair\n")
    opcao = input()
    opcao = int(opcao)
    
    if opcao == 1:
        print("Qual o tamanho das amostras?\n")
        print("1: n = 1\n")
        print("2: 1 < n < 11\n")
        print("3: n > 10\n")
        print("0: Sair\n")
        opcao = input()
        opcao = int(opcao)
        if opcao == 1:
            print("Gráficos X e mR\n")
            opcao = 0
        if opcao == 2:
            print("Gráficos X barra e R\n")
            opcao = 0
        if opcao == 3:
            print("Gráficos X barra e S\n")
            opcao = 0

    if opcao == 2:
        print("As amostras apresentam mais de um defeito\n")
        print("por unidade?\n")
        print("1: Sim.")
        print("2: Não.")
        print("0: Sair\n")
        opcao = input()
        opcao = int(opcao)
        if opcao == 1:
            print("As amostras têm o mesmo tamanho?")
            print("1: Sim.")
            print("2: Não.")
            print("0: Sair\n")
            opcao = input()
            opcao = int(opcao)
            if opcao == 1:
                print("Gráfico C")
                opcao = 0
            if opcao == 2:
                print("Gráfico U")
                opcao = 0
        if opcao == 2:
            print("As amostras têm o mesmo tamanho?")
            print("1: Sim.")
            print("2: Não.")
            print("0: Sair\n")
            opcao = input()
            opcao = int(opcao)
            if opcao == 1:
                print("Gráfico np")
                opcao = 0
            if opcao == 2:
                print("Gráfico p")
                opcao = 0

    if opcao == 0:
        print("Obrigado! Processo finalizado.")
