# 系统模块

# 三方模块
import pygame
# 项目模块


# 窗口
class Image():
    # 初始化
    # path : 图像资源地址
    # name : 资源名
    # tmp_type : 游戏类型
    # parent : 父级窗口
    def __init__(self, parent, path, name, tmp_type):
        self.parent = parent    # 父级窗口
        self.image_list = []    # 子级窗口列表
        self.image = self.background = pygame.image.load(path)
        self.name = name        # 对应名字
        self.type = tmp_type    # 游戏类型
        self.width = self.image.get_width()    # 图像宽度
        self.height = self.image.get_height()  # 图像高度
        self.x = 0              # 相对父级的x坐标
        self.y = 0              # 相对父级的y坐标

    # 绘制窗口内的图像资源
    def blit_image(self):
        self.parent.image.blit(self.image, (self.x, self.y))
        # 循环反复调用绘制子级
        for tmp_image in self.image_list:
            tmp_image.blit_image()

    # 添加一个窗口
    # 统一以parent为绘制窗口
    def add_image(self, path, name, tmp_type):
        tmp_image = Image(self.parent, path, name, tmp_type)
        self.image_list.append(tmp_image)

    # 获取点击的图像
    def get_click_image(self, postion):
        # 循环反复调用查找子级
        if self.x < postion.x and (self.x + self.width) > postion.x and self.y < postion.y and (self.y + self.height) > postion.y:
            for tmp_image in self.image_list:
                ret,obj = tmp_image.get_click_image(postion)
                if ret == True:
                    return True,obj
            return True,self
        return False