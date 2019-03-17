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
            "FineArts/png/背景/平常背景图.jpg")    # 平常背景图片
        self.battle_image_list = []  # 战斗图像列表 (注意列表的顺序代表z轴)
        self.battle_background = pygame.image.load(
            "FineArts/png/背景/战斗背景图.jpg")    # 战斗背景图片
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
        self.add_normal_image("FineArts/png/界面/战斗.png", "fight",
                              [0, 0], game_enum.iamge_type.button, self.fight_callback)
        self.add_normal_image("FineArts/png/界面/保存.png", "save",
                              [50, 0], game_enum.iamge_type.button, self.save_callback)

    # 绘制刷新界面
    def blit_image(self):
        # 是否到了刷新时间
        now_time = time.time()
        if self.last_time + 1/self.frames > now_time:
            return

        self.last_time = now_time
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
            # 绘制子级图像
            for tmp_image in self.battle_image_list:
                tmp_image.blit_image()

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
                # 找到图像，并且回调存在
                if ret == True and obj.name in self.image_callback:
                    self.image_callback[obj.name]()
                    return

    # 添加一个图像
    # path : 图像资源地址
    # name : 名字
    # postion : 位置
    # tmp_type : 图像资源类型
    # callback : 回调函数

    def add_normal_image(self, path, name, postion, tmp_type, callback):
        # 添加图像到列表
        tmp_image = Image(self, path, name, tmp_type)
        tmp_image.x = postion[0]
        tmp_image.y = postion[1]
        self.normal_image_list.append(tmp_image)
        self.image_callback[name] = callback

    # 加载战斗中需要用到的角色资源
    def load_battle_image(self):
        self.battle_image_list = []
        battle_image_list = self.battle_image_list
        actor_path = "FineArts/actor"
        # 加载己方的资源
        myself_actor = self.battleMgr.myself_actor
        for tmp_actor in myself_actor:
            # 加载站立资源
            id_str = "actor_" + str(tmp_actor.id)
            action_str = "i_stand"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + action_str
            tmp_image = Image(self, actor_path_str, image_name, "actor", [0,0])
            battle_image_list[image_name] = tmp_image
            # 加载攻击资源
            id_str = "actor_" + str(tmp_actor.id)
            action_str = "i_0"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + action_str
            tmp_image = Image(self, actor_path_str, image_name, "actor", [0,0])
            battle_image_list[image_name] = tmp_image
            id_str = "actor_" + str(tmp_actor.id)
            action_str = "i_1"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + action_str
            tmp_image = Image(self, actor_path_str, image_name, "actor", [0,0])
            battle_image_list[image_name] = tmp_image
            # 加载要用到的技能资源
            skill_path = "FineArts/skill"
            skill = tmp_actor.skill
            for tmp_skill in skill:
                id_str = "skill_" + str(tmp_skill.id)
                skill_path_str = skill_path + "/" + id_str + ".png"
                tmp_image = Image(self, skill_path_str, id_str, "skill", [0,0])
                battle_image_list[id_str] = tmp_image
        # 加载对手的资源
        match_actor = self.battleMgr.match_actor
        for tmp_actor in match_actor:
            # 加载站立资源
            id_str = "actor_" + str(tmp_actor.id)
            action_str = "d_stand"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + action_str
            tmp_image = Image(self, actor_path_str, image_name, "actor", [0,0])
            battle_image_list[image_name] = tmp_image
            # 加载攻击资源
            id_str = "actor_" + str(tmp_actor.id)
            action_str = "d_0"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + action_str
            tmp_image = Image(self, actor_path_str, image_name, "actor", [0,0])
            battle_image_list[image_name] = tmp_image
            id_str = "actor_" + str(tmp_actor.id)
            action_str = "d_1"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + action_str
            tmp_image = Image(self, actor_path_str, image_name, "actor", [0,0])
            battle_image_list[image_name] = tmp_image
            # 加载要用到的技能资源
            skill_path = "FineArts/skill"
            skill = tmp_actor.skill
            for tmp_skill in skill:
                id_str = "skill_" + str(tmp_skill.id)
                skill_path_str = skill_path + "/" + id_str + ".png"
                tmp_image = Image(self, skill_path_str, id_str, "skill", [0,0])
                battle_image_list[id_str] = tmp_image

    # 战斗按钮的回调
    def fight_callback(self):
        print("fight_callback")
        # 设置战斗状态
        self.state = game_enum.state.battle
        # 设置战斗对手
        enemy_arr = [{"id":4,"lv":10},{"id":5,"lv":10},{"id":6,"lv":10},{"id":7,"lv":10}]
        self.battleMgr.set_enemy(enemy_arr)
        # 加载战斗中可能需要的图像资源
        self.load_battle_image()


    # 保存按钮的回调
    def save_callback(self):
        print("save_callback")


imageMgr = ImageMgr()
