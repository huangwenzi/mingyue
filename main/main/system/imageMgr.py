
#图片管理器
import sys
import pygame
pygame.init()
sys.path.append("./config")
sys.path.append("./FineArts")

import image

class ImageMgr():
    def __init__(self):
        #加载角色资源
        config = image.actor_image
        self.actor_image = []   # 角色图片资源总表
        for team in range(0,len(config)):  # 队伍
            self.actor_image.append([])
            for actor_index in range(0,len(config[team])): # 角色
                self.actor_image[team].append([])
                for state in range(0,len(config[team][actor_index])): # 状态
                    self.actor_image[team][actor_index].append([])
                    for index in range(0,len(config[team][actor_index][state])): # 索引
                        self.actor_image[team][actor_index][state].append([])
                        tmp_config = config[team][actor_index][state][index]            # 当前配置
                        tmp_image = self.actor_image[team][actor_index][state][index]   # 加载位置
                        tmp_image = pygame.image.load(tmp_config[0])                    # 加载图片
                        tmp_image = pygame.transform.scale(tmp_image, tmp_config[1])    # 缩放
        
        # 加载技能图片资源
        config = image.skill_image
        self.skill_image = []   # 技能图片资源总表
        for id in range(0,len(config)):  # id
            self.skill_image.append([])
            self.skill_image[id] = pygame.image.load(config[id][0])                             # 加载图片
            self.skill_image[id] = pygame.transform.scale(self.skill_image[id], config[id][1])  # 缩放

        # 加载场景图片资源
        self.screen_image = []  # 场景图片资源总表
        for index in range(0, len(image.screen_image)):
            self.screen_image.append([])
            tmp_image = pygame.image.load(image.screen_image[index][0])  # 加载图片
            self.screen_image[index] = tmp_image

        # 加载视图图片资源
        self.view_image = []    # 视图图片资源总表
        for view_index in range(0, len(image.view_image)):
            self.view_image.append([])
            for image_index in range(0, len(image.view_image[view_index])):
                tmp_config = image.view_image[image_index]          # 图片配置
                tmp_image = pygame.image.load(tmp_config[0])        # 加载图片
                tmp_image = pygame.transform.scale(tmp_image, tmp_config[1])  # 缩放
                self.view_image[image_index] = tmp_image            



imageMgr = ImageMgr()  # 图片资源
