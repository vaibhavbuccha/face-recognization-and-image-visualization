import cv2

cap = cv2.VideoCapture(0) """for camera prifrence"""

"""
cap.read()  """for capturing the photo"""
"""
r , photo = cap.read()

#cv2.imwrite("my.png" , photo) """for saving the photo but not show"""

cv2.imshow("my photo" , photo)  #it show the photo
cv2.waitKey() #for capturing and showing till you dont close it hangs you terinal
cv2.destroyAllWindows() # for not hanging terminal

print(r)


"""this is done with your laptop but how you can run this program on your friends pc
#pwd //for finding current directory
# scp  cam.py ....ip.....:/root   //for transfering the file to fiends pc
# ssh -X .....ip.... python36 /root/cam.py
