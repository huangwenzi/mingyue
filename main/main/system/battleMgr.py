import math		#数学
import time		#时间
import random	#随机数
import sys
import copy
sys.path.append("./config")

from i_enum import enum  # 包含枚举

class BattleMgr():

	#初始化管理器
	#nScreen : 场景
	def __init__(self) :
		self.actorList = []		#队友角色的列表
		self.d_actorList = []	#敌对角色的列表


	#战前准备，初始化两边队伍信息
	def init(self, i_actorList, d_actorList):
		self.actorList = i_actorList	# 队友角色的列表
		self.d_actorList = d_actorList	# 敌对角色的列表


	#战斗环节
	#return: 1:战斗结束
	def run(self):
		#检查是否战斗结束
		if len(self.actorList) == 0:
			self.d_actorList = []
			self.actorList = []
			return 1	#战斗失败
		elif len(self.d_actorList) == 0:
			self.d_actorList = []
			self.actorList = []
			return 2	#战斗胜利

		now_time = time.time()	#现在时间
		#己队遍历
		for actor in self.actorList :
			#处在动作时间内
			if actor.actor.share_attr.do_time < now_time : 
				self.find_target(actor)
				self.do_target(actor) 

		#敌队遍历
		for actor in self.d_actorList :
			#处在动作时间内
			if actor.actor.share_attr.do_time < now_time : 
				self.find_target(actor)	#寻找最近目标
				self.do_target(actor)	#对目标操作
		return 0
		

	#寻找最近敌人
	#actor	: 角色
	def find_target(self, actor) :
		target_list = None
		if actor.actor.share_attr.team == 'i':
			target_list = self.d_actorList
		elif actor.actor.share_attr.team == 'd':
			target_list = self.actorList

		actor.actor.share_attr.target = target_list[0]
		tmp_target = actor.actor.share_attr.target
		for target in target_list:  # 利用勾股定理，x，y平方得直线距离平方
			a_range = (tmp_target.actor.share_attr.pos_x - actor.actor.share_attr.pos_x)**2 + (tmp_target.actor.share_attr.pos_y - actor.actor.share_attr.pos_y)**2
			d_range = (target.actor.share_attr.pos_x - actor.actor.share_attr.pos_x)**2 + (target.actor.share_attr.pos_y - actor.actor.share_attr.pos_y)**2
			if d_range < a_range :	#比较距离
				actor.actor.share_attr.target = target
				

	#操作目标
	#actor	: 角色
	def do_target(self, actor):
		target = actor.actor.share_attr.target
		d_range = (target.actor.share_attr.pos_x - actor.actor.share_attr.pos_x)**2 + (target.actor.share_attr.pos_y - actor.actor.share_attr.pos_y)**2 #距离的平方
		if d_range > actor.actor.attribute.attack_range**2:  # 如果不在攻击范围内
			self.move_target(actor)
		else :
			self.attack_target(actor)


	#向目标移动
	#actor	: 角色
	def move_target(self, actor) :
		target = actor.actor.share_attr.target
		range_x = target.actor.share_attr.pos_x - actor.actor.share_attr.pos_x  # x距离
		range_y = target.actor.share_attr.pos_y - actor.actor.share_attr.pos_y  # y距离

		#计算xy各移动多少
		d_range = math.sqrt((range_x**2 + range_y**2))						#距离
		move_x = range_x/d_range * actor.actor.attribute.move
		move_y = range_y/d_range * actor.actor.attribute.move

		#设置位置,状态和动作时间
		actor.actor.share_attr.pos_x = actor.actor.share_attr.pos_x + move_x
		actor.actor.share_attr.pos_y = actor.actor.share_attr.pos_y + move_y
		actor.actor.share_attr.state = 1
		now_time = time.time()	#现在时间
		actor.actor.share_attr.do_time = now_time + 0.1


	#攻击目标
	#actor	: 角色
	def attack_target(self, actor):
		#不处于战斗状态
		if actor.actor.share_attr.state != enum.state.battle :
			actor.actor.share_attr.state = enum.state.battle
			actor.actor.share_attr.image_idx = 0
			actor.actor.share_attr.now_image = actor.image_2[0]
		# 处于战斗状态
		elif actor.actor.share_attr.state == enum.state.battle:
			image_count = len(actor.image_2)
			#没输出完战斗图
			if actor.actor.share_attr.image_idx + 1 <= image_count :
				actor.actor.share_attr.now_image = actor.image_2[actor.actor.share_attr.image_idx]
				actor.actor.share_attr.image_idx += 1
			else :#输出完战斗图片
				actor.actor.share_attr.state = enum.state.normal
				actor.actor.share_attr.image_idx = 0
				actor.actor.share_attr.now_image = actor.image_1[0]
				self.do_skill(actor)

		now_time = time.time()	#现在时间
		actor.actor.share_attr.do_time = now_time + actor.actor.attribute.speed + 0.2


	#使用技能
	#actor	: 角色
	def do_skill(self, actor) :
		target = actor.actor.share_attr.target
		#随机技能
		kill = None
		rand = 0
		while True:
			rand = random.randint(0,100)
			if rand < 50 :
				rand = 1
			elif rand < 70 :
				rand = 2
			elif rand < 90 :
				rand = 3
			else :
				rand = 1
			#不能直接使用被动技能
			if actor.actor.skill[rand].m_type != enum.skill_type.passivity :
				kill = actor.actor.skill[rand]
				break

		
		target_list = []		#目标列表
		number = actor.actor.skill[rand].Number #目标人数
		#技能目标
		if actor.actor.skill[rand].target == enum.skill_target.myself :
			target_list.append(actor)
		elif actor.actor.skill[rand].target == enum.skill_target.team :
			if actor.actor.share_attr.team == "i" :	#区分角色队伍
				target_list = self.actorList
			else :
				target_list = self.d_actorList
		elif actor.actor.skill[rand].target == enum.skill_target.Enemy :
			if actor.actor.share_attr.team == "i" :	#区分角色队伍
				target_list = self.d_actorList
			else :
				target_list = self.actorList

		#技能优先
		count = len(target_list)	#计数
		if count <= 1 or count < number or actor.actor.skill[rand].first == enum.skill_first.whole:	#去掉不需要查找符合条件的人数
			number = count
		else :
			if actor.actor.skill[rand].first == enum.skill_first.rand :	#随机
				list_count = count  #实时列表计数
				tmp = []
				for num in range(list_count) :
					tmp.append(num)
				tmp_list = []
				for num in range(number) :
					rand = random.randint(0,list_count - 1)
					idx = tmp.pop(rand)
					tmp_list.append(target_list[idx])
					list_count -= 1
				target_list = tmp_list
			elif actor.actor.skill[rand].first == enum.skill_first.hpLow :	#生命最低
				tmp = target_list[0]
				for num in range(count) :
					if target_list[num].actor.attribute.hp > tmp.actor.attribute.hp :
						tmp = target_list[num]
				target_list = [tmp]
				number = 1
			elif actor.actor.skill[rand].first == enum.skill_first.hurtHigh :	#攻击最高
				tmp = target_list[0]
				for num in range(count) :
					if target_list[num].actor.attribute.attack > tmp.actor.attribute.attack :
						tmp = target_list[num]
				target_list = [tmp]
				number = 1
			elif actor.actor.skill[rand].first == enum.skill_first.front :	#最近目标
				target_list = [target]


		#技能类型
		if actor.actor.skill[rand].m_type == enum.skill_type.hurt :	#伤害型
			hurt = actor.actor.attribute.attack * kill.Multiple #伤害值
			#是否暴击
			attack_rand = random.randint(1,100)
			if attack_rand < actor.actor.attribute.Violent :
				hurt *= 2
			#遍历符合的目标
			for num in range(number):
				self.deduct_hp(hurt, target_list[num])
				print(actor.actor.self_attr.name + " 对 " + target_list[num].actor.self_attr.name+ ":" + str(hurt) )

		#添加技能特效,持续时间到目标
		target.actor.share_attr.effect = actor.image_4[rand]
		target.actor.share_attr.effect_time = 30
			
	#扣血
	#nHurt	: 伤害
	#target: 目标
	#nSkill_idx : 技能索引
	def deduct_hp(self, nHurt, target) :
		nHurt *= (1 - target.actor.attribute.defense/100)
		target.actor.attribute.hp -= nHurt
		
