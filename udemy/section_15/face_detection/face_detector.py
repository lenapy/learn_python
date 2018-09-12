import cv2

face_cascade = cv2.CascadeClassifier(r"Files\haarcascade_frontalface_default.xml")
# load image
img = cv2.imread(r"Files\news.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5) # 1.05 -> 5%

for x, y, w, h in faces:
	img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

print(faces)

# resized = cv2.resize(img, (img.shape[1]//3, img.shape[0]//3))

cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


