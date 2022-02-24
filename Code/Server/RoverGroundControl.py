from servo import *
import time
# pwm=Servo()
# pwm.setServoPwm('1', 160)
# pwm.setServoPwm('0', 0)

servo_origin = 90
check_constants = [10, 45, 120]

def side_scan(pwm, pitstop_angle, direction):
    if direction == 'l':
        for period in range(servo_origin, 9, -1):
            pwm.setServoPwm('0',period)
            if period in check_constants and period!= 90:
                upward_check(pwm, 2) # Can change checking_count here
            else:
                time.sleep(0.01)
        for period in range(0, servo_origin + 1, 1):
            pwm.setServoPwm('0',period)
            time.sleep(0.01)
    elif direction == 'r':
        # Then right
        for period in range(servo_origin, 121, 1):
            pwm.setServoPwm('0',period)
            if period in check_constants and period!= 90:
                upward_check(pwm, 2) # Can change checking_count here
            else:
                time.sleep(0.01)
        for period in range(121, servo_origin-1, -1):
            pwm.setServoPwm('0',period)
            time.sleep(0.01)
    else:
        raise ValueError("Wrong input for direction")


def upward_check(pwm, checking_count):
    assert checking_count > 0 and checking_count <=3
    maximum_upward_angle = 120
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

    pitstop_angle = 40
    side_scan(pwm, pitstop_angle, 'l')
    side_scan(pwm, pitstop_angle, 'r')

    # pwm.setServoPwm('1',90)
    # for period in range(90, 130, 1):
    #     pwm.setServoPwm('0',period)
    #     time.sleep(0.01)
    # pwm.setServoPwm('1',115)
    #
    # # for period in range(130, 0, -1):
    # #     pwm.setServoPwm('0',period)
    # #     time.sleep(0.01)
