#testando a conexão com a internet com python
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento!')
else:
    print('o site acessado com sucesso')
    print(site.read())# ver o código HTML do site acessado

