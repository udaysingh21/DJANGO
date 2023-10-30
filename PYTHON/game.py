import random

# Get guess from player
def get_guess():
    # casting str into list so as to modify it as str is immutable
    return list(input("What is your guess ? "))

# Generate 3 digit unique code
def generate_code():
    # first get unique digits from 0-9 , then shuffle it and get first 3 unique digits as code from the list
    digits=[str(num)for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

# Generate clues for player to guess

def generate_clues(code,user_guess):
    # First Match then close...
    if user_guess==code:
        return "CODE CRACKED"

    clues=[]

    for idx,num in enumerate(user_guess):
        if num==code[idx]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if not clues:
        return ["Nope"]
    else:
        return clues

# run game logic
print("Welcome Code Breaker !!")
computer_code=generate_code()
clue_report=[]
while clue_report!="CODE CRAKCED":
    guess=get_guess()
    clue_report=generate_clues(computer_code,guess)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)

