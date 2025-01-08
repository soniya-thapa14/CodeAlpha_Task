import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
''', '''
  +---+
  |   |
      |
      |
      |
      |
''']
word_list=['summary','beginner','visual']
lives = 6
chosen_word=random.choice(word_list)
display=[]
for letter in chosen_word:
    display += '_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1
        
        if lives == 0:
            game_over = True
            print('you lose!!')
    if '_' not in display:
        game_over=True
        print('you win')
    print(stages[lives])
print(f"The word is {chosen_word}")