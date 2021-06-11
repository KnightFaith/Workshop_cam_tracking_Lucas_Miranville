import cv2

#Open camera
cam = cv2.VideoCapture

while True:
    #read camera
    [...],[...] = cam.read()
    #checkError
    if not [...]:
        print("Unable to open camera\n")
        break
    #show camera
    cv2.[...]("name", [...])
    #close W
    if (cv2.waitkey()) == ord([...]):
        break
    cv2.destroyAllWindows()python doc open camera