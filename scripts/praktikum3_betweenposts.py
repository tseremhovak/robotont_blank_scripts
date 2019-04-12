#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
from robotont_sensors.msg import LaserScanSplit

velocity_publisher = rospy.Publisher(
    '/robotont/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def closing():
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)


distances = LaserScanSplit()


def scan_callback(data):
    global distances
    distances = data


def move():
    global distances
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

    rospy.Subscriber('/scan_to_distance', LaserScanSplit, scan_callback)

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        ########################
        # YOUR CODE HERE START #
        ########################
       if distances.centerMin < 0.6  and distances.leftMin < 0.6: 
         vel_msg.linear.x = 0
         vel_msg.linear.y = 0
         vel_msg.angular.z = -0.2
         velocity_publisher.publish(vel_msg)
         time.sleep(0.2)

       elif distances.centerMin < 0.6 and distances.rightMin < 0.6:
         vel_msg.linear.x = 0
         vel_msg.linear.y = 0
         vel_msg.angular.z = 0.2
         velocity_publisher.publish(vel_msg)
         time.sleep(0.2)

      
       elif distances.leftMin < 0.6 and distances.centerMin < 0.6:
         vel_msg.linear.x = 0
         vel_msg.linear.y = 0
         vel_msg.angular.z = -0.2
         velocity_publisher.publish(vel_msg)
         time.sleep(0.2)


       elif distances.rightMin < 0.6 and distances.centerMin < 0.6:
         vel_msg.linear.x = 0
         vel_msg.linear.y = 0
         vel_msg.angular.z = 0.2
         velocity_publisher.publish(vel_msg)
         time.sleep(0.2)

       else:
          vel_msg.linear.x = 0.2
          vel_msg.linear.y = 0
          vel_msg.angular.z = 0
          velocity_publisher.publish(vel_msg)
          time.sleep(0.2)
          
        ######################
        # YOUR CODE HERE END #
        ######################
          velocity_publisher.publish(vel_msg)
          rospy.sleep(0.05)


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
