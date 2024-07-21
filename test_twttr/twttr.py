def main():
    word = input("enter: ")
    print(shorten(word))

def shorten(word):
    q = ["e", "a", "i", "u", "o"]
    result = ""
    for letter in word:
        if not letter.lower() in q:
            result += letter
    return result

if __name__ == "__main__":
    main()
