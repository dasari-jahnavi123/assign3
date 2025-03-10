import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button_pin = 18
led_pin = 23

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button as input
GPIO.setup(led_pin, GPIO.OUT)  # LED as output

# Main loop
try:
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:  # Button pressed
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on LED
        else:
            GPIO.output(led_pin, GPIO.LOW)  # Turn off LED
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO settings when exiting
