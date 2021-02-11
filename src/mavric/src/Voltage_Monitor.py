#!/usr/bin/env python
import rospy
<<<<<<< HEAD
from std_msgs.msg import string
from i2c import I2C

vref = 5
max_reading = 2**12-1.0
bits = 1023  # number of steps
reference = 3300  # reference voltage in mV
voltage_divider = 8.718  # R1=68k, R2=10k
publishers = []
=======
from std_msgs.msg import Float64
from i2c import I2C

vref = 5
max_reading = (2**12)-1.0
bits = 4096  # number of steps
reference = 5000  # reference voltage in mV
voltage_divider = 8.718  # R1=68k, R2=10k
>>>>>>> 57566be7273ce2c8f52361557d5725e1678139fc


def talker():
    rospy.init_node('ADC_Monitor', anonymous=True)
<<<<<<< HEAD
    rate = rospy.Rate(10)  # 10hz
    for i in range(0, 1):
=======
    publishers = []
    for i in range(0, 2):
>>>>>>> 57566be7273ce2c8f52361557d5725e1678139fc
        pub = rospy.Publisher("ADC_Channels/CH" + str(i), Float64, queue_size=10)
        publishers.append(pub)

    frequency = rospy.get_param("frequency", 100)
    i2c_address = rospy.get_param("address", 0x18)
    rate = rospy.Rate(frequency)  # 10hz
<<<<<<< HEAD
    adc = I2C(i2c_address, 1)

    while not rospy.is_shutdown():
        for i in range(0, 1):
            voltage = read_from_adc(adc, i)
            result = ((reference * voltage_divider) / bits) * voltage  # in mV
            Rospy.loginfo(result)
            publihers[i].publish(result)
=======
    adc = 1 #I2C(i2c_address, 1)

    while not rospy.is_shutdown():
        for i in range(0, 2):
            voltage = read_from_adc(adc, i)
            result = ((reference * voltage_divider) / bits) * voltage  # in mV
            rospy.loginfo(result)
            publishers[i].publish(result)
>>>>>>> 57566be7273ce2c8f52361557d5725e1678139fc
            rate.sleep()


def read_from_adc(adc, channel):
    #print(channel)
    #sign = channel%2
    #sel = channel/2
    #message = bytearray()
    #message.append(0b10001000 | (sign << 6) | (sel << 4))
    #print(len(message))
    #adc.write(message)

    #reading = adc.read(i2c_read_bytes)
    #valor = (((reading[0]) << 4) + (reading[1] >> 4))
<<<<<<< HEAD
    #volts = valor * vref / max_reading
    #print(volts)
    volts = 100
=======
    valor = 2048
    volts = valor * vref / max_reading * 1000
    print(volts)
>>>>>>> 57566be7273ce2c8f52361557d5725e1678139fc
    return volts


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
