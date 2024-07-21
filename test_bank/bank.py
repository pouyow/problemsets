def main():
    koli = input("Enter: ")
    result = value(koli)
    print(result)

def value(greeting):
    flitt = greeting.capitalize()[0].lower().strip()
    fword = greeting.split()[0].lower().replace(",", "").strip()

    if fword == "hello":
        return "$0"
    elif flitt == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()
