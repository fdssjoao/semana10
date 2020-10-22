

def dados_alunos():
    d = dict()

    while True:
        matricula = input().strip()
        
        if matricula == '':
            break

        nome = input().strip()
        nota_1 = float(input())
        nota_2 = float(input())

        media = (nota_1 + nota_2) / 2

        d[matricula] = nome, nota_1, nota_2, media

    return d


def matriculas():
    m = []
    while True:
        matricula_entrada = input().strip()
        if matricula_entrada == '':
            break

        m.append(matricula_entrada)
    
    return m


def main():
    d = dados_alunos()

    m = matriculas()

    i = 0
    while i < len(m):
        for k, v in d.items():
            if k == m[i]:
                print('{}: {:.1f}'.format(v[0], v[3]))

        i += 1


if __name__ == "__main__":
    main()