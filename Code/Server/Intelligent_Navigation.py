from Motor import *
from servo import *
import time
from RoverGroundControl import *
from Ultrasonic import *

def move_for_a_foot(motor: Motor, curr_strike):
    PWM.setMotorModel(-1000,-1000,-1000,-1000) #Backward
    if not (curr_strike):
        time.sleep(0.8)
    else:
        time.sleep(0.2)
    PWM.setMotorModel(0,0,0,0) # Stop the rover
    time.sleep(1)

def turn_row(motor: Motor):
    pass

def continue_forward(left_data, right_data, ultrasonic, strike):
    full_data = list()
    full_data.extend(right_data)
    full_data.extend(left_data)
    if sum(full_data):
        data=ultrasonic.get_distance()
        if data < 34:
            # Will hit or be too close to obstacle in next move_for_a_foot()
            return False
        strike = 0
        return True, strike
    else:
        strike += 1
        if strike > 2:
            return False, strike
        return True, strike



if __name__ == "__main__":
    PWM=Motor()
    pwm=Servo()
    ultrasonic=Ultrasonic()
    pitstop_angle = 40
    take_step = True
    strike = 0

    while take_step:
        move_for_a_foot(PWM, strike)
        left_data = side_scan(pwm, pitstop_angle, 'l')
        right_data = side_scan(pwm, pitstop_angle, 'r')

        take_step, strike = continue_forward(left_data, right_data, ultrasonic, strike)
