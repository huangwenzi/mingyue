
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

class Share_attr() :        # 角色共有属性，反正以后也记不得了
    def __init__(self):
        self.level = 1              # 等级
        self.exp = 0                # 经验
        self.pos_x = 0              # 位置
        self.pos_y = 0
        self.team = None            # 是否队友 i = 队友 d = 敌人
        self.actor_idx = 0          # 角色的索引序列
        self.list_index = 0         # 列表的索引序列
        self.team_idx = 0           # 队伍的索引序列
        self.state = enum.state.wait  # 当前状态 1：待命  2：战斗
        self.image_idx = 0          # 当前状态的图片索引
        self.target = None          # 目标敌人
        self.now_image = None       # 当前图片
        self.effect = None          # 身上的特效
        self.effect_time = 0        # 特效时间
        self.do_time = 0            # 可以动作的时间
        self.die = enum.actor.live  # 是否死亡

#存放角色表    (0是占位，用来索引对齐)
actor_tab = [i_actor_0(), i_actor_1(), i_actor_2(), i_actor_3(), i_actor_4(), i_actor_5(), i_actor_6(), i_actor_7(), ]

class Actor():
    #初始化角色
    #nIndex : 角色索引
    #nScreen : 场景数据
    #nTeam_idx : 队伍索引
    #nTeam : 'i'=队友 'd'=敌人
    #list_index : 列表里的索引
    def __init__(self, nIndex, nScreen, nTeam_idx, nTeam, nLevel, list_index):
        #角色初始化
        actor = copy.deepcopy(actor_tab[nIndex])    # 添加角色属性 用深拷贝，保持角色表的变量不受拷贝对象改变
        self.name = actor.name                  # 角色名
        self.index = actor.index            # 角色索引
        self.introduce = actor.introduce        # 介绍
        self.location = actor.location          # 定位
        self.self_attr = actor.self_attr        # 展示属性
        self.battle_attr = actor.battle_attr    # 战斗属性
        self.growUp = actor.growUp              # 成长
        self.skill = actor.skill                # 技能
        self.share_attr = Share_attr()          # 共有属性
     
        # 创建角色共有属性
        self.share_attr = share_attr()
        self.share_attr.actor_idx = nIndex
        self.share_attr.team_idx = nTeam_idx
        self.share_attr.list_index = list_index
        self.share_attr.team = nTeam
        self.share_attr.level = nLevel

        # 自身属性计算
        # 等级成长属性
        tmp_enum = enum.attr_type     #属性枚举
        self.self_attr[tmp_enum.MaxHp] += nLevel * self.growUp[tmp_enum.MaxHp]      # 最大生命值
        self.self_attr[tmp_enum.hp] = self.self_attr[tmp_enum.MaxHp]                # 现有生命值
        self.self_attr[tmp_enum.attack] += nLevel * self.growUp[tmp_enum.attack]    # 攻击
        self.self_attr[tmp_enum.defense] += nLevel * self.growUp[tmp_enum.defense]  # 防御
        self.self_attr[tmp_enum.violent] += nLevel * self.growUp[tmp_enum.violent]  # 暴击
        self.self_attr[tmp_enum.antiriot] += nLevel * self.growUp[tmp_enum.antiriot]# 抗暴
        self.self_attr[tmp_enum.speed] += nLevel * self.growUp[tmp_enum.speed]      # 攻击速度
        self.self_attr[tmp_enum.move] += nLevel * self.growUp[tmp_enum.move]        # 移动速度
        self.self_attr[tmp_enum.attack_range] += nLevel * self.growUp[tmp_enum.attack_range]  # 攻击范围

        #永久性被动加成
        for num in range(0, config.skill.count):
            skill_id = self.skill[num][0]   # 技能id
            tmp_skill = skill_tab[skill_id] # 获取对应id的技能数据
            if tmp_skill.m_type == enum.skill_type.passivity :
                self.self_attr[tmp_enum.MaxHp] += nLevel * tmp_skill.attr[tmp_enum.MaxHp]       # 最大生命值
                self.self_attr[tmp_enum.hp] = self.self_attr[tmp_enum.MaxHp]                    # 现有生命值
                self.self_attr[tmp_enum.attack] += nLevel * tmp_skill.attr[tmp_enum.attack]     # 攻击
                self.self_attr[tmp_enum.defense] += nLevel * tmp_skill.attr[tmp_enum.defense]   # 防御
                self.self_attr[tmp_enum.violent] += nLevel * tmp_skill.attr[tmp_enum.violent]   # 暴击
                self.self_attr[tmp_enum.antiriot] += nLevel * tmp_skill.attr[tmp_enum.antiriot] # 抗暴
                self.self_attr[tmp_enum.speed] += nLevel * tmp_skill.attr[tmp_enum.speed]       # 攻击速度
                self.self_attr[tmp_enum.move] += nLevel * tmp_skill.attr[tmp_enum.move]         # 移动速度
                self.self_attr[tmp_enum.attack_range] += nLevel * tmp_skill.attr[tmp_enum.attack_range]  # 攻击范围

        # 名字
        self.name = config.font.font.render(self.self_attr.name, True, config.font.font_color)

        # 位置设置
        self.share_attr.pos_y = nTeam_idx%config.Max_row * config.actor_space + config.y_aline    #五个一行  再加上一点点位置校准
        self.rect.bottom = self.share_attr.pos_y
        if nTeam == config.team :
            self.share_attr.pos_x = nTeam_idx//config.Max_col * config.actor_space + config.y_aline    # 加一点微调
        elif nTeam == config.enemy :  # 敌人放在另一边
            self.share_attr.pos_x = nScreen.get_width() - nTeam_idx//config.Max_col * config.actor_space - config.y_aline
        self.rect.centerx = self.share_attr.pos_x
        self.share_attr.state = enum.state.normal

        # 场景尺寸数据
        self.rect = self.image_1[0].get_rect()
        self.screen = nScreen
        self.screen_rect = nScreen.get_rect()
        
        


    def blitme(self):
        #绘制角色图像
        self.rect.bottom = self.share_attr.pos_y
        self.rect.centerx = self.share_attr.pos_x
        self.screen.blit(self.share_attr.now_image, self.rect)

        #绘制身上的特效图片
        now_time = time.time()
        if self.share_attr.effect :
            self.screen.blit(self.share_attr.effect, self.rect)
            if self.share_attr.effect_time <= now_time:
                self.share_attr.effect = None

        #绘制名字
        self.screen.blit(self.name, (self.rect.centerx - 50, self.rect.bottom - 115))

        #绘制生命框
        pygame.draw.rect(self.screen, config.font.font_color, (self.rect.centerx - 50, self.rect.bottom - 100, config.hpBar.left, config.hpBar.height), 3)#生命条外框
        hpX = self.self_attr.hp/self.self_attr.MaxHp    #计算生命值长度
        pygame.draw.rect(self.screen, config.hp_bar.bar_color, (self.rect.centerx - 47, self.rect.bottom - 97, hpX * 84, 10), )#剩余生命值
        hp_number = config.font.font.render('%.1f' % (self.self_attr.hp), True, config.font.font_color)  # 生命值数值
        self.screen.blit(hp_number, (self.rect.centerx - 30, self.rect.bottom - 100))
