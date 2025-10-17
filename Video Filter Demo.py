# Capture video from webcam
# Convert to gray → blur → detect edges → show live result


import cv2 as cv

# Reading the video from Webcam
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    # just incase the webcam dropped a frame or somthing
    if not isTrue:
        break
    # making the webcam full screen
    frame = cv.resize(frame, (1920, 1080))
    # To maintain the original aspect ratio dynamically:
    scale = 0.5  # 50% smaller
    frame = cv.resize(frame, (0, 0), fx=scale, fy=scale)
    # Applying gray scale
    gray_webcam = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Live video', gray_webcam)

    # Applying blur on grey scale
    blur = cv.GaussianBlur(gray_webcam, (9, 9), cv.BORDER_DEFAULT)
    #cv.imshow('blured grey web cam', blur)

    # Appling canny edges to blured gray webcam
    canny = cv.Canny(blur, 50, 150)
    #cv.imshow('canny web cam', canny)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

# Release the webcam
capture.release()
# exit all the windows
cv.destroyAllWindows()
