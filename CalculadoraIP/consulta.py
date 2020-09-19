from abcd import SubredeHostes
from pstq import Mascara
from intervalo import *
import re



class Consulta:
    def __init__(self, ip, cidr):
        self.ip = ip
        self.cidr = cidr
        self.octeto = [128, 64, 32, 16, 8, 4, 2, 1]


    @property
    def ip(self):
        return self._ip

    @property
    def cidr(self):

        return self.prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido.')

        self._ip = valor

    @cidr.setter
    def cidr(self, valor):

        try:
            valor = int(valor)
        except:
            raise ValueError('Prefixo precisa ser um inteiro e não pode ser nulo.')

        if valor > 32 or valor < 0:
            raise TypeError('Prefixo precisa ter 32Bits.')

        self.prefixo = valor

    @staticmethod
    def _valida_ip(ip):

        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    def Classificacao(self):
        ip = self.ip.replace('.', ' ').split()
        analise = int(ip[0])
        mascqtd = []


        if analise >= 0 and analise <172:
            mascaradeci = Mascara.primeiro(self.octeto, self.cidr) # calcula a masacara em decimal
            qtd = SubredeHostes.A(self.cidr) # calcula a quantidade de Ip e subrede
            inter = Intervalo(self.ip, self.cidr)
            mascqtd.append(mascaradeci)
            mascqtd.append(qtd)
            mascqtd.append(Intervalo.set_rede(inter))
            mascqtd.append(Intervalo.set_broadcast(inter))

        elif analise >= 172 and analise <192:

            mascaradeci = Mascara.terceiro(self.octeto, self.cidr) # calcula a quantidade de Ip e subrede
            qtd = SubredeHostes.B(self.cidr) # calcula a quantidade de Ip e subrede
            inter = Intervalo(self.ip, self.cidr)
            mascqtd.append(mascaradeci)
            mascqtd.append(qtd)
            mascqtd.append(Intervalo.set_rede(inter))
            mascqtd.append(Intervalo.set_broadcast(inter))

        elif analise >= 192 and analise <224:
            mascaradeci = Mascara.quarto(self.octeto, self.cidr) # calcula a quantidade de Ip e subrede
            qtd = SubredeHostes.C(self.cidr) # calcula a quantidade de Ip e subrede
            inter = Intervalo(self.ip, self.cidr)
            mascqtd.append(mascaradeci)
            mascqtd.append(qtd)
            mascqtd.append(Intervalo.set_rede(inter))
            mascqtd.append(Intervalo.set_broadcast(inter))


        return mascqtd



