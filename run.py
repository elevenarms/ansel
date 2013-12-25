import gaugette.rotary_encoder
import gaugette.switch
import picamera
import time
from datetime import datetime
import subprocess



A_PIN  = 7
B_PIN  = 9
encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
last_state = None
rotCount = 0
while True:
	delta = encoder.get_delta()
	if delta!=0:
		rotCount = rotCount + 1
		if (rotCount >= 2):
			timeStart = datetime.now()
			print 'rotation detected'
			with picamera.PiCamera() as camera:
				camera.resolution = (320, 240)
				print 'recording started'
				time.sleep(.3)
				recPath = '/home/pi/crank/video/'
				recTime =   time.strftime("%Y%m%d-%Hh%Mm-%Ss")  
				gifPath = '/home/pi/crank/gifs/'
				camera.start_recording(recPath + recTime + '.h264')
				camera.wait_recording(3)
				print 'recording stopped'
				camera.stop_recording()
				print 'waiting'

				print 'converting'
    			subprocess.call('mplayer '+ recPath+recTime + '.h264 -fps 30 -ao null -ss 0:00:0 -endpos 10 -vo gif89a:fps=5:output=' + gifPath + recTime + '.gif -vf scale=320:240', shell=True)
        		print 'chmodding'
        		subprocess.call('chmod 777 ' + gifPath + recTime + '.gif', shell=True)
        		print "rotate %d" % delta
 			rotCount = 0
    #sw_state = switch.get_state()
    #if sw_state != last_state:
    #    print "switch %d" % sw_state
     #   last_state = sw_state
