# importação das bibliotecas
import PySimpleGUI as sg
import pyodbc as od

# definindo conexão com a base de dados

dados_conexao = ("""
                 Driver={SQL Server};
                 Server=LAPTOP-FCR3HP98\SQLEXPRESS;
                 Database=Usuario_basico;
                 """)
conexao = od.connect(dados_conexao)
cursor = conexao.cursor()

# declaração das classes

class Usuario_Cadastro:
    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        if email == '':
            self.email = 'null'
        elif email != '':
            self.email = email
        
    def Cadastro_Usuario(self):
        if self.email in 'null':
            self.comando = f"""
                exec sp_cadastro_usuario '{self.nome}', '{self.senha}', {self.email}
            """
        else: 
            self.comando = f"""
                exec sp_cadastro_usuario '{self.nome}', '{self.senha}', '{self.email}'
            """
        cursor.execute(self.comando)
        cursor.commit()
        sg.popup("""Usuário cadastrado com sucesso!
                 Voltando para tela de Login.
                 """, button_color='#c10')
        
        
class Usuario_Login:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        
        
    def Login_Usuario(self):
        self.comando = f"""
            select * from tb_usuario where nome_usuario = '{self.nome}' and senha_usuario = '{self.senha}'
        """
        cursor.execute(self.comando)
        
        self.lista_usuario = cursor.fetchall()
        
        if len(self.lista_usuario[0:]) == 0:
            sg.popup("Nome de usuário ou senha inválidos.\nTente novamente.", button_color='#c10')
        elif len(self.lista_usuario[0:]) > 0:
            sg.popup(f"Bem-vindo(a) {self.nome}.", button_color='#c10') 
    
         
    
# definição das janelas

# janela de login
def janela_login():
    # layout
    sg.theme('Reddit')
    
    layout_login = [
        [sg.Text('Usuário'), sg.Input(key='usuario_login', size=(20, 1))],
        [sg.Text('Senha'), sg.Input(key='senha_login', password_char='*', size=(20, 1))],
        [sg.Button('Entrar', size=(10,1), button_color='#c10'), sg.Button('Cadastrar', size=(10,1), button_color='#c10')]
    ]    
    # janela
    return sg.Window('Login', layout=layout_login, finalize=True)


# janela de cadastro
def janela_cadastro():
    # layout
    sg.theme('Reddit')
    
    layout_cadastro = [
        [sg.Text('*Nome de Usuário: '), sg.Input(key='usuario_cadastro', size=(30,1))],
        [sg.Text('*Senha: '), sg.Input(key='senha_cadastro', password_char='*', size=(20,1))],
        [sg.Text('Email: '), sg.Input(key='email_cadastro', size=(40,1))],
        [sg.Button('Confirmar Cadastro', size=(15,1), button_color='#c10')]
    ]
    # janela
    return sg.Window('Cadastro de Usuário', layout=layout_cadastro, finalize=True)

# criando as janelas
janela1, janela2 = janela_login(), None
# eventos da aplicação

while True:
    janela, eventos, valores = sg.read_all_windows()
    # fechar janelas, finaliza aplicação
    if janela == janela1 and eventos == sg.WIN_CLOSED:
        break
    # eventos da janela1
    if janela == janela1:
        # entrar
        if eventos == 'Entrar':
            if valores['usuario_login'] == '' or valores['senha_login'] == '':
                sg.popup("Necessario preenchimento de todos os campos.", button_color='#c10')
            elif valores['usuario_login'] != '' and valores['senha_login'] != '':
                usuario_login = valores['usuario_login']
                senha_login = valores['senha_login']
                usuario = Usuario_Login(usuario_login, senha_login)
                usuario.Login_Usuario()
        # cadastrar
        # troca de janela
        if eventos == 'Cadastrar':
            janela1.hide()
            janela2 = janela_cadastro()
    # eventos da janela2
    if janela == janela2:
        # fechar janela, voltar para anterior
        if eventos == sg.WIN_CLOSED:
            janela2.close()
            janela = janela1
            janela1.un_hide()
        # confirmar cadastro
        if eventos == 'Confirmar Cadastro':
            if valores['usuario_cadastro'] == '' or valores['senha_cadastro'] == '':
                sg.popup("Necessário preenchimento de todos os campos que tiverem *.", button_color='#c10')
            elif valores['usuario_cadastro'] != '' and valores['senha_cadastro'] != '':
                usuario_cadastro = valores['usuario_cadastro']
                senha_cadastro = valores['senha_cadastro']
                email_cadastro = valores['email_cadastro']
                cadastro = Usuario_Cadastro(usuario_cadastro, senha_cadastro, email_cadastro)
                cadastro.Cadastro_Usuario()
                    
    
    