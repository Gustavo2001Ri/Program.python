quantidade = int(input('Quantos aparelhos serão instalados em sua residencia?'))
for i in range(quantidade):
    cliente = input('Digite seu nome: ')
    marca = input('Qual o modelo do seu aparelho de ar condicionado: ')
    BTU = int(input('Quantidade em BTU do aparelho citado? 8000 a 45000mil BTU'))
    if BTU >=8000 and BTU <=12000:
        modelo1 = int('110')
        valor = int('600')
    elif BTU >=15000 and BTU <=18000:
        modelo1 = int('180')
        valor = int('800')
    elif BTU >=19000 and BTU <=45000:
        modelo1 = int('240')
        valor = int('1200')
    else:
        print('opção invalida!!')   
    metros = input('O condensadora sera instalada atras da evaporadora? [S][N]').upper()
    if metros == 'S':
        print(f'Ok... nenhum acrescimo no valor, teremos uma instalação simples! na maquina {marca} ')
        print(f'Seu ar condicionado do modelo: {marca}, será cobrado o valor de instalação o total \n de: {valor}Reais')
    elif metros == 'N':
        qMetros = float(input('A condensadora ficará a quantos metros de distancia da evaporadora?'))
        print(f'Seu ar condicionado do modelo: {marca}, será cobrado o valor de instalação o total \n de: {(qMetros * modelo1) + valor}Reais, levando em consideração que foi cobrado o valor de {valor} \n pela instalação e o total de: {modelo1} por metros adicionais do cobre')

    else:
        print('opção invalida')
    #print(f'Seu ar condicionado do modelo: {modelo}, será cobrado o valor de instalação o total \n de: {(qMetros * modelo1) + valorIns}Reais, levando em consideração que foi cobrado o valor de {valorIns} \n pela instalação e o total de: {modelo1} por metros adicionais do cobre')