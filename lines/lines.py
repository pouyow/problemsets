import sys

def main():
    if len(sys.argv) == 0 :
        print("Too few command-line arguments")
    if len(sys.argv) > 2 :
        print("Too many command-line arguments")
    if not (sys.argv[1]).endswith(".py"):
        sys.exit("Not a Python file")
        return

    filename = sys.argv[1]
    line_count = count(filename)
    print(line_count)

def count(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0

    lencode = 0
    for line in lines:
        striped = line.strip()
        if striped and not striped.startswith("#"):
            lencode += 1
    return lencode

if __name__ == "__main__":
    main()
