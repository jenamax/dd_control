#!/usr/bin/env python3
import rospy, yaml, sys
from geometry_msgs.msg import Twist
from numpy import zeros, array, linspace
from math import ceil

if __name__ == '__main__':


  # now get gains from parameter server
  rospy.init_node('dd_control')
  pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
  while not rospy.is_shutdown():
      tv = Twist()
      tv.linear.x = 10
      tv.linear.y = 0
      tv.linear.z = 0

      tv.angular.x = 0
      tv.angular.y = 0
      tv.angular.z = 0
      pub.publish(tv)
