#场景管理器

import sys
import time  # 时间
import pygame
import copy
sys.path.append("./config")				# 配置地址
sys.path.append("./enum")

from i_enum import enum  	# 包含枚举
from config import config  	# 包含枚举
from imageMgr import imageMgr   # 图片管理器
import image				# 图片的配置

class ScreenMgr():
	def __init__(self):
		#相关管理器的引用
		self.actorMgr = None
		# 基本设置
		self.screen = pygame.display.set_mode(config.screen.screen_size)
		self.view_1 = enum.image.view_main  # 一级视图 
		self.view_2 = enum.image.view_close # 二级视图
		
		#当前状态
		self.click_state = enum.input.click_open# 鼠标状态
		self.state = enum.state.normal  		# 场景状态
		self.bg_index = 0  						# 当前背景图索引


	#添加角色管理器
	def load_actorMgr(self,actorMgr):
		self.actorMgr = actorMgr


	#绘制场景内容
	def blitme_screen(self):
		self.screen.blit(imageMgr.screen_image[self.bg_index], (0,0))	# 背景绘制
		self.actorMgr.blitme()		# 角色绘制
		# 视图绘制
		# 主视图
		main_config = image.view_image[0]
		for num in range(0, len(main_config)):
			self.screen.blit(imageMgr.view_image[enum.image.view_main][num], image.view_image[enum.image.view_main][num][2])

		# 一级视图
		# 如果没有打开的一级视图
		if self.view_1 == enum.image.view_main or self.view_1 == enum.image.view_close:
			return

		if self.view_1 == enum.image.view_actor:	# 角色视图
			pass
		elif self.view_1 == enum.image.view_bag:	# 背包
			pass


		
	#绘制角色信息
	def show_actor(self):
		#绘制展示背景
		#绘制角色图
		#绘制各个属性
		a = 1 #取消报错


	#绘制物品信息
	def show_item(self):
		#绘制物品展示背景
		#绘制物品图片
		#绘制物品属性
		a = 1  # 取消报错


	#绘制展示信息
	def show_blitem(self):
		if self.show[0] == 0:	#绘制角色信息
			self.show_actor()
		elif self.show[0] > 0:	#绘制物品信息
			self.show_item()


	#事件获取
	def event(self):
		pressde = pygame.mouse.get_pressed()	#获取鼠标按下信息
		position = pygame.mouse.get_pos()		#获取鼠标位置
		index = -1	#点击的视图索引
		#鼠标点击左键
		if pressde[0]:
			#如果上次的点击还没放开
			if self.click_flag == 1:
				return

			#设置点击标志
			self.click_flag = 1
			print(position)
			#获取点击视图索引
			index = self.get_parts(position)

			#有视图的有效点击,设置当前需要绘制的图片资源
			if index >= 0:
				#如果点击的视图还有一层视图
				if self.partsCfg[self.parts_index][index][4] > 0:
					self.parts_index = self.partsCfg[self.parts_index][index][4]
					# self.parts_now_image = self.parts_image[self.parts_index]
					self.show = [-1, -1]	#清除信息绘制
				#如果是需要绘制点击的物品信息
				elif self.partsCfg[self.parts_index][index][4] == 0:
					self.show = [self.parts_index, index]  #设置显示信息的视图索引和物品索引
				#如果是执行对应的功能函数
				elif self.partsCfg[self.parts_index][index][4] == -1:
					#是否有触发执行函数
					if self.parts_func[self.parts_index] == 0:
						pass
					else:
						func = self.parts_func[self.parts_index]
						func()
			elif index == -1:
				index = self.get_actor(position)
				#如果角色点击有效
				if index >= 0:
					self.parts_index = 0
					#设置绘制角色信息
					self.show = [0, index]

			print(index)
			

		#记录释放鼠标左键
		else:
			self.click_flag = 0


	#获取点击的视图
	#position ：鼠标位置
	def get_parts(self, position):
		count = len(self.parts_now_image)
		index = -1 #点击的索引，为-1表示没有有效点击
		parts_list = self.parts_now_image	#遍历的视图列表

		#开始遍历点击区域
		for i in range(0, count):
			Lx = parts_list[i][1][0]  # 左边x
			Rx = parts_list[i][1][0] + parts_list[i][2][0]  # 右边x
			Uy = parts_list[i][1][1]  # 上边y
			Dy = parts_list[i][1][1] + parts_list[i][2][1]  # 下边y
			#如果在图片内
			if position[0] >= Lx and position[0] <= Rx and position[1] >= Uy and position[1] <= Dy:
				index = i
				break

		#返回索引，-1为没有选中视图
		return index


	#获取点击的角色
	#position ：鼠标位置
	def get_actor(self, position):
		count = len(self.actor_image)
		flag = -1  # 点击的索引，为-1表示没有有效点击
		parts_list = self.actor_image  # 遍历的视图列表

		#开始遍历点击区域
		for i in range(0, count):
			Lx = parts_list[i][1][0] - parts_list[i][2][0]/2  # 左边x	#角色位置是在中心点绘制的
			Rx = parts_list[i][1][0] + parts_list[i][2][0]/2  # 右边x
			Uy = parts_list[i][1][1] - parts_list[i][2][1]/2  # 上边y
			Dy = parts_list[i][1][1] + parts_list[i][2][1]/2  # 下边y
			#如果在图片内
			if position[0] >= Lx and position[0] <= Rx and position[1] >= Uy and position[1] <= Dy:
				flag = i
				break

		#返回索引，-1为没有选中视图
		return flag

	#进入战斗
	def enetr_battle(self):
		self.state = "battle"
		#深拷贝到战斗列表
		self.actorMgr.i_actorList = copy.deepcopy(self.actorMgr.actorList)
		#添加敌人
		self.actorMgr.addHostile(8, 1, 10)
		self.actorMgr.addHostile(6, 2, 10)
		self.actorMgr.addHostile(2, 3, 10)
		self.actorMgr.addHostile(5, 7, 10)
