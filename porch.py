import RPi.GPIO as GPIO
import time
import datetime

readPIR = 11  # GPIO17
ledStrip = 13  # GPIO27
ledDebug = 15  # GPIO22
ledStrip2 = 16 #GPIO23
# GPIO17 (header pin 11)taken
# GPIO27 (header pin 13)taken
# GPIO22 (header pin 15)taken
# GPIO23 (header pin 16)taken
# GPIO24 (header pin 18)
# GPIO25 (header pin 22)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(readPIR, GPIO.IN)  # Read output from PIR motion sensor
GPIO.setup(ledStrip, GPIO.OUT)  # LEDSTRIP output pin
GPIO.setup(ledDebug, GPIO.OUT)  # LEDDEBUG output pin
GPIO.setup(ledStrip2, GPIO.OUT) # LEDSTRIP2 output pin

def debugTrickerTreater(pirValue):
    if (pirValue == 0):
        print("No Trick-or-treaters", pirValue)
    else:
        print("Yes Trick-or-treaters", pirValue)

    GPIO.output(ledDebug, pirValue)



try:
    while True:
        i = GPIO.input(readPIR)
        debugTrickerTreater(i)

        if i == 0:  # When output from motion sensor is LOW
            GPIO.output(ledStrip, 0)  # Turn OFF LED STRIP
            time.sleep(1)
        elif i == 1:  # When output from motion sensor is HIGH
            x = 0
            # Turn ON LED
            while x < 5:

                print("led running loop",x)

                #T=0
                debugTrickerTreater(GPIO.input(readPIR))
                GPIO.output(ledStrip, 1)
                time.sleep(1.3)

                #T=1.3
                debugTrickerTreater(GPIO.input(readPIR))
                GPIO.output(ledStrip2, 0)
                time.sleep(.4)

                #T=1.7
                debugTrickerTreater(GPIO.input(readPIR))
                GPIO.output(ledStrip2, 1)
                time.sleep(1.3)

                #T=3
                debugTrickerTreater(GPIO.input(readPIR))
                GPIO.output(ledStrip, 0)
                time.sleep(.4)

                #T=3.4
                x += 1

        print("exited led running loop")

        GPIO.output(ledStrip, 0) #not needed
        GPIO.output(ledStrip2, 0)

        print(datetime.datetime.now())
        print
finally:
    GPIO.cleanup()  # clean up after yourself
