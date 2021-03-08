import cv2
import sys, copy, numpy
import CtrlTool as ctl
# Setting
global SIZE
SIZE = 1.0
global THRESHOLD, DELTA
global BDOWN, BUP, BLOCKSIZE, Base_x, Base_y
BUP = 1.0
BLOCKSIZE = BUP
BDOWN = 0.9
THRESHOLD = 0.8
DELTA = 10
Base_x = 735
Base_y = 116
block_img = ctl.read_img("./Block3.png", SIZE * 0.951)
img = cv2.imread("cap.png", -1)
res =  cv2.matchTemplate(img, block_img, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
loc = numpy.where(res >= 0.7)  # 输出符合条件的坐标
# ran = loc[0]
# Draw
print(loc)