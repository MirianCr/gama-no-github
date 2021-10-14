"""
3Faça um programa que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais
barato

"""
precoProduto1 = float(input("Digite o preÃ§o do primeiro produto: "))
precoProduto2 = float(input("Digite o preÃ§o do segundo produto: "))
precoProduto3 = float(input("Digite o preÃ§o do terceiro produto: "))

if precoProduto1 < precoProduto2:
    if precoProduto1 < precoProduto3:
        print("VocÃª deve comprar o primeiro produto!")
    else:
        print("VocÃª deve comprar o terceiro produto!")
else:
    if precoProduto2 < precoProduto3:
        print("VocÃª deve comprar o segundo produto!")
    else:
        print("VocÃª deve comprar o terceiro produto!")
