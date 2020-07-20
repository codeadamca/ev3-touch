#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Turn off the light
ev3.light.off()

# Initialize EV3 touch sensor and motors
motor = Motor(Port.A)
touch = TouchSensor(Port.S1)
touchButton = "Off"

# Create a loop to react to buttons
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        ev3.light.off()
        break

    # If the touch sensor is pressed
    if touch.pressed() is True and touchButton == "Off":

        motor.dc(100)
        touchButton = "On"

    # If the touch sensor is released
    elif touch.pressed() is False and touchButton == "On":

        motor.stop()
        touchButton = "Off"

    wait(20)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
