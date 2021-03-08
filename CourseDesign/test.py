import pyautogui
import cv2
import numpy
import CtrlTool as ctl

bug = cv2.imread("Bug.png", -1)
block_img = cv2.imread("Block3.png", -1)
bug = cv2.cvtColor(bug, cv2.COLOR_BGR2RGB)
block_img = cv2.cvtColor(block_img, cv2.COLOR_BGR2RGB)
a, w, h = block_img.shape[::-1]
res = cv2.matchTemplate(bug, block_img, cv2.TM_CCOEFF_NORMED)
loc = numpy.where(res >= 0.8)  # 输出符合条件的坐标
# ran = loc[0]
# Draw
for pt in zip(*loc[::-1]):
	cv2.rectangle(bug, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)
cv2.imshow("ddd", bug)
cv2.waitKey()