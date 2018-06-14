import time
import sys
sys.path.append("config")	#配置地址
sys.path.append("entity")	#实体地址
sys.path.append("system")	#子系统地址
sys.path.append("FineArts\png")	#图片保存位置
import pygame
from screen import Screen   #界面配置
from actorMgr import ActorMgr #角色管理器	
from battleMgr import BattleMgr #战斗管理器


def run_game():
	#获取配置
	screenCfg = Screen()
	#初始化游戏
	pygame.init()
	screen = pygame.display.set_mode((screenCfg.width, screenCfg.higth))
	background = pygame.image.load("FineArts/png/背景/背景图.jpg")
	pygame.display.set_caption("广职明月")

	#角色管理
	i_actorList = []	#存放队伍角色
	d_actorList = []	#存放敌对角色
	actorMgr = ActorMgr(screen, i_actorList, d_actorList)

	#战斗管理器
	battleMgr = BattleMgr(i_actorList, d_actorList)

	#队友
	actorMgr.addTeam(1, 1, 10)
	actorMgr.addTeam(4, 2, 10)
	actorMgr.addTeam(3, 3, 10)
	actorMgr.addTeam(7, 7, 10)
	
	

	#敌人
	actorMgr.addHostile(8, 1, 10)
	actorMgr.addHostile(6, 2, 10)
	actorMgr.addHostile(2, 3, 10)
	actorMgr.addHostile(5, 7, 10)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#重绘屏幕
		screen.blit(background, (0,0))		#背景图
		battleMgr.run()						#战斗计算
		actorMgr.blitme()					#战斗人物绘画
		#显示
		pygame.display.flip()



run_game()