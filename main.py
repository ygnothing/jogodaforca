# Projeto Jogo da Forca para o curso de Automação Industrial no IFRS!
# Criador: Michael Rodrigues dos Santos
# GitHub: github.com/ygnothing
# Versão Python: ">=3.10.0,<3.11"

from random import choice
import os  # Importar dispositivo
import time  # Calcular tempo de jogo


# Função de limpar a tela
def limpar_tela():
  if os.name == 'nt': # Caso Seja Windows utiliza "cls"
    os.system('cls')
  else:
    os.system('clear') # Caso Seja macOS/Linux utiliza "clear"


# Puxar palavras do banco de dados
arq = open('banco.txt', 'r')
banco = arq.read().splitlines()  # Ler as palavras do banco
arq.close()  # Fechar "arq"
secreta = choice(banco)  # Sortear Palavra no banco

# Construção do Boneco *Forca* em forma de lista
boneco = [
  '''
    +---+
    |   |
        |
        |
        |
        |
  =========
Letras certas e faltando:''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
Letras certas e faltando:''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
Letras certas e faltando:''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
Letras certas e faltando:''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
Letras certas e faltando:''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
Letras certas e faltando:''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
Letras certas e faltando: '''
]

acertos = ['_' for letra in secreta]
erro = 0
letras_erradas = []
iniciotempo = time.time()  # COMEÇA A CONTAR O TEMPO

limpar_tela()  # Limpar tela antes de começar

while erro < 6:  # SE ERRAR 6 PERDE
  print(boneco[erro])
  print(' '.join(acertos))

  if letras_erradas:  # Se errar:
    print(f'Número de erros: {erro}')
    print(f'Letras incorretas: {", ".join(letras_erradas)}')

  chute = input('Escolha uma letra ou digite "." para chutar a palavra: '
                ).lower()  # Chutar

  if chute == '.':  # Use '.' para chutar!
    chute = input('Qual a palavra? ').lower()

    if chute == secreta:  # Se acertar
      finaltempo = time.time()  # TEMPO
      print('Parabéns! Você acertou a palavra!')
      break
    else:  # Se errar
      erro += 1
      print(f'Você errou! Erros: {erro}')

  elif chute in secreta:  # Letra correta
    for i, letra in enumerate(secreta):

      if letra == chute:
        acertos[i] = letra

    if '_' not in acertos:  # Se acertar a palavra
      finaltempo = time.time()  # Calcular tempo de jogo
      print(f'Parabéns! Você acertou a palavra! Palavra: {secreta}')
      break
    else:  # Se acertar a letra
      print("Você acertou a letra!")

  else:  # Se errar a letra
    erro += 1
    letras_erradas.append(chute)
    print(f'Você errou! Erros: {erro}')
  limpar_tela()  # Limpar tela

if erro == 6:  # Caso a pessoa perca
  finaltempo = time.time()
  print(boneco[erro])
  print(f'Você perdeu! A palavra era {secreta}')

tempototal = finaltempo - iniciotempo  # SUBSTRAÇÃO ENTRE INICIO DO TEMPO E FINAL D O TEMPO
print(f"Você levou {tempototal:.2f} segundos para completar o jogo.")
