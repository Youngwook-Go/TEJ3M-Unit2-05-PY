"""
Created by: Youngwook Go
Created on: OCT 2023
Moves a servo motor.
"""

import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP0, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

while True:
    my_servo.throttle = 1.0
    time.sleep(0.5)
    print("clock")
    my_servo.throttle = -1.0
    time.sleep(0.5)
    print("reverse")