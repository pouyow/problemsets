def main():
    x = input("enter: ")
    y = convert (x)
    if y >= 7 and y <= 8:
        print("breakfast time")
    elif y >= 12 and y <= 13:
        print ("lunch time")
    elif y >= 18 and y <=19:
        print ("dinner time")
def convert(time):
    #or hour , minute = time.split(":")
    tim = time.split(":")
    hour = float(tim[0])
    minute = float(tim[1]) / 60
    return (hour +(minute))
if __name__ == "__main__":
    main()
