import os, time
import cv2, numpy
import pyautogui
from PIL import ImageGrab

#######Screencap #######
global screencapLast, screencapNow
screencapLast = 0
screencapNow = 1

def Get_Cap(Base_x, Base_y):#get picture of game
    scope = (Base_x, Base_y, Base_x + 450, Base_y + 670)
    pic = ImageGrab.grab(scope)
    pic.save('D:\\code\\CourseDesign\\cap.png')

def screen(Base_x, Base_y):#get picture_data
    # Calc FPS
    time.sleep(2)
    global screencapLast, screencapNow
    screencapLast = screencapNow
    screencapNow = time.time()
    # Create & Pull
    Get_Cap(Base_x, Base_y)
    screencapName = "cap.png"
    # Read & Return
    img = cv2.imread(screencapName, -1) #返回值为一个三维矩阵，通过RGB来表示图片中的每一个点
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def screen_fps():
    global screencapLast, screencapNow
    return "FPS: {}".format(1.0/(screencapNow-screencapLast))


####### PyAutoGui Click #######D
def click(x, y, Base_x, Base_y):
    pyautogui.click(x+Base_x, y+Base_y, 1, 0, "left")


def sweep(x0, y0, x1, y1, ctime = 50):
    os.system("adb shell input touchscreen swipe %d %d %d %d %d" % (x0, y0, x1, y1, ctime))


def long_click(x, y, ctime = 1000):
    sweep(x, y, x+5, y+5, ctime)


###### CV ######
def read_img(file, fx):
    # Read
    img = cv2.imread(file, -1)

    # Resize
    a, w, h = img.shape[::-1]
    w = int(w * fx)
    h = int(h * fx)
    img = cv2.resize(img, (w, h))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow("ddd", img)
    # cv2.waitKey()
    return img


def match_img(img, tem, thr): #总图片  待匹配图片  threshold
    # Info
    a, w, h = tem.shape[::-1]
    # print(img.shape)
    # print(tem.shape)
    #tem = cv2.cvtColor(tem, cv2.COLOR_BGR2RGB)
    res = cv2.matchTemplate(img, tem, cv2.TM_CCOEFF_NORMED) #得到一个res矩阵，表示每次移动相似度
    # print(res)

    # Select
    loc = numpy.where(res >= thr) #输出符合条件的坐标
    # ran = loc[0]
    # Draw
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)
                        # 左上角坐标   右下角的坐标            边框的颜色   边框的厚度
    # cv2.imshow("dff", img)
    # cv2.waitKey()
    return loc, res


def show_img(img, title = "screen", height = 800):
    # Resize
    size = img.shape
    dsize = (size[1] * height // size[0], height)
    disp = cv2.resize(img, dsize)

    # Show
    cv2.imshow(title, disp)

    # Waitkey
    return cv2.waitKey(1)


###### Main ######

def main():
    block_img = read_img("Block3.png", 0.9)
    cv2.imshow("dddd", block_img)
    cv2.waitKey()
    a = 1
    while True:
        img = screen()
        cv2.imshow('image', img)
        k = cv2.waitKey(1)
        if k == 27:  # wait for ESC key to exit
            cv2.destroyAllWindows()
        elif k == ord('s'):  # wait for 's' key to save and exit
            cv2.imwrite('messigray.png', img)
            cv2.destroyAllWindows()
    # pass

if __name__ == "__main__": main()

