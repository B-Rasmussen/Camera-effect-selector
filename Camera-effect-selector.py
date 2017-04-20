from picamera import PiCamera
from time import sleep
import sys

camera = PiCamera()

def CameraFunc():
  camera.image_effect = user_input
  camera.start_preview()
  print('preview')
  print(camera.image_effect)
  sleep(3)
  camera.stop_preview()
  question = raw_input('\n' + 'would you like to take a photo Y/N?' + '\n')
  if question == 'Y':
    print ('photo taken with ' + camera.image_effect)
    camera.capture('/home/pi/Desktop/photo.jpg')
  elif question =='N':
    print('photo was not taken')
  else:
    print('please select either Y or N' + '\n')
    return CameraFunc()
    
def CameraFuncNone():
  camera.image_effect = "none"
  camera.start_preview()
  print('preview')
  sleep(3)
  camera.stop_preview()
  question = raw_input('\n' + 'would you like to take a photo Y/N?' + '\n')
  if question == 'Y':
    print ('photo taken')
    camera.capture('/home/pi/Desktop/photo.jpg')
  elif question =='N':
    print('photo was not taken')
  else:
    print('please select either Y or N' + '\n')
    return CameraFunc()

While True:
  user_input = (raw_input('\n' + 'Select your effect' + '\n'
                          + 'or type list to show all effects' +'\n'
                         + 'if you would like no effects type none' + '\n'
                          + ' and if you would like to quit type quit:' +'\n'))
  List_effect = ('negative','solarize','sketch','denoise','emboss','oilpaint','hatch','gpen','pastle',
                 'watercolor','film','blur','saturation','colorswap','washedout','posterise',
                 'colorpoint','colorblance','cartoon','deinterlace1','deinterlace2')

  if user_input =="list":
    print List_effect
  elif user_input == "none":
    CameraFuncNone()
  elif user_input == "negative":
    CameraFunc()
  elif user_input == "solarize":
    CameraFunc()
  elif user_input == "sketch":
    CameraFunc()
  elif user_input == "denoise":
    CameraFunc()
  elif user_input == "emboss":
    CameraFunc()
  elif user_input == "oilpaint":
    CameraFunc()
  elif user_input == "hatch":
    CameraFunc()
  elif user_input == "gpen":
    CameraFunc()
  elif user_input == "pastle":
    CameraFunc()
  elif user_input == "watercolor":
    CameraFunc()
  elif user_input == "film":
    CameraFunc()
  elif user_input == "blur":
    CameraFunc()
  elif user_input == "saturation":
    CameraFunc()
  elif user_input == "colorswap":
    CameraFunc()
  elif user_input == "washedout":
    CameraFunc()
  elif user_input == "posterise":
    CameraFunc()
  elif user_input == "colorpoint":
    CameraFunc()
  elif user_input == "colorbalance":
    CameraFunc()
  elif user_input == "cartoon":
    CameraFunc()
  elif user_input == "deinterlace1":
    CameraFunc()
  elif user_input == "deinterlace2":
    CameraFunc()
  elif user_input == "quit":
    sys.exit()
  else:
    print "error"
