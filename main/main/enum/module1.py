

#______________________________事件使用
#部件点击事件
class Parts_event():
    next = 0  # 可替换当前的部件索引
    show = 1  # 展示信息
    func = 2  # 执行对应的函数

#_______________________________技能使用
#技能类型


class Skill_type():
    hurt = 1            # 伤害型
    passivity = 2       # 永久被动型
    change_passivity = 3  # 变动被动型
    curse = 4           # 增减益型

#技能目标


class Skill_target():
    myself = 1      # 自身
    team = 2        # 团队
    Enemy = 3       # 敌人
    #everyone = 4   # 不分敌我(暂不支持)

#优先攻击


class Skill_first():
    front = 1       # 最近
    rand = 2        # 随机
    hp_high = 3     # 生命高
    hp_low = 4      # 生命低
    hurt_high = 5   # 攻击高
    speed_high = 6  # 攻击速度高
    back = 7        # 最远
    whole = 8       # 全体

# 被动变化条件


class Skill_condition(object):
    hp_down = 0     # 生命下降


#_______________________________属性使用
#属性类型
class Attr_type():
    MaxHp = 0  # 最大生命值
    hp = 1  # 生命值
    attack = 2  # 攻击
    defense = 3  # 防御
    violent = 4  # 暴击
    antiriot = 5  # 抗暴
    speed = 6  # 攻击速度
    move = 7  # 移动速度
    attack_range = 8  # 攻击范围

# buff


class Buff_type(object):
    one = 0        # 一次计算   （添加buff时对属性计算一次）
    heap = 1       # 叠加计算   （每个回合叠加一次）

#_______________________________待机状态


class State():
    normal = 1      # 待命
    battle = 2      # 战斗

#_______________________________图片


class Image():
    # type图片类型
    icon = "icon"
    item = "item"

    # 视图类型
    view_main           # 主视图
    view_actor = 1      # 角色
    view_bag = 2        # 背包
    view_battle = 3     # 战斗
    view_formation = 4  # 阵型
    view_sava = 5       # 保存

    # actor图片资源枚举
    # 队伍
    team = 0      # 队友
    enemy = 1     # 敌人
    #状态
    wait = 0        # 待命
    battle = 1      # 战斗

#_______________________________角色


class Actor():
    # 状态
    wait = 1        # 待命
    battle = 2      # 战斗
    battle = 2      # 技能

    # 队伍
    team = 0        # 队友
    enemy = 1       # 敌人

    # 存活
    live = 0        # 生存
    die = 1         # 死亡


#所有的枚举放这里
class Enum():
    #————————————事件使用
    parts_event = Parts_event()     # 部件点击事件
    #————————————技能使用
    skill_type = Skill_type()       # 技能类型
    skill_target = Skill_target()   # 技能目标
    skill_first = Skill_first()     # 优先攻击
    #____________属性使用
    attr_type = Attr_type()         # 属性类型
    state = State()                 # 待机状态
    skill_condition = Skill_condition()
    #____________图片
    image = Image()
    #____________角色
    actor = Actor()  # 角色枚举


enum = Enum()   # 实例化枚举
