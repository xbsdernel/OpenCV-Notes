# Create a blank image
# draw 3 rectangles, text and lines.

import cv2 as cv
import numpy as np

# create a blank image
blank = np.zeros((512,512,3), np.uint8)

# Making the full image pink
blank[:] = 255,0,255
#cv.imshow('test',blank)

# drawing 3 different rectangles
cv.rectangle(blank, (80, 80), (25, 50), (0,255,0), thickness=-1)
cv.rectangle(blank, (50, 320), (80, 140), (255,255,0), thickness=-1)
cv.rectangle(blank, (150, 28), (230, 280), (0,255,255), thickness=-1)
#cv.imshow('test',blank)

# drawing text and lines
text = "Mohamed Hussien"
cv.line(blank, (150, 500), (400, 400), (0,0,0), thickness=1)
cv.putText(blank, text, (200,350), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0), 2)
cv.imshow('test',blank)
cv.waitKey(0)
