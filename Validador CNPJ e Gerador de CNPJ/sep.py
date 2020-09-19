import re
import primerio_calc
import segunda_calc

def separador(cnpj):
    cnpj_seprado = re.sub(r'[^0-9]', "", cnpj)
    primerio_calc.primeiro(cnpj_seprado) #retornando 1
    juntando_com_segundo_dig = segunda_calc.segundo(cnpj_seprado)
    if cnpj_seprado == juntando_com_segundo_dig:
        return 'O numero de CNPJ:', cnpj,'é verdadeiro!'
    else:
        return 'CNPJ:', cnpj ,'é Inválido'

