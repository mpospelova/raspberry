import time
import picamera

i = 0
while(True):
	with picamera.PiCamera() as camera:
	    camera.resolution = (1024, 768)
	    camera.start_preview()
	    # Camera warm-up time
	    time.sleep(2)
	    camera.capture('pictures/name-{}.jpg'.format(i))
	    i += 1
