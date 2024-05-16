import os
import time

def menu():
    print('''---------MENU---------
             [A] Depositar
             [B] Sacar
             [C] Extrato
             [D] Criar usuário
             [E] Criar conta
             [F] Listar contas
             [G] Sair''')

def limpatela():
    os.system('cls')

def deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: {valor:.2F}')
        print('A o operação de depósito foi realizada com sucesso!')
    else:
        print('Sua operação falhou! Digite uma quantia válida.')
    return saldo, extrato

def saque(*, saldo, valor, extrato, controle_saque, limite, numero_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = controle_saque >= numero_saque

    if excedeu_saldo:
        print('Você não tem saldo suficiente. Operação cancelada!')
    elif excedeu_limite:
        print('Você excedeu o limite de R$ 500,00. Operação cancelada!')
    elif excedeu_saque:
        print('Você excedeu o limite de saques diários. Operação cancelada!')
    elif valor > 0:
        saldo = saldo - valor
        extrato.append (f'Saque: {valor:.2F}')
        controle_saque += 1
        print('Operação realizada com sucesso!')
    else:
        os.system('cls')
        print('O valor digitado é inválido! Operação não realizada.')

    return saldo, extrato, controle_saque

def mostrar_extrato(saldo, / , *, extrato):
    print('---------EXTRATO---------')
    if not extrato:
        print('Não foram realizadas movimentações!')
    else:
        for transacao in extrato:
            print(transacao)
    print(f'\nSaldo:\t\t {saldo:.2F}')

def criar_usuario(usuarios, lista_cpf):
    cpf = input('Digite o CPF do usuário:')
    usuario = verificar_cpf(lista_cpf, cpf)
    if usuario:
        print('Já existe um usuário cadastrado com esse CPF.')
        return
    nome = input('Digite seu nome:')
    data_nascimento = input('Digite sua data de nascimento (dd-mm-aaaa):')
    endereco = input('Informe seu endereço (logradouro, numero - bairro - cidade/sigla estado)')
    lista_cpf.append(cpf)  # Adiciona o novo CPF à lista
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'cpf': cpf})
    print('Seu usuário foi criado com sucesso!')

def verificar_cpf(lista_cpf, cpf):
    return cpf in lista_cpf

def criar_conta(agencia, numero_conta, usuarios, lista_cpf):
    cpf = input('Informe o CPF do usuário: ')
    if not verificar_cpf(lista_cpf, cpf):
        print('Usuário não encontrado! Conta não criada.')
        return None
    usuario = next((user for user in usuarios if user['cpf'] == cpf), None)
    if usuario:
        print('Conta criada!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('Usuário não encontrado! Conta não criada.')

def listar_contas(contas):
    for conta in contas:
        print('---------------------------------------')
        print(f'Agência: {conta["agencia"]}')
        print(f'Conta corrente: {conta["numero_conta"]}')
        print(f'Titular: {conta["usuario"]["nome"]}')

# Lista para armazenar os CPFs dos usuários
lista_cpf = []

# Variáveis iniciais
agencia = '0001'
saldo = 0
extrato = []
controle_saque = 0
numero_saque = 3
limite = 500
usuarios = []
contas = []

# Loop principal do programa
while True:
    menu()
    opcao = input('Digite sua opção: ').strip().upper()

    if opcao == 'A':
        limpatela()
        print('----Tela de Depósito----')
        valor = float(input('Digite o valor que deseja depositar: '))
        saldo, extrato = deposito(valor, saldo, extrato)

    elif opcao == 'B':
        limpatela()
        print('----Tela de Saque----')
        print('Você tem direito a 3 saque(s) diário(s).')
        valor = float(input('Digite o valor que deseja sacar:'))
        saldo, extrato, controle_saque = saque(saldo=saldo, valor=valor, extrato=extrato, controle_saque=controle_saque, limite=limite, numero_saque=numero_saque)

    elif opcao == 'C':
        limpatela()
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == 'D':
        limpatela()
        criar_usuario(usuarios, lista_cpf)

    elif opcao == 'E':
        limpatela()
        numero_conta = len(contas) + 1
        conta = criar_conta(agencia, numero_conta, usuarios, lista_cpf)
        if conta:
            contas.append(conta)

    elif opcao == 'F':
        limpatela()
        listar_contas(contas)

    elif opcao == 'G':
        break
