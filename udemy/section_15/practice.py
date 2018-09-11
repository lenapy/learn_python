import cv2
import glob

"""
Write a script that resizes all images in a directory to 100x100.

"""

def resize(path):
	list_of_images = glob.glob("{path}/*.jpg".format(path=path))
	for img in list_of_images:
		image_name = img.split("\\")[-1]
		new_name = "resized_%s" % image_name
		img = cv2.imread(img, 1)
		resized_img = cv2.resize(img, (100, 100))
		cv2.imwrite(new_name, resized_img)


resize(r".\sample-images")