
import pygame
import sys
import copy
import skill 
sys.path.append(".\config")
from actor_1 import Actor as i_actor_1
from actor_2 import Actor as i_actor_2
from actor_3 import Actor as i_actor_3
from actor_4 import Actor as i_actor_4
from actor_5 import Actor as i_actor_5
from actor_6 import Actor as i_actor_6
from actor_7 import Actor as i_actor_7
from actor_8 import Actor as i_actor_8

class share_attr() :		#角色共有属性，反正以后也记不得了
	def __init__(self):
		self.level = 1			#等级
		self.pos_x = 0			#位置
		self.pos_y = 0
		self.team = None		#是否队友 i = 队友 d = 敌人
		self.actor_idx = 0		#角色的索引序列
		self.team_idx = 0		#队伍的索引序列
		self.state = 1			#当前状态 1：站立  2：战斗
		self.image_idx = 0		#当前状态的图片索引
		self.target = None		#目标敌人
		self.now_image = None	#当前图片
		self.effect = None		#身上的特效
		self.effect_time = 0	#特效时间
		self.do_time = 0		#可以动作的时间

#存放角色表
actor_tab = [i_actor_1(), i_actor_2(), i_actor_3(), i_actor_4(), i_actor_5(), i_actor_6(), i_actor_7(), i_actor_8(),]

class Actor():
	#image_1 站立图片资源
	#image_2 战斗图片资源
	#rect			图片大小(100, 110)   bottom or centerx(位置)
	#screen			场景
	#screen_rect	场景大小
	#font			字体
	#name			显示的名字文本
	

	"""description of class"""
	#初始化角色
	#nIndex : 角色索引
	#nScreen : 场景数据
	#nTeam_idx : 队伍索引（列表索引）
	#nTeam : ture=队友 false=敌人
	def __init__(self, nIndex, nScreen, nTeam_idx, nTeam, nLevel):
		#角色与界面大小处理
		actor = actor_tab[nIndex - 1]
		self.actor = copy.deepcopy(actor)		#添加角色属性 用深拷贝，保持角色表的变量不受拷贝对象改变
		self.actor.share_attr = share_attr()

		str_image = "FineArts/actor/actor_%d/%s_%d_%d.png"#图片位置 :角色，队伍，状态
		#站立图片资源
		imageFile = str_image % (nIndex, nTeam, 1, 1)#图片位置 :角色，队伍，状态
		self.image_1 = []
		self.image_1.append(pygame.image.load(imageFile))
		self.image_1[0] = pygame.transform.scale(self.image_1[0], (100, 110), )#(缩放)
		self.actor.share_attr.actor_idx = nIndex
		self.actor.share_attr.team_idx = nTeam_idx
		self.actor.share_attr.team = nTeam
		self.actor.share_attr.level = nLevel
		self.actor.share_attr.now_image = self.image_1[0]


		#战斗图片资源
		self.image_2 = []
		for num in range(1,3):
			imageFile = str_image % (nIndex, nTeam, 2, num)#图片位置 :角色，队伍，状态
			self.image_2.append(pygame.image.load(imageFile))
			self.image_2[num - 1] = pygame.transform.scale(self.image_2[num - 1], (100, 110), )#(缩放)

		#技能图片资源
		self.image_4 = []
		for num in range(1,5):
			imageFile = str_image % (nIndex, "i", 4, num)#图片位置 :角色，队伍，状态
			self.image_4.append(pygame.image.load(imageFile))
			self.image_4[num - 1] = pygame.transform.scale(self.image_4[num - 1], (100, 110), )#(缩放)

		self.rect = self.image_1[0].get_rect()
		self.screen = nScreen
		self.screen_rect = nScreen.get_rect()

		#生命框的图像
		self.hpBar = {"color" : (0,0,0), "left" : 90, "height" : 16}

		#字体处理
		self.font = pygame.font.SysFont('SimHei', 16)
		self.name = self.font.render(self.actor.self_attr.name, True, (0,0,0))

		#位置设置
		self.actor.share_attr.pos_y = (nTeam_idx)%5 * 120 + 300	#五个一行  再加上一点点位置校准
		self.rect.bottom = self.actor.share_attr.pos_y
		if nTeam == "i" :
			self.actor.share_attr.pos_x = (nTeam_idx)//5 * 100 + 50	#加一点微调
		elif nTeam == "d" :#敌人放在另一边
			self.actor.share_attr.pos_x = nScreen.get_width() - (nTeam_idx)//5 * 100 - 50
		self.rect.centerx = self.actor.share_attr.pos_x
		self.actor.share_attr.state = 1

		#自身属性计算
		#等级成长属性
		self.actor.attribute.MaxHp += nLevel * self.actor.growUp.hp
		self.actor.attribute.hp = self.actor.attribute.MaxHp
		self.actor.attribute.attack += nLevel * self.actor.growUp.attack
		self.actor.attribute.defense += nLevel * self.actor.growUp.defense
		self.actor.attribute.Violent += nLevel * self.actor.growUp.Violent
		self.actor.attribute.speed += nLevel * self.actor.growUp.speed
		#被动加成
		for num in range(4):
			if self.actor.skill[num].m_type == skill.skill_type.passivity :
				self.actor.attribute.MaxHp += nLevel * self.actor.skill[num].attr[1]
				self.actor.attribute.hp = self.actor.attribute.MaxHp
				self.actor.attribute.attack += nLevel * self.actor.skill[num].attr[2]
				self.actor.attribute.defense += nLevel * self.actor.skill[num].attr[3]
				self.actor.attribute.Violent += nLevel * self.actor.skill[num].attr[4]


	def blitme(self):
		#绘制角色图像
		self.rect.bottom = self.actor.share_attr.pos_y
		self.rect.centerx = self.actor.share_attr.pos_x
		self.screen.blit(self.actor.share_attr.now_image, self.rect)

		#绘制特效图片
		if self.actor.share_attr.effect :
			self.screen.blit(self.actor.share_attr.effect, self.rect)
			self.actor.share_attr.effect_time -= 1
			if self.actor.share_attr.effect_time <= 0 :
				self.actor.share_attr.effect = None

		#绘制名字
		self.screen.blit(self.name, (self.rect.centerx - 50, self.rect.bottom - 115))

		#绘制生命框
		pygame.draw.rect(self.screen, self.hpBar["color"], (self.rect.centerx - 50, self.rect.bottom - 100, self.hpBar["left"], self.hpBar["height"]), 3)#生命条外框
		hpX = self.actor.attribute.hp/self.actor.attribute.MaxHp	#计算生命值长度
		pygame.draw.rect(self.screen, (0, 100, 0), (self.rect.centerx - 47, self.rect.bottom - 97, hpX * 84, 10), )#剩余生命值
		hp_number = self.font.render('%.1f' % (self.actor.attribute.hp),True,(0,0,0))	#生命值数值
		self.screen.blit(hp_number, (self.rect.centerx - 30, self.rect.bottom - 95))
