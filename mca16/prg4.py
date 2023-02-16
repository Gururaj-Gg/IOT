import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
relay=38
gpio.setup(relay,gpio.OUT,initial=0)  #initially off


#cron file
try:
	
	print("start of the program")
	gpio.output(relay, True)    #on
	print("relay on") 
	time.sleep(2)
	gpio.output(relay, False)   #off
	print("relay off")
		
except KeyboardInterrupt:
	#cleanup GPIO setting before exiting
	gpio.cleanup()
	print("END OF PROGRAM")
	
