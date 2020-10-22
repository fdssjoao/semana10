def criando_dados():
    dados = [] 
    livro = {} 

    c = 101
    while True:
        livro.clear()
        livro['codigo'] = c
        livro['titulo'] = input().strip()
        if livro['titulo'] == '':
            break
        livro['isbn'] = input().strip()
        livro['autor'] = input().strip()
        livro['preco'] = float(input())

        c += 1
        dados.append(livro.copy())

    return dados


def main():
    dados = criando_dados()

    for livro in dados:
        print('Código: {}'.format(livro['codigo']))
        print('Título: {}'.format(livro['titulo']))
        print('ISBN: {}'.format(livro['isbn']))
        print('Autor: {}'.format(livro['autor']))
        print('Preço: {:.2f}'.format(livro['preco']))


if __name__ == "__main__":
    main()
