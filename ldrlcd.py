import Adafruit_ADS1x15
from time import sleep, strftime, time
import RPi.GPIO as GPIO
import numpy
import lcddriver
from time import *

lcd = lcddriver.lcd() 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

pinLed = 16
GPIO.setup(pinLed, GPIO.OUT)

# collect/read ldr sensor value wit ADS1115
def ldr():
    ldrValue = adc.read_adc(0, gain=GAIN)
    return ldrValue

 # run forever except terminated
while True:
	try:
    #convert to 0 - 100% if needed
		per = numpy.interp(ldr(), [0,4000], [0, 100])
    
    #print values
		print('LDR raw value: ' + str(ldr()) + ' :::' + str(int(per)) + '%')
    
    #if value < 6000: it is now dark, turn LED on
		if ldr() < 500:
			GPIO.output(pinLed, GPIO.HIGH)
                        lcd.lcd_display_string("3DPRINTER STATUS", 1)
                        lcd.lcd_display_string("STATUS ON", 2)
		else:
			GPIO.output(pinLed, GPIO.LOW)
                        lcd.lcd_display_string("3DPRINTER STATUS", 1)
                        lcd.lcd_display_string("STATUS OFF", 2)
		sleep(2)	
	except KeyboardInterrupt:
        	GPIO.cleanup()
	        sleep(1)

