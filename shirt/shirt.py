import sys
import os
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

    input_ext = os.path.splitext(input_image)[1]
    output_ext = os.path.splitext(output_image)[1]

    if input_ext.lower() != output_ext.lower():
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(input_image)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size

    image = ImageOps.fit(image, size, method=Image.Resampling.LANCZOS)

    image.paste(shirt, (0, 0), shirt)

    image.save(output_image)

if __name__ == "__main__":
    main()
