def main():
    payam = input("enter: ").strip
    q = ["e","a","i","u","o"]
    f=find(payam, q)
    for i in f:
         payam = payam.replace(i,"")
    print(payam)

def find(payam, q):
     result=[]
     for i in payam:
          if i in q:
           result.append(i)
     return result


main()