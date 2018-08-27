#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('robot_cleaner', anonymous=True)
VELOCITY_PUBLISHER = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
VELOCITY_MSG = Twist()
#function to move straight.
def move():
# Checking if the movement is forward or backwards
    speed = 3
# Since we are moving just in x-axis
    VELOCITY_MSG.linear.y = 0
    VELOCITY_MSG.linear.z = 0
    VELOCITY_MSG.angular.x = 0
    VELOCITY_MSG.angular.y = 0
    VELOCITY_MSG.angular.z = 0
    VELOCITY_MSG.linear.x = speed
    distance = 3
# Setting the current time for distance calculus
    tim_old = rospy.Time.now().to_sec()
    current_distance = 0

# Loop to move the turtle in an specified distance
    while current_distance < distance:
# Publish the velocity
        VELOCITY_PUBLISHER.publish(VELOCITY_MSG)
# Takes actual time to velocity calculus
        tim_new = rospy.Time.now().to_sec()
# Calculates distancePoseStamped
        current_distance = speed*(tim_new-tim_old)
# After the loop, stops the robot
    VELOCITY_MSG.linear.x = 0
# Force the robot to stop
    VELOCITY_PUBLISHER.publish(VELOCITY_MSG)
    return


# Since we are moving just in x-axis
def rotate():

    VELOCITY_MSG.linear.y = 0
    VELOCITY_MSG.linear.z = 0
    VELOCITY_MSG.angular.x = 0
    VELOCITY_MSG.angular.y = 0
    VELOCITY_MSG.angular.z = 3
    VELOCITY_MSG.linear.x = 3
    speed = 3
# Setting the current time for distance calculus
    tim_old = rospy.Time.now().to_sec()
# tim_new=tim_old
    current_distance = 0
    distance = 10
# Loop to move the turtle in an specified distance
    while current_distance < distance:
# Publish the velocity
        VELOCITY_PUBLISHER.publish(VELOCITY_MSG)
# Takes actual time to velocity calculus
        tim_new = rospy.Time.now().to_sec()
# Calculates distancePoseStamped
        current_distance = speed*(tim_new-tim_old)
# After the loop, stops the robot
    VELOCITY_MSG.linear.x = speed
# Force the robot to stop
    VELOCITY_PUBLISHER.publish(VELOCITY_MSG)
    return

if __name__ == '__main__':
    try:
# Testing our function
        rotate()
        move()
        rotate()
    except rospy.ROSInterruptException:
        pass
