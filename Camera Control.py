import picamera
camera = picamera.PiCamera()
day = datetime.date.today()
class Camera(object):

    def __init__():

    def Reset_Camera():
        camera.sharpness = 0
        camera.contrast = 0
        camera.brightness = 50
        camera.saturation = 0
        camera.ISO = 0
        camera.video_stabilization = False
        camera.exposure_compensation = 0
        camera.exposure_mode = 'auto'
        camera.meter_mode = 'average'
        camera.awb_mode = 'auto'
        camera.image_effect = 'none'
        camera.color_effects = None
        camera.rotation = 0
        camera.hflip = False
        camera.vflip = False
        camera.crop = (0.0, 0.0, 1.0, 1.0)
        
    def grab_image()
        camera.capture('%s_space.jpg',%datetime.date.time())  
    def grab_contrast_range()
        for i in range(100):
            camera.contrast = i
            sleep(0.2)
            camera.capture('%s_space_contrast(%s)_.jpg' %datetime.date.time(),i)
    
        