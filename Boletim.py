print("BOLETIM DE LANÇAMENTO DE NOTAS")

nome = str (input ("Nome do(a) aluno(a): "))

curso = input ("Curso: ")

disciplina = input ("Disciplina: ")

nota = float (input("Nota: "))


if nota > 59 and nota < 101:
    print ("Está Aprovado!")

elif nota < 20:
        print ("Está REPROVADO!")
else:
    print ("EXAME FINAL, SEGUNDA VIDA")
