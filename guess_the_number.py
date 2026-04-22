
def guess_the_number(num):
    while True:
        inp = int(input("Guess the number : "))
        if(inp-num) == 0:
            print(f"{'*'*5} YOU GUESSED THE NUMBER {'*'*5}")  
            break
        elif( abs(inp-num) < 6):
            print("You are too much close to number")
        elif( abs(inp-num) < 11):
            print("You are too close to number")
        elif( abs(inp-num) < 21):
            print("You are close to number")
        else:
            print("You are too far from the number.")


            
    
    
