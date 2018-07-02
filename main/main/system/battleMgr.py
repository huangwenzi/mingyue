import math		# 数学
import time		# 时间
import random	# 随机数
import sys
import copy
sys.path.append("./config")
sys.path.append("./enum")

from i_enum import enum  	# 包含枚举
from config import config   # 包含配置
from skill import skill_tab # 包含技能表

class BattleMgr():
	# 初始化管理器
	# nScreen : 场景
	def __init__(self) :
		self.actor_list = []		# 队友角色的列表
		self.d_actor_list = []		# 敌对角色的列表


	# 战前准备，初始化两边队伍信息
	# actor_list : 自己队伍
	# d_actor_list : 敌对队伍
	def init(self, actor_list, d_actor_list):
		self.actor_list = actor_list  		# 队友角色的列表
		self.d_actor_list = d_actor_list	# 敌对角色的列表


	# 战后状态复位
	def renew(self, parameter_list):
		# 己队遍历
		for actor in self.actor_list:
			actor.share_attr.die = enum.actor.live
		# 敌队遍历
		for actor in self.d_actor_list:
			actor.share_attr.die = enum.actor.live


	# 战斗环节
	# return : 0:战斗未结束
	def run(self):
		now_time = time.time()	# 现在时间
		count = 0 				# 存活角色计数
		# 己队遍历
		for actor in self.actor_list :
			# 如果角色已经死亡
			if actor.battle_attr[enum.attr_type.hp] <= 0:
				actor.share_attr.die = enum.actor.die
				continue

			count += 1	# 存活计算加一
			# 处在动作时间内
			if actor.share_attr.do_time < now_time: 
				self.find_target(actor)
				self.do_target(actor) 
		if count <= 0:
			return 1  # 战斗失败
		

		# 敌队遍历
		count = 0
		for actor in self.d_actor_list:
			# 如果角色已经死亡
			if actor.battle_attr[enum.attr_type.hp] <= 0:
				actor.share_attr.die = enum.actor.die
				continue

			count += 1  # 存活计算加一
			# 处在动作时间内
			if actor.share_attr.do_time < now_time:
				self.find_target(actor)
				self.do_target(actor)
		if count <= 0:
			return 2  # 战斗胜利
		

	#寻找最近敌人
	#actor : 角色
	def find_target(self, actor):
		target_list = None
		# 根据队伍索引决定目标列表
		if actor.share_attr.team == enum.actor.team:
			target_list = self.d_actor_list
		elif actor.share_attr.team == enum.actor.enemy:
			target_list = self.actor_list

		actor.share_attr.target = target_list[0]
		tmp_target = actor.share_attr.target
		for target in target_list:  # 利用勾股定理，x，y平方得直线距离平方
			# 跳过已经死亡的角色
			if target.share_attr.die == enum.actor.die:
				continue
			a_range = (tmp_target.share_attr.pos_x - actor.share_attr.pos_x)**2 + (tmp_target.share_attr.pos_y - actor.share_attr.pos_y)**2
			d_range = (target.share_attr.pos_x - actor.share_attr.pos_x)**2 + (target.share_attr.pos_y - actor.share_attr.pos_y)**2
			if d_range < a_range :	#比较距离
				actor.share_attr.target = target
				

	# 操作目标
	# actor	: 角色
	def do_target(self, actor):
		target = actor.share_attr.target
		d_range = (target.share_attr.pos_x - actor.share_attr.pos_x)**2 + (target.share_attr.pos_y - actor.share_attr.pos_y)**2 # 距离的平方
		if d_range > actor.battle_attr[enum.attr_type.attack_range]**2:  # 如果不在攻击范围内
			self.move_target(actor)
		else :
			self.attack_target(actor)


	# 向目标移动
	# actor	: 角色
	def move_target(self, actor) :
		target = actor.share_attr.target
		range_x = target.share_attr.pos_x - actor.share_attr.pos_x  # x距离
		range_y = target.share_attr.pos_y - actor.share_attr.pos_y  # y距离

		# 计算xy各移动多少
		d_range = math.sqrt((range_x**2 + range_y**2))		# 实际移动的直线距离
		move_x = range_x/d_range * actor.battle_attr[enum.attr_type.move]
		move_y = range_y/d_range * actor.battle_attr[enum.attr_type.move]

		# 设置位置,状态和动作时间
		actor.share_attr.pos_x = actor.share_attr.pos_x + move_x
		actor.share_attr.pos_y = actor.share_attr.pos_y + move_y
		actor.share_attr.state = enum.state.wait
		now_time = time.time()	# 现在时间
		actor.share_attr.do_time = now_time + config.actor.move_time


	# 攻击目标
	# actor	: 角色
	def attack_target(self, actor):
		now_time = time.time()  # 现在时间
		# 不处于战斗状态
		if actor.share_attr.state != enum.state.battle:
			actor.share_attr.state = enum.state.battle
			actor.share_attr.image_idx = 0
		# 处于战斗状态
		elif actor.share_attr.state == enum.state.battle:
			#没输出完战斗图
			if actor.share_attr.image_idx < config.Actor_image.battle_count:
				actor.share_attr.image_idx += 1
			else :#输出完战斗图片
				actor.share_attr.state = enum.state.normal
				actor.share_attr.image_idx = 0
				self.do_skill(actor)
		# 设置下一个动作时间
		actor.share_attr.do_time = now_time + actor.battle_attr[enum.attr_type.speed] + config.actor.attack_time


	#使用技能
	#actor	: 角色
	def do_skill(self, actor):
		#随机技能
		index = 0						# 使用的技能id
		rand = random.randint(0, 100)	# 随机数
		for num in range(0, len(actor.skill)):
			skill = actor.skill[num]	# 当前技能
			# 如果在概率内
			if skill[1] <= rand:
				index = skill[0]
			else:
				rand -= skill[1]

		# 如果没有选中的技能，默认使用第一个技能
		if index == 0:
			index = actor.skill[0][0]

		# 开始进行技能效果的判断
		skill = skill_tab[index]	# 选中的技能
		target_list = []			# 目标列表
		#技能目标
		if skill.target == enum.skill_target.myself:	# 对自己使用
			target_list.append(actor)
		elif skill.target == enum.skill_target.team:	# 对队友使用
			if actor.share_attr.team == enum.actor.team:# 区分角色队伍
				target_list = self.actor_list
			else:
				target_list = self.d_actor_list
		elif skill.target == enum.skill_target.Enemy :	 # 对敌人使用
			if actor.share_attr.team == enum.actor.team :# 区分角色队伍
				target_list = self.d_actor_list
			else :
				target_list = self.actor_list

		count = len(target_list)	# 目标列表计数
		tmp = []					# 存活角色索引
		tmp_list = []				# 存活角色列表
		number = skill.Number 		# 目标人数
		# tmp添加存活的目标
		for num in range(0, len(target_list)):
			if target_list[num].share_attr.die == enum.actor.live:
				tmp.append(num)

		count = len(tmp)
		# 技能优先
		if count <= number or skill.first == enum.skill_first.whole:# 去掉不需要查找符合条件的人数
			number = count
		else:	
			# 开始判断
			if skill.first == enum.skill_first.front:  	# 最近目标
				# 先根据距离排个序
				for num in range(0, count):
					# 添加第一个做对比
					if len(tmp_list) == 0: 
						tmp_list.append(target_list[ tmp[0] ])
						continue
					for num_1 in range(0, len(tmp_list)):
						a_target = target_list[ tmp[num] ]		# 目标列表
						d_target = tmp_list[num_1]		# 对比列表
						# 各自到玩家的距离
						a_range = (a_target.share_attr.pos_x - actor.share_attr.pos_x)**2 + (a_target.share_attr.pos_y - actor.share_attr.pos_y)**2
						d_range = (d_target.share_attr.pos_x - actor.share_attr.pos_x)**2 + (d_target.share_attr.pos_y - actor.share_attr.pos_y)**2
						# 如果比当前近，插入到当前位置
						if a_range < d_range:
							tmp_list.insert(num_1, target_list[ tmp[num] ])
							break
			elif skill.first == enum.skill_first.rand: 	# 随机
				for num in range(0, number) :
					rand = random.randint(0, count - 1)
					# 添加选中的目标,删除目标列表索引对应的索引
					tmp_list.append(target_list[ tmp[rand] ])
					tmp.remove(rand)
					count -= 1
			elif skill.first == enum.skill_first.hp_high:  # 生命最高
				# 先根据生命值排个序
				for num in range(0, count):
					# 添加第一个做对比
					if len(tmp_list) == 0:
						tmp_list.append(target_list[ tmp[0] ])
						continue
					for num_1 in range(0, count):
						# 如果比当前高，插入到当前位置
						if target_list[ tmp[0] ].battle[enum.attr_type.hp] > tmp_list[num_1].battle[enum.attr_type.hp]:
							tmp_list.insert(num_1, target_list[num])
							break
			elif skill.first == enum.skill_first.hp_low :	# 生命最低
				# 先根据生命值排个序
				for num in range(0, count):
					# 添加第一个做对比
					if len(tmp_list) == 0:
						tmp_list.append(target_list[ tmp[0] ])
						continue
					for num_1 in range(0, len(count)):
						# 如果比当前低，插入到当前位置
						if target_list[ tmp[num] ].battle[enum.attr_type.hp] < tmp_list[num_1].battle[enum.attr_type.hp]:
							tmp_list.insert(num_1, target_list[ tmp[num] ])
							break
			elif skill.first == enum.skill_first.hurt_high :	#攻击最高
				# 先根据攻击力排个序
				for num in range(0, count):
					# 添加第一个做对比
					if len(tmp_list) == 0:
						tmp_list.append(target_list[ tmp[0] ])
						continue
					for num_1 in range(0, len(tmp_list)):
						# 如果比当前高，插入到当前位置
						if target_list[ tmp[num] ].battle[enum.attr_type.attack] > tmp_list[num_1].battle[enum.attr_type.attack]:
							tmp_list.insert(num_1, target_list[ tmp[num] ])
							break
			elif skill.first == enum.skill_first.speed_high:  # 攻击速度最高
				# 先根据攻击速度排个序
				for num in range(0, count):
					# 添加第一个做对比
					if len(tmp_list) == 0:
						tmp_list.append(target_list[ tmp[0] ])
						continue
					for num_1 in range(0, len(tmp_list)):
						# 如果比当前高，插入到当前位置
						if target_list[ tmp[num] ].battle[enum.attr_type.speed] > tmp_list[num_1].battle[enum.attr_type.speed]:
							tmp_list.insert(num_1, target_list[ tmp[num] ])
							break
			elif skill.first == enum.skill_first.back:  # 距离最远
				# 先根据距离排个序
				for num in range(0, count):
					# 添加第一个做对比
					if len(tmp_list) == 0:
						tmp_list.append(target_list[0])
						continue
					for num_1 in range(0, len(tmp_list)):
						a_target = target_list[ tmp[num] ] 	# 目标列表
						d_target = tmp_list[num_1]			# 对比列表
						# 各自到玩家的距离
						a_range = (a_target.share_attr.pos_x - actor.share_attr.pos_x)**2 + (a_target.share_attr.pos_y - actor.share_attr.pos_y)**2
						d_range = (d_target.share_attr.pos_x - actor.share_attr.pos_x)**2 + (d_target.share_attr.pos_y - actor.share_attr.pos_y)**2
						# 如果比当前远，插入到当前位置
						if a_range > d_range:
							tmp_list.insert(num_1, target_list[ tmp[num] ])
							break
			elif skill.first == enum.skill_first.whole:  # 全体
				target_list = target_list
			# 赋值给目标列表
			target_list = tmp_list[0:number]


		# 技能类型
		if skill.m_type == enum.skill_type.hurt :	# 伤害型
			# 遍历符合的目标
			for num in range(0, number):
				hurt = actor.battle_attr[enum.attr_type.attack] * skill.Multiple  # 伤害值
				# 是否暴击
				rand = random.randint(0, 100)
				if rand + target_list[num].battle_attr[enum.attr_type.antiriot] < actor.battle_attr[enum.attr_type.Violent]:
					hurt *= 2

				# 扣除防御减免的伤害
				hurt -= target_list[num].battle_attr[enum.attr_type.defense] * config.actor.defense_coefficient
				if hurt <= 0:	# 不能让伤害变成加血
					hurt = 1
				# 扣除血量
				target_list[num].battle_attr[enum.attr_type.hp] -= hurt
				# 死亡判断
				if target_list[num].battle_attr[enum.attr_type.hp] <= 0:
					target_list[num].share_attr.die = enum.actor.die

				#添加技能特效id,持续时间到目标
				target_list[num].share_attr.effect_index = index
				now_time = time.time()
				target_list[num].share_attr.effect_time = now_time + config.Skill.image_time

				print(actor.self_attr.name + " 对 " + target_list[num].actor.self_attr.name+ ":" + str(hurt) )
			
