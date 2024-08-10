from datetime import date
import inflect

def main():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    print(minutes_lived(birthdate))

def minutes_lived(birthdate):
    try:
        birthdate = date.fromisoformat(birthdate)
    except ValueError:
        return None

    today = date.today()

    days_lived = (today - birthdate).days

    minutes = days_lived * 24 * 60

    p = inflect.engine()
    return p.number_to_words(minutes, andword="")

if __name__ == "__main__":
    main()

