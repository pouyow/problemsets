import sys
import csv

def main():
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input.csv output.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv") or not output_file.endswith(".csv"):
        print("Both input and output files must be CSV files.")
        sys.exit(1)

    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        print(f"Could not read {input_file}")
        sys.exit(1)

    with open(output_file, "w", newline='') as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            name = row["name"]
            last, first = name.split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})

if __name__ == "__main__":
    main()

