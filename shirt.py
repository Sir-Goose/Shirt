import os.path

from PIL import Image, ImageOps
import sys

if len(sys.argv) == 3:
    extensions = ['.jpg', '.jpeg', '.png']
    extensionsA = os.path.splitext(sys.argv[1])
    extensionsB = os.path.splitext(sys.argv[2])
    if extensionsA[1] == extensionsB[1] and extensionsA[1] in extensions:
        try:
            input_image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Input does not exist")

        shirt = Image.open("shirt.png")
        size = shirt.size

        input_image = ImageOps.fit(input_image, size)
        input_image.paste(shirt, shirt)
        input_image.save(sys.argv[2])
    elif extensionsA[1] != extensionsB[1]:
        sys.exit("Input and output have different extensions")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
