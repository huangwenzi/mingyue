


#______________________________事件使用
#部件点击事件
class Parts_event():
    next = 0    #可替换当前的部件索引
    show = 1    #展示信息
    func = 2    #执行对应的函数

#_______________________________技能使用
#技能类型
class Skill_type():
	hurt = 1         # 伤害型
	passivity = 2    # 被动型
	curse = 3        # 增减益型

#技能目标
class Skill_target():
	myself = 1      # 自身
	team = 2        # 团队
	Enemy = 3       # 敌人
	#everyone = 4	#不分敌我(暂不支持)

#优先攻击
class Skill_first():
	rand = 1  # 随机
	hpHigh = 2  # 生命高
	hpLow = 3  # 生命低
	hurtHigh = 4  # 攻击高
	speedHigh = 5  # 速度高
	defenseHigh = 6  # 防御高
	front = 8  # 最近
	back = 9  # 最远
	whole = 10  # 全体

#_______________________________属性使用
#属性类型
class Attr_type():
    MaxHp =     0  # 最大生命值
    hp =        1  # 生命值
    attack =    2  # 攻击
    defense =   3  # 防御
    Violent =   4  # 暴击
    speed =     5  # 攻击速度
    move =      6  # 移动速度
    attack_range = 7  # 攻击范围

#_______________________________待机状态
class State():
    normal = 1      # 待命
    battle = 2      # 战斗

#_______________________________图片
class Image():
    #type图片类型
    icon = "icon"
    item = "item"
    
    #actor图片枚举
    wait = 1        # 等待
    battle = 2      # 战斗

    skill = 4       # 技能

#_______________________________角色
class Actor():
    wait = 1        # 等待
    battle = 2      # 战斗
    battle = 2      # 技能

    team = 'i'      # 队友
    enemy = 'd'     # 敌人

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
    #____________图片
    image = Image()


enum = Enum()   # 实例化枚举
