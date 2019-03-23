# 系统模块
import time
import random
# 三方模块

# 项目模块
from enums.game_enum import game_enum
from control.actor import Actor, Target
from system.configMgr import configMgr

# 战斗管理器
# set_enemy : 设置敌人
# get_front_target : 获取最近的敌对角色
# actor_move : 角色朝目标移动一个距离
# actor_attack : 对目标进行攻击
# battle_reckon : 战斗计算
# rand_skill : 为角色随机技能
# get_target_obj : 获取目标角色对象
# get_survival_actor : 获取存活角色
# skill_reckon : 计算技能效果
# init_passivity_skill : 初始化被动技能
class BattleMgr():

    def __init__(self):
        player_data = configMgr.player
        self.myself_actor = []      # 自己的角色
        self.match_actor = []       # 对手的角色

        # 载入角色
        actro_arr = player_data["actor"]
        for idx in range(0, len(actro_arr)):
            tmp_id = actro_arr[idx]["id"]
            tmp_lv = actro_arr[idx]["lv"]
            self.myself_actor.append(Actor(tmp_id, tmp_lv))

    # 设置敌人
    # enemy_arr : 敌人数据数组
    def set_enemy(self, enemy_arr):
        # 先把旧数据清空
        self.match_actor = []
        # 载入数据
        for idx in range(0, len(enemy_arr)):
            tmp_id = enemy_arr[idx]["id"]
            tmp_lv = enemy_arr[idx]["lv"]
            self.match_actor.append(Actor(tmp_id, tmp_lv))

    # 获取最近的敌对角色
    # actor : 对应角色
    # 返回对应的目标
    def get_front_target(self, actor):
        # 获取对应的敌方角色数组
        target_arr = []
        target = None
        z_pow = -1
        if actor.camp == game_enum.actor.team:
            target_arr = self.match_actor
        elif actor.camp == game_enum.actor.enemy:
            target_arr = self.myself_actor
        # 遍历寻找最近的敌人
        for tmp_target in target_arr:
            # 判断是否还存活
            if tmp_target.state == game_enum.actor.die:
                continue
            # 获取目标和自己的距离平方
            x_pow = pow(actor.x - tmp_target.x, 2)
            y_pow = pow(actor.y - tmp_target.y, 2)
            # 如果未存在第一个目标
            if z_pow == -1:
                target = tmp_target
                z_pow = x_pow + y_pow
            else:   # 否者替换更近的目标
                if z_pow > (x_pow + y_pow):
                    target = tmp_target
                    z_pow = x_pow + y_pow

        ret_target = Target()
        ret_target.camp = target.camp
        ret_target.id = target.id
        ret_target.x = target.x
        ret_target.y = target.y
        return ret_target

    # 角色朝目标移动一个距离
    # actor : 对应角色
    def actor_move(self, actor):
        i_x = abs(actor.x - actor.target.x)
        i_y = abs(actor.y - actor.target.y)
        move_x = actor.battle_attr.move * i_x/(i_x+i_y)
        move_y = actor.battle_attr.move * i_y/(i_x+i_y)
        # 对是否反向做判断
        if i_x > 0:
            move_x = -1 * move_x
        if i_y > 0:
            move_y = -1 * move_y
        actor.x += move_x
        actor.x += move_y
        actor.set_actor_state(game_enum.actor.stand)
        # 设置下次行动的时间
        actor.next_time += time.time() + configMgr.game["move_interval"]

    # 对目标进行攻击
    # actor : 对应角色
    def actor_attack(self, actor):
        # 如果没有在攻击状态,设置攻击状态,设置使用的技能
        if actor.state != game_enum.actor.attack:
            actor.set_actor_state(game_enum.actor.attack)
            # 设置技能
            self.rand_skill(actor)
        # 如果在攻击索引内，还没到最后一下
        if actor.state_idx < actor.ATTACK_MAX_IDX:
            # 判断目标是否还存活
            target = self.get_target_obj(actor)
            if target.state == game_enum.actor.die:
                actor.set_actor_state(game_enum.actor.stand)
                return
            actor.state_idx += 1
        #　最后一下攻击
        elif actor.state_idx >= actor.ATTACK_MAX_IDX:
            # 状态重置
            actor.set_actor_state(game_enum.actor.stand)
            # 计算技能效果
            self.skill_reckon(actor)

        # 设置下次行动的时间
        actor.next_time += time.time() + 1/actor.speed

    # 战斗计算
    def battle_reckon(self):
        now = time.time()
        # 先进行己方的计算
        for tmp_actor in self.myself_actor:
            # 是否在行动时间,并且角色未死亡
            if tmp_actor.state != game_enum.actor.die and tmp_actor.next_time < now:
                # 如果没有进行攻击，寻找最近的目标
                if tmp_actor.state == game_enum.actor.stand:
                    tmp_actor.target = self.get_front_target(tmp_actor)
                # 如果没有行动目标
                if tmp_actor.target.id == -1:
                    tmp_actor.target = self.get_front_target(tmp_actor)
                # 是否在攻击范围内
                distance = tmp_actor.two_pos_distance(tmp_actor, tmp_actor.target)
                # 在范围内进行攻击
                if pow(tmp_actor.battle_attr.attack_range, 2) >= distance:
                    self.actor_attack(tmp_actor)
                # 不在范围内进行移动,设置状态和下次行动的时间
                else:   
                    self.actor_move(tmp_actor)
        # 进行敌方的计算
        for tmp_actor in self.match_actor:
            # 是否在行动时间,并且角色未死亡
            if tmp_actor.state != game_enum.actor.die and tmp_actor.next_time < now:
                # 如果没有进行攻击，寻找最近的目标
                if tmp_actor.state == game_enum.actor.stand:
                    tmp_actor.target = self.get_front_target(tmp_actor)
                # 如果没有行动目标，寻找最近的目标
                if tmp_actor.target.id == -1:
                    tmp_actor.target = self.get_front_target(tmp_actor)
                # 获取距离
                distance = tmp_actor.two_pos_distance(tmp_actor, tmp_actor.target)
                # 在范围内进行攻击
                if pow(tmp_actor.battle_attr.attack_range, 2) >= distance:
                    self.actor_attack(tmp_actor)
                # 不在范围内进行移动,设置状态和下次行动的时间
                else:
                    self.actor_move(tmp_actor)
        # # 伤害计算完后检查检查是否有角色死亡 （已经在修改生命的时候修改状态了）
        # for tmp_actor in self.myself_actor:
        #     if tmp_actor.battle_attr.hp <= 0:
        #         tmp_actor.set_actor_state(game_enum.actor.die)
        # for tmp_actor in self.match_actor:
        #     if tmp_actor.battle_attr.hp <= 0:
        #         tmp_actor.set_actor_state(game_enum.actor.die)

    # 为角色随机技能
    # actor : 对应角色
    def rand_skill(self, actor):
        skill_id = actor.skill[0].id
        skill_arr = actor.skill
        # 计算权重
        sum_weight = 0
        for tmp_skill in skill_arr:
            sum_weight += tmp_skill.pro
        rand = random.randrange(sum_weight)
        for tmp_skill in skill_arr:
            if rand < tmp_skill.pro:
                skill_id == tmp_skill.id
                break
            else:
                rand -= tmp_skill.pro
        actor.now_skill = skill_id

    # 获取目标角色对象
    # actor : 对应角色
    def get_target_obj(self, actor):
        target = actor.target
        target_arr = []
        target_obj = None
        if actor.camp == game_enum.actor.team:
            target_arr = self.match_actor
        elif actor.camp == game_enum.actor.enemy:
            target_arr = self.myself_actor
        for tmp_target in target_arr:
            if tmp_target.id == target.id:
                target_obj = tmp_target
                break
        return target_obj

    # 获取存活角色
    # actor : 对应角色
    # camp : 获取相对角色而已的队伍, 默认全部, game_enum.actor
    def get_survival_actor(self, actor, camp = "all"):
        obj_arr = []
        actor_arr = []
        # 获取全部存活角色
        if camp == "all":
            actor_arr = self.myself_actor + self.match_actor
        # 获取队友
        elif camp == game_enum.actor.team:
            # 区分本身阵营
            if actor.camp == game_enum.actor.team:
                actor_arr = self.myself_actor
            else:
                actor_arr = self.match_actor
        # 获取敌人
        elif camp == game_enum.actor.enemy:
            # 区分本身阵营
            if actor.camp == game_enum.actor.team:
                actor_arr = self.match_actor
            else:
                actor_arr = self.myself_actor
        # 提取存活的人
        for tmp_actor in actor_arr:
            if tmp_actor.state != game_enum.actor.die:
                obj_arr.append(tmp_actor)
        return obj_arr

    # 计算技能效果
    # actor : 对应角色
    def skill_reckon(self, actor):
        # 查找对应的技能
        skill_id = actor.now_skill
        skill_obj = None
        for tmp_skill in actor.skill:
            if tmp_skill.id == skill_id:
                skill_obj = tmp_skill
        
        # 伤害型(直接造成伤害)
        if skill_obj.m_type == game_enum.skill_type.hurt:
            # 获取存活的作用目标
            acotr_arr = self.get_survival_actor(actor, game_enum.actor.enemy)
            # 计算伤害
            hurt_vlaue = skill_obj.reckon_num(actor)
            # 获取作用目标
            eff_actor = skill_obj.get_eff_actor(acotr_arr)
            # 扣除生命
            for tmp_actor in eff_actor:
                tmp_actor.add_hp(-hurt_vlaue)
        # # 
        # elif skill_obj.m_type == game_enum.skill_type.hurt:

    # 初始化被动技能
    def init_passivity_skill(self):
        # 先初始化队友
        for tmp_actor in self.myself_actor:
            # 遍历技能，是否有
