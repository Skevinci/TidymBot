from gpiozero import Servo
from time import sleep

class Gripper():
    def __init__(self):
        self.myGPIO = 11
        self.myCorrection = 0.5
        self.maxPW = (2.0 + self.myCorrection) / 1000
        self.minPW = (1.0 - self.myCorrection) / 1000
        self.servo = Servo(self.myGPIO, min_pulse_width=self.minPW, max_pulse_width=self.maxPW)
        self.servo.value = -1

    def grab(self):
        # -1~0
        self.servo.value =-1
        sleep(0.3)
        for value in range(0,11,1):
            value2 = (float(value) - 10) / 10
            self.servo.value = value2
            print(value2)
            sleep(0.05)
        self.servo.value=0
        sleep(1)

    def release(self):
        # for value in range(0,11,1):
        #     value2 = (float(value) - 10) / 10
        #     servo.value = value2
        #     print(value2)
        #     sleep(0.3)
        
        # +0.0 to +0.9
        # for value in range(11,-1,-1):
        #     value2 = (float(value) - 10) / 10
        #     servo.value = value2
        #     print(value2)
        #     sleep(0.5)
        
        self.servo.value = -1
        sleep(1)
    
# servo.value = 0 
# grab()

# release()

# grab()

# release()
# while True:
#     print("Set value range -1.0 to +0.0")
    
 
    # print("Set value range +0.0 to -0.9")
    # for value in range(11,20,1):
    #     value2 = (float(value) - 10) / 10
    #     servo.value = value2
    #     print(value2)
    #     sleep(0.5)
# from gpiozero.pins.pigpio import PiGPIOFactory
# from gpiozero import AngularServo
# from time import sleep

# factory = PiGPIOFactory()
# joint_base = AngularServo(11, min_angle=-90, max_angle=90, pin_factory=factory)
# angle_base = 0
# while True:
#     angle = int(input("Angle: "))

#     angle_base = angle
#     joint_base.angle = angle_base

#     print(angle, angle_base)