import cv2

image_path = 'img/cats.jpg'
image_cat = cv2.imread(image_path)

# cv2.imshow('Cats', image_cat)
# cv2.waitKey(5000)

cats_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
cats_face = cats_face_cascade.detectMultiScale(image_cat)

# print(cats_face)
# cv2.imshow('Cats', image_cat)
# cv2.waitKey()

for (x, y, w, h) in cats_face:
    print(x, y, w, h)
    cv2.rectangle(image_cat, (x, y), (x + w, y + h), (0, 0, 255), 3)

cv2.imshow('Cats', image_cat)
cv2.waitKey()
