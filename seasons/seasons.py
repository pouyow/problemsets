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

    # بزرگ کردن حروف اول کلمات
    capitalized_words = words.capitalize()

    return capitalized_words

if __name__ == "__main__":
    main()
