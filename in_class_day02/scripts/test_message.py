#!/user/bin/env python3
""" This script explores publishing ROS messages in ROS using python."""

#imports
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point
import rospy

#setup
#initalize node with roscore
rospy.init_node('test_message')
#initalize a publisher on topic /my_point
publisher = rospy.Publisher('/my_point', PointStampedm queue_size=10)

#create and fill message
#define message contents
my_header = Header(stamp=rospy.Time.Now(), frame_id="odom"
my_point = Point(1.0,2.0,0.0)
#create message from contents
my_point_stamped = PointStamped(heder=my_header,point=my_point)

#publish message every 2 seconds
#set the rate of the loop (how many seconds it takes to run the loop
r = rospy.Rate(2)
#loop while rospy is running
while not rospy.is_shutdown():
    #update message timestamp
    my_point_stamped.header.stamp = rospy.Time.now()
    #publish pointstamp
    publisher.publish(my_point_stamped)
    #pause until the loop has completed
    r.sleep()
