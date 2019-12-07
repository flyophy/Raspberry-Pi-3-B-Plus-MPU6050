#!/usr/bin/python
# Raspberry Pi 3 B+ / MPU6050
# Python3
import smbus
import math
import time

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(reg):
    return bus.read_byte_data(address, reg)

def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value

def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_donme(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_donme(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1) 
address = 0x68       

bus.write_byte_data(address, power_mgmt_1, 0)

while True:
   time.sleep(.1)
   jiroskop_xout = read_word_2c(0x43)
   jiroskop_yout = read_word_2c(0x45)
   jiroskop_zout = read_word_2c(0x47)

   ivmeolcer_xout = read_word_2c(0x3b)
   ivmeolcer_yout = read_word_2c(0x3d)
   ivmeolcer_zout = read_word_2c(0x3f)

   ivmeolcer_xout_olcek = ivmeolcer_xout / 16384.0
   ivmeolcer_yout_olcek = ivmeolcer_yout / 16384.0
   ivmeolcer_zout_olcek = ivmeolcer_zout / 16384.0

   jiroskop_xout_olcek = jiroskop_xout / 131
   jiroskop_yout_olcek = jiroskop_yout / 131
   jiroskop_zout_olcek = jiroskop_zout / 131

   print ("Jiroskop")
   print ("-------------------------------------")
   print ("jiroskop X : ", ("%5d" % jiroskop_xout), " olcekli: ", jiroskop_xout_olcek) 
   print ("jiroskop Y : ", ("%5d" % jiroskop_yout), " olcekli: ", jiroskop_yout_olcek)
   print ("jiroskop Z : ", ("%5d" % jiroskop_zout), " olcekli: ", jiroskop_zout_olcek)

   print ("Ivmeolcer")

   print ("-------------------------------------")

   print ("Ivmeolcer X : ", ("%6d" % ivmeolcer_xout), " olcekli: ", ivmeolcer_xout_olcek)
   print ("Ivmeolcer Y : ", ("%6d" % ivmeolcer_yout), " olcekli: ", ivmeolcer_yout_olcek)
   print ("Ivmeolcer Z : ", ("%6d" % ivmeolcer_zout), " olcekli: ", ivmeolcer_zout_olcek)

   print ("-------------------------------------")

   print ("X Dondurme: " , get_x_donme(ivmeolcer_xout_olcek, ivmeolcer_yout_olcek, ivmeolcer_zout_olcek))
   print ("Y Dondurme: " , get_y_donme(ivmeolcer_xout_olcek, ivmeolcer_yout_olcek, ivmeolcer_zout_olcek))

   print ("--------------------------------------------------------------------------") 
   time.sleep(.5)
