from projCam import projCam

cam = projCam()
refarea = 0
ref = [0,0,0,0]
while True:
    ref = cam.getBlock()
    refarea = ref[2]*ref[3]
    if ref[0] != 0:
        break;

k = "n"
while k == "n":
    temp = cam.getBlock()
    area = temp[2]*temp[3] 
    threshold = 30
    if temp[0] > (ref[0] + threshold): #right
        print("right\n")
    elif temp[0] < (ref[0] - threshold): #left
        print("left\n")
    elif area > (1.25*refarea):
        print("backward\n")
    elif area < (0.75*refarea):
        print("forward\n")
    else:
        print("nothing\n")
    k = raw_input("")
    
cam.stop()