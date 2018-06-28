import math		#数学
import time		#时间
import random	#随机数
import sys
import copy
sys.path.append("./config")
import skill 

class BattleMgr():

	#初始化管理器
	#nScreen : 场景
	def __init__(self, i_actorList, d_actorList) :
		self.i_actorList = i_actorList
		self.d_actorList = d_actorList


	#战斗环节
	#return: 1:战斗结束
	def run(self):
		#检查是否战斗结束
		if len(self.i_actorList) == 0 or len(self.d_actorList) == 0:
			self.d_actorList = []
			self.i_actorList = []
			return 1

		now_time = time.time()	#现在时间
		#己队遍历
		for actor in self.i_actorList :
			#处在动作时间内
			if actor.actor.share_attr.do_time < now_time : 
				self.find_target(actor, self.d_actorList)
				self.do_target(actor, actor.actor.share_attr.target) 

		#敌队遍历
		for actor in self.d_actorList :
			#处在动作时间内
			if actor.actor.share_attr.do_time < now_time : 
				self.find_target(actor, self.i_actorList)	#寻找最近目标
				self.do_target(actor, actor.actor.share_attr.target)	#对目标操作
		return 0

	#寻找最近敌人
	#nActor	: 角色
	#nD_actorList	: 寻找的列表
	def find_target(self, nActor, nD_actorList) :
		nActor.actor.share_attr.target = nD_actorList[0]
		a = nActor.actor.share_attr.target
		for target in nD_actorList :	#利用勾股定理，x，y平方得直线距离平方
			a_range = (a.actor.share_attr.pos_x - nActor.actor.share_attr.pos_x)**2 + (a.actor.share_attr.pos_y - nActor.actor.share_attr.pos_y)**2
			d_range = (target.actor.share_attr.pos_x - nActor.actor.share_attr.pos_x)**2 + (target.actor.share_attr.pos_y - nActor.actor.share_attr.pos_y)**2
			if d_range < a_range :	#比较距离
				nActor.actor.share_attr.target = target
				

	#操作目标
	#nActor	: 角色
	#nTarget: 目标
	def do_target(self, nActor, nTarget) :
		d_range = (nTarget.actor.share_attr.pos_x - nActor.actor.share_attr.pos_x)**2 + (nTarget.actor.share_attr.pos_y - nActor.actor.share_attr.pos_y)**2 #距离的平方
		if d_range > nActor.actor.attribute.attack_range**2 :	#如果不在攻击范围内
			self.move_target( nActor, nTarget)
		else :
			self.attack_target(nActor, nTarget)


	#向目标移动
	#nActor	: 角色
	#nTarget: 目标
	def move_target(self, nActor, nTarget) :
		range_x = nTarget.actor.share_attr.pos_x - nActor.actor.share_attr.pos_x	#x距离
		range_y = nTarget.actor.share_attr.pos_y - nActor.actor.share_attr.pos_y	#y距离	

		#计算xy各移动多少
		d_range = math.sqrt((range_x**2 + range_y**2))						#距离
		move_x = range_x/d_range * nActor.actor.attribute.move
		move_y = range_y/d_range * nActor.actor.attribute.move

		#设置位置,状态和动作时间
		nActor.actor.share_attr.pos_x = nActor.actor.share_attr.pos_x + move_x
		nActor.actor.share_attr.pos_y = nActor.actor.share_attr.pos_y + move_y
		nActor.actor.share_attr.state = 1
		now_time = time.time()	#现在时间
		nActor.actor.share_attr.do_time = now_time + 0.1


	#攻击目标
	#nActor	: 角色
	#nTarget: 目标
	def attack_target(self, nActor, nTarget) :
		#不处于战斗状态
		if nActor.actor.share_attr.state != 2 :
			nActor.actor.share_attr.state = 2
			nActor.actor.share_attr.image_idx = 0
			nActor.actor.share_attr.now_image = nActor.image_2[0]
		else :#处于战斗状态
			image_count = len(nActor.image_2)
			#没输出完战斗图
			if nActor.actor.share_attr.image_idx + 1 <= image_count :
				nActor.actor.share_attr.now_image = nActor.image_2[nActor.actor.share_attr.image_idx]
				nActor.actor.share_attr.image_idx += 1
			else :#输出完战斗图片
				nActor.actor.share_attr.state = 1
				nActor.actor.share_attr.image_idx = 0
				nActor.actor.share_attr.now_image = nActor.image_1[0]
				self.do_skill(nActor, nTarget)
		now_time = time.time()	#现在时间
		nActor.actor.share_attr.do_time = now_time + nActor.actor.attribute.speed + 0.2

	#使用技能
	#nActor	: 角色
	#nTarget: 目标
	def do_skill(self, nActor, nTarget) :
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
			if nActor.actor.skill[rand].m_type != skill.skill_type.passivity :
				kill = nActor.actor.skill[rand]
				break

		
		target_list = []		#目标列表
		number = nActor.actor.skill[rand].Number #目标人数
		#技能目标
		if nActor.actor.skill[rand].target == skill.skill_target.myself :
			target_list.append(nActor)
		elif nActor.actor.skill[rand].target == skill.skill_target.team :
			if nActor.actor.share_attr.team == "i" :	#区分角色队伍
				target_list = self.i_actorList
			else :
				target_list = self.d_actorList
		elif nActor.actor.skill[rand].target == skill.skill_target.Enemy :
			if nActor.actor.share_attr.team == "i" :	#区分角色队伍
				target_list = self.d_actorList
			else :
				target_list = self.i_actorList

		#技能优先
		count = len(target_list)	#计数
		if count <= 1 or count < number or nActor.actor.skill[rand].first == skill.skill_first.whole:	#去掉不需要查找符合条件的人数
			number = count
		else :
			if nActor.actor.skill[rand].first == skill.skill_first.rand :	#随机
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
			elif nActor.actor.skill[rand].first == skill.skill_first.hpLow :	#生命最低
				tmp = target_list[0]
				for num in range(count) :
					if target_list[num].actor.attribute.hp > tmp.actor.attribute.hp :
						tmp = target_list[num]
				target_list = [tmp]
				number = 1
			elif nActor.actor.skill[rand].first == skill.skill_first.hurtHigh :	#攻击最高
				tmp = target_list[0]
				for num in range(count) :
					if target_list[num].actor.attribute.attack > tmp.actor.attribute.attack :
						tmp = target_list[num]
				target_list = [tmp]
				number = 1
			elif nActor.actor.skill[rand].first == skill.skill_first.front :	#最近目标
				target_list = [nTarget]


		#技能类型
		if nActor.actor.skill[rand].m_type == skill.skill_type.hurt :	#伤害型
			hurt = nActor.actor.attribute.attack * kill.Multiple #伤害值
			#是否暴击
			attack_rand = random.randint(1,100)
			if attack_rand < nActor.actor.attribute.Violent :
				hurt *= 2
			#遍历符合的目标
			for num in range(number):
				self.deduct_hp(hurt, target_list[num])
				print(nActor.actor.self_attr.name + " 对 " + target_list[num].actor.self_attr.name+ ":" + str(hurt) )

		#添加技能特效,持续时间到目标
		nTarget.actor.share_attr.effect = nActor.image_4[rand]
		nTarget.actor.share_attr.effect_time = 30
			
	#扣血
	#nHurt	: 伤害
	#nTarget: 目标
	#nSkill_idx : 技能索引
	def deduct_hp(self, nHurt, nTarget) :
		nHurt *= (1 - nTarget.actor.attribute.defense/100)
		nTarget.actor.attribute.hp -= nHurt
		
