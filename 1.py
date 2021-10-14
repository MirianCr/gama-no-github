"""
1)Faça um programa para a leitura de duas notas parciais de um aluno. O
programa deve calcular a média alcançada por aluno e apresentar:
a. A mensagem "Aprovado", se a média alcançada for maior ou
igual a sete;
b. A mensagem "Reprovado", se a média for menor do que sete;
c. A mensagem "Aprovado com Distinção", se a média for igual a
dez.

"""


def main():
    nota1 = int(input("Digite a nota 1: "))
    nota2 = int(input("Digite a nota 2: "))
    media = (nota1 + nota2) / 2

    if media >= 7:
        print("Aprovado")
    if media == 10:
        print("Aprovado com glamur")
    else:
        print("Reprovado")
main()
