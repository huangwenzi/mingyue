#琪琪的角色属性

import sys
import skill

#自身属性
class Self_attr() :
	def __init__(self):
		self.name = "琪琪"			#名字
		self.introduce = "null"		#介绍
		self.location = "法师"		#定位
	

#可变属性	受被动技能影响
class Attribute() :
	def __init__(self):
		self.MaxHp =  100			#最大生命值
		self.hp =  100				#生命值
		self.attack =  20			#攻击
		self.defense =  0			#防御
		self.Violent =  0			#暴击
		self.speed =  0.4			#攻击速度
		self.move =  10				#移动速度
		self.attack_range =  300	#攻击范围


#成长
class GrowUp() :
	def __init__(self):
		self.hp = 10				#生命值
		self.attack = 2				#攻击
		self.defense = 1			#防御
		self.Violent = 0			#暴击
		self.speed = -0.01			#攻击速度

#个人buff	存放只有自己受影响的buff
class Self_buff() :
	def __init__(self):
		self.MaxHp = 0				#最大生命值
		self.hp = 0					#生命值
		self.attack = 0				#攻击
		self.defense = 0			#防御
		self.speed = 0				#攻击速度
		self.move = 0				#移动速度
		self.attack_range = 0		#攻击范围

#团队buff	存放全队受影响的buff
class Team_buff() :
	def __init__(self):
		self.MaxHp = 0				#最大生命值
		self.hp = 0					#生命值
		self.attack = 0				#攻击
		self.defense = 0			#防御
		self.speed = 0				#攻击速度
		self.move = 0				#移动速度
		self.attack_range = 0		#攻击范围

class Actor():
	def __init__(self):
		self.self_attr = Self_attr()		#自身属性
		self.attribute = Attribute()		#可变属性
		self.growUp = GrowUp()				#成长
		self.skill = []						#技能
		self.skill.append(skill.Despise())
		self.skill.append(skill.Despise_rand())
		self.skill.append(skill.Flirt())
		self.skill.append(skill.Deadly_everyone())
		share_attr = None			#共有属性，角色创建时赋值