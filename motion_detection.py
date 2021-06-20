# Credit to pageauc for most of the motion detection code. Find his repo at:
# https://github.com/pageauc/pi-motion-lite/blob/master/pi-motion-lite.py
import time
import datetime
import picamera
import picamera.array

verbose = True
width = 128
height = 80
threshold = 30
sensitivity = 300

def detect_motion(img1, img2):
    motion = False
    pixColor = 1
    pixChanges = 0
    for w in range(0, width):
        for h in range(0, height):
            difference = abs(int(img1[h][w][pixColor]) - int(img2[h][w][pixColor]))
            if difference >= threshold:
                pixChanges += 1
            if pixChanges > sensitivity:
                break
        if pixChanges > sensitivity:
            break
    if pixChanges > sensitivity:
        motion = True
    return motion

def getImage():
    with picamera.PiCamera() as camera:
        time.sleep(.5)
        camera.resolution = (width, height)
        with picamera.array.PiRGBArray(camera) as stream:
            camera.exposure_mode = "auto"
            camera.awb_mode = "auto"
            camera.capture(stream, format="rgb")
            return stream.array

def Main():
    stream1 = getImage()
    stream2 = getImage()
    if detect_motion(stream1, stream2):
        return True

