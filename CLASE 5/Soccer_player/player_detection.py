#Import libraries
import cv2
import os
import numpy as np

#Reading the video
vidcap = cv2.VideoCapture('cutvideo.mp4')
success,image = vidcap.read()
count = 0
success = True
idx = 0

#Read the video frame by frame
while success:
	#converting into hsv image
	hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	#green range
	lower_green = np.array([40,40, 40])
	upper_green = np.array([70, 255, 255])
	#blue range
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	#Red range
	lower_red = np.array([0,31,255])
	upper_red = np.array([176,255,255])

	#white range
	lower_white = np.array([0,0,0])
	upper_white = np.array([0,0,255])

    #Define a mask ranging from lower to uppper
	mask = cv2.inRange(hsv, lower_green, upper_green)
    #Do masking
	res = cv2.bitwise_and(image, image, mask=mask)
	#convert to hsv to gray
	res_bgr = cv2.cvtColor(res,cv2.COLOR_HSV2BGR)
	res_gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

    #Defining a kernel to do morphological operation in threshold image to 
    #get better output.
	kernel = np.ones((13,13),np.uint8)
	thresh = cv2.threshold(res_gray,127,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
	

    #find contours in threshold image     
	im2,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	

	prev = 0
	font = cv2.FONT_HERSHEY_SIMPLEX
	
	for c in contours:
		x,y,w,h = cv2.boundingRect(c)
		if(h>=(1.5)*w):
			if(w>15 and h>= 15):
				idx = idx+1
				player_img = image[y:y+h,x:x+w]
				cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
	count += 1
	cv2.imshow('Match Detection',image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	success,image = vidcap.read()
    
vidcap.release()
cv2.destroyAllWindows()

