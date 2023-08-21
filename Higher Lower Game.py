from art import vs, logo
from game_data import data
import random
import os
# Format the account data into printable format.
def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"


## Use if statement to check if user is correct.
def check_answer(guess, a_followers, b_followers):
  """Takes the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Display Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


# Make the game repeatable.
while game_should_continue:
  # Generate a random account from the game data.
  # Making account at position B become the next account at position A.
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"\n\n\nAgainst B: {format_data(account_b)}")
  
  # Ask user for a guess.
  guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
  
  # Check if user is correct.
  ## Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear the screen
  os.system('clear')
  print(logo)
  # Give user feedback on their guess.
  #score keeping
  if is_correct:
    score += 1
    print(f"you're right! current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score {score}")
    game_should_continue = False