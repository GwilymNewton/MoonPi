#! /usr/bin/python
# Author: Gwilym Newton
from gps import **
import time
import threading



class GpsPoller(threading.Thread):

  gpsd = None #seting the global variable
  polling_time = 5

  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      time.sleep(5)
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

  def get_GPS_alt()
    return gpsd.fix.altitude
  
  def get_GPS_lat()
    return gpsd.fix.latitude
  
  def get_GPS_long()
    return gpsd.fix.longitude
  
  def get_GPS_climb()
    return gpsd.fix.climb
  
  def get_GPS_speed()
    return gpsd.fix.speed
    
  def get_polling_time()
    return polling_time
    
  def set_polling_ti(set)
    polling_time=set
  
  def stop_poller() :
    print "\nKilling Thread..."
    self.running = False
    self.join() # wait for the thread to finish what it's doing
    print "Done.\nExiting."