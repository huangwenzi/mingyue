
# _______________________________场景使用
# 鼠标键盘
class Mouse():
    click_free = 0  # 鼠标空闲
    click_down = 1  # 鼠标按下
    click_open = 2  # 鼠标放开

# 图像类型
class Iamge_type():
    button = 0      # 按钮(点击有对应的功能)
    actor = 1      # 角色
    skill = 2      # 技能

# _______________________________技能使用
# 技能类型
class Skill():
    hurt = "hurt"               # 伤害型(直接造成伤害)
    passivity = "passivity"     # 永久被动型(一直提升属性)
    change_passivity = "change_passivity"  # 变动被动型(根据当前属性修改参数)
    curse = "curse"             # 增减益型(添加属性，不可叠加)
    curse_add = "curse_add"     # 增减益型(添加属性，可叠加)
    Continued = "Continued"     # 持续型(添加属性，不可叠加，每个攻击间隔添加)
# 技能目标
    myself = "myself"      # 自身
    team = "team"        # 团队
    enemy = "enemy"       # 敌人
    # everyone = 3   # 不分敌我(暂不支持)
# 优先作用目标
    front = "front"         # 最近
    rand = "rand"           # 随机
    hp_high = "hp_high"     # 生命高
    hp_low = "hp_low"       # 生命低
    attack_high = "attack_high" # 攻击高
    speed_high = "speed_high"  # 攻击速度高
    back = "back"           # 最远
    whole = "whole"         # 全体
# 加成基于
    lv = "lv"       # 玩家等级
    attr = "attr"   # 玩家属性
# 技能范围类型
    actor_num = "actor_num"         # 玩家数量
    actor_range = "actor_range"     # 目标范围

# 被动变化条件(暂未加入)
class Skill_condition(object):
    hp_down = 0     # 生命下降


# _______________________________属性使用
# 属性类型
class Attr():
    hp = "hp"               # 生命值
    attack = "attack"       # 攻击
    attack_def = "attack_def"  # 防御
    magic = "magic"         # 法功
    magic_def = "magic_def" # 法防
    violent = "violent"     # 暴击
    antiriot = "antiriot"   # 抗暴
    speed = "speed"         # 攻击速度
    move = "move"           # 移动速度
    attack_range = "attack_range"  # 攻击范围

# buff
class Buff_type(object):
    one = 0        # 一次计算   （添加buff时对属性计算一次）
    heap = 1       # 叠加计算   （每个回合叠加一次）

# _______________________________待机状态
class State():
    wati = "wati"      # 待命
    battle = "battle"  # 战斗
    over = "over"  # 战斗结束

# _______________________________角色
# 定位
class Actor():
    adc = "adc"         # 射手
    ad = "ad"           # 战士
    ap = "ap"           # 法师
    tank = "tank"       # 坦克
    fz = "fz"           # 辅助
    ass = "ass"         # 刺客
# 状态
    stand = "stand"        # 站立
    attack = "attack"      # 攻击
    die = "die"            # 死亡
# 队伍
    team = "i"        # 队友
    enemy = "d"       # 敌人

# 所有的枚举放这里
class Game_enum():
    # ____________场景
    mouse = Mouse()                 # 输入
    iamge_type = Iamge_type()       # 图像类型
    # ————————————技能
    skill = Skill()       # 技能
    # ____________属性
    attr = Attr()         # 属性类型
    state = State()                 # 待机状态
    skill_condition = Skill_condition()
    # ____________角色
    actor = Actor()                 # 角色枚举

game_enum = Game_enum()   # 实例化枚举
