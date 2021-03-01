import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()#ret returns True or False, True if video capture is complete
    width,height=int(cap.get(3)),int(cap.get(4))

    image=np.zeros(frame.shape, np.uint8)
    frameshrunk=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)#Shrinks to 1/4 th as fx*fy=0.25
    image[:height//2, :width//2]=frameshrunk [:,::-1]          #first quadrant, similar cartesian i.e. top right is 1st quadrant; frameshrunk[keeps it straight:flips horizontally ie across y axis]
    image[:height//2, width//2:] = frameshrunk                   #2nd quadrnt, top left is 2nd quadrant
    image[height//2:, width//2:] = frameshrunk[::-1,:]         # 3rd quadrant, bottom left is 3rd quadrant
    image[height//2:, :width//2] = frameshrunk[::-1,::-1]    # 4th quadrant, bottom right is 4th quadrant

#Reference graph below:
#               |
# IInd quadrant |  1st quadrant
#               |
#               |
#  _____________|_______________
#               |
#               |
#     3rd       |      4th
#               |
 
                       
    cv2.imshow('frame',image)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
