import copy
import sys
sys.path.append("./FineArts/actor")

from actor import Actor

class ActorMgr():

	#初始化管理器
	#nScreen : 场景
	def __init__(self, nScreen):
		self.screen = nScreen	#场景
		self.i_actorList = []	# 战斗队友列表
		self.d_actorList = []	# 敌人列表
		self.actorList = []		# 队友列表

	#添加队友角色
	#index : 角色索引
	#nTeam_idx : 队伍位置索引
	#nlevel : 等级
	def addTeam(self, nIndex, nTeam_idx, nLevel):
		if nIndex == None:	#没有角色索引
			return 1

		list_index = len(self.i_actorList)	#列表里的索引
		addActor = Actor(nIndex, self.screen, nTeam_idx, "i", nLevel, list_index)
		naddActor = Actor(nIndex, self.screen, nTeam_idx, "i", nLevel, list_index)
		self.i_actorList.append(addActor)
		self.actorList.append(naddActor)


	#删除队友角色
	#list_index:列表
	def remove_Team(self, list_index):
		self.i_actorList.remove(list_index)
		self.actorList.remove(list_index)


	#添加敌对角色
	#index : 角色索引
	#nTeam_idx : 队伍位置索引
	#nlevel : 等级
	def addHostile(self, nIndex, nTeam_idx, nLevel):
		if nIndex == None:	#没有角色索引
			return 1

		list_index = len(self.d_actorList)  # 列表里的索引
		addActor = Actor(nIndex, self.screen, nTeam_idx, "d", nLevel, list_index)
		self.d_actorList.append(addActor)


	#删除敌对角色
	#list_index:列表
	def remove_Hostile(self, list_index):
		self.d_actorList.remove(list_index)


	#遍历绘画角色
	def blitme(self):
		count = 0
		for nActor in self.i_actorList:	#遍历队友
			nActor.blitme()
			#如果没有生命就销毁
			if nActor.actor.attribute.hp <= 0:
				del self.i_actorList[count]
				count -= 1
			count += 1

		count = 0
		for nActor in self.d_actorList:	# 遍历敌人
			nActor.blitme()
			#如果没有生命就销毁
			if nActor.actor.attribute.hp <= 0:
				del self.d_actorList[count]
				count -= 1
			count += 1
		

		
		

