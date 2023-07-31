from CursoemVideo.ex115.lib.interface import cabeçalho, menu,leiaInt
from CursoemVideo.ex115.lib.arquivo import arquivoExiste, criarArquivo, lerArquivo, cadastrar
from time import sleep


arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):#print('Arquivo encontrado com sucesso!')
    criarArquivo(arq)
 #print('Arquivo não encontrado!')



while True:
    resposta=menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta==1:
        #Opcão de listar o contéudo de um arquivo
        lerArquivo(arq)
    elif resposta==2:
        cabeçalho('Novo Cadastro')
        nome = str(input('NOME: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta==3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)


