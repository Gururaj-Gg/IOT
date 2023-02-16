import RPi.GPIO as GPIO
import time
import datetime

led = 13 
led1=38 
led2=36 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT,initial=0)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(led1,GPIO.OUT,initial=0)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT,initial=0)
GPIO.setup(led2,GPIO.OUT)


from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def hello_world():
	return render_template('web.html')
@app.route('/redledon')
def redledon():
	GPIO.output(13,GPIO.HIGH)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M:%S")
	templateData ={
	'states' : 'ON',
	'time' : timeString
	}
	return render_template('web.html',name="f1",**templateData)
	
@app.route('/redledoff')
def redledoff():
	GPIO.output(13,GPIO.LOW)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M:%S")
	templateData ={
	'states' : 'OFF',
	'time' : timeString
	}
	return render_template('web.html',name="f2",**templateData)
	
@app.route('/redled1on')
def redled1on():
	GPIO.output(38,GPIO.HIGH)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M:%S")
	templateData ={
	'states' : 'ON',
	'time' : timeString
	}
	return render_template('web.html',name="f3",**templateData)
@app.route('/redled1off')
def redled1off():
	GPIO.output(38,GPIO.LOW)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M:%S")
	templateData ={
	'states' : 'OFF',
	'time' : timeString
	}
	return render_template('web.html',name="f4",**templateData)
	
@app.route('/redled2on')
def redled2on():
	GPIO.output(36,GPIO.HIGH)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M:%S")
	templateData ={
	'states' : 'ON',
	'time' : timeString
	}
	return render_template('web.html',name="f5",**templateData)
	
@app.route('/redled2off')
def redled2off():
	GPIO.output(36,GPIO.LOW)
	now=datetime.datetime.now()
	timeString=now.strftime("%y-%m-%d %H:%M:%S")
	templateData ={
	'states' : 'OFF',
	'time' : timeString
	}
	return render_template('web.html',name="f6",**templateData)
	
if __name__=="__main__":
	app.run(debug=True,port=4000,host='172.16.0.83')
	
