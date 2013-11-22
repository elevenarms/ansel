import RPi.GPIO as GPIO


def testButton(channel):
	print "fuck yea button press!"

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(25, GPIO.FALLING, callback=testCallback,bouncetime=300)

