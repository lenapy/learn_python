import cv2

video_path = r'.\1507940147251-drlcss.mp4'
video = cv2.VideoCapture(video_path)
# a = 0
# while True:
# 	a+=1
check, frame = video.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow("Capturing", gray)
cv2.waitKey(0)
	# key = cv2.waitKey(20)
	# if key == ord('q'):
# 		break
#
# print(a)
video.release()
cv2.destroyAllWindows()