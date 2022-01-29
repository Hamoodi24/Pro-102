import cv2
import dropbox
import time
import random


startTime = time.time()

def takeSnapshot():
    n = random.randint(0, 100)
    
    vcObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = vcObject.read()

        imageName = "image" + str(n) + ".png"

        cv2.imwrite(imageName, frame)
        result = False

    return imageName
    print("Snapshot taken!")
    vcObject.release()
    cv2.destroyAllWindows()
    

def dropboxUpload(imageName):
    accessToken = "sl.BBBSNxzKaz3Y810TfcsdExXMyi4SgNWA3lRJNF2k5XfHsgLi7dfJr-JrFkiCyPBLRYwXsqi3Z-_mekFXDI0pTQZxMUvsiTApxCZeNv3R3rWCgbIR1q9W_y0lBdNWSmgdIC3UxXDxZSFz"
    fileFrom = imageName
    fileTo = "/images/"+(imageName)
    dbx = dropbox.Dropbox(accessToken)

    with open(fileFrom, 'rb') as f:
        dbx.files_upload(f.read(), fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded!")


def main():
    while(True):
        if( (time.time()- startTime ) >= 10  ):
            imgName = takeSnapshot()
            dropboxUpload(imgName)

main()








