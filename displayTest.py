import gaugette.ssd1306 as SSD1306_I2C
import socket
import fcntl
import struct
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.output(25,GPIO.HIGH)


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def displayIP(dispObj):
	piIP =  get_ip_address('eth0')
	dispObj.clear_display()
	dispObj.draw_text(24,24,piIP)
	#DRAW CAMERA GLYPH!
	ssd1306.draw_rect(7,16,5,4,1)
	ssd1306.draw_line(0,22,20,22,0)
	#ssd1306.fill_rect(0,20,20,12,1)
	ssd1306.fill_round_rect(0,20,20,12,2,3)
	ssd1306.fill_circle(9,26,4,0)
	dispObj.display()




ssd1306 = ssd1306.SSD1306_I2C(bus=1, device=0x3c)

ssd1306.begin()
ssd1306.clear_display()

displayIP(ssd1306)
