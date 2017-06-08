import projCam
from pynq.board import LED
from pynq.board import button
import time

class CATU:
    
    cam
    leds[4]
    buttons[4]
    ref
    
    def __init__ (self):
        cam = projCam()
        for i in range(MAX_LEDS):
            leds[i] = LED(i)
        for i in range(MAX_BUTTONS):
            buttons[i] = Button(i)
        
    def run (self):
        for i in Range(4):
            leds[i].off()
        while True:
            leds[3].toggle()
            time.sleep(.5)
            good = False
            if buttons[3].read():
                good = True
            while good:
                if buttons[0].read():
                    ref = cam.getBlock()
                if ref[0] > 0 or ref[1] > 0:
                    for i in Range(4):
                        leds[i].off()
                    temp = cam.getblock()
                    area = temp[2]*temp[3]
                    refarea = ref[2]*ref[3]
                    threshold = 20
                    if temp[0] > (ref[0] + threshold): #right
                        leds[0].on()
                    elif temp[0] < (ref[0] - threshhold): #left
                        leds[1].on
                    elif area > (refarea +threshhold):
                        leds[2].on()
                    elif area < (refarea - threshold):
                        leds[3].on()