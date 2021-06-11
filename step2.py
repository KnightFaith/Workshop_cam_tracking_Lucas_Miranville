import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    #checkError
    if not ret:
        print("Unable to open camera\n")
        break
    #show camera
    cv2.vids("name", [...])
    #close W
    if (cv2.waitkey()) == ord([...]):
        break
    cv2.destroyAllWindows()