# 系统模块

# 三方模块
import pygame
# 项目模块
from enums.game_enum import game_enum

# 鼠标事件的返回
class Postion():
    def __init__(self):
        self.type = game_enum.mouse.click_free
        self.x = 0
        self.y = 0

# 鼠标事件处理
class Mouse():

    def __init__(self):
        self.left_set = False   # 左键是否置位
        self.right_set = False  # 右键是否置位

    # 鼠标事件
    # type : 0:无操作, 1:点击左键, 2:左键弹起
    def mouse_event(self):
        pressde = pygame.mouse.get_pressed()    # 获取鼠标按下信息
        position = pygame.mouse.get_pos()       # 获取鼠标位置
        ret = Postion()
        ret.x = position[0]
        ret.y = position[1]
        if pressde[0]:
            self.left_set = True
            ret.type = game_enum.mouse.click_down
        elif pressde[0] == 0 and self.left_set == True:
            self.left_set = False
            ret.type = game_enum.mouse.click_open
        return ret
