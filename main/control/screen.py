# 系统模块

# 三方模块
import pygame
# 项目模块


# 窗口
class Screen():
    
    def __init__(self, path, name, tmp_type):
        self.screen_list = []   # 子级窗口列表
        self.screen = self.background = pygame.image.load(path)
        self.name = name        # 对应名字
        self.type = tmp_type    # 游戏类型
        self.width = self.screen.get_width()    # 图片宽度
        self.height = self.screen.get_height()  # 图片高度
        self.x = 0              # 相对父级的x坐标
        self.y = 0              # 相对父级的y坐标

