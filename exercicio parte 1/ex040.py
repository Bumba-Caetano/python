nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
if média >= 7:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
    print('O aluno está Aprovado')
elif média >= 5.0 and média < 7:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
    print(' O aluno está em Recuperação')
elif média <= 5:
    print('Tirando {:.1f} e {}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
    print('O aluno está Reprovado')
