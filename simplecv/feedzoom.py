""" Select a rectangular part of feed and zoom it. Left click to leave zooming 
    Pass filename as first argument and output will be saved to video file"""

print __doc__


from SimpleCV import Display, Camera, Color, VideoStream
import sys

# init #

cam = Camera()
disp = Display()
    
(lx, ly) = (None, None)
inZoomMode = False
inVideoMode = False

if len(sys.argv) > 1:

    vs = VideoStream(sys.argv[1])                   # creates VideoStream object to save results
                                                    # to a video file
    inVideoMode = True

# global vars #

THICK = 2
COLOR = Color.BLUE

# main loop #

while not disp.isDone():
    
    img = cam.getImage()
    img = img.flipHorizontal()                      # just for my convenience - simulates mirror :)
    
    if inVideoMode:
        (orig_h, orig_w) = (img.height, img.width)  # required for VideoStream
    
    px = disp.mouseX
    py = disp.mouseY

    left_down = disp.leftButtonDownPosition()       # grab coordinates for event press
    left_up = disp.leftButtonUpPosition()           # grab coordinates for event release

    if left_down is not None:                       # left mouse button pressed
                                                    # start drawing rectangle
        (lx, ly) = left_down

    if left_up is not None:                         # left mouse button released
                                                    # stop drawing rectangle, go into zoom mode
        (lx, ly) = (None, None)
        inZoomMode = True if not inZoomMode else False  # enter zooming mode
        zoom = (sx, sy, w, h)

    if inZoomMode:
        
        img = img.crop(zoom[0], zoom[1], zoom[2], zoom[3])

        if inVideoMode:
            img = img.adaptiveScale((orig_w, orig_h)) # required for VideoStream

    else:                                           # not in zoom mode
        if lx is not None and ly is not None:
            
            sx = lx if lx < px else px              # drawRectangle needs top corner coordinates
            sy = ly if ly < py else py              # depending on drawing direction these will be
                                                    # either button press coords or actual mouse
                                                    # position
            (w, h) = (abs(px-sx), abs(py-sy))

            img.drawRectangle(sx, sy, w, h, color=COLOR, width=THICK)

    if inVideoMode:
        img.applyLayers()                           # required for VideoStream
        img.save(vs)

    img.save(disp)
