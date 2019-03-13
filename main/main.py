# 系统模块
import time
import sys
# 三方模块
import pygame
# 项目模块
from system import imageMgr_1

# 开始运行文件
def run():
    pygame.display.set_caption("明月")

    # 初始化各管理器
    imageMgr = imageMgr_1.imageMgr	# 初始化场景管理器



    # 游戏循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        imageMgr.event()
        
        # 绘制界面
        imageMgr.blit_image()
        

run()