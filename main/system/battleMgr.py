# 系统模块
import time
# 三方模块

# 项目模块
from enums.game_enum import game_enum
from control.actor import Actor, Target
from system.configMgr import configMgr

# 战斗管理器


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
    # 要查询的角色
    # 返回对应的目类
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

    # 计算返回两个点的直线距离平方
    # pos_0 : [x, y]
    # pos_1 : [x, y]
    def two_pos_distance(self, pos_0, pos_1):
        return pow(pos_0[0] - pos_1[0], 2) + pow(pos_0[1] - pos_1[1], 2)

    # 角色朝目标移动一个距离
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
        actor.state = game_enum.actor.stand
        actor.next_time += time.time() + 1/configMgr.game["frames"]