import time
import serial
import adafruit_gps
import rospy

# setup code for gps
uart = serial.Serial('/dev/ttyTHS2', baudrate=9600, timeout=10)  # create serial connection through serial port J17
gps = adafruit_gps.GPS(uart, debug=False)  # Create GPS instance
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")  # Turn on the basic GGA and RMC info
gps.send_command(b"PMTK220,1000")  # Set update rate to once a second (1hz)


# talker function
def talker():
    rospy.init_node('GPS_Talker')
    pub = rospy.Publisher('GPS_Data', mavric.msg.GPS, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        gps.update()
        h, m, s = gps.timestamp_utc
        pub.publish(gps.has_fix, gps.latitude, gps.longitude, gps.altitude_m, gps.speed_knots, gps.track_angle_deg, h, m, s)
        rate.sleep()


# main loop
last_print = time.monotonic()
if __name__ == '__main__':
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        talker()
