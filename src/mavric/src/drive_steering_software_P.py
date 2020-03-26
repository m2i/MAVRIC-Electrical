import rospy
from std_msgs.msg import String
from mavric.msg import Drivetrain

import time


def talker():
	pub = rospy.Publisher("Drive_Angle", DriveAngle, queue_size=10)
	rospy.init_node('encoder')
	rospy.loginfo('server started')
	while not rospy.is_shutdown():
		data = connection.recv(1024).decode()
        rospy.loginfo(data)
		degrees = input("Enter value : ") 
		if (degrees <-45 || degrees >45):
			turn = 1024/degrees 
			rospy.loginfo(turn)
                left = float(turn[0])
                right = float(-turn[1])#opposite of left motors
                pub.publish(left, right)

if __name__ == '__main__':
        try:
                talker()
        except rospy.ROSInterruptException:
                pass

