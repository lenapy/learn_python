import cv2
import numpy

im_g = cv2.imread(r'C:\Users\Helen\PycharmProjects\learn_python\udemy\files\smallgray.png', 0) # 0 for grey, 1 for rgb

cv2.imwrite('new_small_grey.png', im_g)

ex = im_g[0:2, 2:4]
sh = im_g.shape
num = im_g[2,4] # 182 -> last row and last column in that row

for i in im_g: # i -> row
	print(i)

for i in im_g.T: # i -> column
	print(i)

for i in im_g.flat: # access to arrays elements one by one
	print(i)

ims = numpy.hstack((im_g, im_g)) # concatenate horizontal
print(ims)

ims_v = numpy.vstack((im_g, im_g)) # concatenate vertical
print(ims_v)

lst = numpy.hsplit(ims, 5)
print(lst)