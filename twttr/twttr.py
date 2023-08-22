def main():
    payam = input("enter: ")
    q = ["e","a","i","u","o"]
    f=find(payam, q)
    ss= ''.join(f)
    s = payam.replace(ss,"")
    print(s)


def find(payam, q):
     result=[]
     for i in payam:
          if i in q:
              result.append(i)
              return result

main()