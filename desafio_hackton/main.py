import customtkinter

janela = customtkinter.CTk()
janela.title('HackaTon UNIESP')
janela.geometry('500x500')

def backtest():
    print('funcionando')

texto_login = customtkinter.CTkLabel(janela, text='Login')
texto_login.pack(padx=0, pady=10)

campo_login = customtkinter.CTkEntry(janela, placeholder_text="Digite seu usuário")
campo_login.pack(padx=10, pady=10)


texto_senha = customtkinter.CTkLabel(janela, text='Senha')
texto_senha.pack(padx=0, pady=10)


campo_senha = customtkinter.CTkEntry(janela, placeholder_text='Digite sua senha')
campo_senha.pack(padx=10, pady=10)


botao_entrar = customtkinter.CTkButton(janela, text='Entrar', command=backtest)
botao_entrar.pack(padx=10, pady=10)


botao_cadastro = customtkinter.CTkButton(janela, text='Não sou cadastrado', command=backtest)
botao_cadastro.pack(padx=10, pady=10)

janela.mainloop()
