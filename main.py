import random
import hangman_words
import hangman_art

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)

#player lives
lives = 6

#import game logo
print(hangman_art.logo)

#create a blank space
display = []
for _ in range(len(chosen_word)):
  display += "_"

end_of_game = False
while not end_of_game:
  guess = input("Please enter a letter: ").lower()

  if guess in display:
    print(f"You've already guessed that letter -{guess}- ")

  #Check if the letter the user guessed is one of the letters in the chosen_word.
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter

  #check to see if the guessing words is match if not - 1 lives
  if guess not in chosen_word:
    print(f"wrong letter -{guess}- please try again ")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose")

  #Join all the elements in the list and turn it into a String.
  print(f''.join(display))

  if "_" not in display:
    end_of_game = True
    print("You win")

  print(hangman_art.stages[lives])
