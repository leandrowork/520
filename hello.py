#!/usr/bin/python3
aluno = input(" Digite o nome do aluno: ")
nota1 = int(input("digite numero1: "))
nota2 = int(input("digite numero2: "))


soma = nota1 + nota2
media = soma / 2
print("o aluno {0} tem a media {1}".format(aluno.title(), media))

