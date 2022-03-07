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

def turn_row(motor: Motor, servo: Servo, ultrasonic: Ultrasonic):

    data = ultrasonic.get_distance()
    servo.setServoPwm('1',servo_origin)
    servo.setServoPwm('0', servo_origin)

    # Initiate Turning sequence
    # Will make turning slow to preserve wheels
    for iter in range(20):
        motor.setMotorModel(2000,2000,-1500,-1500)
        time.sleep(0.1)
        motor.setMotorModel(0,0,0,0)

    # Move to 90 degree formation
    for period in range(servo_origin, 9, -1):
        servo.setServoPwm('1',period)
        time.sleep(0.01)

    for period in range(servo_origin, 171, 1):
        servo.setServoPwm('0', period)
        time.sleep(0.01)

    # Finding next row
    while data < 34:
        motor.setMotorModel(-1000,-1000,-1000,-1000)
        time.sleep(0.1)
        motor.setMotorModel(0,0,0,0)
        data = ultrasonic.get_distance()

    motor.setMotorModel(-1000, -1000, -1000, -1000)
    time.sleep(0.4)
    motor.setMotorModel(0, 0, 0, 0)

    for period in range(170, 89, -1):
        servo.setServoPwm('0', period)
        time.sleep(0.1)
    for period in range(servo_origin, 9, -1):
        servo.setServoPwm('1',period)
        time.sleep(0.01)

    for iter in range(20):
        motor.setMotorModel(2000,2000,-1500,-1500)
        time.sleep(0.1)
        motor.setMotorModel(0,0,0,0)

def continue_forward(left_data, right_data, ultrasonic, strike):
    full_data = list()
    full_data.extend(right_data)
    full_data.extend(left_data)
    if sum(full_data):
        data=ultrasonic.get_distance()
        if data < 10:
            # Will hit or be too close to obstacle in next move_for_a_foot()
            return False, -1
        strike = 0
        return True, strike
    else:
        print("Strike...")
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

 # Not running through strike. 
        take_step, strike = continue_forward(left_data, right_data, ultrasonic, strike)
        if strike == -1:
            print("Detected Object...")
            break

    print("Finished Monitoring ...")
        # if strike:
        #     led.ledIndex(0x02,255,125,0)
        #     led.ledIndex(0x04,255,255,0)
        # else:
        #     led.colorWipe(led.strip, Color(0,0,0))
