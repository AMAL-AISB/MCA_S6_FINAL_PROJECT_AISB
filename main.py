
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(15, GPIO.IN) # object detection
GPIO.setup(16, GPIO.IN) # Book Reading
GPIO.setup(18, GPIO.IN) # Google Assstnt

import os

#ga_state = 0

os.system("cd /home/pi/Desktop/Project/darknet-nnpack")
while True:
	print ("Waiting for input...")
	if GPIO.input(15) == GPIO.HIGH:
		os.system("raspistill -o /home/pi/Desktop/Project/darknet-nnpack/Image_from_camera/img.jpg")
		os.system("./darknet detector test cfg/voc.data cfg/yolov3-tiny.cfg yolov3-tiny.weights Image_from_camera/img.jpg -dont_show < data/train.txt > results.txt")
		os.system("python cleaning.py")
		os.system("python3 sound.py")
	if GPIO.input(16) == GPIO.HIGH:
		os.system("raspistill -o /home/pi/Desktop/Project/darknet-nnpack/Image_from_camera/img.jpg")
		os.system("python3 book.py --image bk.png")
	if GPIO.input(18) == GPIO.HIGH:
        os.system("/home/${USER}/env/bin/python -u /home/${USER}/GassistPi/src/main.py --device_model_id 'amalassistant-1ca0d-amalassistant-uq0vyi' --project_id 'amalassistant-1ca0d'")
			
