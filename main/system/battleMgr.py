# 系统模块
import time
# 三方模块

# 项目模块
from enums.game_enum import game_enum


# 战斗管理器
class BattleMgr():

    def __init__(self):
        self.myself_actor = []      # 自己的角色
        self.match_actop = []       # 对手的角色