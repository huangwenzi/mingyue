# 系统模块
import time
# 三方模块

# 项目模块
from enums.game_enum import game_enum
from system.configMgr import configMgr

# 属性
class Attr():
    hp = 0          # 生命
    attack = 0      # 物攻
    attack_def = 0  # 物防
    magic = 0       # 法功
    magic_def = 0   # 法防
    violent = 0     # 暴击
    antiriot = 0    # 抗暴
    speed = 0       # 攻击速度
    move = 0        # 移动速度
    attack_range = 0# 攻击范围

# 技能
class Skill():
    id = 0      # 技能id
    pro = 0     # 概率

# 角色
class Actor():
    # 初始化角色属性
    # id : 角色id
    # lv : 角色等级
    def __init__(self, id, lv):
        # 根据id获取数据
        tmp_actor = configMgr.actor[id]
        # 角色id
        self.id = tmp_actor["id"]
        # 角色名字
        self.name = tmp_actor["name"]
        # 角色介绍
        self.introduce = tmp_actor["introduce"]
        # 角色定位
        self.location = tmp_actor["location"]
        # 角色初始属性
        self.init_attr = Attr()
        # 角色成长属性
        self.growUp = Attr()
        # 角色技能
        self.growUp = []

        self.init_attr
        self.init_attr = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
        self.id = tmp_actor["id"]
