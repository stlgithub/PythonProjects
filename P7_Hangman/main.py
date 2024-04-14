import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
game_over = False

#Set 'lives' to equal 6.
lives = 6

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for each in chosen_word:
  display.append("_")
blank_counter = len(display)
guessed_letters = []

while not game_over:
  print(hangman_art.stages[lives])
  print(display)
  guess = input("Guess a letter: ").lower()
  if guess in guessed_letters:
    print("You've already tried this letter!")
  else:
    guessed_letters.append(guess)
#Check guessed letter
  for x in range(len(chosen_word)):
    a = chosen_word[x]
    if a == guess:
      display[x] = a
      blank_counter -= 1
      if blank_counter < 1:
        game_over = True
        print("Congratulations, you won!")
  if guess not in chosen_word:
    print(f"The letter {guess} is not in the word.")
    lives -=1
    if lives < 1:
      game_over = True
      print(hangman_art.stages[lives])
      print("You lost!")