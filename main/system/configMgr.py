# 系统模块
import time
import json
# 三方模块

# 项目模块
        # 读取数据

# 配置管理器
class ConfigMgr():

    # 初始化各个要加载的配置文件
    def __init__(self):
        self.game = self.load_config("config/game.json")        # 游戏配置
        self.player = self.load_config("config/player.json")    # 玩家配置
        self.actor = self.load_config("config/actor.json")      # 角色配置
        self.skill = self.load_config("config/skill.json")      # 技能配置
        
    # 加载json
    # path : 要加载的文件地址
    def load_config(self, path):
        path = "main/" + path
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return json.load(f)

configMgr = ConfigMgr()