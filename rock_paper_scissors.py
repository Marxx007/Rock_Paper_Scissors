import random

# ROCK_PAPER_SCISSORS GAME
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose ROCK(r)
    elif comp == 'r':
        if you=='p':
            return True
        elif you=='s':
            return False
    
    # Check for all possibilities when computer chose PAPER(p)
    elif comp == 'p':
        if you=='s':
            return True
        elif you=='r':
            return False
    
    # Check for all possibilities when computer chose SCISSORS(s)
    elif comp == 's':
        if you=='r':
            return True
        elif you=='p':
            return False

print("Comp Turn: ROCK(r) PAPER(p) or SCISSORS(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: ROCK(r) PAPER(p) or SCISSORS(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("THE GAME IS A TIE!")
elif a:
    print("YOU WIN!")
else:
    print("YOU LOSE!")
