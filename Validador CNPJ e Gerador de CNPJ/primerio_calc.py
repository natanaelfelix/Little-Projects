import somando1
def primeiro(cnpj_separado):
    reverso = 5
    soma1 = 0
    for numero_cnpj in range(12):
        if reverso <2:
            reverso_novo = 9
            soma2 = 0
            pegando_parte_do_cnpj = cnpj_separado[4:12]
            for outros_numeros in pegando_parte_do_cnpj:
                soma = int(outros_numeros) * reverso_novo
                soma2 = soma2 + soma
                reverso_novo = reverso_novo -1
            else:
                resu = somando1.somando(soma1 , soma2)
                digito = 11 - (resu % 11)
                if digito > 9:
                    return 0
                else:
                    return digito
        soma = int(cnpj_separado[numero_cnpj]) * reverso
        soma1 = soma + soma1
        reverso = reverso - 1



