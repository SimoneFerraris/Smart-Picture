import touchphat
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep 
import cv2

@touchphat.on_touch(["A"])
def handle_touch(event):
    #apre telecamera
        # import the necessary packages
    
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    # allow the camera to warmup
    time.sleep(0.1)
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        # if the `q` key was pressed, break from the loop
        record()
        @touchphat.on_touch(["Back"])           #Boh ??? Break outside
        def handle_touch(event):
            break


def record():
    
    @touchphat.on_touch(["C"])
    def handle_touch(event):
        #salva immagini
        camera = PiCamera()
        camera.start_preview()
        sleep(2)
        for filename in camera.capture_continuous('img{counter:03d}.jpg'):
            print('Captured %s' % filename)
            sleep(0.4) # wait 5 minutes
        #riconosce Immagine?
        # si -> compare immagine + testo + audio + bottone per fermare
        # # no -> compare testo errore