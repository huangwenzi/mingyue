import copy
import sys
sys.path.append(".\FineArts\actor")

from actor import Actor

class ActorMgr():
	#screen			场景
	#actorList		队友列表
	#i_actorList	战斗队友列表
	#d_actorList	战斗敌人列表

	#初始化管理器
	#nScreen : 场景
	def __init__(self, nScreen):
		self.screen = nScreen
		self.i_actorList = []
		self.d_actorList = []
		self.actorList = []

	#添加队友角色
	#index : 角色索引
	#nTeam_idx : 队伍位置索引
	#nlevel : 等级
	def addTeam(self, nIndex, nTeam_idx, nLevel):
		if nIndex == None:	#没有角色索引
			return 1

		addActor = Actor(nIndex, self.screen, nTeam_idx, "i", nLevel)
		naddActor = Actor(nIndex, self.screen, nTeam_idx, "i", nLevel)
		self.i_actorList.append(addActor)
		self.actorList.append(naddActor)

	#添加敌对角色
	#index : 角色索引
	#nTeam_idx : 队伍位置索引
	#nlevel : 等级
	def addHostile(self, nIndex, nTeam_idx, nLevel):
		if nIndex == None:	#没有角色索引
			return 1

		addActor = Actor(nIndex, self.screen, nTeam_idx, "d", nLevel)
		self.d_actorList.append(addActor)

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
		

		
		

