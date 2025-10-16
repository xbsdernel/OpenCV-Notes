# OpenCV-Notes
Repo for sharing my notes while Studing OpenCv.

## Source i study from:

OpenCV Course - Full Tutorial with Python (FreeCodeCamp on youtube)


## Basics:

1- Reading Images and Videos

2- Image Transformations

3- Drawing Shapes

4- Putting Text

## Advanced:

1- Color Spaces

2- BITWISE operations

3- Masking

4- Histogram Computation

5- Edge Detection

## Faces: 

1- Face Detection

2- Face Recognition

3- Deep Computer Vision to classify between characters in a TV show


### Intro

OpenCV is a computer vision library that is available in python, C++ and java. 

A computer vision is an application of deep learning that is primary  driving insights from media files that is images and video.



### 1- Reading images in OpenCV

```Python
'''  
How to read images in Opencv  
'''  
import cv2 as cv  
  
# reading image, it takes an image and return it as matrix of pixels  
cat_img = cv.imread('opencv-course-master\\Resources\\Photos\\cat_large.jpg')  
  
# display the image, it displays the image as a new window (name of the window, matrix of pixels)  
cv.imshow('Cat', cat_img)  
  
# key (keyboard) ending function, it waits for time in mille seconds for a key to be preseed  
# 0 means it will wait for infinite amount of time  
cv.waitKey(0)
```

### 2- Reading Videos in OpenCV

```Python
'''  
Reading Videos in OpenCv  
'''  
import cv2 as cv  
  
# Method that takes integer argument or a path to a video file  
# you will provide integer argument if you are using a webcam or camera  
# capture variable is an instance of 'VideoCapture' class  
capture = cv.VideoCapture('opencv-course-master\\resources\\Videos\\dog.mp4')  
  
while True:  
    #inside the loop  
    # we grampe the video fram by frame by utlizing 'capture.read' method    # we displayed each frame of the video by using 'cv.imshow' method    # we end this loop by using waitkey of 20 mille seconds and OxFF    # 0xFF -> means if letter d is pressed on keyboard -> end the loop which means stop the video and close  
  
    # reads the video frame by frame    # it returns the frame and bool that says if frame have read or not    isTrue, frame = capture.read()  
    # to display the video  
    cv.imshow('Video', frame)  
    # to stop the video from playing infinitly  
    # waitKey(20) adds a 20ms delay between frames to control playback speed    
    if cv.waitKey(20) & 0xFF == ord('d'):  
        break  
  
# release the VideoCapture object (free camera/file resources)  
capture.release()  
# close all OpenCV windows opened by cv.imshow()  
cv.destroyAllWindows()  
  
# when the video ends you get this error in terminal  
'''  
 (-215:Assertion failed)'''  
# that error means OpenCv can`t find media file at that particular location that you specifiead  
# the reason why this happens in video is bec the video run out of the frames, openCv can`t find anymoe frames after the last frame in the video so it`s unenspextdly it brokes out of the loop by itself  
# BTW the same error will Gonna appear if ypu insert a long location of a video or image
```

### 3 - Resizing & Rescaling Images and Videos
```Python
'''  
Resizing & Rescaling Images  
  
we usally resize and rescale video files and images to prevent computational ...  
large media files tend to store alot of information in it  
displaying it takes alot of processing needs that a computer needs to resign  
  
so by resizing and rescaling we actually trying to get rid of some of that information  
  
rescaling a video implies modifing a height and width to particular height and width  
genrarly it always best practice to downscale or change the width and height of your video files to a smaller value than the orignal dimentions  
  
This is beacuse most cameras (your webcam included) don`t spose going higher than it`s maxiumum capapilties  
for ex: if camera shoots in 720P, so it`s not gonna be able to shoot in 1080P or Higher  
  
so to rescale a videoframe or an image  
  
'''  
import cv2  
  
  
# rescale a videoframe or an image  
# function does, it takes a frame and scales that frame by a particular scale value (0.75)  
# This method (rescaleFrame) will work for Images, Videos and Live videos  
def rescaleFrame(frame, scale= 0.75):  
    # frame.shape[1] -> the width of your frame or image  
    width = int(frame.shape[1] * scale)  
    # frame.shape[0] -> the width of your frame or image  
    height = int(frame.shape[0] * scale)  
  
    diemenstions = (width, height)  
    # it resizes the frame into a particular diemenstion  
    return cv2.resize(frame, diemenstions, interpolation = cv2.INTER_AREA)  
  
  
# The video read code + some code  
import cv2 as cv  
  
capture = cv.VideoCapture('opencv-course-master\\resources\\Videos\\dog.mp4')  
  
  
  
while True:  
    isTrue, frame = capture.read()  
    # calling the function to resize each fram of the video by 75%  
    frame_resized = rescaleFrame(frame)  
  
  
    cv.imshow('Video', frame)  
    # preview the resized video  
    cv.imshow('Video Resized', frame_resized)  
  
    if cv.waitKey(20) & 0xFF == ord('d'):  
        break  
capture.release()  
cv.destroyAllWindows()  
  
  
# read images code + some code  
import cv2 as cv  
  
cat_img = cv.imread('opencv-course-master\\Resources\\Photos\\cat_large.jpg')  
  
# preview the resized cat image by 20%  
cv.imshow('Cat', rescaleFrame(cat_img,0.2))  
  
  
cv.waitKey(0)  
  
  
  
# Changing the resolution of the image and video  
# This method (changeResolution) will work only for Live videos (for ex: webcam)  
  
def changeResolution(width, height):  
    # 3 refrenses to width, 4 refrences to height  
    capture.set(3, width)  
    capture.set(4, height)
```

### 4 - Draw Shapes and write text on an image
**Need a review again with Chatgpt
```Python

# 1- Creating a blank image

# np.zero -> cretaing a zero Matrix

# A zero Matrix means the image is black

# (height, width, no. of channls)

# unit8 -> the datatype of image

blank = np.zeros((512, 512, 3), 'uint8')

  

# 2- Painting the image

# make the full image Green

blank[:] = 0,255,0

  

# 3- Painting a part of an image

# 200:300 -> height

# 300:400 -> width

blank[200:300, 300:400] = 0,0,255

  

# 4- Drawing a Rectangle on an image

# blank -> image path

# (0,0) -> top left corner

# (250, 500) -> bottom right corner

# (0,255,0) -> The color of the rectangle

# thickness = -1 -> fill the rectangle with the green color

cv.rectangle(blank, (0, 0), (250, 500), (0,255,0), thickness=-1)

  

# 5- Drawing a circle on an image

# (blank.shape[1]//2, blank.shape[0]//2) under

# draw a circle in the middle of the image

# 40 is half of the diameter

# (0,0,255) -> Red color

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)

  

# 6- Drawing a line

# it draws a line between 2 points

# first point (100, 250)

# second point (300, 400)

# (255,255,255) -> Red color

cv.line(blank, (100, 250), (300, 400), (255,255,255), thickness=3)

  

# 7- Write a text on image

# (225,225) -> position where text starts

# cv.FONT_HERSHEY_SIMPLEX -> font type

# 1.0 -> size of the font

# 2 -> thickness

cv.putText(blank, 'Mohamed ---- Hussien', (225,225), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 2)

  
  

```

### 5 - Essential Functions
```Python
import cv2 as cv  
  
# BGR image  
img = cv.imread('opencv-course-master\\Resources\\Photos\\lady.jpg')  
  
cv.imshow('cat', img)  
  
# converting image to grey scale (3 Ways)  
# this method takes the image path as the first argument  
# and the second argument tou spesify the color you want (BGR2GRAY or BGR2RED etc...)  
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
  
# cv.imshow('grey cat', gray)  
  
  
  
# Bluring an image (Remove some of the noise that exsist in an image)  
# the guassian Blur  
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)  
#cv.imshow('blur', blur)  
  
  
# Edge CasCade  
canny = cv.Canny(img, 175, 200)  
#cv.imshow('canny', canny)  
  
  
# how to dialete an image using a spesific structuring element  
dialeted = cv.dilate(canny, None, iterations=1)  
cv.imshow('dialeted', dialeted)  
  
cv.waitKey(0)
```
