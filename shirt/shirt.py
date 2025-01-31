from PIL import Image
import sys
import os


def main():
    if validate_input(sys.argv):
        build_image(sys.argv[1], sys.argv[2])


def validate_input(args):
    valid = (".jpg", ".png")
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    elif not args[1].endswith(valid):
        sys.exit("Invalid input")
    elif not args[2].endswith(valid):
        sys.exit("Invalid output")
    elif not args[1].endswith(valid[0]) == args[2].endswith(valid[0]):
        sys.exit("Input and output have different extensions")
    elif not args[1].endswith(valid[1]) == args[2].endswith(valid[1]):
        sys.exit("Input and output have different extensions")
    elif not os.path.isfile(f"./{args[1]}"):
        sys.exit("Input does not exist")
    return True


def build_image(image, new_image):
    before_img = Image.open(image).convert("RGBA")
    shirt = Image.open("shirt.png").convert("RGBA")

    width, height = before_img.size
    cropped_height = height - 150
    before_img = before_img.crop((0, 0, width, cropped_height))
    shirt_resized = shirt.resize(before_img.size)
    before_img.paste(shirt_resized, (0, 0), shirt_resized)

    if new_image.lower().endswith(".jpg") or new_image.lower().endswith(".jpeg"):
        before_img = before_img.convert("RGB")
    before_img.save(new_image)


if __name__ == "__main__":
    main()
