import time
import os

for x in range(0,8):
	print 8-x
	time.sleep(60)

print 0
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (2, 3000))