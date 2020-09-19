import somando2
import primerio_calc


def segundo(cnpj_separado):
    jutando_primeiro = cnpj_separado[0:12] + str(primerio_calc.primeiro(cnpj_separado))
    reverso = 6
    soma1 = 0
    for numero_cnpj in range(13):
        if reverso < 2:
            reverso_novo = 9
            soma2 = 0
            pegando_parte_do_cnpj = jutando_primeiro[5:13]
            for outros_numeros in pegando_parte_do_cnpj:
                soma = int(outros_numeros) * reverso_novo
                soma2 = soma2 + soma
                reverso_novo = reverso_novo - 1
            else:
                resu = somando2.somando_final(soma1, soma2)
                digito = 11 - (resu % 11)
                if digito > 9:
                    jutando_final = jutando_primeiro + str(0)
                    return jutando_final
                else:
                    jutando_final = jutando_primeiro + str(digito)
                    return jutando_final
        soma = int(jutando_primeiro[numero_cnpj]) * reverso
        soma1 = soma + soma1
        reverso = reverso - 1
    return
