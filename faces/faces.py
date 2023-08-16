def convert(emoji):
     emogi = emoji.replace(":(" , "🙁")
     return emogi.replace(":)" , "🙂")



def main():
    emoji = input("enter: ")
    print(convert(emoji))

main()