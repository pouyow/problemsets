import re

def main():
    html_input = input("HTML: ")
    print(parse(html_input))

def parse(s):
    match = re.search(r'src="https://www\.youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None

if __name__ == "__main__":
    main()
