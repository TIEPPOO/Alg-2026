programa {
  funcao inicio() {
    escreva ("Boletim de Lançamento de Notas")

    cadeia nome
    cadeia curso
    cadeia disciplina
    cadeia semestre
    inteiro nota1
    inteiro nota2
    real media
    

    escreva ("\nNome do(a) Aluno(a):")
    leia (nome)

    escreva("\nCurso: ")
    leia(curso)

    escreva("\nsemestre:")
    leia (semestre)

    escreva("\nDisciplina: ")
    leia (disciplina)

    escreva("\nNota do Primeiro semestre: ")
    leia (nota1)

    escreva ("\nNota do segundo semestre: ")
    leia (nota2)

    media = (nota1+nota2)/2

    escreva("\nA media da disciplina é: ", media)

    se (media >59 e media <=100)
    {
      escreva("\nAPROVADO!")
    }

    se (media >100)
    {
      escreva ("\nErro na media")
    }


    senao{
      se (media <=19)
      escreva ("\nReprovado")
      }
   
    senao{
      se (media >=20 e <59)
      escreva("\nRecuperação")
    }
      



    }

    
    
    




    
  }
}
