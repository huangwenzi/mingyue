# 系统模块
import time
# 三方模块
import pygame
# 项目模块
from control.mouse import Mouse
from control.image import Image
from enums.game_enum import game_enum
from system.battleMgr import BattleMgr

# 图像管理器


class ImageMgr():

    def __init__(self):
        # 基本设置
        self.last_time = 0          # 上次刷新的时间
        self.frames = 50            # 帧数
        self.normal_image_list = []  # 平常图像列表 (注意列表的顺序代表z轴)
        self.normal_background = pygame.image.load(
            "main/FineArts/png/背景/平常背景图.jpg")    # 平常背景图片
        self.battle_image_dict = {}  # 战斗图像字典 (战斗的绘制不同于平常图像)
        self.battle_background = pygame.image.load(
            "main/FineArts/png/背景/战斗背景图.jpg")    # 战斗背景图片
        self.image_callback = {}    # 图像资源对应的回调函数
        self.width = self.normal_background.get_width()    # 图像宽度
        self.height = self.normal_background.get_height()  # 图像高度
        self.image = pygame.display.set_mode((self.width, 500))    # 设置窗体
        self.x = 0
        self.y = 0
        self.state = game_enum.state.normal  # 当前场景状态

        # 管理器
        self.mouse = Mouse()    # 鼠标事件管理器
        self.battleMgr = BattleMgr()  # 战斗场景管理器

        # 初始界面
        self.add_normal_image("main/FineArts/png/界面/战斗.png", "fight",
                              game_enum.iamge_type.button, [0, 0], self.fight_callback)
        self.add_normal_image("main/FineArts/png/界面/保存.png", "save",
                              game_enum.iamge_type.button, [50, 0], self.save_callback)

    # 绘制刷新界面
    def blit_image(self):
        # 是否到了刷新时间
        now_time = time.time()
        if self.last_time + 1/self.frames > now_time:
            return

        self.last_time += now_time
        # 区分战斗和平常状态下的界面
        if self.state == game_enum.state.normal:    # 平常界面绘制
            # 绘制背景
            self.image.blit(self.normal_background, (self.x, self.y))
            # 绘制子级图像
            for tmp_image in self.normal_image_list:
                tmp_image.blit_image()
        elif self.state == game_enum.state.battle:  # 战斗界面绘制
            # 绘制背景
            self.image.blit(self.battle_background, (self.x, self.y))
            # 根据战斗角色的状态绘制
            self.blit_battle()

        # 显示
        pygame.display.flip()

    # 鼠标事件
    def mouse_event(self):
        # 战斗状态不予许手动操作
        if self.state == game_enum.state.battle:
            return
        mouse_ret = self.mouse.mouse_event()
        if mouse_ret.type == game_enum.mouse.click_open:
            # 查找点击到的图像,从后面开始找
            list_len = len(self.normal_image_list)
            for idx in range(0, list_len):
                tmp_image = self.normal_image_list[list_len - idx - 1]
                ret, obj = tmp_image.get_click_image(mouse_ret)
                # 找到图像，处理退出
                if ret == True:
                    # 如果存在事件函数
                    if obj.name in self.image_callback:
                        self.image_callback[obj.name]()
                    return

    # 添加一个图像
    # path : 图像资源地址
    # name : 名字
    # postion : 位置
    # tmp_type : 图像资源类型
    # callback : 回调函数
    def add_normal_image(self, path, name, tmp_type, postion, callback):
        # 添加图像到列表
        tmp_image = Image(self, path, name, tmp_type, postion)
        self.normal_image_list.append(tmp_image)
        if callback:
            self.image_callback[name] = callback

    # 加载战斗中需要用到的角色资源
    # 加载的资源命名规则
    # 角色 : actor_(actor_id)_(敌我标识)_(状态标识)_(状态序列号)
    # 技能 : skill_(skill_id)
    def load_battle_image(self):
        # 先清空旧数据(战斗结束也清一下，这里再清一遍)
        self.battle_image_dict = {}
        battle_image_dict = self.battle_image_dict
        actor_path = "main/FineArts/actor"
        skill_path = "main/FineArts/skill"

        # 加载己方的资源
        myself_actor = self.battleMgr.myself_actor
        for tmp_actor in myself_actor:
            # 加载站立图像资源
            id_str = "actor_" + str(tmp_actor.id)
            action_str = "i_stand_0"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + "_" + action_str
            tmp_image = Image(self, actor_path_str,
                              image_name, game_enum.iamge_type.actor, [0, 0])
            battle_image_dict[image_name] = tmp_image
            # 加载攻击图像资源
            id_str = "actor_" + str(tmp_actor.id)
            for idx in range(0, 2):
                action_str = "i_attack_" + str(idx)
                actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
                image_name = id_str + "_" + action_str
                tmp_image = Image(self, actor_path_str,
                                    image_name, game_enum.iamge_type.actor, [0, 0])
                battle_image_dict[image_name] = tmp_image
            # 加载要用到的技能资源
            skill = tmp_actor.skill
            for tmp_skill in skill:
                image_name = "skill_" + str(tmp_skill.id)
                skill_path_str = skill_path + "/" + image_name + ".png"
                tmp_image = Image(self, skill_path_str,
                                  image_name, game_enum.iamge_type.skill, [0, 0])
                battle_image_dict[image_name] = tmp_image
        # 加载对手的资源
        match_actor = self.battleMgr.match_actor
        for tmp_actor in match_actor:
            # 加载站立图像资源
            id_str = "actor_" + str(tmp_actor.id)
            action_str = "d_stand_0"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + "_" + action_str
            tmp_image = Image(self, actor_path_str,
                              image_name, game_enum.iamge_type.actor, [0, 0])
            battle_image_dict[image_name] = tmp_image
            # 加载攻击图像资源
            id_str = "actor_" + str(tmp_actor.id)
            for idx in range(0, 2):
                action_str = "d_attack_" + str(idx)
                actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
                image_name = id_str + "_" + action_str
                tmp_image = Image(self, actor_path_str,
                                    image_name, game_enum.iamge_type.actor, [0, 0])
                battle_image_dict[image_name] = tmp_image
            # 加载要用到的技能资源
            skill = tmp_actor.skill
            for tmp_skill in skill:
                image_name = "skill_" + str(tmp_skill.id)
                skill_path_str = skill_path + "/" + image_name + ".png"
                tmp_image = Image(self, skill_path_str,
                                  image_name, game_enum.iamge_type.skill, [0, 0])
                battle_image_dict[image_name] = tmp_image
    
    # 战斗场景初始化
    def battle_scene_init(self):
        # 初始化己方
        myself_actor = self.battleMgr.myself_actor
        count = 0   # 当前是第几个排序的角色，用于设置位置
        for tmp_actor in myself_actor:
            tmp_actor.x = (count//4 + 1) * 50
            tmp_actor.y = (count% 4 + 1) * 100
            tmp_actor.camp = game_enum.actor.team
            self.last_time = time.time()
            tmp_actor.init_battle_attr()
            tmp_actor.state = game_enum.actor.stand
            tmp_actor.state_idx = 0
        # 初始化敌方
        match_actor = self.battleMgr.match_actor
        count = 0   # 当前是第几个排序的角色，用于设置位置
        for tmp_actor in match_actor:
            tmp_actor.x = self.width - (count//4 + 1) * 50
            tmp_actor.y = (count% 4 + 1) * 100
            tmp_actor.camp = game_enum.actor.enemy
            self.last_time = time.time()
            tmp_actor.init_battle_attr()
            tmp_actor.state = game_enum.actor.stand
            tmp_actor.state_idx = 0

    # 战斗过程计算
    def battle_reckon(self):
        pass

    # 战斗绘制
    def blit_battle(self):
        # 先绘制己方
        myself_actor = self.battleMgr.myself_actor
        for tmp_actor in myself_actor:
            image_name = tmp_actor.get_actor_image_name()
            # 如果是站立和移动状态，只需要绘制角色就好了(移动还没有，后面再出对应图像)
            if tmp_actor.state == game_enum.actor.stand:
                self.image.blit(self.battle_image_dict[image_name], (tmp_actor.x, tmp_actor.y))
            elif tmp_actor.state == game_enum.actor.attack:
                self.image.blit(self.battle_image_dict[image_name], (tmp_actor.x, tmp_actor.y))
                # 如果是攻击的最后一下，还要把对应的技能显示出来
                if tmp_actor.state_idx == tmp_actor.ATTACK_MAX_IDX:
                    skill_name = tmp_actor.get_skill_image_name()
                    self.image.blit(self.battle_image_dict[skill_name], (tmp_actor.x, tmp_actor.y))#这里的显示位置应该作用对象的位置

    # 战斗按钮的回调
    def fight_callback(self):
        print("fight_callback")
        # 设置战斗状态
        self.state = game_enum.state.battle
        # 设置战斗对手
        enemy_arr = [{"id": 4, "lv": 10}, {"id": 5, "lv": 10},
                     {"id": 6, "lv": 10}, {"id": 7, "lv": 10}]
        self.battleMgr.set_enemy(enemy_arr)

        # 加载战斗中可能需要的图像资源
        self.load_battle_image()

        # 初始化角色起始位置和状态
        self.battle_scene_init()

    # 保存按钮的回调
    def save_callback(self):
        print("save_callback")


imageMgr = ImageMgr()
