import PySimpleGUI as sg
import pyodbc as od


def conexao_banco():
    conexao = od.connect("""
        Driver={SQL Server};
        Server=LAPTOP-FCR3HP98\SQLEXPRESS;
        Database=Usuario_basico;
        """)
    
    cursor = conexao.cursor()
    return cursor


def consulta_banco():
    comando = f"""select*from tb_usuario
                    """
    return comando 


def login_banco(n, s):
    nome = n
    senha = s
    comando = f"""select*from tb_usuario where nome_usuario like {'%nome%'} and senha_usuario like {'%senha%'}
                    """
    #cursor.execute(comando)
    return n, s, comando

    
def cadastro_banco(self, n, s, mail):
    self.nome = n
    self.senha = s
    self.email = mail
    comando = f"""exec sp_cadastro_usuario {'nome'}, {'senha'}, {'email'}"""
    #cursor.execute(comando)
    #cursor.commit()
    return n, s, mail, comando



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
        if valores['usuario_login'] != '' and valores['senha_login'] != '':
            usuario1 = valores['usuario_login']
            senha1 = valores['senha_login']
            conexao = conexao_banco()
            
        
            login1 = login_banco(n=usuario1, s=senha1)
            
            consulta = login1
            conexao.execute(consulta)
            if login_banco(od.count) > 0:
                sg.popup(f'Seja Bem-Vindo {usuario1}!')
            else:
                sg.popup('Usuário ou senha incorretos, tente novamente.')
        else:
            sg.popup('Preencha todos os campos.')
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