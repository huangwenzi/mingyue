
#角色类
import pygame
import sys
import copy
import time
sys.path.append("./config")
from actor_1 import Actor as i_actor_1
from actor_2 import Actor as i_actor_2
from actor_3 import Actor as i_actor_3
from actor_4 import Actor as i_actor_4
from actor_5 import Actor as i_actor_5
from actor_6 import Actor as i_actor_6
from actor_7 import Actor as i_actor_7
from actor_8 import Actor as i_actor_8
from enum import enum  # 包含枚举
from config import config  # 包含配置

class share_attr() :		#角色共有属性，反正以后也记不得了
	def __init__(self):
		self.level = 1			#等级
		self.exp = 0			#经验
		self.pos_x = 0			#位置
		self.pos_y = 0
		self.team = None		#是否队友 i = 队友 d = 敌人
		self.actor_idx = 0		#角色的索引序列
		self.list_index = 0		#列表的索引序列
		self.team_idx = 0		#队伍的索引序列
		self.state = enum.State.wait  # 当前状态 1：待命  2：战斗
		self.image_idx = 0		#当前状态的图片索引
		self.target = None		#目标敌人
		self.now_image = None	#当前图片
		self.effect = None		#身上的特效
		self.effect_time = 0	#特效时间
		self.do_time = 0		#可以动作的时间

#存放角色表	(0是占位，用来索引对齐)
actor_tab = [0, i_actor_1(), i_actor_2(), i_actor_3(), i_actor_4(), i_actor_5(), i_actor_6(), i_actor_7(), i_actor_8(),]

class Actor():
	#初始化角色
	#nIndex : 角色索引
	#nScreen : 场景数据
	#nTeam_idx : 队伍索引
	#nTeam : 'i'=队友 'd'=敌人
	#list_index : 列表里的索引
	def __init__(self, nIndex, nScreen, nTeam_idx, nTeam, nLevel, list_index):
		#角色与界面大小处理
		actor = actor_tab[nIndex]
		self.actor = copy.deepcopy(actor)		#添加角色属性 用深拷贝，保持角色表的变量不受拷贝对象改变
		# 创建角色共有属性
		self.actor.share_attr = share_attr()
		self.actor.share_attr.actor_idx = nIndex
		self.actor.share_attr.team_idx = nTeam_idx
		self.actor.share_attr.list_index = list_index
		self.actor.share_attr.team = nTeam
		self.actor.share_attr.level = nLevel

		#站立图片资源
		str_image = "FineArts/actor/actor_%d/%s_%d_%d.png"#图片位置 :角色，队伍，状态
		imageFile = str_image % (nIndex, nTeam, enum.image.wait, 1)	#图片位置 :角色，队伍，状态
		self.image_1 = []
		self.image_1.append(pygame.image.load(imageFile))
		self.image_1[0] = pygame.transform.scale(self.image_1[0], config.actor_image.actor_size )  # (缩放)
		self.actor.share_attr.now_image = self.image_1[0]

		#战斗图片资源
		self.image_2 = []
		for num in range(0,2):
			imageFile = str_image % (nIndex, nTeam, enum.image.battle, num + 1)#图片位置 :角色，队伍，状态
			self.image_2.append(pygame.image.load(imageFile))
			self.image_2[num] = pygame.transform.scale(self.image_2[num], config.actor_image.actor_size )#(缩放)

		#技能图片资源
		self.image_4 = []
		for num in range(0,4):
			imageFile = str_image % (nIndex, config.actor.team, enum.image.skill, num + 1)  # 图片位置 :角色，队伍，状态
			self.image_4.append(pygame.image.load(imageFile))
			self.image_4[num] = pygame.transform.scale(self.image_4[num], config.actor_image.actor_size )#(缩放)

		self.rect = self.image_1[0].get_rect()
		self.screen = nScreen
		self.screen_rect = nScreen.get_rect()

		#名字
		self.name = config.font.font.render(self.actor.self_attr.name, True, config.font.font_color)

		#位置设置
		self.actor.share_attr.pos_y = nTeam_idx%config.actor.Max_row * config.actor.actor_space + config.actor.y_aline	#五个一行  再加上一点点位置校准
		self.rect.bottom = self.actor.share_attr.pos_y
		if nTeam == config.actor.team :
			self.actor.share_attr.pos_x = nTeam_idx//config.actor.Max_col * config.actor.actor_space + config.actor.y_aline	#加一点微调
		elif nTeam == config.actor.enemy :  # 敌人放在另一边
			self.actor.share_attr.pos_x = nScreen.get_width() - nTeam_idx//config.actor.Max_col * config.actor.actor_space - config.actor.y_aline
		self.rect.centerx = self.actor.share_attr.pos_x
		self.actor.share_attr.state = enum.State.wait

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
			if self.actor.skill[num].m_type == enum.skill_type.passivity :
				self.actor.attribute.MaxHp += nLevel * self.actor.skill[num].attr[enum.attr_type.MaxHp]
				self.actor.attribute.hp = self.actor.attribute.MaxHp
				self.actor.attribute.attack += nLevel * self.actor.skill[num].attr[enum.attr_type.attack]
				self.actor.attribute.defense += nLevel * self.actor.skill[num].attr[enum.attr_type.defense]
				self.actor.attribute.Violent += nLevel * self.actor.skill[num].attr[enum.attr_type.Violent]
				self.actor.attribute.speed += nLevel * self.actor.skill[num].attr[enum.attr_type.speed]
				self.actor.attribute.move += nLevel * self.actor.skill[num].attr[enum.attr_type.move]
				self.actor.attribute.attack_range += nLevel * self.actor.skill[num].attr[enum.attr_type.attack_range]


	def blitme(self):
		#绘制角色图像
		self.rect.bottom = self.actor.share_attr.pos_y
		self.rect.centerx = self.actor.share_attr.pos_x
		self.screen.blit(self.actor.share_attr.now_image, self.rect)

		#绘制身上的特效图片
		now_time = time.time()
		if self.actor.share_attr.effect :
			self.screen.blit(self.actor.share_attr.effect, self.rect)
			if self.actor.share_attr.effect_time <= now_time:
				self.actor.share_attr.effect = None

		#绘制名字
		self.screen.blit(self.name, (self.rect.centerx - 50, self.rect.bottom - 115))

		#绘制生命框
		pygame.draw.rect(self.screen, config.font.font_color, (self.rect.centerx - 50, self.rect.bottom - 100, config.hpBar.left, config.hpBar.height), 3)#生命条外框
		hpX = self.actor.attribute.hp/self.actor.attribute.MaxHp	#计算生命值长度
		pygame.draw.rect(self.screen, config.hp_bar.bar_color, (self.rect.centerx - 47, self.rect.bottom - 97, hpX * 84, 10), )#剩余生命值
		hp_number = config.font.font.render('%.1f' % (self.actor.attribute.hp), True, config.font.font_color)  # 生命值数值
		self.screen.blit(hp_number, (self.rect.centerx - 30, self.rect.bottom - 100))
