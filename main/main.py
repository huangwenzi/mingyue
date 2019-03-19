# 系统模块
import time
import sys
# 三方模块
import pygame
# 项目模块
from system.imageMgr import imageMgr

# 开始运行文件
def run():
    pygame.display.set_caption("明月")

    # 游戏循环
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            # 处理鼠标事件
            imageMgr.mouse_event()
            # 战斗管理器战斗计算
            imageMgr.battle_reckon()
            # 绘制界面
            imageMgr.blit_image()
        except OSError as err:
            print("OS error: {0}".format(err))
        

run()