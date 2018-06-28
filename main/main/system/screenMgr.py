#场景管理器

import sys
import time  # 时间
import pygame
import copy
sys.path.append("./FineArts/screen")	#场景图片
sys.path.append("config")	#配置地址
import screen

class ScreenMgr():
	
	def __init__(self):
		#部件配置总表
		self.partsCfg = [screen.parts_0_Cfg, 
						
					]

		#部件图片总表
		self.parts_image = []	#parts_image[type][index]

		#部件物品信息总表(未完成)
		self.item_list = []  	#item_list[type][index]

		#部件触发的函数总表
		self.parts_func = [0]*20

		self.screen = pygame.display.set_mode((720, 800))
		self.parts_state = 1			#部件状态 （当前鼠标点击打开层次）

		#背景资源加载
		self.black_image = {}
		#self.battle_bg = pygame.image.load("FineArts/screen/战斗背景图.jpg")	#战斗背景
		#self.normal_bg = pygame.image.load("FineArts/screen/平时背景.jpg")		#平时背景
		self.black_image["battle"] = pygame.image.load("FineArts/screen/战斗背景图.jpg")
		self.black_image["normal"] = pygame.image.load("FineArts/screen/平时背景.jpg")  # 平时背景

		#添加部件图片(添加最好按索引顺序)
		self.add_prats(0, self.partsCfg[0])

		#添加部件触发函数
		self.parts_func[3] = self.enetr_battle	#进入战斗

		#当前状态
		self.click_flag = 0  #上次点击是否释放（避免运行速度过快，导致的多次点击）
		self.state = "normal"		#normal:平时  battle:战斗
		self.parts_index = 0		#当前部件索引
		self.background = self.black_image[self.state]  # 当前背景图
		self.parts_now_image = self.parts_image[self.parts_index]	#当前部件图片
		self.show = [-1,-1]		#展示的信息  [0]:类型 0:角色信息 
										#	[1]:索引

		#相关管理器的引用
		self.actorMgr = None
	

	#添加角色管理器
	def load_actorMgr(self,actorMgr):
		self.actorMgr = actorMgr
		self.load_actor()


	#重新加载角色图片资源
	def load_actor(self):
		#设置角色列表信息
		actor_list = self.actorMgr.actorList

		#初始化存储角色图片资源的列表
		number = len(actor_list)
		self.actor_image = [0]*number

		for i in range(0, number):
			self.actor_image[i] = [
				actor_list[i].image_1[0],  # 图片资源
				[actor_list[i].actor.share_attr.pos_x, actor_list[i].actor.share_attr.pos_y],  # 图片位置
				[100,110],	#图片缩放
			]


	#删除角色图片资源
	#list_index:删除的列表索引
	def remove_actor(self, list_index):
		self.actor_image.remove(list_index)


	#添加部件图片资源
	def add_prats(self, index, cfg):
		#如果没有能储存当前索引的列表
		if index >= len(self.parts_image) :
			for i in range(len(self.parts_image), index+1):
				self.parts_image.append([])

		#清空当前列表，重新加载
		self.parts_image[index] = []
		for v in cfg :
			image = pygame.image.load(v[0])	#图片地址
			image = pygame.transform.scale(image, v[1] )#(缩放)
			self.parts_image[index].append([image, v[2] ,v[1]])#图片资源，位置, 缩放


	#绘制背景
	def black_blitme(self):
		self.screen.blit(self.background, (0,0))


	#绘制场景内容
	def scren_blitem(self):
		self.parts_blitme()
		self.show_blitem()


	#绘制部件
	def parts_blitme(self):
		for v in self.parts_now_image:
			self.screen.blit(v[0], v[1])

		
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
		index = -1	#点击的部件索引
		#鼠标点击左键
		if pressde[0]:
			#如果上次的点击还没放开
			if self.click_flag == 1:
				return

			#设置点击标志
			self.click_flag = 1
			print(position)
			#获取点击部件索引
			index = self.get_parts(position)

			#有部件的有效点击,设置当前需要绘制的图片资源
			if index >= 0:
				#如果点击的部件还有一层部件
				if self.partsCfg[self.parts_index][index][4] > 0:
					self.parts_index = self.partsCfg[self.parts_index][index][4]
					# self.parts_now_image = self.parts_image[self.parts_index]
					self.show = [-1, -1]	#清除信息绘制
				#如果没有下一层，而是需要绘制点击的物品信息
				elif self.partsCfg[self.parts_index][index][5] == 0:
					self.show = [self.parts_index, index]  #设置显示信息的部件索引和物品索引
			elif index == -1:
				index = self.get_actor(position)
				#如果角色点击有效
				if index >= 0:
					self.parts_index = 0
					#设置绘制角色信息
					self.show = [0, index]

			print(index)
			#是否有触发执行函数
			if self.parts_func[self.parts_index] != 0:
				func = self.parts_func[self.parts_index]
				func()

		#记录释放鼠标左键
		else:
			self.click_flag = 0


	#获取点击的部件
	#position ：鼠标位置
	def get_parts(self, position):
		count = len(self.parts_now_image)
		index = -1 #点击的索引，为-1表示没有有效点击
		parts_list = self.parts_now_image	#遍历的部件列表

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

		#返回索引，-1为没有选中部件
		return index


	#获取点击的角色
	#position ：鼠标位置
	def get_actor(self, position):
		count = len(self.actor_image)
		flag = -1  # 点击的索引，为-1表示没有有效点击
		parts_list = self.actor_image  # 遍历的部件列表

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

		#返回索引，-1为没有选中部件
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
