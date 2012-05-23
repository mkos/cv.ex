""" draws circle around mouse pointer; shows live coordinates """

print __doc__

from SimpleCV import Display, Camera, Color

cam = Camera()
disp = Display()

while not disp.isDone():
    
    px = disp.mouseX
    py = disp.mouseY
    rad = 30
    offset = 50
    thick = 2
    length = 60
    font = 24
    spacing = -4
    color = Color.WHITE

    img = cam.getImage()

    img.drawCircle((px, py),
                    rad,
                    color,
                    thickness=thick)

    img.drawLine((px + rad, py),
                (px + rad + offset, py - offset),
                color,
                thickness=thick)

    img.drawLine((px + rad + offset, py - offset),
                (px + rad + offset + length, py - offset),
                color,
                thickness=thick)
    
    img.drawText(str(px) + ":" + str(py),
                px + rad + offset,
                py - offset - font - spacing,
                color,
                font)

    img.save(disp)
