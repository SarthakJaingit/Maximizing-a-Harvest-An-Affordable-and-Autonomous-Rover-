from Led import *
from Motor import *


led=Led()
led.ledIndex(0x04,255,255,0)
led.ledIndex(0x80,0,255,0)
time.sleep(5)
led.colorWipe(led.strip, Color(0,0,0)) #turn off


PWM=Motor()
PWM.setMotorModel(2000,2000,2000,2000)
time.sleep(3)
PWM.setMotorModel(0,0,0,0)
#import Motor #create an object #Forward
#waiting 3 second #Stop
