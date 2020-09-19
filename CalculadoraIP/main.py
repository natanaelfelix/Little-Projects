from consulta import Consulta

print (
    """
    
==============================================================================
  ____________________________________________________________  __
 |    _____   ______     ___      __   __   __      ___       ||__\_____
 |   /     | /      |   /   \    |  \ |  | |  |    /   \      ||      ___\.
 |  |   (--'|  ,----'  /  _  \   |   \|  | |  |   /  _  \     ||     |   ||
 |   \   \  |  |      /  /_\  \  |  . `  | |  |  /  /_\  \    ||     \___||
 | .--)   | |  `----./  _____  \ |  |\   | |  | /  _____  \   ||          ]
 | |_____/   \_____/|__/     \__||__| \__| |__||__/     \__|  ||          ]
 |____________________________________________________________||______   (]
    \. .-.  .-. //                              //.-.\.===========/.-.\   ]
    `( o )( o )'                                '( o )`=========='( o )`==
      '-'  '-'                                    '-'              '-'
                **CALCULADORA DE IP LITC**
==============================================================================
""")
while True:
    endereco_ip = input('Digite o endereço de IP:')
    cidr = input('Digite a mascara CIDR /: ')

    if endereco_ip == "" or cidr == "":
        print('Você esqueçeu de digitar algo...')

        saida = input('Voce deseja continuar os calculos? S[s] N [n]')
        if saida == 's' :
            pass
        else:
            print('Obrigado por utilizar nossa calculadora')
            break
    else:
        endereco_ip.replace('.', ' ').split()
        analise = int(endereco_ip[0])

        calculando = Consulta(ip=endereco_ip, cidr=cidr)

        resultado = calculando.Classificacao()

        print(f"Mascara: {resultado[0][0]}.{resultado[0][1]}.{resultado[0][2]}.{resultado[0][3]}\n"
              f"Sub redes possíveis: {resultado[1][0]}\n"
              f"Quantidade de Hotes: {resultado[1][1]}\n"
              f"Endereço de rede: {resultado[2]}\n"
              f"Broadcast: {resultado[3]}\n")
        saida = input('Voce deseja realizar mais algum calculo? S[s] N [n]')
        if saida == 's' :
            pass
        else:
            print('Obrigado por utilizar nossa calculadora')
            break

