
def convert(time):
    tim = time.split(":")
    hour = int(tim[0])
    minute = int(tim[1]) / 100
    return (hour + minute)

def main():
    x = input("enter: ")
    y = convert (x)
    if (7>=y<=8):
        print("breakfast time")
    elif (12>=y<=13):
        print ("lunch time")
    elif (18>=y<=19):
        print ("dinner time")

main()
