from Motor import *
import time
PWM=Motor()
PWM.setMotorModel(-1000,-1000,-1000,-1000) #Backward
time.sleep(1.5)
PWM.setMotorModel(0,0,0,0) # Stop the rover
time.sleep(1)
