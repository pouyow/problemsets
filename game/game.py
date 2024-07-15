import random

while True:
    try:
        level = input("level: ")
        l = int(level)
        if l > 0:
            rand = random.randrange(l)
            found = False
            while not found:
                try:
                    guess = input("guess: ")
                    g = int(guess)
                    if g > 0:
                        if rand == g:
                            print("just right!")
                            found = True
                            break
                        elif rand > g:
                            print("too small")
                        elif rand < g:
                            print("too big")
                        else:
                            False
                    else:
                        False
                except ValueError:
                    print("Invalid input. Please enter a number.")
            if found:
                break
    except ValueError:
        print("Invalid input. Please enter a number.")
