""" Gezichten herkennen """
import cv2

BLUE = (255,0,0)
RED = (0,0,255)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
video_input = cv2.VideoCapture(0)

while True:
    _, img = video_input.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 100)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), BLUE, 3)
        face = img[y:y+h, x:x+w]
        blur_face = cv2.blur(face, (50, 50))
        img[y:y+h, x:x+w] = blur_face
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), RED, 1)

    # img = cv2.bitwise_not(img)
    # img=cv2.blur(faces, (50, 50))
    # img = cv2.Canny(img, 100, 100)
    cv2.imshow('img', img)

    key = cv2.waitKey(10)
    if key == 32:
        break

video_input.release()
cv2.destroyAllWindows()
