import random
def getchoices():
  player_choice = input("Enter your choice rock,paper,scissors:")
  options = ["rock","paper","scissors"] 
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer":computer_choice}
  return choices

def check_win(player,computer):
  print(f"You chose {player} and computer chose {computer}")
  if(player==computer):
    print("It's a tie")
  elif(player=="rock"):
    if computer=="scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose!"
  elif(player=="scissors"):
    if computer=="paper":
      return "Scissors cut paper! You win!"
    else:
      return "Rock smashes scissors! You lose!"
  elif(player=="paper"):
    if computer=="rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cut paper! You lose!"

choice=getchoices()
result=check_win(choice["player"],choice["computer"])
print(result)
