import time
import sys
sys.path.append("config")	#配置地址
sys.path.append("entity")	#实体地址
sys.path.append("system")	#子系统地址
sys.path.append("FineArts/screen")	#图片保存位置
import pygame
from actorMgr import ActorMgr #角色管理器	
from battleMgr import BattleMgr #战斗管理器
from dataMgr import DataMgr		#数据管理器
from screenMgr import ScreenMgr	#场景管理器


def run_game():
	#初始化游戏
	pygame.init()
	pygame.display.set_caption("明月")

	#初始化管理器
	screenMgr = ScreenMgr()	#初始化场景管理器
	actorMgr = ActorMgr(screenMgr.screen)		#角色管理器
	battleMgr = BattleMgr(actorMgr.i_actorList, actorMgr.d_actorList)#战斗管理器
	dataMgr = DataMgr()		#数据管理器

	#添加 

	#队友
	actorMgr.addTeam(1, 1, 10)
	actorMgr.addTeam(4, 2, 10)
	actorMgr.addTeam(3, 3, 10)
	actorMgr.addTeam(7, 7, 10)
	
	#敌人
	#actorMgr.addHostile(8, 1, 10)
	#actorMgr.addHostile(6, 2, 10)
	#actorMgr.addHostile(2, 3, 10)
	#actorMgr.addHostile(5, 7, 10)

	#相关管理器连接
	screenMgr.load_actorMgr(actorMgr)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#重绘屏幕
		screenMgr.black_blitme()				#绘制背景图

		#如果是在平时
		if screenMgr.state == "normal":
			actorMgr.blitme()					#人物绘画
			screenMgr.event()					#鼠标事件
			screenMgr.scren_blitem()			#绘制场景内容
		#在战斗时
		elif screenMgr.state == "battle":
			ret = battleMgr.run()				#战斗计算
			#如果战斗结束了
			if ret == 1:
				screenMgr.state = "normal"
			actorMgr.blitme()					#人物绘画

		#显示
		pygame.display.flip()



run_game()
