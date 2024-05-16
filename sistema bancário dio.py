import os
import time

limites_saque = 3
controle_deposito = 0
controle_saque = 3
saida_saque = 2
extrato = 0

while True:
    controle_deposito = 0
    saida_saque = 2

    print('''-----Sistema Bancário-----
    SELECIONE UMA DAS OPÇÕES ABAIXO:
    [A] DEPOSITAR
    [B] SACAR
    [C] EXTRATO
    [D] SAIR
''')

    opcao_operacao = input('SUA OPÇÃO: ')
    time.sleep(2)
    os.system('cls')

    if opcao_operacao == 'A' or opcao_operacao == 'a':

        while controle_deposito == 0:
            print('----Tela de Depósito----')
            valor_deposito = float(input('Digite o valor a ser depositado: '))

            if valor_deposito >= 0:
                extrato = extrato + valor_deposito
                time.sleep(2)
            else:
                print('O valor digitado é inválido! Operação não realizada.')
                time.sleep(2)
            print(f'Seu saldo atual é R$: {extrato:.2F}')
            controle_deposito = int(input('Digite 0 para continuar ou outro número para parar: '))
            time.sleep(2)
            os.system('cls')


    elif opcao_operacao == 'B' or opcao_operacao == 'b':

        if not extrato == 0 and not controle_saque == 0:
            while not controle_saque == 0 and saida_saque == 2:

                print('----Tela de Saque----')
                print(f'Seu saldo R$: {extrato:.2F}')
                print('O senhor tem direito a 3 saques diários, saques acima de R$:500,00  não serão aceitos!')
                print(f'Restam {controle_saque} saques.')
                saque = float(input('Digite a quantidade que deseja sacar: '))
                time.sleep(2)

                if saque > 0 and extrato > saque and saque <= 500:
                    extrato = extrato - saque
                    controle_saque = controle_saque - 1
                    print('Operação realizada com sucesso!')

                else:
                    os.system('cls')
                    print('O valor digitado é inválido ou maior que o extrato! Operação não realizada.')

                saida_saque = int(input('Digite 1 para voltar ou 2 para continuar: '))
                os.system('cls')

                if not saida_saque == 1 and not saida_saque == 2:
                    while not saida_saque == 1:
                        os.system('cls')
                        print('Opção inválida! tente novamente!')
                        saida_saque = int(input('Digite 1 para retornar.'))

        elif controle_saque == 0:
            print('Atingiu o máximo de saques diários, volte amanhã!')
            voltar = int(input('Digite 1 para voltar:'))

        elif extrato == 0:
            print('Seu saldo está vazio! Faça um deposito primeiro.')
            opcao_operacao = input('''SELECIONE UMA DAS OPÇÕES ABAIXO:
            [A] VOLTAR
            [D] SAIR''')
            if opcao_operacao == 'D' or opcao_operacao =='d':
                break


    elif opcao_operacao == 'C' or opcao_operacao == 'c':
        if not extrato == 0:
            print('Seus extrato abaixo:')
            print(f'R$: {extrato:.2F}')
            voltar = int(input('Digite 1 para voltar: '))
            os.system('cls')
            
        else:
            print('Não há extratos, faça um depósito!')


    elif opcao_operacao == 'D' or opcao_operacao == 'd':
        break

    else:
        print('Opção inválida!')

print('Você escolheu sair da operação!') 