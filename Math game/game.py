import random
import time

def timed_input(prompt, timeout):
    start = time.time()
    s = input("({}s) {}".format(timeout, prompt))
    stop = time.time()
    if stop-start > timeout:
        print("TIMEOUT!")
        return ''
    return s

def multiplication():

        difficulty = 0
        correct = 0
        seconds = 5
        increaseX = 0
        increaseY = 0

        time.sleep(1)
        print("Welcome to multiplication mode!\n")
        time.sleep(1)
        print("""You have one try at this. We'll start you off easy with small numbers but remember...\n
for every five questions answered correctly, you get 5 extra seconds of additional time and the questions get increasingly challenging""")
        time.sleep(7)
        print("Are you ready?\n")
        print("In 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1..")
        time.sleep(1)
        print("BEGIN!\n")


        x = random.randint(1, 10)
        y = random.randint(1,10)

        answer = timed_input("What will {} multiplied by {} give you? ".format(x,y),seconds)
        if answer == '':
            print("You were too slow\n")
            print("It's...\n")
            time.sleep(1)
            print("GAME OVER :(")
            return 0

        while(int(answer) == x*y):
            print("You are correct!")
            correct += 1
            x = random.randint(1+increaseX, 10+increaseY)
            y = random.randint(1,10)

            if correct % 5 == 0:
                seconds += 5
                increaseX += 10
                increaseY += 10
            print("\n")
            answer = timed_input("What will {} multiplied by {} give you? ".format(x,y),seconds)

            if answer == '':
                print("You were too slow\n")
                break

        print("\n")
        time.sleep(1)
        print("Ouchie ouch. Mission failed. We'll get 'em next time!\n")
        time.sleep(1)
        print("You score was {}\n".format(correct))
        print("It's...\n")
        time.sleep(1)
        print("GAME OVER :(")
        return 0
def mode_select(mode):

    if (mode == 1):
        flag
    elif (mode == 2):
        addition()
    elif (mode == 3):
        division()

def launch_game():
    print("\n")
    print("Welcome to MATH F R E N Z Y. Here we test your mental math skills involving one of the basic operations in math: Multiplication\n")
    print("For every 5 questions you get right, you get 5 seconds of additional time but the questions get more challanging as well\n")
    print("""
    1.) Begin
    2.) Exit\n\n""")

    mode = input("Press 1 to begin or press 2 to exit: ")

    if int(mode) == 1:
        if (multiplication() == 0):
            prompt = input("Would you like to play again? (Y/N): ")

            while (prompt.startswith("Y") or prompt.startswith("y")):
                multiplication()

                prompt = input("Would you like to play again? (Y/N): ")

            print("Program shutting down in 3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...\n")
            time.sleep(1)
            print("Good bye :(")
    elif int(mode) == 2:
        print("Program shutting down in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...\n")
        time.sleep(1)
        print("Good bye :(")

launch_game()
