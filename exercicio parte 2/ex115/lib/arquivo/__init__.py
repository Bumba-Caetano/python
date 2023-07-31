from CursoemVideo.ex115.lib.interface import cabeçalho, menu

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #tentar abrir arquivo de modo texto
        a.close()
    except FileNotFoundError: # se o arquivo não for encontrado
        return False
    else:
       return True

def criarArquivo(nome):
    try:
        a=open(nome, 'wt+')# wt escreva algum arquivo de texto, e o + quer dizer se ele não encontrar arquivo deve criar
        a.close()
    except:
        print('Houve um erro na criação de arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()



def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')#Adicionar arquivo (at) = append, t= arquivo de texo
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
         a.write(f'{nome}; {idade}\n')# escrever o nome
        except:
            print('Houve erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()


