import cv2
import mediapipe as mp

def detect_hand():
    cam = cv2.VideoCapture(0)
    mpHand = mp.solutions.Hands
    hands = mpHand.Hands()
    while True:
        ret, frame = cam.read()
        if not ret:
            print("unable to open camera")
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        print(results.multi_hand)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord('q'):
            break
cv2.destroyAllWindows()