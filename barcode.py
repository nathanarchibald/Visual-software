import cv2
import numpy as np 
import pyzbar.pyzbar as pyzbar

'''
img=cv2.imread("pysource_qrcode.png")

decodedObject=pyzbar.decode(img)

print(decodedObject)

cv2.imshow("image", img)
cv2.wait(key)
'''
#^reads and shows image, then decodes info in image
#output:
# [Decoded(data=b'https://www.kaspersky.com', type='QRCODE', rect=Rect(left=88, 
# top=88, width=986, height=986), polygon=[Point(x=88, y=88), Point(x=88, y=1070), Point(x=1074, y=1074), Point(x=1070, y=88)])]


#how do we take a video as pictures
cap=cv2.VideoCapture(1)
#picks from diferent cameras, for soem reason snap camera is my main camera
font= cv2.FONT_HERSHEY_SIMPLEX
#accessing fonts in cv
while True:
  _, frame= cap.read()
  #reading frames from camera
  decodedObjects=pyzbar.decode(frame)
  #decodes the qr code
  for obj in decodedObjects:
    #print("Data", obj.data)
    #^prints info from qr code into terminal
    cv2.putText(frame, str(obj.data), (50,50), font, 1, (205,0, 2), 1)

  cv2.imshow("Frame", frame)
  #showing the frames
  key=cv2.waitKey(1)
  #print("wow")
  print(key)
  if key == 115:
      print("bloop if")
      break
    #^key 27 is s key on keyboard, so it displays frame until s key is pressed
  #EVERYTHING WORKS perfectly except hitting s to close the window for some reason

  #this is the basics. then you will use it to check if the qr code is correct or whatever