from PIL import Image

image = Image.open('Meu amor!.jpg')

pixel_map = image.load()

width, height = image.size

for i in range(width):
    for j in range(height):
        r, g, b = image.getpixel((i, j))

        newR = (r * 0.393 + g * 0.769 + b * 0.189)
        newG = (r * 0.349 + g * 0.686 + b * 0.168)
        newB = (r * 0.272 + g * 0.534 + b * 0.131)

        pixel_map[i, j] = (int(newR), int(newG), int(newB))

image.show()
