def main():
    payam = input("enter: ")
    q = ["e","a","i","u","o"]
    f=find(payam, q)
    for i in f:
         payam = payam.replace(i,"")
    print(payam.strip)

def find(payam, q):
     result=[]
     for i in payam:
          if i in q:
           result.append(i)
     return result


main()