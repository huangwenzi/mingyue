# 系统模块
import time
# 三方模块
import pygame
# 项目模块
from control.mouse import Mouse
from control.image import Image
from enums.game_enum import game_enum
from system.battleMgr import BattleMgr
from system.configMgr import configMgr

# 图像管理器
# blit_image : 绘制刷新界面
# mouse_event : 鼠标事件
# add_normal_image : 添加一个图像
# load_actor_image : 加载角色资源
# load_battle_image : 加载战斗中需要用到的角色资源
# battle_scene_init : 战斗场景初始化
# battle_reckon : 战斗过程计算
# blit_skill : 绘制角色的技能
# blit_skill : 在界面上绘制角色
# blit_battle : 战斗绘制
# fight_callback : 战斗按钮的回调
# save_callback : 保存按钮的回调
class ImageMgr():

    def __init__(self):
        # 基本设置
        self.next_time = 0          # 下次刷新的时间
        self.frames = configMgr.game["frames"]         # 帧数
        self.normal_image_list = []  # 平常图像列表 (注意列表的顺序代表z轴)
        self.normal_background = pygame.image.load(
            "main/FineArts/png/背景/平常背景图.jpg")    # 平常背景图片
        self.battle_image_dict = {}  # 战斗图像字典 (战斗的绘制不同于平常图像)
        self.battle_background = pygame.image.load(
            "main/FineArts/png/背景/战斗背景图.jpg")    # 战斗背景图片
        self.image_callback = {}    # 图像资源对应的回调函数
        self.width = self.normal_background.get_width()    # 图像宽度
        self.height = self.normal_background.get_height()  # 图像高度
        self.image = pygame.display.set_mode((self.width, 600))    # 设置窗体
        # self.image = pygame.display.set_mode((1, 1))    # 设置窗体
        # print(pygame.font.get_fonts())    # 打印可以用的字体
        pygame.font.init()
        self.font = pygame.font.SysFont(configMgr.game["font"], configMgr.game["font_size"])    # 设置字体
        self.font_color = configMgr.game["font_color"]      # 字体颜色
        self.bar_color = (0, 100, 0)        # 血条颜色
        self.x = 0
        self.y = 0
        self.state = game_enum.state.wati  # 当前场景状态

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
        if now_time < self.next_time:
            return

        self.next_time = now_time + 1/self.frames
        # 区分战斗和平常状态下的界面
        if self.state == game_enum.state.wati:    # 平常界面绘制
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

    # 加载角色资源
    # actor_arr : 角色数组
    def load_actor_image(self, actor_arr):
        battle_image_dict = self.battle_image_dict
        actor_path = "main/FineArts/actor"
        skill_path = "main/FineArts/skill"
        for tmp_actor in actor_arr:
            # 加载站立图像资源
            id_str = "actor_" + str(tmp_actor.id)
            action_str = tmp_actor.camp + "_stand_0"
            actor_path_str = actor_path + "/" + id_str + "/" + action_str + ".png"
            image_name = id_str + "_" + action_str
            tmp_image = Image(self, actor_path_str,
                              image_name, game_enum.iamge_type.actor, [0, 0])
            battle_image_dict[image_name] = tmp_image
            # 加载攻击图像资源
            id_str = "actor_" + str(tmp_actor.id)
            for idx in range(0, 2):
                action_str = tmp_actor.camp + "_attack_" + str(idx)
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

    # 加载战斗中需要用到的角色资源
    # 加载的资源命名规则
    # 角色 : actor_(actor_id)_(敌我标识)_(状态标识)_(状态序列号)
    # 技能 : skill_(skill_id)
    def load_battle_image(self):
        # 先清空旧数据(战斗结束也清一下，这里再清一遍)
        # 清空战斗图像资源
        self.battle_image_dict = {}
        self.load_actor_image(self.battleMgr.myself_actor)
        self.load_actor_image(self.battleMgr.match_actor)
    
    # 战斗场景初始化
    def battle_scene_init(self):
        # 初始化己方位置状态
        myself_actor = self.battleMgr.myself_actor
        count = 0   # 当前是第几个排序的角色，用于设置位置
        for tmp_actor in myself_actor:
            tmp_actor.x = (count//4 + 1) * 50
            tmp_actor.y = (count% 4 + 1) * 100 + 50
            tmp_actor.camp = game_enum.actor.team
            self.last_time = time.time()
            tmp_actor.set_actor_state(game_enum.actor.stand)
            count += 1
        # 初始化敌方位置状态
        match_actor = self.battleMgr.match_actor
        count = 0   # 当前是第几个排序的角色，用于设置位置
        for tmp_actor in match_actor:
            tmp_actor.x = self.width - (count//4 + 1) * 50
            tmp_actor.y = (count% 4 + 1) * 100 + 50
            tmp_actor.camp = game_enum.actor.enemy
            self.last_time = time.time()
            tmp_actor.set_actor_state(game_enum.actor.stand)
            count += 1
        # 初始化当前属性
        for tmp_actor in myself_actor:
            tmp_actor.init_now_attr()
        for tmp_actor in match_actor:
            tmp_actor.init_now_attr()
        # 初始化被动技能
        self.battleMgr.init_passivity_skill()
        # 初始化战斗属性
        for tmp_actor in myself_actor:
            tmp_actor.init_battle_attr()
        for tmp_actor in match_actor:
            tmp_actor.init_battle_attr()

    # 战斗过程计算
    def battle_reckon(self):
        if self.state != game_enum.state.battle:
            return
        self.battleMgr.battle_reckon()

    # 绘制角色的技能
    # actor : 对应的角色
    def blit_skill(self, actor):
        skill_name = actor.get_skill_image_name()
        skill_range = actor.skill_range
        image = self.battle_image_dict[skill_name].image
        # 根据技能类型绘制技能图像资源
        # 根据角色数量
        if skill_range.m_type == game_enum.skill.actor_num:
            for tmp_actor in skill_range.actor_arr:
                self.image.blit(image, (tmp_actor.x, tmp_actor.y))
        # 根据角色范围
        elif skill_range.m_type == game_enum.skill.actor_range:
            # 以第一个角色为中心点
            tmp_actor = skill_range.actor_arr[0]
            self.image.blit(image, (tmp_actor.x, tmp_actor.y))

    # 在界面上绘制角色
    # actor_arr : 要绘制的角色数组
    def blit_acotr_arr(self, actor_arr):
        for tmp_actor in actor_arr:
            # 已经死亡的不绘制
            if tmp_actor.state == game_enum.actor.die:
                return
            image_name = tmp_actor.get_actor_image_name()
            # 如果是站立和移动状态，只需要绘制角色就好了(移动还没有，后面再出对应图像)
            self.image.blit(self.battle_image_dict[image_name].image, (tmp_actor.x, tmp_actor.y))
            # 战斗并且是最后一下，还需要绘制技能
            if tmp_actor.state == game_enum.actor.attack and tmp_actor.state_idx == tmp_actor.ATTACK_MAX_IDX:
                self.blit_skill(tmp_actor)
            #绘制名字
            name = self.font.render(tmp_actor.name,1,self.font_color)
            self.image.blit(name, (tmp_actor.x - 50, tmp_actor.y - 115))
            #绘制生命框
            pygame.draw.rect(self.image, self.font_color, (tmp_actor.x - 50, tmp_actor.y - 100, 90, 16), 3)#生命条外框
            hpX = tmp_actor.battle_attr.hp/tmp_actor.now_attr.hp    #计算生命值长度
            pygame.draw.rect(self.image, self.bar_color, (tmp_actor.x - 47, tmp_actor.y - 97, hpX * 84, 10), )#剩余生命值
            hp_number = self.font.render('%.1f' % (tmp_actor.battle_attr.hp), True, self.font_color)  # 生命值数值
            self.image.blit(hp_number, (tmp_actor.x - 30, tmp_actor.y - 100))

    # 战斗绘制
    def blit_battle(self):
        self.blit_acotr_arr(self.battleMgr.myself_actor)
        self.blit_acotr_arr(self.battleMgr.match_actor)
        
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
