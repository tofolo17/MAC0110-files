from PIL import Image

image = Image.open('Meu amor!.jpg')

pixel_map = image.load()

width, height = image.size

for i in range(width):
    for j in range(height):
        r, g, b = image.getpixel((i, j))

        pixel_map[i, j] = (int(0), int(g), int(b))

image.show()
