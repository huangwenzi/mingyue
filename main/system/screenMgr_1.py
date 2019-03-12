# 系统模块
import time
# 三方模块
import pygame
# 项目模块
from control.mouse import Mouse
from control.screen import Screen

# 窗口管理器
class ScreenMgr():
    
    def __init__(self):
        # 基本设置
        self.last_time = 0   # 上次刷新的时间
        self.frames = 50     # 帧数
        self.screen_list = []# 窗口列表
        self.screen = pygame.display.set_mode((500, 500))
        self.background = pygame.image.load("main/FineArts/png/背景/背景图.jpg")
        self.mouse = Mouse()

        
    # 绘制刷新界面
    def blit_screen(self):
        # 是否到了刷新时间
        now_time = time.time()
        if self.last_time + 1/self.frames > now_time:
            return

        self.screen.blit(self.background, (0,0))
        self.last_time = now_time
        #显示
        pygame.display.flip()
    
    # 鼠标事件
    def event(self):
       mouse_ret = self.mouse.mouse_event()
       if mouse_ret.type == 2:
           print(mouse_ret.position)
        
    # 添加一个窗口
    def add_screen(self, path, name, tmp_type):
        tmp_screen = Screen(path, name, tmp_type)
        self.screen_list.append(tmp_screen)

screenMgr = ScreenMgr()