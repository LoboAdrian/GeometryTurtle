import turtle
import time

s = turtle.getscreen()

print("I am the Geometry Turtle. I can draw several shapes!")


def draw():
    t = turtle.Turtle()

    t.shape("turtle")

    # Asks the number of sides
    sides = int(input("Number of sides: "))

    # Asks for the length of sides
    length = int(input("Length of sides: "))
    
    # Asks for color
    color = str(input("Color: "))
    
    try:
        t.color(color)
    except:
        print("Try another color")
        draw()

    # Finds the angle measures
    angles = float(180 - (360 / sides))

    # Checks if it's possible to draw the shape
    if sides < 3:
        print("A shape has at least 3 sides.")
    else:
        # Little countdown here
        print("Drawing in...")
        wait = 3
        for i in reversed(range(wait)):
            time.sleep(1)
            print(i + 1, "...")
        # Fun fact
        print(sides, "sides and each angle is", angles, "degrees!")
        # The actual drawing code
        for faces in range(sides):
            t.fd(length)
            t.lt(180 - angles)

    # The end
    def fin():
        end = input("Do you want to draw more?(y/n) ")
        if end == "y":
            t.clear()
            t.reset()
            draw()
        elif end == "n":
            print("See you next time!")
            print("Closing in...")
            final = 3
            for i in reversed(range(final)):
                time.sleep(1)
                print(i + 1, "...")
        else:
            print('Type "y" for yes and "n" for no.')
            fin()

    fin()


draw()
