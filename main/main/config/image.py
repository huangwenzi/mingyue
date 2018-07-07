# 图片资源配置文件
import sys
sys.path.append("./enum")

from i_enum import enum



# 角色图片资源的配置
# team 敌我 0:队友 1:敌人
# actor_index角色索引
# state 状态 0:待命 1:攻击
# index 索引
# [地址][缩放]
actor_image = [
    [   # 0 team 队友
        [   # 0 阿五
            [   # 0 待命
                ["FineArts/actor/actor_0/i_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_0/i_1_0.png", [100,110], ],
                ["FineArts/actor/actor_0/i_1_1.png", [100,110], ],
            ],
        ],

        [   # 1 琪琪
            [   # 0 待命
                ["FineArts/actor/actor_1/i_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_1/i_1_0.png", [100,110], ],
                ["FineArts/actor/actor_1/i_1_1.png", [100,110], ],
            ],
        ],

        [   # 2 阿亮
            [   # 0 待命
                ["FineArts/actor/actor_2/i_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_2/i_1_0.png", [100,110], ],
                ["FineArts/actor/actor_2/i_1_1.png", [100,110], ],
            ],
        ],

        [   # 3 阿晓
            [   # 0 待命
                ["FineArts/actor/actor_3/i_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_3/i_1_0.png", [100,110], ],
                ["FineArts/actor/actor_3/i_1_1.png", [100,110], ],
            ],
        ],

         [   # 4 牛哥哥
            [   # 0 待命
                ["FineArts/actor/actor_4/i_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_4/i_1_0.png", [100,110], ],
                ["FineArts/actor/actor_4/i_1_1.png", [100,110], ],
            ],
        ],

        [   # 5 陆半仙
            [   # 0 待命
                ["FineArts/actor/actor_5/i_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_5/i_1_0.png", [100,110], ],
                ["FineArts/actor/actor_5/i_1_1.png", [100,110], ],
            ],
        ],

         [   # 6 舍长
            [   # 0 待命
                ["FineArts/actor/actor_6/i_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_6/i_1_0.png", [100,110], ],
                ["FineArts/actor/actor_6/i_1_1.png", [100,110], ],
            ],
        ],

         [   # 7 娘炮
            [   # 0 待命
                ["FineArts/actor/actor_7/i_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_7/i_1_0.png", [100,110], ],
                ["FineArts/actor/actor_7/i_1_1.png", [100,110], ],
            ],
        ],
    ],
    
    [   # 1 enemy 敌对
        [   # 0 阿五
            [   # 0 待命
                ["FineArts/actor/actor_0/d_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_0/d_1_0.png", [100,110], ],
                ["FineArts/actor/actor_0/d_1_1.png", [100,110], ],
            ],
        ],

        [   # 1 琪琪
            [   # 0 待命
                ["FineArts/actor/actor_1/d_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_1/d_1_0.png", [100,110], ],
                ["FineArts/actor/actor_1/d_1_1.png", [100,110], ],
            ],
        ],

        [   # 2 阿亮
            [   # 0 待命
                ["FineArts/actor/actor_2/d_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_2/d_1_0.png", [100,110], ],
                ["FineArts/actor/actor_2/d_1_1.png", [100,110], ],
            ],
        ],

        [   # 3 阿晓
            [   # 0 待命
                ["FineArts/actor/actor_3/d_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_3/d_1_0.png", [100,110], ],
                ["FineArts/actor/actor_3/d_1_1.png", [100,110], ],
            ],
        ],

         [   # 4 牛哥哥
            [   # 0 待命
                ["FineArts/actor/actor_4/d_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_4/d_1_0.png", [100,110], ],
                ["FineArts/actor/actor_4/d_1_1.png", [100,110], ],
            ],
        ],

        [   # 5 陆半仙
            [   # 0 待命
                ["FineArts/actor/actor_5/d_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_5/d_1_0.png", [100,110], ],
                ["FineArts/actor/actor_5/d_1_1.png", [100,110], ],
            ],
        ],

         [   # 6 舍长
            [   # 0 待命
                ["FineArts/actor/actor_6/d_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_6/d_1_0.png", [100,110], ],
                ["FineArts/actor/actor_6/d_1_1.png", [100,110], ],
            ],
        ],

         [   # 7 娘炮
            [   # 0 待命
                ["FineArts/actor/actor_7/d_0_0.png", [100,110], ],
            ],
            [   # 1 攻击
                ["FineArts/actor/actor_7/d_1_0.png", [100,110], ],
                ["FineArts/actor/actor_7/d_1_1.png", [100,110], ],
            ],
        ],
    ],
]

# 技能图片资源的配置
# 技能id
# [地址][缩放]
skill_image = [
    ["FineArts/skill/skill_0.png", [100,110], ], # 0
    ["FineArts/skill/skill_1.png", [100,110], ], # 1
    ["FineArts/skill/skill_2.png", [100,110], ], # 2
    ["FineArts/skill/skill_3.png", [100,110], ], # 3
    ["FineArts/skill/skill_4.png", [100,110], ], # 4
    ["FineArts/skill/skill_5.png", [100,110], ], # 5
    ["FineArts/skill/skill_6.png", [100,110], ], # 6
    ["FineArts/skill/skill_7.png", [100,110], ], # 7
    ["FineArts/skill/skill_8.png", [100,110], ], # 8
    ["FineArts/skill/skill_9.png", [100,110], ], # 9
    ["FineArts/skill/skill_10.png", [100,110], ], # 10
    ["FineArts/skill/skill_11.png", [100,110], ], # 11
    ["FineArts/skill/skill_12.png", [100,110], ], # 12
    ["FineArts/skill/skill_13.png", [100,110], ], # 13
    ["FineArts/skill/skill_14.png", [100,110], ], # 14
    ["FineArts/skill/skill_15.png", [100,110], ], # 15
    ["FineArts/skill/skill_16.png", [100,110], ], # 16
    ["FineArts/skill/skill_17.png", [100,110], ], # 17
    ["FineArts/skill/skill_18.png", [100,110], ], # 18
    ["FineArts/skill/skill_19.png", [100,110], ], # 19
    ["FineArts/skill/skill_20.png", [100,110], ], # 20
    ["FineArts/skill/skill_21.png", [100,110], ], # 21
    ["FineArts/skill/skill_22.png", [100,110], ], # 22
    ["FineArts/skill/skill_23.png", [100,110], ], # 23
    ["FineArts/skill/skill_24.png", [100,110], ], # 24
    ["FineArts/skill/skill_25.png", [100,110], ], # 25
    ["FineArts/skill/skill_26.png", [100,110], ], # 26
    ["FineArts/skill/skill_27.png", [100,110], ], # 27
    ["FineArts/skill/skill_28.png", [100,110], ], # 28
    ["FineArts/skill/skill_29.png", [100,110], ], # 29
    ["FineArts/skill/skill_30.png", [100,110], ], # 30
    ["FineArts/skill/skill_31.png", [100,110], ], # 31 
]

# 场景图片资源配置
# index 图片索引
# 图片地址
screen_image = [
    ["FineArts/screen/0.jpg",],   
    ["FineArts/screen/1.jpg",],
]

# 视图图片资源配置
# index 图片索引
# 图片索引[类型，id]，缩放[宽，高], 绘制位置[x,y], 视图名, 视图索引(为-1表示没有下一视图)
view_image = [
    [   # 0 : 主界面
	    ["./FineArts/parts/角色.png", [100, 100], [0, 0],   "角色", enum.image.view_actor],
	    ["./FineArts/parts/背包.png", [100, 100], [100, 0], "背包", enum.image.view_bag],
	    ["./FineArts/parts/战斗.png", [100, 100], [200, 0], "战斗", enum.image.view_battle],
	    ["./FineArts/parts/阵型.png", [100, 100], [300, 0], "阵型", enum.image.view_formation],
	    ["./FineArts/parts/保存.png", [100, 100], [400, 0], "保存", enum.image.view_sava],
    ],

    # [   # 1 : 角色

    # ],

    # [   # 2 : 背包

    # ],

    # [   # 3 : 战斗

    # ],

    # [   # 4 : 阵型

    # ],

    # [   # 5 : 保存

    # ],

]
