import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the PIR sensor's output
pir_sensor_pin = 18

# Set up the GPIO pin as an input
GPIO.setup(pir_sensor_pin, GPIO.IN)

try:
    print("PIR sensor test. Press Ctrl+C to exit.")
    time.sleep(2)  # Allow the sensor to stabilize
    
    while True:
        if GPIO.input(pir_sensor_pin) == GPIO.HIGH:
            print("Motion detected!")
        else:
            print("No motion detected.")
        
        time.sleep(0.5)  # Add a delay to avoid frequent readings

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
