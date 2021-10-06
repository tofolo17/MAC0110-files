from PIL import Image

image = Image.open('Meu amor!.jpg')

pixel_map = image.load()

width, height = image.size

for i in range(width):
    for j in range(height):
        r, g, b = image.getpixel((i, j))

        grayscale = (0.3 * r + 0.59 * g + 0.11 * b)

        pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))

image.show()
