#!/usr/bin/env python
# Input node. Recieves commands from the base station and publishes them as ros messages to the output topic.
# command format: <F|S|R> for Forward, Stop, Reverse.

# Parameters:
#   outForward - The value to output for forward motion, defaults to 0.002
#   outStop - The value to output for no motion, defaults to 0.0015
#   outReverse - The value to output for backwards motion, defaults to 0.001

# Topics:
#   output - Publication: publishes any user commands to ROS.

import rospy
from std_msgs.msg import Float64
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = ""
port = 10001
print (host)
print (port)

def talker():
        rospy.init_node('Actuator_Interface')
        pub = rospy.Publisher("output", Float64, queue_size=10)
        forward = rospy.get_param("~outForward", 0.002)
        stop = rospy.get_param("~outStop", 0.0015)
        reverse = rospy.get_param("~outReverse", 0.001)
        serversocket.bind((host, port))
        serversocket.listen(1)
        rospy.loginfo('server started')
        while not rospy.is_shutdown():
                connection, address = serversocket.accept()
                data = connection.recv(1024).decode()
                rospy.loginfo(data)
                if (data[0] == 'F'):
                        pub.publish(forward)
                if (data[0] == 'S'):
                        pub.publish(stop)
                if (data[0] == 'R'):
                        pub.publish(reverse)
                connection.close()
        serversocket.close()


if __name__ == '__main__':
        try:
                talker()
        except rospy.ROSInterruptException:
                pass
