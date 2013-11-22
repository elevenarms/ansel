import RPi.GPIO as GPIO


def testButton(channel):
	print "fuck yea button press!"

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(22, GPIO.FALLING, callback=testButton,bouncetime=300)

while True:
	print "waiting..."