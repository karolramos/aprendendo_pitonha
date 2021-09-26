import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# Escolher uma palavra aleatória da lista de palavras
word_list = ['banana', 'maçã', 'uva', 'mamão', 'acerola', 'graviola', 'manga', 'laranja', 'abacate', 'melancia',
             'melao']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# print(f"A palavra escolhida: {chosen_word}")

# Criar uma lista vazia e fazer um loop por cada letra da palavra escolhida adicionando "_" no lugar de cada letra
display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    # Escolher uma letra, transformar em minúscula e imprimir a letra escolhida
    guess = input('Escolha uma letra: ').lower()

    # Fazendo um loop e verificando se cada uma letra da palavra escolhida é compatível e adc no lugar certo
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose. :(')

    print(f"{' '.join(display)}")

    if "_" not in display:  # Se caso n existir mais espaços em branco
        end_of_game = True
        print('You win! : )')

    print(stages[lives])
