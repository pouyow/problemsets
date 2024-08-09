import re

def main():
    html = input("HTML: ")
    print(parse(html))

def parse(s):
    match = re.search(r'<iframe [^>]*src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"', s)
    if match:
        return match.group(1)
    return None

if __name__ == "__main__":
    main()
