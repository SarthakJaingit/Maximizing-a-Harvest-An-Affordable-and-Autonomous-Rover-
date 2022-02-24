from Motor import *
from servo import *
import time
from RoverGroundControl import *


def move_for_a_foot(motor: Motor):
    PWM.setMotorModel(-1000,-1000,-1000,-1000) #Backward
    time.sleep(0.8)
    PWM.setMotorModel(0,0,0,0) # Stop the rover
    time.sleep(1)




if __name__ == "__main__":
    PWM=Motor()
    pwm=Servo()
    pitstop_angle = 40

    for i in range(0, 3):
        move_for_a_foot(PWM)
        side_scan(pwm, pitstop_angle, 'l')
        side_scan(pwm, pitstop_angle, 'r')
