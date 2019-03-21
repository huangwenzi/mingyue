# 系统模块
import time
import copy
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
    attack_range = 0  # 攻击范围

# 技能
class Skill():
    id = 0      # 技能id
    pro = 0     # 概率

    def __init__(self, rme_str):
        skill_arr = rme_str.split(",")
        self.id = int(skill_arr[0])
        self.pro = float(skill_arr[1])

# 目标
class Target():
    # 阵营
    camp = ""
    # 目标id
    id = -1
    # 目标位置
    x = 0
    y = 0


# 角色
class Actor():
    # 当前的攻击最大索引号,大于就重置
    ATTACK_MAX_IDX = 3

    # 初始化角色属性
    # id : 角色id
    # lv : 角色等级
    def __init__(self, id, lv):
        # 根据id获取数据
        tmp_actor = configMgr.actor[str(id)]
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
        # 角色当前属性(计算等级之类的加成后)
        self.now_attr = Attr()
        # 角色成长属性
        self.growUp = Attr()
        # 角色技能
        self.skill = []

        # 下面数据战斗中使用
        # 位置
        self.x = 0
        self.y = 0
        # 阵营是玩家的队友或是敌人
        self.camp = ""
        # 下次行动的时间
        self.next_time = 0
        # 战斗中属性
        self.battle_attr = Attr()
        # 当前行动状态
        self.state = game_enum.state.wati
        # 当前状态的步骤
        self.state_idx = 0
        # 正在使用的技能
        self.now_skill = 0
        # 要攻击的目标
        self.target = Target()

        # 数据处理
        # 初始属性解析
        init_attr_arr = tmp_actor["init_attr"].split("|")
        self.init_attr.hp = float(init_attr_arr[game_enum.attr_type.hp])
        self.init_attr.attack = float(
            init_attr_arr[game_enum.attr_type.attack])
        self.init_attr.attack_def = float(
            init_attr_arr[game_enum.attr_type.attack_def])
        self.init_attr.magic = float(init_attr_arr[game_enum.attr_type.magic])
        self.init_attr.magic_def = float(
            init_attr_arr[game_enum.attr_type.magic_def])
        self.init_attr.violent = float(
            init_attr_arr[game_enum.attr_type.violent])
        self.init_attr.antiriot = float(
            init_attr_arr[game_enum.attr_type.antiriot])
        self.init_attr.speed = float(init_attr_arr[game_enum.attr_type.speed])
        self.init_attr.move = float(init_attr_arr[game_enum.attr_type.move])
        self.init_attr.attack_range = float(
            init_attr_arr[game_enum.attr_type.attack_range])
        # 成长属性解析
        growUp_arr = tmp_actor["growUp"].split("|")
        self.growUp.hp = float(growUp_arr[game_enum.attr_type.hp])
        self.growUp.attack = float(growUp_arr[game_enum.attr_type.attack])
        self.growUp.attack_def = float(
            growUp_arr[game_enum.attr_type.attack_def])
        self.growUp.magic = float(growUp_arr[game_enum.attr_type.magic])
        self.growUp.magic_def = float(
            growUp_arr[game_enum.attr_type.magic_def])
        self.growUp.violent = float(growUp_arr[game_enum.attr_type.violent])
        self.growUp.antiriot = float(growUp_arr[game_enum.attr_type.antiriot])
        self.growUp.speed = float(growUp_arr[game_enum.attr_type.speed])
        self.growUp.move = float(growUp_arr[game_enum.attr_type.move])
        self.growUp.attack_range = float(
            growUp_arr[game_enum.attr_type.attack_range])
        # 技能解析
        skill_arr = tmp_actor["skill"].split("|")
        for idx in range(0, len(skill_arr)):
            self.skill.append(Skill(skill_arr[idx]))

        # 计算属性
        # 计算等级对应的属性
        self.now_attr.hp = self.init_attr.hp + lv * self.growUp.hp
        self.now_attr.attack = self.init_attr.attack + lv * self.growUp.attack
        self.now_attr.attack_def = self.init_attr.attack_def + lv * self.growUp.attack_def
        self.now_attr.magic = self.init_attr.magic + lv * self.growUp.magic
        self.now_attr.magic_def = self.init_attr.magic_def + lv * self.growUp.magic_def
        self.now_attr.violent = self.init_attr.violent + lv * self.growUp.violent
        self.now_attr.antiriot = self.init_attr.antiriot + lv * self.growUp.antiriot
        self.now_attr.speed = self.init_attr.speed + lv * self.growUp.speed
        self.now_attr.move = self.init_attr.move + lv * self.growUp.move
        self.now_attr.attack_range = self.init_attr.attack_range + \
            lv * self.growUp.attack_range

    # 初始化战斗属性
    def init_battle_attr(self):
        # 先拷一份基础属性
        self.battle_attr = copy.deepcopy(self.now_attr)
        # 计算技能被动加成（自身的加成在这里计算，群体的在外面一起计算叠加）

    # 获取当前状态对应的角色图像资源名
    def get_actor_image_name(self):
        name = "actor_" + str(self.id) + "_" + self.camp + "_" + self.state + "_" + str(self.state_idx)
        return name
    
    # 获取当前使用的技能图像资源名
    def get_skill_image_name(self):
        name = "skill_" + str(self.now_skill)
        return name