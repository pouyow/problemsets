def main():
    x = input("enter: ")
    cnvrt (x)

def cnvrt(time):
    tim = time.split(":")
    hour = int(tim[0])
    minute = int(tim[1])
    if (7>=hour<=8):
        print("breakfast time")
    elif (12>=hour<=13):
        print ("lunch time")
    elif (18>=hour<=19):
        print ("dinner time")
main()
