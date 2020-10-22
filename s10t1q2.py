def criando_agenda(n):
    agenda = []
    contato = {}

    i = 0
    while i < n:
        contato.clear()
        contato['nome'] = input().strip()
        contato['cidade'] = input().strip()
        contato['estado'] = input().strip()
        contato['telefone'] = input().strip()

        agenda.append(contato.copy())
        
        i += 1

    return agenda


def main():
    n = int(input())

    agenda = criando_agenda(n)

    for contato in agenda:
        print(contato['nome'], end='')

        print(' '*(25 - len(contato['nome'])), end='')
        
        print(contato['cidade'], end='')
        
        print('({})'.format(contato['estado']), end='')
        
        print(' ' * (24 - len(contato['cidade']) + len(contato['estado'])), end='')
        
        print(contato['telefone'])


if __name__ == "__main__":
    main()
