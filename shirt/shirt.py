import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    input_image = sys.argv[1]
    output_image = sys.argv[2]

    if not (input_image.lower().endswith(('.png', '.jpg', '.jpeg')) and output_image.lower().endswith(('.png', '.jpg', '.jpeg'))):
        sys.exit("Invalid output")

    if input_image.split('.')[-1] != output_image.split('.')[-1]:
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(input_image)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    image = ImageOps.fit(image, shirt.size, method=0, bleed=0.0, centering=(0.5, 0.5))

    image.paste(shirt, shirt)

    image.save(output_image)

if __name__ == "__main__":
    main()
