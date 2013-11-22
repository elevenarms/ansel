import RPi.GPIO as GPIO


def testCallback(channel):
	print "fuck yea button press!"

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(22, GPIO.FALLING, callback=testCallback,bouncetime=300)

