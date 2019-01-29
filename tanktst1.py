from bottle import route, run, template, request, static_file
import Adafruit_PCA9685
import time
import atexit
#Glen Zachacz 8/11/2017
#Gle Zachacz edit 5/1/2018

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

# Handler for the home page
@route('/')
def index():
    
    turret = [150,315,360,380,390,415,600] # list of turret positions

    
    cmd = request.GET.get('command', '')
    if cmd == 'f': # Moves the tank forward continously
        pwm.set_pwm(0, 0, 600)
        pwm.set_pwm(1, 0, 150)
    elif cmd == 'l': # Turns the tank left continously 
        pwm.set_pwm(0, 0, 600)
        pwm.set_pwm(1, 0, 600)
    elif cmd == 's': # Stops the tank
        pwm.set_pwm(0, 0, 0)
        pwm.set_pwm(1, 0, 0)
    elif cmd == 'r': # Turns the tank right continously
        pwm.set_pwm(0, 0, 300)
        pwm.set_pwm(1, 0, 300)
    elif cmd == 'b': # Moves tank backwards for 1 second
        pwm.set_pwm(0, 0, 150)
        pwm.set_pwm(1, 0, 600)
        time.sleep(1)
        pwm.set_pwm(0, 0, 0)
        pwm.set_pwm(1, 0, 0)
#    elif cmd == 'lo': #Turns lights on
#        pwm.set_pwm(4, 0, 4000)
#        pwm.setPWM(5, 0, 4000)
#    elif cmd == 'Lof': # Turns lights off
#        pwm.set_pwm(4, 0, 0)
#        pwm.set_pwm(5, 0, 0) 
    elif cmd == 'TL3':# Turns the turret at max speed to the left
        pwm.set_pwm(2, 0, 600)
    elif cmd == 'TL2':# Turns the turret left at medium speed
        pwm.set_pwm(2, 0, 415)
    elif cmd == 'TL1': # Turns the turret left at minimun speed
        pwm.set_pwm(2, 0, 390)
    elif cmd == 'CT': # Stops the turret
        pwm.set_pwm(2, 0, 0)
    elif cmd == 'TR1':# Turret right at minimum speed
        pwm.set_pwm(2, 0, 360)
    elif cmd == 'TR2':# Turret medium speed right
        pwm.set_pwm(2, 0, 315)
    elif cmd == 'TR3': # Turret full speed right
        pwm.set_pwm(2, 0, 150)
    elif cmd == 'sf': # Chasis dance command
#        if ss.get_distance() >= 20:
#           pwm.set_pwm(0, 0, 150)
#            pwm.set_pwm(1, 0, 550)
#            time.sleep(1)
            pwm.set_pwm(0, 0, 0)
            pwm.set_pwm(1, 0, 0)
    elif cmd == 'td': #turret dance command
        for x in range(0,6):
            temp = turret[x]
            pwm.set_pwm(2, 0, temp)
            time.sleep(.256)
        for x in range(0,6):
            temp = turret[6-x]
            pwm.set_pwm(2, 0, temp)
            time.sleep(.256)

#       pwm.set_pwm(2, 0, 360)
#	time.sleep(1)
#	pwm.set_pwm(2, 0, 0)        
                                         
    return template('home.tpl', name='Version 2.0') # returns updated web page
        
# Start the webserver running on port 80
try: 
    run(host=IP_ADDRESS, port=80)
finally:  # most likely redundant but covers turning main motors off when server shuts down.
    pwm.set_pwm(0, 0, 0)
    pwm.set_pwm(1, 0, 0)
