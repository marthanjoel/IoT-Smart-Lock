import RPi.GPIO as GPIO
import Lock
import connection

try:
    c = connection
    lock = Lock
    lock.unlock()
    print(lock.getState())
    lock.lock()
    print(lock.getState())
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanUp()