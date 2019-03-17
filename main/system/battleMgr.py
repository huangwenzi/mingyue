# 系统模块
import time
# 三方模块

# 项目模块
from enums.game_enum import game_enum
from control.actor import Actor
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
    # enemy : 敌人数据
    def set_enemy(self, enemy_arr):
        # 先把旧数据清空
        self.match_actor = []
        # 载入数据
        for idx in range(0, len(enemy_arr)):
            tmp_id = enemy_arr[idx]["id"]
            tmp_lv = enemy_arr[idx]["lv"]
            self.match_actor.append(Actor(tmp_id, tmp_lv))

    