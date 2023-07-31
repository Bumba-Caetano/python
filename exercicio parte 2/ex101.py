


def voto(ano):
    from datetime import date #Escopo de importação:
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: Não Vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: Voto opcional.'
    else:
        return f'com {idade} anos: Voto Obrigatório'
nas = int(input('Em que ano voçê nasceu? '))
print(voto(nas))
