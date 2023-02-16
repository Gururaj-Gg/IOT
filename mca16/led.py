import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

led1=15
led2=13

gpio.setup(led1,gpio.OUT,initial=0)  #initially off
gpio.setup(led2,gpio.OUT,initial=1)

fh=open("led.txt")
ontime=int(fh.readlines(1)[0].split("=")[1])
offtime=int(fh.readlines(2)[0].split("=")[1])

try:
	while(True):
		gpio.output(led1, False)   #on
		time.sleep(ontime)
		gpio.output(led1, True)   #off
		time.sleep(offtime)
		gpio.output(led2,False)   #on
		time.sleep(ontime)
		gpio.output(led2, True)   #off
		time.sleep(offtime)
except KeyboardInterrupt:
	gpio.cleanup()
