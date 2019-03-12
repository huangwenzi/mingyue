# 系统模块
import time
import sys
# 三方模块
import pygame
# 项目模块
from system import screenMgr_1

# 开始运行文件
def run():
    pygame.display.set_caption("明月")

    # 初始化各管理器
    screenMgr = screenMgr_1.screenMgr	# 初始化场景管理器

    # 添加测试窗口
    # "main\FineArts\png\界面\战斗.png"


    # 游戏循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        screenMgr.event()
        
        # 绘制界面
        screenMgr.blit_screen()
        

run()