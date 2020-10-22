

def main():
    texto = input().strip().lower()

    a, e, i, o, u = contagem_vogais(texto)

    print('A: {}'.format(a['A']))
    print('E: {}'.format(e['E']))
    print('I: {}'.format(i['I']))
    print('O: {}'.format(o['O']))
    print('U: {}'.format(u['U']))


def contagem_vogais(texto):
    quant_a = 0
    quant_e = 0
    quant_i = 0
    quant_o = 0
    quant_u = 0

    for letra in texto:
        if letra in letra_a():
            quant_a += 1
        if letra in letra_e():
            quant_e += 1
        if letra in letra_i():
            quant_i += 1
        if letra in letra_o():
            quant_o += 1
        if letra in letra_u():
            quant_u += 1

    a = {'A': quant_a}
    e = {'E': quant_e}
    i = {'I': quant_i}
    o = {'O': quant_o}
    u = {'U': quant_u}

    return a, e, i, o, u 


def letra_a():
    return 'aáàâã'


def letra_e():
    return 'eéê'


def letra_i():
    return 'ií'


def letra_o():
    return 'oóô'


def letra_u():  
    return 'uú'


if __name__ == "__main__":
    main()