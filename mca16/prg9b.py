
import socket
import RPi.GPIO as gpio
import time

Buzzer=36

HOST="192.168.14.53"
PORT=4000
gpio.setmode(gpio.BOARD)

gpio.setup(Buzzer,gpio.OUT)
gpio.setwarnings(False)

try:
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		s.connect((HOST,PORT))
		while True:
			data=s.recv(1024).decode('utf-8')
			print(data)
			if(str(data)=='alert'):
				print("Alert | Gas Leackage detected")
				gpio.output(Buzzer,True)
				time.sleep(3)
				gpio.output(Buzzer,False)
				time.sleep(3)
except KeyboardInterrupt:
	s.close()
	GPIO.cleanup()
	             
