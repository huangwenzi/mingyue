#阿晓的角色属性

import sys
import skill  # 技能


class Actor():
    def __init__(self):
        self.name = "阿晓"      # 名字
        self.index = 4          # 角色索引
        self.introduce = "null" # 介绍
        self.location = "射手"  # 定位
        self.self_attr = [      # 展示属性
            200, 200,           # 最大生命值, 生命值
            25,    5,           # 攻击, 防御
            20,    0,           # 暴击, 抗暴
            0.4, 10,            # 攻击速度, 移动速度
            150,                # 攻击范围
        ]
        self.battle_attr = None # 战斗属性
        self.growUp = [      # 成长
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度
            150,             # 攻击范围
        ]
        self.skill = [[16, 50], [17, 30], [18, 0], [19, 20], ]  # 技能 [技能id, 释放概率]
        self.share_attr = None  # 共有属性，角色创建时赋值
        self.buff = []       # 身上的buff [[结束时间，属性列表],[结束时间，属性列表],......]