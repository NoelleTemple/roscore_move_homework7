#!/usr/bin/env python

#import dependencies 
import rospy
from std_msgs.msg import Float32
import time

from servocntl_pkg import servo

#method will be called when new data is published
def callback(data):
    #log data
    rospy.loginfo(rospy.get_caller_id() + "I heard %f", data.data)
    #set data as variable range
    range = data.data
    #create duty cycle-my servo runs on inputs from 2 to 13 and this converts data from the sensor (0-255) to a duty cycle (2-13) so 255 is at the 0 position)
    dutycycle=2+11*range/255 
    #move the servo
    test.moveservo(float(dutycycle))

def listener():
    # see ros wiki for more information
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Float32, callback, queue_size=1)
    rospy.spin()

if __name__== '__main__':
    #setup pwm signal for servo pin
    test = servo(description = "test", boardpin = 33, frequency = 50)
    test.setup()

    listener()

