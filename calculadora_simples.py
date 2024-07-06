#Calculadora que detecta a operação sem que o usuário precise informar o que é.
while True:
    print('Bem vindo / Welcome!\n')
    print("""Choose your option / Escolha sua opção:
        [1] Para usar essa calculadora em Portugês
        [2] To use this calculator in English.
        [3] Para usar esta calculadora en Español.
        [4] Sair / Exit\n""")
    idioma = input('Digite sua opção / Type your option >>').strip()

    if idioma == '1':
        print('CALCULADORA \n')
        print('Digite a operação para ver o resutado (ex.: 2+2, 5-1, 3*3, 8/2)')
        print("Para sair do programa digite 'sair'\n")
        while True:
            operacao = input('Digite a operação ou sair >> ').strip() 

            adicao = operacao.find('+')
            subtracao = operacao.find('-')
            multiplicacao = operacao.find('*')
            divisao = operacao.find('/')

            if operacao == 'sair':
                print ('Até a proxima!')
                break

            if adicao == -1 and subtracao == -1 and multiplicacao == -1 and divisao == -1:
                print('Essa não é uma operação matemática.')

            if adicao != -1:

                n1 = int(operacao[0: adicao])
                n2 = int(operacao[adicao+1:]) 
                somar = n1 + n2 
                print('{} + {} = {}'.format(n1, n2, somar)) 

            elif subtracao != -1:
                n1 = int(operacao[0: subtracao])
                n2 = int(operacao[subtracao+1:])
                subtrair = n1 - n2
                print('{} - {} = {}'.format(n1, n2, subtrair))

            elif multiplicacao != -1:
                n1 = int(operacao[0: multiplicacao])
                n2 = int(operacao[multiplicacao+1:])
                multiplicar = n1 * n2
                print('{} * {} = {}'.format(n1, n2, multiplicar))

            elif divisao != -1:
                n1 = float(operacao[0:divisao])
                n2 = float(operacao[divisao+1:])
                if n2 == 0:
                    print ('ERRO: Não é possível dividir por 0.')
                dividir = n1 / n2
                print('{} / {} = {:.2f}'.format(n1, n2, dividir))

            else:
                print(ArithmeticError)

    elif idioma == '2':
        print('CALCULATOR \n')
        print('Type a math operation to see the result (ex.: 2+2, 5-1, 3*3, 8/2)')
        print("To go back to the main menu type 'exit'\n")
        while True:
            operacao = input("Type a math operation or 'exit' to leave >> ").strip() 

            adicao = operacao.find('+')
            subtracao = operacao.find('-')
            multiplicacao = operacao.find('*')
            divisao = operacao.find('/')

            if operacao == 'exit':
                print ('See you later, mate!')
                break

            if adicao == -1 and subtracao == -1 and multiplicacao == -1 and divisao == -1:
                print('ERROR: This is not a valid operation, please try again.')

            if adicao != -1:

                n1 = int(operacao[0: adicao])
                n2 = int(operacao[adicao+1:]) 
                somar = n1 + n2 
                print('{} + {} = {}'.format(n1, n2, somar)) 

            elif subtracao != -1:
                n1 = int(operacao[0: subtracao])
                n2 = int(operacao[subtracao+1:])
                subtrair = n1 - n2
                print('{} - {} =float {}'.format(n1, n2, subtrair))

            elif multiplicacao != -1:
                n1 = int(operacao[0: multiplicacao])
                n2 = int(operacao[multiplicacao+1:])
                multiplicar = n1 * n2
                print('{} * {} = {}'.format(n1, n2, multiplicar))

            elif divisao != -1:
                n1 = float(operacao[0:divisao])
                n2 = float(operacao[divisao+1:])
                if n2 == 0:
                    print ('ERROR: Is not possible to divide by 0.')
                dividir = n1 / n2
                print('{} / {} = {:.2f}'.format(n1, n2, dividir))

            else:
                print(ArithmeticError)


    elif idioma == '3':
        print('Lo siento, no hablo españhol :/\n')
    elif idioma == '4':
        break
