#场景管理器

import sys
sys.path.append(".\FineArts\screen")	#场景图片
sys.path.append("config")	#配置地址
import pygame
import screen

class ScreenMgr():
	
	def __init__(self):
		#配置总表
		self.partsCfg = [screen.parts_1_Cfg, 
						
					]
		#层次图片总表
		self.parts_image = []

		self.screen = pygame.display.set_mode((720, 800))
		self.parts_state = 1			#部件状态 （当前鼠标点击打开层次）

		#背景资源加载
		self.battle_bg = pygame.image.load("FineArts/screen/战斗背景图.jpg")	#战斗背景
		self.normal_bg = pygame.image.load("FineArts/screen/平时背景.jpg")		#平时背景
		self.background = self.normal_bg			#当前背景图

		#设置层次图片
		self.add_prats(0, self.partsCfg[0])

		#当前状态
		self.state = "normal"		#normal:平时  battle:战斗
		self.parts_index = 0
		self.parts_now_image = self.parts_image[self.parts_index]

	#添加角色信息
	def add_actor(self, ):


	#添加层次图片资源
	def add_prats(self, index, cfg):
		while True:
			if len(self.parts_image) >= index + 1 :
				break
			self.parts_image.append([])

		self.parts_image[index] = []
		for v in cfg :
			image = pygame.image.load(v[0])
			image = pygame.transform.scale(image, v[1], )#(缩放)
			self.parts_image[index].append([image, v[2] ])#图片资源，位置

	#绘制背景
	def blitme(self):
		self.screen.blit(self.background, (0,0))

	#绘制部件
	def parts_blitme(self):
		for v in self.parts_now_image:
			self.screen.blit(v[0], v[1])

	#事件获取
	def event(self):
		pressde = pygame.mouse.get_pressed()	#获取鼠标按下信息
		position = pygame.mouse.get_pos()	#获取鼠标位置
		index = 0	#选中索引
		#鼠标点击左键
		if pressde[0]:
			index = self.get_parts(position)
			if index == -1 :
				self.get_actor(position)

	#获取点击的部件
	#position ：鼠标位置
	def get_parts(self, position):
		count = len(self.parts_now_image)
		num = 0
		flag = -1 #点击的索引，为-1表示没有有效点击
		cfg = self.partsCfg[self.parts_index]
		while num < count :
			Lx = cfg[num][2][0]					#左边x
			Rx = cfg[num][2][0] + cfg[num][1][0]#右边x
			Uy = cfg[num][2][1]					#上边y
			Dy = cfg[num][2][1] + cfg[num][1][1]#下边y
			#如果在图片内
			if position[0] >= Lx and position[0] <= Rx and position[1] >= Uy and position[1] <= Dy :
				flag = num
				break
			num = num + 1

		#返回索引，-1为没有选中图片
		return flag

	#获取点击的角色
	#position ：鼠标位置
	def get_actor(self, position):
		
			