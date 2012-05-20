from SimpleCV import Camera, Display, Image
import time
# Initialize the camera
cam = Camera(1, {"width":1280, "height":720})
# Initialize the display
display = Display()
# Snap a picture using the camera
img = cam.getImage()
# Show some text
img.drawText("Hello World!")
# Show the picture on the screen
img.save(display)
# Wait five seconds so the window doesn't close right away
time.sleep(5)
