# 系统模块
import time
# 三方模块
import pygame
# 项目模块
from control.mouse import Mouse
from control.image import Image
from enums.game_enum import game_enum

# 图像类型
# 界面按钮
BUTTON = 1

# 图像管理器
class ImageMgr():

    def __init__(self):
        # 基本设置
        self.last_time = 0          # 上次刷新的时间
        self.frames = 50            # 帧数
        self.image_list = []        # 图像列表 (注意列表的顺序代表z轴)
        self.image_callback = {}    # 图像资源对应的回调函数
        self.image = pygame.display.set_mode((500, 500))    # 设置窗体
        self.background = pygame.image.load("main/FineArts/png/背景/背景图.jpg")    # 设置背景图片
        self.x = 0
        self.y = 0

        # 管理器
        self.mouse = Mouse()    # 鼠标事件管理器

        # 初始界面
        self.add_image("main/FineArts/png/界面/战斗.png", "fight", [0,0], BUTTON, self.fight_callback)
        self.add_image("main/FineArts/png/界面/保存.png", "save", [100,100], BUTTON, self.fight_callback)

    # 绘制刷新界面
    def blit_image(self):
        # 是否到了刷新时间
        now_time = time.time()
        if self.last_time + 1/self.frames > now_time:
            return
        # 绘制背景
        self.image.blit(self.background, (self.x, self.y))
        self.last_time = now_time
        # 绘制子级图像
        for tmp_image in self.image_list:
            tmp_image.blit_image()
        # 显示
        pygame.display.flip()

    # 鼠标事件
    def event(self):
        mouse_ret = self.mouse.mouse_event()
        if mouse_ret.type == game_enum.mouse.click_open:
            print(str(mouse_ret.x) + "," + str(mouse_ret.y))
            # 查找点击到的图像
            for tmp_image in self.image_list:
                ret,obj = tmp_image.get_click_image(mouse_ret)
                if ret == True:
                    self.image_callback[obj.name]()
                    return True
            return False
            

    # 添加一个图像
    # path : 图像资源地址
    # name : 名字
    # postion : 位置
    # tmp_type : 图像资源类型
    # callback : 回调函数
    def add_image(self, path, name, postion, tmp_type, callback):
        # 添加图像到列表
        tmp_image = Image(self, path, name, tmp_type)
        tmp_image.x = postion[0]
        tmp_image.y = postion[1]
        self.image_list.append(tmp_image)
        self.image_callback[name] = callback

    # 战斗按钮的回调
    def fight_callback(self):
        print("fight_callback")

imageMgr = ImageMgr()
