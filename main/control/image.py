# 系统模块

# 三方模块
import pygame
# 项目模块


# 窗口
class Image():
    # 初始化
    # parent : 父级窗口
    # path : 图像资源地址
    # name : 资源名
    # tmp_type : 图像类型
    # postion : 坐标
    def __init__(self, parent, path, name, tmp_type, postion):
        self.parent = parent    # 父级窗口
        self.image_list = []    # 子级窗口列表
        self.image = self.background = pygame.image.load(path)
        self.name = name        # 对应名字
        self.type = tmp_type    # 游戏类型
        self.width = self.image.get_width()    # 图像宽度
        self.height = self.image.get_height()  # 图像高度
        self.x = postion[0]
                      # 相对父级的x坐标
        self.y = postion[1]              # 相对父级的y坐标

    # 绘制窗口内的图像资源
    def blit_image(self):
        self.parent.image.blit(self.image, (self.x, self.y))
        # 循环反复调用绘制子级
        for tmp_image in self.image_list:
            tmp_image.blit_image()

    # 添加一个窗口
    # 统一以parent为绘制窗口
    # path : 图像资源地址
    # name : 资源名
    # tmp_type : 图像类型
    # postion : 坐标
    # callback : 对应的回调函数
    def add_image(self, path, name, tmp_type, postion, callback):
        # 添加图像到列表
        tmp_image = Image(self.parent, path, name, tmp_type, postion)
        self.image_list.append(tmp_image)
        self.parent.image_callback[name] = callback

    # 获取点击的图像
    def get_click_image(self, postion):
        # 循环反复调用查找子级
        if self.x < postion.x and (self.x + self.width) > postion.x and self.y < postion.y and (self.y + self.height) > postion.y:
            # 查找点击到的图像,从后面开始找
            list_len = len(self.image_list)
            for idx in range(0, list_len):
                tmp_image = self.image_list[list_len - idx - 1]
                ret,obj = tmp_image.get_click_image(postion)
                if ret == True:
                    return True,obj
            return True,self
        return False,self