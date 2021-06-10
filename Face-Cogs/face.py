import cv2

print("hello there human, your webcam will open now and you'll see the magic for youself")

trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

# choosing an image to test here (READING THE IMAGE)
#img = cv2.imread('mp.png')


webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()

    # converting to grayscale for algorithm to detect the image
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv2.imshow("Nik's Face Detector", frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break


"""
# Detect the faces in the image(single/many)
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


# Drawing a rectangle over the face
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)


# print(face_coordinates)


# to show the image (DISPLAYING THE IMAGE)
cv2.imshow("Nik's Face Detector", img)
cv2.waitKey()
"""
