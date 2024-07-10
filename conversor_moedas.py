# Crie um programa que converte valores entre diferentes moedas, utilizando uma API para obter as taxas de câmbio atuais.

import customtkinter

# criar e configurar a janela

# Cor e tema:
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# cria e define o tamanho da janela:
janela = customtkinter.CTk()
janela.title('Coversor de Moedas - by Pablo Costa')
janela.geometry("500x500") # difinir o tamanho da janela utilizando o métido geometry

# criar botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text='Conversor de moedas', font=('', 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text='Selecione a moeda de origem')
texto_moeda_destino = customtkinter.CTkLabel(janela, text='Selecione a moeda de destino')

# Com os rótulos adicionados, podemos inserir os campos para selecionar as moedas. Esses campos são o CTkOptionMenu()
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=['USD', 'BRL', 'EUR', 'BTC'])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=['USD', 'BRL', 'EUR', 'BTC'])

# Função para botão de conversão das moedas (deve ser criada antes da criação do botão)
def converter_moeda():
    print('converter_moeda')

# cria o botão de conversão das moedas
botao_converter = customtkinter.CTkButton(janela, text='Converter', command=converter_moeda)

# lista com os nome completos das moedas
# O CTkScrollableFrame() só precisa receber como parâmetro a janela que ele será vinculado.
lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ['USD: Dólar Americano', 'BRL: Real Brasileiro', 'EUR: Euro', 'BTC: Bitcoin']
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

# Posicionando os campos com o método pack(), respeitando a ordem que você quer que os elementos aparacençam.
# Colocar todos os elementos na tela
# o método pack() dispõe os elementos na tela na ordem em que os declaramos dentro do código, então primeiro ele adiciona o título, abaixo dele o rótulo da moeda de origem, e em sequência o da moeda de destino.
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)


# método mainloop, que garante que a janela do aplicativo permaneça aberta e funcional até que o usuário a feche manualmente
janela.mainloop()
