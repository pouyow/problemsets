import re

def main():
    html = input("HTML: ")
    print(parse(html))

def parse(s):
    match = re.search(r'<iframe [^>]*src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"', s)
    if match:
        url = match.group(1)
        url = url.replace("https://www.youtube.com/embed/", "https://youtu.be/")
        return url
    return None

if __name__ == "__main__":
    main()
