# 角色管理器

import pygame
pygame.init()
import copy
import time
import sys
sys.path.append("./FineArts/actor")

from actor import Actor
from i_enum import enum         # 包含枚举
from config import config       # 包含配置
from imageMgr import imageMgr   # 图片管理器


class ActorMgr():

    #初始化管理器
    #nScreen : 场景
    def __init__(self, nScreen):
        self.screen = nScreen    # 场景
        self.actor_list = []      # 队友列表
        self.d_actor_list = []    # 敌人列表


    # 战斗前的初始化战斗属性
    def battle_begin(self):
        for actor in self.actor_list:    # 遍历队友
            actor.battle_attr = copy.deepcopy(actor.self_attr)
            actor.share_attr.die = enum.actor.live
        for actor in self.d_actor_list:  # 遍历敌人
            actor.battle_attr = copy.deepcopy(actor.self_attr)
            actor.share_attr.die = enum.actor.live


    # 战斗结束时初始化战斗属性
    def battle_end(self):
        for actor in self.actor_list:    # 遍历队友
            actor.battle_attr = copy.deepcopy(actor.self_attr)
            actor.share_attr.die = enum.actor.live
        for actor in self.d_actor_list:  # 遍历敌人
            actor.battle_attr = copy.deepcopy(actor.self_attr)
            actor.share_attr.die = enum.actor.live
                

    # 添加队友角色
    # index : 角色索引
    # nTeam_idx : 队伍位置索引
    # nlevel : 等级
    def addTeam(self, nIndex, nTeam_idx, nLevel):
        if nIndex == None:    #没有角色索引
            return 1

        addActor = Actor(nIndex, self.screen, nTeam_idx, enum.actor.team, nLevel)
        self.actor_list.append(addActor)


    # 删除队友角色
    # index : 角色索引
    def remove_Team(self, index):
        for num in range(0, len(self.actor_list)):
            # 寻找符合条件的角色
            if self.actor_list[num].index == index:
                self.actor_list[num].remove(num)
                break


    # 添加敌对角色
    # index : 角色索引
    # nTeam_idx : 队伍位置索引
    # nlevel : 等级
    def addHostile(self, nIndex, nTeam_idx, nLevel):
        if nIndex == None:    #没有角色索引
            return 1

        addActor = Actor(nIndex, self.screen, nTeam_idx, enum.actor.enemy, nLevel)
        self.d_actor_list.append(addActor)


    # 删除敌对角色
    # index : 列表
    def remove_Hostile(self, index):
        for num in range(0, len(self.d_actor_list)):
            # 寻找符合条件的角色
            if self.d_actor_list[num].index == index:
                self.d_actor_list[num].remove(num)
                break


    # 绘画角色
    # actor: 绘画的角色
    def blitem_actor(self, actor):
        # 加载当前图片资源
        team = actor.share_attr.team            # 队伍
        actor_id = actor.share_attr.actor_idx   # 角色id
        state = actor.share_attr.state          # 当前状态
        image_idx = actor.share_attr.image_idx  # 当前状态图片索引
        now_image = imageMgr.actor_image[team][actor_id][state][image_idx]# 当前绘制的图片资源

        #绘制角色图像
        actor.rect = now_image.get_rect()   # 获取角色图片尺寸
        actor.rect.bottom = actor.share_attr.pos_y
        actor.rect.centerx = actor.share_attr.pos_x
        actor.screen.blit(now_image, actor.rect)

        #绘制身上的特效图片
        now_time = time.time()
        if actor.share_attr.effect:
            actor.screen.blit(actor.share_attr.effect, actor.rect)
            if actor.share_attr.effect_time <= now_time:
                actor.share_attr.effect = None

        #绘制名字
        actor.screen.blit(actor.name, (actor.rect.centerx - 50, actor.rect.bottom - 115))

        #绘制生命框
        pygame.draw.rect(actor.screen, config.font.font_color, (actor.rect.centerx - 50, actor.rect.bottom - 100, config.hpBar.left, config.hpBar.height), 3)#生命条外框
        hpX = actor.actor_attr.hp/actor.actor_attr.MaxHp    #计算生命值长度
        pygame.draw.rect(actor.screen, config.hp_bar.bar_color, (actor.rect.centerx - 47, actor.rect.bottom - 97, hpX * 84, 10), )#剩余生命值
        hp_number = config.font.font.render('%.1f' % (actor.actor_attr.hp), True, config.font.font_color)  # 生命值数值
        actor.screen.blit(hp_number, (actor.rect.centerx - 30, actor.rect.bottom - 100))


    #遍历绘画角色
    def blitme(self):
        for actor in self.actor_list:    #遍历队友
            # 只绘制存活的角色
            if actor.share_attr.die == enum.actor.live:
                self.blitem_actor(actor)

        for actor in self.d_actor_list:    # 遍历敌人
            # 只绘制存活的角色
            if actor.share_attr.die == enum.actor.live:
                self.blitem_actor(actor)

        

        
        

