import re

def main():
    print(count(input("Text: ")))

def count(s):
    # الگوی regex برای شمارش تعداد "um" که به تنهایی آمده
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
