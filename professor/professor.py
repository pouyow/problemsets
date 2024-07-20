import random
def main():
 level = get_level()
 score = mainly_main(level)
 print(score)



def get_level():
 while True:
  try:
    level = int(input("Level: "))
    if level in [1,2,3]:
     break
  except:
   pass
 return level
def generate_integer(level):
 if level == 1:
  randx = random.randint(0,10)
  randy = random.randint(0,10)
 elif level == 2:
    randx = random.randint(10,100)
    randy = random.randint(10,100)
 else:
    randx = random.randint(100,1000)
    randy = random.randint(100,1000)
 return randx , randy

def calculate(randx,randy):
 eee = 1
 while eee <= 3:
  try:
    this = int(input(f"{randx} + {randy} = "))
    if this == (randx + randy):
     return True
    else:
     eee += 1
     print("EEE")
  except:
   print("EEE")
 print(f"{randx} + {randy} = {randx+randy}")

def mainly_main(level):
 score = 0
 for _ in range(10):
    randx, randy = generate_integer(level)
    if calculate(randx, randy):
        score += 1
 return score
if __name__ == "__main__":
 main()
