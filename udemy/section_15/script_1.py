import cv2
"""
1 : read image as it is, with colors (rgb)
0 : read image as black and white
-1 : color image, which will have transparency capabilities
type of img is <class 'numpy.ndarray'>
"""
img = cv2.imread("galaxy.jpg", 0)
img_shape = img.shape
img_dimensional = img.ndim
print(img)
print(img_shape)
print(img_dimensional)

resized_img = cv2.resize(img, (img_shape[1]//2, img_shape[0]//2))
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_resized.jpg", resized_img)
cv2.waitKey(0) # in msec
cv2.destroyAllWindows()