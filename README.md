# Description

Designed for headless setups, this python script runs every 10 seconds, checking to see if a network IP address is available.  
This script was intented to run on a 16x2 LCD
Once an IP is detected, it will be printed on a single line to the LCD display.  
This script is most useful when setting up a Pi on a network you do not have admin access to, or larger public networks where scanning for IPs is not possible.  


## Operating

First check that the pin-outs setup within PiIP-LCD.py match the same as you have.  
This script is intended to be run at startup, to remove the need to connect any extra displays to discover the current IP.  
The IP displayed upon the LCD display will update itself every 10 seconds. So network IP address changes will be reflected.  


# Credit

Created by Richard Marshall  
Contact: Richard@live.cl