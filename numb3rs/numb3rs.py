import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"

    if re.fullmatch(pattern, ip):
        return True
    return False

if __name__ == "__main__":
    main()
