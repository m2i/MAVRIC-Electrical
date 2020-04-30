import rospy
from std_msgs.msg import string


def talker():
	pub=rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker')
	rate=rospy.Rate(10) # 10
	while not rospy.is_shutdown():
		Voltage=read_from ADC(...)
		bits =1023 #number of steps
		reference = 3300 #reference voltage in mV
		voltage_divider = 8.718 # R1=68k, R2=10k
		Result = ((reference*voltage_divider)/bits)*Voltage #in mV
		Rospy.loginfo(Result)
		Pub.publish(Result)
		Rate.sleep()

def read_from_ADC():
	pub=rospy.Publisher(...)
	rospy.init_node(...)
	rate=rospy.Rate(..)# 100
	while not rospy.is_shutdown():
		Subscribe<std_msgs:strings("Result",...,chatter Callback);

