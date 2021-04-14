from PIL import Image

path = input("Enter thw path to the image: ")
img = Image.open(path).convert("RGB")

width, height = img.size

pixels = img.load()
# print(pixels[1, 2])  # rgb of the given pixel

def red(r,g,b):
    new_r = r
    new_g = 0
    new_b = 0
    return (new_r, new_g, new_b)

def inverse_purple(r, g, b):
    new_r = g
    new_g = b
    new_b = r
    return (new_r, new_g, new_b)

def inverse_green(r, g, b):
    new_r = b
    new_g = r
    new_b = g
    return (new_r, new_g, new_b)

def blue(r, g, b):
    new_r = 0
    new_g = 0
    new_b = b
    return (new_r, new_g, new_b)

def green(r, g, b):
    new_r = 0
    new_g = g
    new_b = 0
    return (new_r, new_g, new_b)

def sky_blue(r, g, b):
    new_r = b
    new_g = g
    new_b = r
    return (new_r, new_g, new_b)

def yellow_green(r, g, b):
    new_r = g
    new_g = r
    new_b = b
    return (new_r, new_g, new_b)

def black_white(r, g, b):
    avg = int((r+g+b)/3)
    new_r = avg
    new_g = avg
    new_b = avg
    return (new_r, new_g, new_b)

def sepia(r, g, b):
    new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
    new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
    new_b = int(r * 0.272 + g * 0.534 + b * 0.131)
    return (new_r, new_g, new_b)

def vignette(r, g, b):
    new_r = r//2
    new_g = g//2
    new_b = b//2
    return (new_r, new_g, new_b)
while(True):
    choice = '''
    Choice of filter:
        1. red
        2. blue
        3. green
        4. sepia
        5. black and white
        6. inverse purple
        7. inverse green
        8. sky blue
        9. yellow green
        10. vignette
    '''

    print(choice)
    inp = int(input("Enter your choice: "))

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))  # getting the value of rgb from the pixels
            if inp == 1:
                getVal = red(r, g, b)
            elif inp == 2:
                getVal = blue(r, g, b)
            elif inp == 3:
                getVal = green(r, g, b)
            elif inp == 4:
                getVal = sepia(r, g, b)
            elif inp == 5:
                getVal = black_white(r, g, b)
            elif inp == 6:
                getVal = inverse_purple(r, g, b)
            elif inp == 7:
                getVal = inverse_green(r, g, b)
            elif inp == 8:
                getVal = sky_blue(r, g, b)
            elif inp == 9:
                getVal = yellow_green(r, g, b)
            elif inp == 10:
                getVal = vignette(r, g, b)
            else:
                getVal = (r, g, b)
            pixels[px,py] = getVal

    img.show()

    # saving the image
    opt = input("Enter s to save else enter anything else: ")
    if opt == 's':
        img.save("new_pic.jpg")

    # exiting the loop
    exit_code = input("Enter q to quit else press any other key: ")
    if exit_code == 'q':
        break