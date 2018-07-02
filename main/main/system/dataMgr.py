import sys
sys.path.append("./save")

import save_actor

# 账号数据管理器

# 角色列表
# actor_tab = [
#		[角色索引, 等级, ],
#		[角色索引, 等级, ],
#		[角色索引, 等级, ],
# ]


class DataMgr():
	actor_list = []	# 角色列表

	# 保存现在的角色列表
	# i_actor_list : 玩家角色列表信息
	def save_actor(self, i_actor_list):
		actor_list = []	# 保存的表

		# 循环保存队友列表里的角色
		for actor in i_actor_list:
			tab = []
			tab.append(actor.actor.share_attr.actor_idx)	# 角色索引
			tab.append(actor.actor.share_attr.level)		# 角色等级
			tab.append(actor.actor.share_attr.exp)			# 角色经验
			actor_list.append(tab)

		with open("save/save_actor.py","w") as save_file:
			save_file.write("actor_tab = ")
			save_file.write(repr(actor_list))

	# 读取角色数据
	def read_actor(self):
		self.actor_list = save_actor.actor_tab
		return save_actor.actor_tab
