#!/usr/bin/python
# Author: Gwilym Newton
import Adafruit_BMP.BMP085 as BMP085
import logging
import datetime

#Varribles
    #Logging
    debug_log='%s_Data_capture_log.debug' %datetime.date.today()
    #BMP
    bmp_sensor = BMP085.BMP085()
    Sealevel_Pressure = 101325.0
    
#Functions    
    
def init ():
    return
    
def init_sealevel_Pressure ():
   altitude_from_gps = 80
   Sealevel_Pressure = read_sealevel_pressure(altitude_from_gps)
   return
   
def init_logging ():   
   logging.basicConfig(filename=debug_log,level=logging.DEBUG)
   return
   
def get_BMP_Temp ():
    return '{0:0.2f} *C'.format(bmp_sensor.read_temperature())
    
def get_BMP_Pressure ():
    return '{0:0.2f} Pa'.format(bmp_sensor.read_pressure())
    
def get_BMP_Alt ():
    return '{0:0.2f} m'.format(bmp_sensor.read_altitude(Sealevel_Pressure))   
    
    