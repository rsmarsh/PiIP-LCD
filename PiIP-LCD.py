#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

# Setting up Pins for the LCD screen
lcd_rs        = 24  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 23
lcd_d4        = 18
lcd_d5        = 17
lcd_d6        = 4
lcd_d7        = 22
lcd_backlight = 4

lcd_columns = 16
lcd_rows    = 2

lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# when run, this command finds the available info from any connected networks
cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1 | cut -s -d. -f1,2,3,4"

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

# run endlessly, as the IP may also change when changing networks
while 1:
    # Clear the current LCD display each loop
    lcd.clear()
    # Attempt to find an IP address
    ipaddr = run_cmd(cmd)
    lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
    
    # If a connection has been made and an IP is available
    if len(ipaddr) > 1:
        lcd.message('%s' % (ipaddr))
    else:
        lcd.message('Waiting for IP')
    sleep(10)
	
