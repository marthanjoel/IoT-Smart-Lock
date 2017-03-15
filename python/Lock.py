from move import Motor
import state
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

currentState = state
motor = Motor([18,22,24,26])
motor.rpm = 5
state = state

def lock():
    motor.lock()
    state.lockState()

def unlock():
    motor.unlock()
    state.openState()

def getState():
    return state


