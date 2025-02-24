import time
import random

# contains easter eggs.
def main():
    #contains easter eggs.
    references = [
    "See you Space Cowboy...",
    "See you at the finish line...",
    "I really want to stay at your house...",
    "May the force be with you...",
    "Mission completed, exiting...",
    "Ill take you to the moon...",
    "You have become death, destroyer of worlds...",
    "Only you can prevent V-buck Scams...",
    "Dont dig straght down...",
    "Dont forget to thank the bus driver...",
    "How disgusting...",
    "Fly me to the moon...", 
    "You musin't run away...",
    "Gotta catch them all (at leat this functon)...",
    "Terminateing function, (dramaticly eats potato chip)...",
    "Ill be baaak...",
    "Why So Serious     - The Jonkler",
    "I Came, I Saw, I Compiled...",
    "Ask not what your program can do for you, but what you can do for your program..."
    ]
    # initialize input scanning via input()
    continues = True
    while continues == True:
        print("continue using function? Y/N")
        confirm = input().lower()
        if confirm == "y":
            print("\rheres yo numbers nigga\n")
        else:
            randomQuip = int(random.random() * len(references))
            print(references[randomQuip])
            for i in range(13):
                randomsus = 1 + int(random.random() * 9999)
                print("\rclosing file: " + str(randomsus), end="")
                time.sleep(0.5)  # 500 milliseconds
                print("\r", end="")
                if i < 1:
                    time.sleep(0.3)  # 300 milliseconds
                    print("> This ensures data is not traceable")
            time.sleep(2)  # 2000 milliseconds
            continues = False
            break
    #for demo only, void for real implications
    print("")
    print("\rHome: Functions")
    print("(1)log")
    print("(2)exponental")
    print("(3)compounding")
    
if __name__ == "__main__":
    main()
