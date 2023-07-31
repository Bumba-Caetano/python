import pyttsx3

#Cria um objeto de síntese de voz;

engine = pyttsx3.init()
#Define as configurações de voz, taxa de fala e volume;

engine.setProperty('voice', 'brazil') # Seleciona a voz em português do Brasil;

engine.setProperty('rate', 150) # Define a taxa de fala para 150 palavras por minuto;

engine.setProperty('volume', 0.7) # Define o volume para 70%

#Solicita que o usuário digite um texto a ser convertido em fala;

texto = input("Digite um texto para a síntese de voz: ")
#Realiza a síntese de voz do texto digitado pelo usuário;

try:
    engine.say(texto)
    engine.runAndWait()
except Exception as e:
    print("Ocorreu um erro na síntese de voz: ", e)

