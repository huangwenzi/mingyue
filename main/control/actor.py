# 系统模块
import time
import copy
import random
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

    # 设置属性
    # attr_str : 属性字符串
    def __init__(self, attr_str = ""):
        if attr_str == "":
            return
        attr_arr = attr_str.split("|")
        self.hp = float(attr_arr[0])
        self.attack = float(attr_arr[1])
        self.attack_def = float(attr_arr[2])
        self.magic = float(attr_arr[3])
        self.magic_def = float(attr_arr[4])
        self.violent = float(attr_arr[5])
        self.antiriot = float(attr_arr[6])
        self.speed = float(attr_arr[7])
        self.move = float(attr_arr[8])
        self.attack_range = float(attr_arr[9])

    # 属性相加
    def add_attr(self, attr):
        self.hp = attr.hp
        self.attack = attr.attack
        self.attack_def = attr.attack_def
        self.magic = attr.magic
        self.magic_def = attr.magic_def
        self.violent = attr.violent
        self.antiriot = attr.antiriot
        self.speed = attr.speed
        self.move = attr.move
        self.attack_range = attr.attack_range

# 技能
# reckon_num : 计算技能作用数值
# get_eff_actor : 获取作用目标
class Skill():
    id = 0      # 技能id
    pro = 0     # 概率

    # rme_str : 属性字符串
    def __init__(self, rme_str):
        skill_arr = rme_str.split(",")
        # 技能id
        self.id = int(skill_arr[0])
        # 技能使用概率
        self.pro = float(skill_arr[1])
        # 从配置表加载技能属性
        skill_cfg = configMgr.skill[skill_arr[0]]
        # 技能名称
        self.name = skill_cfg["name"]
        # 技能说明
        self.explain = skill_cfg["explain"]
        # 最小使用等级
        self.minLevel = skill_cfg["minLevel"]
        # 技能类型
        self.m_type = skill_cfg["m_type"]
        # 作用目标
        self.target = skill_cfg["target"]
        # 优先作用目标
        self.first = skill_cfg["first"]
        # 作用数量
        self.number = skill_cfg["number"]
        # 属性对应的加成
        self.multiple = Attr(skill_cfg["multiple"])
        # 持续时间
        self.eff_time = skill_cfg["eff_time"]

    # 计算技能作用数值
    # actor : 计算基于的玩家，及他的战斗属性
    def reckon_num(self, actor):
        value = 0
        value += self.multiple.hp * actor.battle_attr.hp
        value += self.multiple.attack * actor.battle_attr.attack
        value += self.multiple.attack_def * actor.battle_attr.attack_def
        value += self.multiple.magic * actor.battle_attr.magic
        value += self.multiple.magic_def * actor.battle_attr.magic_def
        value += self.multiple.violent * actor.battle_attr.violent
        value += self.multiple.antiriot * actor.battle_attr.antiriot
        value += self.multiple.speed * actor.battle_attr.speed
        value += self.multiple.move * actor.battle_attr.move
        value += self.multiple.attack_range * actor.battle_attr.attack_range
        return value

    # 排序函数汇总
    # hp
    def sort_hp(self, elem):
        return elem.battle_attr.hp
    # attack
    def sort_attack(self, elem):
        return elem.battle_attr.attack
    # speed
    def sort_speed(self, elem):
        return elem.battle_attr.speed

    # 获取作用目标
    # actor : 对应角色
    def get_eff_actor(self, actor, actor_arr):
        # 作用的数量
        max_num = self.number  
        if len(actor_arr) < self.number:
            max_num = len(actor_arr)
        # 返回的作用角色
        ret_arr = []    
        # 根据条件排序
        # 最近
        if self.first == game_enum.skill_first.front:
            # 计算每一个的距离
            value_arr = []
            for tmp_actor in actor_arr:
                value_arr.append(actor.two_pos_distance(actor, tmp_actor))
            # 拷贝一份，后面找索引
            tmp_arr = copy.deepcopy(value_arr)
            value_arr.sort()
            tmp_arr = []    # 这个用来装拍完序的角色
            for idx in range(0, len(value_arr)):
                now_value = value_arr[idx]
                actor_arr_idx = tmp_arr.index(now_value)
                tmp_arr.append(actor_arr[actor_arr_idx])
            ret_arr = tmp_arr[0:max_num]
        # 随机
        elif self.first == game_enum.skill_first.rand:
            rand_arr = list(range(0, len(actor_arr)))
            for idx in range(0, max_num):
                rand = random.randrange(len(rand_arr))
                ret_arr.append(actor_arr[rand_arr[rand]])
                del rand_arr[rand]
        # 生命高
        elif self.first == game_enum.skill_first.rand:
            actor_arr.sort(self.sort_hp, reverse=True)
            ret_arr = actor_arr[0:max_num]
        # 生命低
        elif self.first == game_enum.skill_first.rand:
            actor_arr.sort(self.sort_hp, reverse=False)
            ret_arr = actor_arr[0:max_num]
        # 攻击高
        elif self.first == game_enum.skill_first.rand:
            actor_arr.sort(self.sort_attack, reverse=False)
            ret_arr = actor_arr[0:max_num]
        # 攻击速度高
        elif self.first == game_enum.skill_first.rand:
            actor_arr.sort(self.sort_speed, reverse=False)
            ret_arr = actor_arr[0:max_num]
        # 最远
        elif self.first == game_enum.skill_first.rand:
            # 计算每一个的距离
            value_arr = []
            for tmp_actor in actor_arr:
                value_arr.append(actor.two_pos_distance(actor, tmp_actor))
            # 拷贝一份，后面找索引
            tmp_arr = copy.deepcopy(value_arr)
            value_arr.sort()
            tmp_arr = []    # 这个用来装拍完序的角色
            for idx in range(0, len(value_arr)):
                now_value = value_arr[idx]
                actor_arr_idx = tmp_arr.index(now_value)
                tmp_arr.append(actor_arr[actor_arr_idx])
            ret_arr = tmp_arr[len(tmp_arr) - max_num:]
        # 全体
        elif self.first == game_enum.skill_first.rand:
            ret_arr = actor_arr
        return ret_arr

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
# init_battle_attr : 初始化战斗属性
# get_actor_image_name :　获取当前状态对应的角色图像资源名
# get_skill_image_name　: 获取当前使用的技能图像资源名
# set_actor_state : 设置当前状态
# two_pos_distance : 计算返回两个角色的直线距离平方
class Actor():
    # 当前的攻击最大索引号,大于就重置
    ATTACK_MAX_IDX = 3

    # 初始化角色属性
    # id : 角色id
    # lv : 角色等级
    def __init__(self, id, lv):
        # 根据id获取数据
        tmp_cfg = configMgr.actor[str(id)]
        # 角色id
        self.id = tmp_cfg["id"]
        # 角色名字
        self.name = tmp_cfg["name"]
        # 角色介绍
        self.introduce = tmp_cfg["introduce"]
        # 角色定位
        self.location = tmp_cfg["location"]
        # 角色初始属性(包括等级加成)
        self.init_attr = Attr(tmp_cfg["init_attr"])
        # 角色成长属性
        self.growUp = Attr(tmp_cfg["growUp"])
        # 角色当前属性(计算等级之类的加成后)
        self.now_attr = Attr()
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
        # 技能解析
        skill_arr = tmp_cfg["skill"].split("|")
        for idx in range(0, len(skill_arr)):
            self.skill.append(Skill(skill_arr[idx]))

        # 计算属性
        # 计算等级对应的属性
        self.hp = self.hp + lv * self.growUp.hp
        self.attack = self.attack + lv * self.growUp.attack
        self.attack_def = self.attack_def + lv * self.growUp.attack_def
        self.magic = self.magic + lv * self.growUp.magic
        self.magic_def = self.magic_def + lv * self.growUp.magic_def
        self.violent = self.violent + lv * self.growUp.violent
        self.antiriot = self.antiriot + lv * self.growUp.antiriot
        self.speed = self.speed + lv * self.growUp.speed
        self.move = self.move + lv * self.growUp.move
        self.attack_range = self.attack_range + \
            lv * self.growUp.attack_range

    # 初始化战斗属性(这个有问题，要在外面把技能被动加成计算到now_attr先)
    def init_battle_attr(self):
        # 计算技能被动加成（应该在外面就进行一边计算）
        # 先拷一份当前属性
        self.battle_attr = copy.deepcopy(self.init_attr)
        
    # 获取当前状态对应的角色图像资源名
    def get_actor_image_name(self):
        name = "actor_" + str(self.id) + "_" + self.camp + \
            "_" + self.state + "_" + str(self.state_idx)
        return name

    # 获取当前使用的技能图像资源名
    def get_skill_image_name(self):
        name = "skill_" + str(self.now_skill)
        return name

    # 设置当前状态
    # state : 要设置的状态
    def set_actor_state(self, state):
        if state not in [game_enum.actor.stand, game_enum.actor.attack, game_enum.actor.die]:
            return False
        self.state = state
        self.state_idx = 0
        return True

    # 计算返回两个角色的直线距离平方
    # actor_1 : {x, y}
    # actor_2 : {x, y}
    def two_pos_distance(self, actor_1, actor_2):
        pos_0 = [actor_1.x, actor_1.y]
        pos_1 = [actor_2.x, actor_2.y]
        return pow(pos_0[0] - pos_1[0], 2) + pow(pos_0[1] - pos_1[1], 2)

    # 修改生命
    # value : 要扣除的数量
    def add_hp(self, value):
        old = self.battle_attr.hp + value
        # 不可以大于上限，不可以小于下限
        old = min(self.now_attr.hp, old)
        old = max(0, old)
        add_value = self.battle_attr.hp - old
        self.battle_attr.hp = old
        # 死亡的要修改状态
        if old <= 0:
            self.set_actor_state(game_enum.actor.die)
        return add_value


