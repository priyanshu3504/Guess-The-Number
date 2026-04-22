from guess_the_number import guess_the_number
import random as rdm

def main():
    print(f"{'-'*10} NUMBER GUESSING GAME {'-'*10}")
    while True:
        print("1. Want to play the GAME")
        print("2. Exit")
        choice = int(input("Enter your choice(1-2) : "))

        match choice:
            case 1:
                num = rdm.randint(1,100)
                # print(num)
                guess_the_number(num)
                
            case 2:
                print(f"{'-'*10} THANKS TO PLAY THE GAME {'-'*10}")
                break
                    
            case _:
                print("Enter a valid choice.")

if __name__ == "__main__":
    main()