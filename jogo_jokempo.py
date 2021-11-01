from time import sleep
import random

print('========================================')
print('  Pedra, Papel, Tesoura, Lagarto e Spock')
print('========================================')

print('                        Regras:')
print('0 - Pedra               É muito simples. Olhe:')
print('1 - Papel               Tesoura corta pepel')
print('2 - Tesoura             Papel cobre pedra')
print('3 - Lagarto             Pedra esmaga lagarto')
print('4 - Spock               Lagarto envenena Spock')
print('                        Spock esmaga tesoura')
print('                        Tesoura decapita lagarto')
print('                        Lagarto come papel')
print('                        Papel refuta Spock')
print('                        Spock vaporiza padra e como sempre...')
print('                        Pedra quebra tesoura.')
print('                        - Sheldon Cooper')


op = int(input('\nEscolha uma opção: '))
while op <= 0 or op >= 66:
    print('Opção Inválida')
    op = int(input('Escolha uma opção: '))


itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')


def vencedor(opcao):
    maq = random.randrange(1, 5)

    print(f'Computador jogou: {itens[maq]}')
    print(f'Você jogou: {itens[opcao]}')

    if maq == 0:
        if op == 0:
            print('Temos um empate!')
        elif op == 1:
            print('Você venceu humano!!!')
            print('Parabéns')
        elif op == 2:
            print('A máquina venceu!!!')
            print('Tente na próxima')
        elif op == 3:
            print('A máquina venceu!!!')
            print('Tente na próxima')
        elif op == 4:
            print('Você venceu humano!!!')
            print('Parabéns')
    elif maq == 1:
        if op == 0:
            print('A máquina venceu!!!')
            print('Tente na próxima')
        elif op == 1:
            print('Temos um empate!')
        elif op == 2:
            print('Você venceu humano!!!')
            print('Parabéns')
        elif op == 3:
            print('Você venceu humano!!!')
            print('Parabéns')
        elif op == 4:
            print('A máquina venceu!!!')
            print('Tente na próxima')
    elif maq == 2:
        if op == 0:
            print('Você venceu humano!!!')
            print('Parabéns')
        elif op == 1:
            print('A máquina venceu!!!')
            print('Tente na próxima')
        elif op == 2:
            print('Temos um empate!')
        elif op == 3:
            print('A máquina venceu!!!')
            print('Tente na próxima')
        elif op == 4:
            print('Você venceu humano!!!')
            print('Parabéns')
    elif maq == 3:
        if op == 0:
            print('Você venceu humano!!!')
            print('Parabéns')
        elif op == 1:
            print('A máquina venceu!!!')
            print('Tente na próxima')
        elif op == 2:
            print('Você venceu humano!!!')
            print('Parabéns')
        elif op == 3:
            print('Temos um empate!')
        elif op == 4:
            print('A máquina venceu!!!')
            print('Tente na próxima')
    elif maq == 4:
        if op == 0:
            print('A máquina venceu!!!')
            print('Tente na próxima')
        elif op == 1:
            print('Você venceu humano!!!')
            print('Parabéns')
        elif op == 2:
            print('A máquina venceu!!!')
            print('Tente na próxima')
        elif op == 3:
            print('Você venceu humano!!!')
            print('Parabéns')
        elif op == 4:
            print('Temos um empate!')
    print('===============================')
    print('         Fim de Jogo!          ')
    print('      Paz e Prosperidade!      ')
    print('===============================')


vencedor(op)
