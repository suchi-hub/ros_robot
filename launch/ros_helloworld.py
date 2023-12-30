#!/usr/bin/python3

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# class Motor:
#     def __init__(self, pinFwd, pinBack, frequency=20, maxSpeed=100):
#         self.pinFwd = pinFwd
#         self.pinBack = pinBack
#         self.maxSpeed = maxSpeed
#         self.frequency = frequency
        
#         GPIO.setup(self.pinFwd, GPIO.OUT)
#         GPIO.setup(self.pinBack, GPIO.OUT)
#         self.pwm1 = GPIO.PWM(self.pinFwd, frequency)
#         self.pwm2 = GPIO.PWM(self.pinBack, frequency)
#         self.pwm1.start(0)
#         self.pwm2.start(0)

#     def move(self, speed):
#         if speed > self.maxSpeed:
#             speed = 100
#         elif speed < -100:
#             speed = -100
        
#         if speed > 0:
#             self.pwm1.ChangeDutyCycle(speed)
#             self.pwm2.ChangeDutyCycle(0)
#         else:
#             self.pwm1.ChangeDutyCycle(0)
#             self.pwm2.ChangeDutyCycle(-speed)

#     def stop(self):
#         self.pwm1.ChangeDutyCycle(0)
#         self.pwm2.ChangeDutyCycle(0)

# class Wheelie:
#     def __init__(self):
#         self.leftMotor = Motor(10, 9)
#         self.rightMotor = Motor(8, 7)
#         self.leftMotor.move(0)
#         self.rightMotor.move(0)

#     def stop(self):
#         self.leftMotor.stop()
#         self.rightMotor.stop()

#     def turnLeft(self, speed=50):
#         self.leftMotor.setSpeed(-speed)
#         self.rightMotor.setSpeed(speed)

#     def turnRight(self, speed=50):
#         self.leftMotor.setSpeed(speed)
#         self.rightMotor.setSpeed(-speed)

#     def forward(self, speed=50):
#         self.leftMotor.setSpeed(speed)
#         self.rightMotor.setSpeed(speed)

#     def backward(self, speed=50):
#         self.leftMotor.setSpeed(-speed)
#         self.rightMotor.setSpeed(-speed)

class Publisher:
    def __init__(self):
        rospy.init_node('command_publisher', anonymous=True)
        self.pub = rospy.Publisher('command', String, queue_size=10)
        self.rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            command = f"Time is {rospy.get_time()}"
            # command = input("Enter command: ")
            rospy.loginfo(command)
            self.pub.publish(command)
            self.rate.sleep()
        
class subscriber:
    def __init__(self):
        rospy.init_node('command_subscriber', anonymous=True)
        rospy.Subscriber('command', String, self.callback)
        rospy.spin()

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def main():
    pub = Publisher()
    sub = subscriber()
    # wheelie = Wheelie()

if __name__ == "__main__":
    main()

