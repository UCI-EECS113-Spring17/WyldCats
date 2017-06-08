from pixy import *
from ctypes import *

# Pixy Python SWIG get blocks example #

class projCam(object):
    class Blocks (Structure):
          _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]
        
    def __init__ (self):
        # Initialize Pixy Interpreter thread #
        pixy_init()
        

    def getBlock(self):
        blocks = BlockArray(1)
        count = pixy_get_blocks(1, blocks)
        if count > 0:
            # Blocks found #
            return [blocks[0].x, blocks[0].y, blocks[0].width, blocks[0].height]
        else:
            return [0,0,0,0]
        
    def stop(self):
        pixy_close()
