from bottle import route, run, template, request, static_file
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import Adafruit_PCA9685
import time
import atexit
import socket

UDP_IP = "172.24.1.1" #Which is my local ip for my computer
UDP_PORT = 8060

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
mh = Adafruit_MotorHAT(addr=0x60)
pwm.set_pwm_freq(60)
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)

while True:
   data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
   if data == "forward":
     myMotor1.setSpeed(255)
     myMotor1.run(Adafruit_MotorHAT.BACKWARD);
     myMotor2.setSpeed(255)
     myMotor2.run(Adafruit_MotorHAT.BACKWARD);         
   elif data == "backward":
     myMotor1.setSpeed(255)
     myMotor2.run(Adafruit_MotorHAT.FORWARD);
     myMotor2.setSpeed(255)
     myMotor1.run(Adafruit_MotorHAT.FORWARD);
   elif data == "left":
     myMotor1.setSpeed(150)
     myMotor1.run(Adafruit_MotorHAT.FORWARD);
     myMotor2.setSpeed(150)
     myMotor2.run(Adafruit_MotorHAT.BACKWARD)
   elif data == "right":
     myMotor1.setSpeed(150)
     myMotor2.run(Adafruit_MotorHAT.FORWARD);
     myMotor2.setSpeed(150)
     myMotor1.run(Adafruit_MotorHAT.BACKWARD);
     
   elif data == 'camLeft':
     pwm.set_pwm(0, 0, 390)
   elif data == 'camRight': 
     pwm.set_pwm(0, 0, 570)
   elif data == 'camHor': 
     pwm.set_pwm(0, 0, 0)   

   elif data == 'camDown':
     pwm.set_pwm(1, 0, 390)
   elif data == 'camVer': 
     pwm.set_pwm(1, 0, 0)
   elif data == 'camUp': 
     pwm.set_pwm(1, 0, 570)
        
   else :
     myMotor1.run(Adafruit_MotorHAT.RELEASE);
     myMotor2.run(Adafruit_MotorHAT.RELEASE);
     pwm.set_pwm(1, 0, 0) 
     pwm.set_pwm(0, 0, 0)
   #print (data)