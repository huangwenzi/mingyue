# 角色管理器

import pygame
pygame.init()
import copy
import sys
sys.path.append("./FineArts/actor")

from actor import Actor
from i_enum import enum     # 包含枚举
from config import config   # 包含配置
from imageMgr import imageMgr   # 图片管理器


class ActorMgr():

    #初始化管理器
    #nScreen : 场景
    def __init__(self, nScreen):
        self.screen = nScreen    #场景
        self.actorList = []        # 队友列表
        self.d_actorList = []    # 敌人列表


    # 战斗前的初始化战斗属性
    def battle_init(self):
        for actor in self.i_actorList:    #遍历队友
            actor.battle_attr = copy.deepcopy(actor.self_attr)
            actor.share_attr.die = enum.actor.live
                
        for actor in self.d_actorList:    # 遍历敌人
            actor.battle_attr = copy.deepcopy(actor.self_attr)
            actor.share_attr.die = enum.actor.live
                

    #添加队友角色
    #index : 角色索引
    #nTeam_idx : 队伍位置索引
    #nlevel : 等级
    def addTeam(self, nIndex, nTeam_idx, nLevel):
        if nIndex == None:    #没有角色索引
            return 1

        list_index = len(self.i_actorList)    #列表里的索引
        addActor = Actor(nIndex, self.screen, nTeam_idx, "i", nLevel, list_index)
        self.actorList.append(addActor)


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
        if nIndex == None:    #没有角色索引
            return 1

        list_index = len(self.d_actorList)  # 列表里的索引
        addActor = Actor(nIndex, self.screen, nTeam_idx, "d", nLevel, list_index)
        self.d_actorList.append(addActor)


    #删除敌对角色
    #list_index:列表
    def remove_Hostile(self, list_index):
        self.d_actorList.remove(list_index)

    # 绘画角色
    # actor: 绘画的角色
    def blitem_actor(self, actor):
        # 加载当前图片资源
        team = None         # 队伍
        if actor.share_attr.team == "i" :
            team = enum.image.team
        elif actor.share_attr.team == "d" :
            team = enum.image.enemy
        actor_id = actor.share_attr.actor_idx   # 角色id
        state = actor.share_attr.state          # 当前状态
        image_idx = actor.share_attr.image_idx  # 当前状态图片索引
        now_image = imageMgr.actor_image[team][actor_id][state][image_idx]# 当前绘制的图片资源

        #绘制角色图像
        actor.rect.bottom = actor.share_attr.pos_y
        actor.rect.centerx = actor.share_attr.pos_x
        actor.screen.blit(now_image, actor.rect)

        #绘制身上的特效图片
        now_time = time.time()
        if actor.share_attr.effect :
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
        for actor in self.i_actorList:    #遍历队友
            # 只绘制存活的角色
            if actor.share_attr.die == enum.actor.live:
                self.blitem_actor(actor)

        for actor in self.d_actorList:    # 遍历敌人
            # 只绘制存活的角色
            if actor.share_attr.die == enum.actor.live:
                self.blitem_actor(actor)

        

        
        

