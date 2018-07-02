
#角色类
import pygame
pygame.init()
import sys
import copy
import time
sys.path.append("./config")
sys.path.append("./enum")
from actor_0 import Actor as i_actor_0
from actor_1 import Actor as i_actor_1
from actor_2 import Actor as i_actor_2
from actor_3 import Actor as i_actor_3
from actor_4 import Actor as i_actor_4
from actor_5 import Actor as i_actor_5
from actor_6 import Actor as i_actor_6
from actor_7 import Actor as i_actor_7
from module1 import enum    # 包含枚举
from config import config   # 包含配置
from skill import skill_tab # 包含技能表

class Share_attr() :        # 角色共有属性
    def __init__(self):
        self.level = 1              # 等级
        self.exp = 0                # 经验
        self.pos_x = 0              # 位置
        self.pos_y = 0
        self.team = None            # 是否队友 
        self.team_idx = 0           # 队伍的索引序列
        self.state = enum.state.wait# 当前状态 
        self.image_idx = 0          # 当前状态的图片索引
        self.target = None          # 目标敌人
        self.effect_index = None    # 身上的技能id
        self.effect_time = 0        # 特效时间
        self.do_time = 0            # 可以动作的时间
        self.die = enum.actor.live  # 是否死亡

#存放角色表
actor_tab = [i_actor_0(), i_actor_1(), i_actor_2(), i_actor_3(), i_actor_4(), i_actor_5(), i_actor_6(), i_actor_7(), ]

class Actor():
    #初始化角色
    #nIndex : 角色索引
    #nScreen : 场景数据
    #nTeam_idx : 队伍索引
    #nTeam : 队伍
    def __init__(self, nIndex, nScreen, nTeam_idx, nTeam, nLevel):
        # 角色初始化
        actor = copy.deepcopy(actor_tab[nIndex])# 添加角色属性 用深拷贝，保持角色表的变量不受拷贝对象改变
        self.name = actor.name                  # 角色名
        self.index = actor.index                # 角色索引
        self.introduce = actor.introduce        # 介绍
        self.location = actor.location          # 定位
        self.skill = actor.skill                # 技能
        self.self_attr = actor.self_attr        # 展示属性
        self.battle_attr = actor.battle_attr    # 战斗属性
        self.share_attr = Share_attr()          # 共有属性
        self.growUp_attr = actor.growUp_attr    # 成长属性
        self.buff = actor.buff                  # buff
        
        # 创建角色共有属性
        self.share_attr.team_idx = nTeam_idx
        self.share_attr.team = nTeam
        self.share_attr.level = nLevel

        # 计算属性
        self.recount_attr()

        # 名字
        self.name = config.font.font.render(self.self_attr.name, True, config.font.font_color)

        # 位置设置
        self.share_attr.pos_y = nTeam_idx%config.Max_row * config.actor_space + config.y_aline    #五个一行  再加上一点点位置校准
        if nTeam == config.team :
            self.share_attr.pos_x = nTeam_idx//config.Max_col * config.actor_space + config.y_aline    # 加一点微调
        elif nTeam == config.enemy :  # 敌人放在另一边
            self.share_attr.pos_x = nScreen.get_width() - nTeam_idx//config.Max_col * config.actor_space - config.y_aline
        self.share_attr.state = enum.state.normal

        
    # 重新计算属性
    def recount_attr(self):
        # 先初始化数据
        # 添加角色展示属性 用深拷贝，保持角色表的变量不受拷贝对象改变
        tmp_attr = copy.deepcopy(actor_tab[self.index].self_attr)
        self.self_attr = tmp_attr

        # 自身属性计算
        tmp_enum = enum.attr_type  # 属性枚举
        self.self_attr[tmp_enum.MaxHp] += self.share_attr.level * self.growUp_attr[tmp_enum.MaxHp]      # 最大生命值
        self.self_attr[tmp_enum.hp] = self.self_attr[tmp_enum.MaxHp]                                    # 现有生命值
        self.self_attr[tmp_enum.attack] += self.share_attr.level * self.growUp_attr[tmp_enum.attack]    # 攻击
        self.self_attr[tmp_enum.defense] += self.share_attr.level * self.growUp_attr[tmp_enum.defense]  # 防御
        self.self_attr[tmp_enum.violent] += self.share_attr.level * self.growUp_attr[tmp_enum.violent]  # 暴击
        self.self_attr[tmp_enum.antiriot] += self.share_attr.level * self.growUp_attr[tmp_enum.antiriot]# 抗暴
        self.self_attr[tmp_enum.speed] += self.share_attr.level * self.growUp_attr[tmp_enum.speed]      # 攻击速度
        self.self_attr[tmp_enum.move] += self.share_attr.level * self.growUp_attr[tmp_enum.move]        # 移动速度
        self.self_attr[tmp_enum.attack_range] += self.share_attr.level * self.growUp_attr[tmp_enum.attack_range]  # 攻击范围

        #永久性被动加成
        for num in range(0, config.skill.count):
            skill_id = self.skill[num][0]    # 技能id
            tmp_skill = skill_tab[skill_id]  # 获取对应id的技能数据
            if tmp_skill.m_type == enum.skill_type.passivity:
                self.self_attr[tmp_enum.MaxHp] += self.share_attr.level * tmp_skill.up_attr[tmp_enum.MaxHp]       # 最大生命值
                self.self_attr[tmp_enum.hp] = self.self_attr[tmp_enum.MaxHp]                                      # 现有生命值
                self.self_attr[tmp_enum.attack] += self.share_attr.level * tmp_skill.up_attr[tmp_enum.attack]     # 攻击
                self.self_attr[tmp_enum.defense] += self.share_attr.level * tmp_skill.up_attr[tmp_enum.defense]   # 防御
                self.self_attr[tmp_enum.violent] += self.share_attr.level * tmp_skill.up_attr[tmp_enum.violent]   # 暴击
                self.self_attr[tmp_enum.antiriot] += self.share_attr.level * tmp_skill.up_attr[tmp_enum.antiriot] # 抗暴
                self.self_attr[tmp_enum.speed] += self.share_attr.level * tmp_skill.up_attr[tmp_enum.speed]       # 攻击速度
                self.self_attr[tmp_enum.move] += self.share_attr.level * tmp_skill.up_attr[tmp_enum.move]         # 移动速度
                self.self_attr[tmp_enum.attack_range] += self.share_attr.level * tmp_skill.up_attr[tmp_enum.attack_range]  # 攻击范围


    # 计算战斗中的变动被动属性
    def recount_change_passivity(self):
        # 拷贝除现有生命值以外的属性
        tmp_enum = enum.attr_type  # 属性枚举
        tmp_attr = copy.deepcopy(self.self_attr)
        tmp_attr[tmp_enum.hp] = self.battle_attr[tmp_enum.hp]
        self.battle_attr = tmp_attr

        # 寻找出变动被动技能
        for num in range(0, config.skill.count):
            skill_id = self.skill[num][0]    # 技能id
            tmp_skill = skill_tab[skill_id]  # 获取对应id的技能数据
            if tmp_skill.m_type == enum.skill_type.change_passivity:
                # 根据生命值下降提升
                if tmp_skill.condition == enum.skill_condition.hp_down:
                    mult = self.battle_attr[tmp_enum.hp] / self.battle_attr[tmp_enum.MaxHp] + 1
                    self.battle_attr[tmp_enum.attack] += self.battle_attr[tmp_enum.attack] * mult       # 攻击
                    self.battle_attr[tmp_enum.defense] += self.battle_attr[tmp_enum.defense] * mult     # 防御
                    self.battle_attr[tmp_enum.violent] += self.battle_attr[tmp_enum.violent] * mult     # 暴击
                    self.battle_attr[tmp_enum.antiriot] += self.battle_attr[tmp_enum.antiriot] * mult   # 抗暴
                    self.battle_attr[tmp_enum.speed] += self.battle_attr[tmp_enum.speed] * mult         # 攻击速度
                    self.battle_attr[tmp_enum.move] += self.battle_attr[tmp_enum.move] * mult           # 移动速度
                    self.battle_attr[tmp_enum.attack_range] += self.battle_attr[tmp_enum.attack_range] * mult  # 攻击范围

    
    # 添加buff时计算附加的属性
    # id : 技能的id
    # end_time : 结束时间
    def add_buff(self, tmp_buff, end_time):
        self.buff.append([end_time, tmp_buff])  # 先添加buff属性到buff列表中
        tmp_enum = enum.attr_type  # 属性枚举
        self.battle_attr[tmp_enum.attack] += tmp_buff[tmp_enum.attack]        # 攻击
        self.battle_attr[tmp_enum.defense] += tmp_buff[tmp_enum.defense]      # 防御
        self.battle_attr[tmp_enum.violent] += tmp_buff[tmp_enum.violent]      # 暴击
        self.battle_attr[tmp_enum.antiriot] += tmp_buff[tmp_enum.antiriot]    # 抗暴
        self.battle_attr[tmp_enum.speed] += tmp_buff[tmp_enum.speed]          # 攻击速度
        self.battle_attr[tmp_enum.move] += tmp_buff[tmp_enum.move]            # 移动速度
        self.battle_attr[tmp_enum.attack_range] += tmp_buff[tmp_enum.attack_range]# 攻击范围

    
    # 检查删除到时间的buff
    def remove_buff(self):
        now_time = time.time()  # 当前的时间
        count = 0
        buff_count = len(self.buff)  # buff数
        while True:
            # 还没有循环完
            if count < buff_count:
                # 如果达到结束时间
                if now_time > self.buff[count][0]:
                    tmp_enum = enum.attr_type       # 属性枚举
                    tmp_buff = self.buff[count][1]  # 属性列表
                    # 减去对应属性
                    self.battle_attr[tmp_enum.attack] -= tmp_buff[tmp_enum.attack]        # 攻击
                    self.battle_attr[tmp_enum.defense] -= tmp_buff[tmp_enum.defense]      # 防御
                    self.battle_attr[tmp_enum.violent] -= tmp_buff[tmp_enum.violent]      # 暴击
                    self.battle_attr[tmp_enum.antiriot] -= tmp_buff[tmp_enum.antiriot]    # 抗暴
                    self.battle_attr[tmp_enum.speed] -= tmp_buff[tmp_enum.speed]          # 攻击速度
                    self.battle_attr[tmp_enum.move] -= tmp_buff[tmp_enum.move]            # 移动速度
                    self.battle_attr[tmp_enum.attack_range] -= tmp_buff[tmp_enum.attack_range]# 攻击范围
                    # 删除buff
                    self.buff.remove(count)
                    count -= 1
                    buff_count -= 1
                count += 1
                continue

            break




