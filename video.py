#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from picamera import PiCamera
import os
import sys
import datetime
import RPi.GPIO as GPIO
import os

class driveRecoder():
    try:
        #Button setup
        SWITCH_PIN=21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SWITCH_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        #Camera setup
        camera = PiCamera()
        resolution_width = 1920
        resolution_height = 1080
        record_time=60
        camera.resolution = (resolution_width, resolution_height)
        camera.framerate = 30
        camera.led = False

        def shutdown():
            print ("shutdown)"
            # os.system("sudo shutdown -h now")

        #Callback function
        #Callback function
	def stopRecording():
	    camera.stop_recording()
	    print("録画終了")
	    #I want to power down after stop recording 
	    #GPIO.cleanup()
	    #shutdown()


        GPIO.add_event_detect(SWITCH_PIN,GPIO.FALLING)
        GPIO.add_event_callback(SWITCH_PIN,stopRecording)

        while True:
            try:
                print("録画開始")

                #setup file name and directory path to save
                now = datetime.datetime.now()
                dir_name = now.strftime('%Y%m%d')
                dir_path = '/home/admini/Video/'+dir_name
                file_name = now.strftime('%H%M%S')

                #Make each date folder if not exist folder
                if not os.path.exists(dir_path):
                        os.makedirs(dir_path)
                        os.chmod(dir_path, 0777)

                #Recording 10 min the loop
                camera.start_recording(dir_path+'/'+file_name+'.h264')
                camera.wait_recording(record_time)
                camera.stop_recording()
                print("録画終了")
                    sleep(2)
            except KeyboardInterrupt:
                camera.stop_recording()
                break
            finally:
                pass
        print("録画終了")
    except KeyboardInterrupt:
        print("ctl+c終了")
        GPIO.cleanup()
        sys.exit(0)
    finally:
        pass
    print("終了")
    GPIO.cleanup()
    sys.exit(0)

