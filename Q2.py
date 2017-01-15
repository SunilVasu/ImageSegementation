import cv2

import numpy as np
import cmath

image = cv2.imread('MixedVegetables.jpg',0)
img=image
print image
cv2.imshow("OriginalImage.jpg",image)
(r,c)=image.shape
print(r,c)
superGrid=np.zeros([2*r+1, 2*c+1])
(p,q)=superGrid.shape
print(p,q)
array=np.zeros_like(superGrid)
for x in xrange(0,p-1):
  for y in xrange (0,q-1):
	array[x,y]=255

cv2.imshow("ThresholdImage.jpg",image)
zc=np.zeros_like(image)

#for x in xrange(0,p-1):
# for y in xrange (0,q-1):
#	crackEdge[x,y]=255

#superGrid[1:r*2+1:2,1:c*2+1:2]=image[0:r:1,0:c:1]
#cv2.imshow("superGrid.jpg",superGrid)
#cv2.imwrite("superGrid.jpg",superGrid)
#print "superGrid",superGrid

#Creating the super grid structure
for x in xrange(0,p-1):
  for y in xrange (0,q-1):
	xx=x/2
 	yy=y/2	
	if(x%2!=0 and y%2!=0):
		superGrid[x,y]=image[(xx),(yy)]
		zc[xx,yy]=image[(xx),(yy)]

crackEdge=superGrid
print "crackEdge",crackEdge
print "test",zc
cv2.imshow("crackEdge.jpg",crackEdge)
cv2.imwrite("crackEdge.jpg",crackEdge)
cv2.imshow("testImage.jpg",zc)
#Value of crack edge point will be the difference in pixel intensity values. Using 4 neighbour.
for x in xrange(0,p-1):
    for y in xrange (0,q-1):	
	xx=x/2
	yy=y/2
   	if(x%2==0):
		if(y%2==0):#(x,y) even even
			crackEdge[x,y]=1
		elif(y%2!=0):#(x,y) even odd
			if(x==0):
				if(y==1):
					crackEdge[x,y]=image[0,0]
				else:
					crackEdge[x,y]=image[0,yy]
			else:
				if(x<p-3 and y<q-3):
					crackEdge[x,y]=abs(image[xx+1,yy]-image[xx-1,yy])
	elif(x%2!=0):
		if(y%2==0):#(x,y) odd even		
			if(y==0):
				crackEdge[x,y]=image[x/2,0]
			else:
				if(x<p-3 and y<q-3):
					crackEdge[x,y]=abs(image[xx,yy+1]-image[xx,yy-1])

print "4 Neighbour",crackEdge
cv2.imwrite("crackEdge2.jpg",crackEdge)
cv2.imshow("crackEdge2.jpg",crackEdge)

#Now take a threshold T1 and mark all crack edges below this T1 as '0' and above it as '1'
for x in xrange(0,p-1):
    for y in xrange (0,q-1):
   	if(x%2==0):
		if(y%2!=0):
				if(crackEdge[x,y]<50):
					crackEdge[x,y]=0 #weak Edges
				else:
					crackEdge[x,y]=1 #Strong Edges			
	elif(x%2!=0):
		if(y%2==0):		
			
				if(crackEdge[x,y]<50):
					crackEdge[x,y]=0 #weak Edges
				else:
					crackEdge[x,y]=1 #Strong Edges
	


#Created a new array, now using the formula we merge the weak crack edge with the its neighbours		
print "After Thresholding",crackEdge
cv2.imshow("Treshold_crackEdge.jpg",crackEdge)
cv2.imwrite("Treshold_crackEdge.jpg",crackEdge)


for x in xrange(0,p-2):
  for y in xrange (0,q-2):
	if(crackEdge[x,y]==1):
		array[x,y]=0	
	#if(crackEdge[x,y]==0 and x%2==0 and y%2!=0 and x!=0):
	#	array[x,y]=abs(crackEdge[x+1,y]+crackEdge[x-1,y])/2
	#if(crackEdge[x,y]==0 and x%2==0 and y%2!=0 and x==0):
	#	array[x,y]=crackEdge[x+1,y]
	#if(crackEdge[x,y]==0 and x%2!=0 and y%2==0 and y!=0):
	#	array[x,y]=abs(crackEdge[x,y+1]+crackEdge[x,y-1])/2
	#if(crackEdge[x,y]==0 and x%2!=0 and y%2==0 and y==0):
	#	array[x,y]=crackEdge[x,y+1]


print array
cv2.imshow("array.jpg",array)
cv2.imwrite("array.jpg",array)

#
flag=1
#while(flag==1):
for z in xrange(0,20):
  for x in xrange(0,p-1):
    for y in xrange (0,q-1):
	if(crackEdge[x,y]==0 and x%2!=0):	
		crackEdge[x,y]=crackEdge[x,y+1]
	elif(crackEdge[x,y]!=0 and x%2!=0 and y%2==0):
		crackEdge[x,y]=0
	#for x in xrange(0,p-1):
         #  for y in xrange (0,q-1):
	#	if(crackEdge[x,y]==0 and x%2!=0 and y%2==0):
	#		flag=1
	#	else:
	#		flag=0

#for z in xrange(0,20):
 for y in xrange(0,q-1):#c
    for x in xrange (0,p-1):#r
	if(crackEdge[x,y]==0 and x%2==0 and y%2!=0):	
		crackEdge[x,y]=crackEdge[x+1,y]
	elif(crackEdge[x,y]==0 and x%2==0 and y%2!=0):
		crackEdge[x,y]=0



#print "After Thresholding",crackEdge
#cv2.imshow("Merge_crackEdge2.jpg",crackEdge)
#cv2.imwrite("Merge_crackEdge2.jpg",crackEdge)

for x in xrange(0,p-1):
    for y in xrange (0,q-1):
	if(crackEdge[x,y]==0 and x%2!=0 and y%2!=0):
		if(crackEdge[x,y]<150):
			crackEdge[x,y]=0
		else:
			crackEdge[x,y]=255
		
#cv2.imshow("NewMerge_crackEdge2.jpg",crackEdge)
#cv2.imwrite("NewMerge_crackEdge2.jpg",crackEdge)
cv2.waitKey(0)
cv2.destroyAllWindows()

