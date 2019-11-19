#!/usr/bin/env python

#import dependencies
import rospy
from std_msgs.msg import Float32

import logging
import time
from rpisensors.proximity import VL6180X
from rpisensors.proximity import VL_ALS_GAIN_20


def talker():
    #set up publisher
    pub = rospy.Publisher('chatter', Float32, queue_size = 10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) #1 Hz
    #set up sensor 
    sensor = VL6180X(1)
    while not rospy.is_shutdown():
        #get data from sensor
        data = sensor.read_distance()
        #log data from sensor
        rospy.loginfo(data)
        #publish data from sensor
        pub.publish(data)
        #sleep based on Hz from earlier (1 Hz = sleep for 1 second; 2 Hz = sleep for 0.5 seconds; etc)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
