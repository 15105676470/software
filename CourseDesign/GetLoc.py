import  os
import  time
import  pyautogui as pg
try:
    while True:
        print("按下组合键 {Ctrl}+C 结束执行\n")
        sW, sH = pg.size()  #获取屏幕的尺寸（像素）screenWidth，screenHeight
        print("屏幕分辨率：\n"+str(sW)+','+str(sH)+'\n')  #打印屏幕分辨率
        x,y = pg.position()   #获取当前鼠标的坐标（像素）
        print("鼠标坐标:\n" + str(x).rjust(4)+','+str(y).rjust(4)) #打印鼠标坐标值
        time.sleep(1) #等待1秒
        os.system('cls')   #清屏
except KeyboardInterrupt:
    print('\n结束,按任意键退出....') #检测到Ctrl+c组合键结束运行