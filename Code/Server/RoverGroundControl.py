from servo import *
import time
# pwm=Servo()
# pwm.setServoPwm('1', 160)
# pwm.setServoPwm('0', 0)

servo_origin = 90

def side_scan(pitstop_angle, direction):
    if direction == 'l':
        for period in range(servo_origin, -1, -1):
            pwm.setServoPwm('0',period)
            if period % pitstop_angle == 0 and period!= 90:
                upward_check(3) # Can change checking_count here
            else:
                time.sleep(0.01)
        for period in range(0, servo_origin + 1, 1):
            pwm.setServoPwm('0',period)
            time.sleep(0.01)

def upward_check(checking_count):
    assert checking_count > 0 and checking_count <=3
    maximum_upward_angle = 150
    turn_angle = (maximum_upward_angle - servo_origin) / checking_count
    assert turn_angle % 1 == 0 # assert that turn_angle is an integer
    for period in range(servo_origin, maximum_upward_angle + 1, 1):
        pwm.setServoPwm('1',period)
        if (period - servo_origin) % turn_angle == 0 and period != 90:
            time.sleep(2)
        else:
            time.sleep(0.01)
    for period in range(maximum_upward_angle + 1, servo_origin - 1, -1):
        pwm.setServoPwm('1',period)
        time.sleep(0.01)


# pwm.setServoPwm('1',80)

if __name__ == "__main__":
    pwm=Servo()

    pitstop_angle = 45
    side_scan(pitstop_angle, 'l')
