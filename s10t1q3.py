

def informacoes():
    cadastro = [] 
    pessoa = {} 

    i = 0
    while i < 20:
        pessoa.clear()
        pessoa['nome'] = input().strip()
        pessoa['idade'] = int(input())
        pessoa['cpf'] = input().strip()
        cadastro.append(pessoa.copy())
        
        i += 1

    return cadastro

def maiores_menores(cadastro):
    menores = []
    maiores = []
    for pessoa in cadastro:
        if pessoa['idade'] < 18:
            menores.append(pessoa.copy())
        else:
            maiores.append(pessoa.copy())

    return maiores, menores


def main():
    cadastro = informacoes()
    maiores, menores = maiores_menores(cadastro)

    c = 0
    print('========== MAIORES DE 18 ANOS ==========')
    while c < len(maiores):
        print('{};{};{}'.format(maiores[c]['nome'], maiores[c]['idade'], maiores[c]['cpf']))
        c += 1
    
    i = 0
    print('========== MENORES DE 18 ANOS ==========')
    while i < len(menores):
        print('{};{};{}'.format(menores[i]['nome'], menores[i]['idade'], menores[i]['cpf']))
        i += 1


if __name__ == "__main__":
    main()