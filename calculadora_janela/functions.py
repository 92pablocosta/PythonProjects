conta = input().strip()
adicao = conta.find('+')
subtracao = conta.find('-')
multiplicacao = conta.find('*')
divisao = conta.find('/')
def somar():
    n1 = float(conta[0: adicao])
    n2 = float(conta[adicao+1:])
    resultado = n1 + n2
    print('{}+{} = {}'.format(n1, n2, resultado))