import cv2

def takeSnapshot():
    vcObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = vcObject.read()

        cv2.imwrite("image.png", frame)
        result = False

    vcObject.release()
    cv2.destroyAllWindows()
    
takeSnapshot()