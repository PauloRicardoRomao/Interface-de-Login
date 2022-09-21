import email
import PySimpleGUI as sg


def janela_login():
    # Layout
    sg.theme('Reddit')
    layout_login = [
        [sg.Text('Usuário'),sg.Input(key='usuario_login', size=(20,1))],
        [sg.Text('Senha'),sg.Input(key='senha_login', password_char='*', size=(20,1))],
        [sg.Button('Entrar', size=(10,1),button_color='#c10'),sg.Button('Cadastrar',size=(10,1),button_color='#c10')]
    ]
    # Janela
    return sg.Window('Login', layout=layout_login, finalize=True)


def janela_cadastro():
    # Layout
    sg.theme('Reddit')
    layout_cadastro = [
        [sg.Text('Usuário*'),sg.Input(key='usuario_cadastro', size=(30,1))],
        [sg.Text('Senha*'),sg.Input(key='senha_cadastro', password_char='*', size=(30,1))],
        [sg.Text('Email*'),sg.Input(key='email_cadastro', size=(40,1))],
        [sg.Button('Confirmar Cadastro',size=(15,1), button_color='#c10')]
    ]
    # Janela
    return sg.Window('Cadastro', layout=layout_cadastro, finalize=True)


#   Criando as janelas
janela1, janela2 = janela_login(), None

# Eventos
while True:
    janela, eventos, valores = sg.read_all_windows()
    
    # Quando a janela for fechada
    if janela == janela1 and eventos == sg.WIN_CLOSED:
        break
    # Quando realizar o login
    if janela == janela1 and eventos == 'Entrar':
        if valores['usuario_login'] == 'Paulo' and valores['senha_login'] == '123456':
            usuario1 = valores['usuario_login']
            sg.popup(f'Seja Bem-Vindo {usuario1}!')
        else:
            sg.popup('Usuário ou senha incorretos, tente novamente.')
    # Quando for para a proxima janela
    if janela == janela1 and eventos == 'Cadastrar':
        janela2 = janela_cadastro()
        janela1.hide()
    # Quando for voltar para janela anterior
    if janela == janela2 and eventos == sg.WIN_CLOSED:
        janela1.un_hide()
        janela.close()
    # Quando for realizar o cadastro
    if janela == janela2 and eventos == 'Confirmar Cadastro':
        if valores['usuario_cadastro'] == '' or valores['senha_cadastro'] == '' or valores['email_cadastro'] == '':
            sg.popup('Preencha corretamente todos os campos obrigatórios(*).')
        
        if valores['usuario_cadastro'] != '' or valores['senha_cadastro'] != '' or valores['email_cadastro'] != '':
            usuario_cadastro = valores['usuario_cadastro']
            senha_cadastro = valores['senha_cadastro']
            email_cadastro = valores['email_cadastro']
            sg.popup('Cadastro realizado com sucesso! Voltando a tela de login.')
            janela.close()