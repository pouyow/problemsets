from datetime import date
import inflect
import sys

def main():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    result = minutes_lived(birthdate)
    if result:
        print(result)
    else:
        sys.exit(1)

def minutes_lived(birthdate):
    try:
        birthdate = date.fromisoformat(birthdate)
    except ValueError:
        return None

    today = date.today()
    days_lived = (today - birthdate).days
    minutes = days_lived * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")

    words = words.replace(",", "").replace("  ", " ").capitalize()
    words = " ".join([word.capitalize() for word in words.split()])

    return words

if __name__ == "__main__":
    main()
