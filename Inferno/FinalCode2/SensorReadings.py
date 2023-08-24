import RPi.GPIO as GPIO
import time
import subprocess
import Lcd_driver as LCD

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
# GPIO pin configuration
PIR_PIN = 2  # PIR sensor input pin
WATER_PIN = 3  # Water level sensor input pin
AUDIO_PIN = 4  # Audio sensor input pin

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(WATER_PIN, GPIO.IN)
GPIO.setup(AUDIO_PIN, GPIO.IN)


LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD.main()


# Loop for sensor reading and audio message
try:
    while True:

        LCD.lcd_string("Starting",LCD_LINE_1)
        pir_state = GPIO.input(PIR_PIN)
        water_state = GPIO.input(WATER_PIN)
        audio_state = GPIO.input(AUDIO_PIN)
        
        if pir_state == GPIO.HIGH:
            print("PIR Sensor detected motion!")
            subprocess.run(["vlc", "--play-and-exit", "audio_audio_alert.wav"])
            LCD.lcd_string(pir_state,LCD_LINE_1)
            time.sleep(2)
        
        if water_state == GPIO.HIGH:
            print("Water Level Sensor detected water!")
            subprocess.run(["vlc", "--play-and-exit", "audio_audio_alert.wav"])     
            LCD.lcd_string(water_state,LCD_LINE_1)
            time.sleep(2)

        if audio_state == GPIO.HIGH:
            print("Audio Sensor detected sound!")
            subprocess.run(["vlc", "--play-and-exit", "audio_audio_alert.wav"])
            LCD.lcd_string(audio_state,LCD_LINE_1)
            time.sleep(2)

        time.sleep(0.5)  # Sleep to prevent rapid triggering


        
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  # Cleanup GPIO on program exit
