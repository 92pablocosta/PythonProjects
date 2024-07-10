#Crie um programa que converte diferentes unidades de medida, como quilômetros para milhas, Celsius para Fahrenheit, etc.

print('CONVERSOR DE TEMPERATURA')
escolha = input('Gostaria de converter [1] ºC para ºF / [2] ºF para ºC')

if escolha == '1':
    celcius = int(input('Graus Celcius: '))
    celcius_far = (celcius * 1.8) + 32
    print('{}ºC equivalem a {}ºF'.format(celcius, celcius_far))
elif escolha == '2':
    fah = int(input('Fahrenheit: '))
    far_celcius = (fah - 32) / 1.8
    print('{}ºF equivalem a {}ºC'.format(fah, far_celcius))
else:
    print('Opção Inválida, tente novamente.')
