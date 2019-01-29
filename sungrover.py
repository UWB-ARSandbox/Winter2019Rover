from bottle import route, run, template, request, static_file
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import Adafruit_PCA9685
import time
import atexit
#Gle Zachacz  6/12/2018

mh = Adafruit_MotorHAT(addr=0x60)
# These three commands host the javascript folder for use by home.tpl
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

# Change these for your setup.
IP_ADDRESS = '172.24.1.1' # of your Pi

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
# recommended for auto-disabling motors on shutdown!
def turnOffMotors(): # cammand for turning the servos off at close and lights
    pwm.set_pwm(0, 0, 0)
    pwm.set_pwm(1, 0, 0)
    pwm.set_pwm(2, 0, 0)#for this servo 380 puls is the center.
    pwm.set_pwm(4, 0, 0)
    pwm.set_pwm(5, 0, 0)
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)

# Handler for the home page
@route('/')
def index():
    
    turret = [150,315,360,380,390,415,600] # list of turret positions

    # Drive commands 
    # 255 is the max speed with 1 being minimum
    cmd = request.GET.get('command', '')
    if cmd == 'f': # Moves the tank forward continously
        myMotor1.setSpeed(255)
        myMotor1.run(Adafruit_MotorHAT.BACKWARD);
        myMotor2.setSpeed(255)
        myMotor2.run(Adafruit_MotorHAT.BACKWARD);
    elif cmd == 'l': # Turns the tank left continously 
        myMotor1.setSpeed(150)
        myMotor1.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.setSpeed(150)
        myMotor2.run(Adafruit_MotorHAT.BACKWARD);
    elif cmd == 's': # Stops the tank
        myMotor1.run(Adafruit_MotorHAT.RELEASE);
        myMotor2.run(Adafruit_MotorHAT.RELEASE);
    elif cmd == 'r': # Turns the tank right continously
        myMotor1.setSpeed(150)
        myMotor2.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.setSpeed(150)
        myMotor1.run(Adafruit_MotorHAT.BACKWARD);
    elif cmd == 'b': # Moves tank backwards for 1 second
        myMotor1.setSpeed(255)
        myMotor2.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.setSpeed(255)
        myMotor1.run(Adafruit_MotorHAT.FORWARD);
 
#Camera rotation commands pulse minimum 390 and max 570
    elif cmd == 'TL3':
        pwm.set_pwm(1, 0, 390)
    elif cmd == 'TL2':
        pwm.set_pwm(1, 0, 415)
    elif cmd == 'TL1': 
        pwm.set_pwm(1, 0, 460)
    elif cmd == 'CT': 
        pwm.set_pwm(1, 0, 0)
    elif cmd == 'TR1':
        pwm.set_pwm(1, 0, 500)
    elif cmd == 'TR2':
        pwm.set_pwm(1, 0, 550)
    elif cmd == 'TR3': 
        pwm.set_pwm(1, 0, 570)

#Camera elavation commands pulse minimum 390 and max 570
    elif cmd == 'TU3':
        pwm.set_pwm(0, 0, 390)
    elif cmd == 'TU2':
        pwm.set_pwm(0, 0, 415)
    elif cmd == 'TU1': 
        pwm.set_pwm(0, 0, 460)
    elif cmd == 'ST': 
        pwm.set_pwm(0, 0, 0)
    elif cmd == 'TD1':
        pwm.set_pwm(0, 0, 500)
    elif cmd == 'TD2':
        pwm.set_pwm(0, 0, 550)
    elif cmd == 'TD3': 
        pwm.set_pwm(0, 0, 570)



        
                                         
    return template('home.tpl', name='Version 2.0') # returns updated web page
        
# Start the webserver running on port 80
try: 
    run(host=IP_ADDRESS, port=80)
finally:  # most likely redundant but covers turning main motors off when server shuts down.
    pwm.set_pwm(0, 0, 0)
    pwm.set_pwm(1, 0, 0)
