programa {
  funcao inicio() {
    escreva ("Boletim de Lançamento de Notas")

    cadeia nome
    cadeia curso
    cadeia disciplina
    inteiro nota

    escreva ("\nNome do(a) Aluno(a):")
    leia (nome)

    escreva("\nCurso: ")
    leia(curso)

    escreva("\nDisciplina: ")
    leia (disciplina)

    escreva("\nNota: ")
    leia (nota)

    se (nota > 59 e nota < 101)
    {
      escreva ("Está APROVADO")
    }
    
    senao {
      se (nota <=19)
      {
        escreva ("Está REPROVADO!")
      }
   senao {
    escreva ("Esta de RECUPERAÇÂO")
   }
    
  }
    




    
  }
}

