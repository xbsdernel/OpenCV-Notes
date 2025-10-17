# 1. Read and show the image
# 2. Convert to gray
# 3. Apply Gaussian blur
# 4. Detect edges (Canny)
# 5. Dilate edges
# 6. Erode edges
# 7. Resize
# 8. Crop


import cv2 as cv

# image path
img_path = 'D:\\OpenCV Projects\\opencv-course-master\\Resources\\Photos\\group 2.jpg'
# reading the image
img = cv.imread(img_path)
# displaying the image
cv.imshow('group photo', img)

# converting img to gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# displaing the gray image
cv.imshow('gray image', gray_img)

# blur the image
blured_img = cv.GaussianBlur(gray_img, (7,7), cv.BORDER_DEFAULT)
# Displaying the image
cv.imshow('Blured image', blured_img)

# Edge detection
canny = cv.Canny(blured_img, 150,250)
# displaying the Image
cv.imshow("gray blured Edge detection", canny)

# dilate the image
dilated = cv.dilate(canny, (5,5), iterations=2)
# displaying the image
cv.imshow("the dialeted image", dilated)

# Erode the dilated image
Eroded = cv.erode(dilated, (5,5), iterations=2)
# displaying the image
cv.imshow("Eroded dilated image", Eroded)

# Resize the Eroded dilated image
resized = cv.resize(Eroded, (500,500), interpolation=cv.INTER_CUBIC)
# displaying the image
cv.imshow("The resized image", resized)

# crop the resized image
croped_img = resized[20:100, 250:350]
# displaying the image
cv.imshow("The cropped resied image", croped_img)

cv.waitKey(0)