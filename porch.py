import RPi.GPIO as GPIO
import time
import datetime

readPIR=11   #GPIO17
outputPIR=13 #GPIO27

# GPIO17 (header pin 11)
# GPIO27 (header pin 13)
# GPIO22 (header pin 15)
# GPIO23 (header pin 16)
# GPIO24 (header pin 18)
# GPIO25 (header pin 22)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(readPIR, GPIO.IN)  # Read output from PIR motion sensor
GPIO.setup(outputPIR, GPIO.OUT)  # LED output pin

try:
    while True:
        i = GPIO.input(readPIR)
        if i == 0:  # When output from motion sensor is LOW
            print "No Trick-or-treaters", i
            GPIO.output(outputPIR, 0)  # Turn OFF LED

        elif i == 1:  # When output from motion sensor is HIGH
            print "Trick-or-treaters detected", i
            GPIO.output(outputPIR, 1)  # Turn ON LED

        time.sleep(1)
        print datetime.datetime.now()
        print
finally:
    GPIO.cleanup()         # clean up after yourself
