import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout_login = [
    [sg.Text('Usuário'),sg.Input(key='usuario_login', size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha_login', password_char='*', size=(20,1))],
    [sg.Button('Entrar', size=(10,1),button_color='#c10'),sg.Button('Cadastrar',size=(10,1),button_color='#c10')]
]
# Janela
janela_login = sg.Window('Tela de Login', layout_login)
# Eventos
while True:
    eventos_login, valores_login = janela_login.read()
    if eventos_login == sg.WINDOW_CLOSED:
        usuario1 = ''
        break
    if eventos_login == 'Entrar':
        if valores_login['usuario_login'] == 'Paulo' and valores_login['senha_login'] == '123456':
            usuario1 = valores_login['usuario_login']
            print(f'Bem-vindo de volta {usuario1}!')
        else:
            print('Usuário ou senha incorretos, tente novamente.')
    if eventos_login == 'Cadastrar':
        pass
