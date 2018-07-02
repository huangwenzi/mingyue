import sys
sys.path.append("./enum")
from i_enum import enum #包含枚举


#一般 1是普通攻击 2是伤害技能 3是被动技能 4是大招
#使用者：阿五，
class Claw_hit(): 
    def __init__(self):
        self.name = "爪击"                      # 技能名
        self.index = 0                          # 技能索引
        self.explain = "普通的用爪勾一下"        # 说明
        self.minLevel = 1                       # 使用等级
        self.m_type = enum.skill_type.hurt      # 技能类型
        self.target = enum.skill_target.Enemy   # 技能目标
        self.first = enum.skill_first.front     # 优先攻击
        self.Number = 1                         # 目标数量
        self.Multiple = 1                       # 攻击倍率
        self.up_attr = [     # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度
            150,             # 攻击范围
        ]

#使用者:阿五
class Claw_poison() :
    def __init__(self):
        self.name = "毒爪"                      # 技能名
        self.index = 1                          # 技能索引
        self.explain = "爪里有毒"               # 说明
        self.minLevel = 1                       # 使用等级
        self.m_type = enum.skill_type.hurt      # 技能类型
        self.target = enum.skill_target.Enemy   # 技能目标
        self.first = enum.skill_first.front     # 优先攻击
        self.Number = 1                         # 目标数量
        self.Multiple = 2                       # 攻击倍率
        self.up_attr = [     # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度
            150,             # 攻击范围
        ]

#使用者:阿五
class Insight_up() :
    def __init__(self):
        self.name = "洞察提升"                #技能名
        self.index = 2                       #技能索引
        self.explain = "敏锐的洞察，带来更高的伤害和暴击"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.passivity    #技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率
        self.up_attr = [        # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度        
            150,             # 攻击范围
        ]

#使用者:阿五
class Deadly_blow() :
    def __init__(self):
        self.name = "取敌首"                #技能名
        self.index = 3                       #技能索引
        self.explain = "呀，你好像比较厉害哦。（对敌方最高攻击发起一击高伤害）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.hurtHigh    #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 3                    #攻击倍率

#使用者:琪琪
class Despise() :
    def __init__(self):
        self.name = "哼"                    #技能名
        self.index = 4                       #技能索引
        self.explain = "没错，就是鄙视你"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率

#使用者:琪琪
class Despise_rand() :
    def __init__(self):
        self.name = "哼哼"                #技能名
        self.index = 5                       #技能索引
        self.explain = "这次看都不看的鄙视你╭∩╮(︶︿︶)╭∩╮。（因为没有看，所以是随机攻击）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.rand        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 2                    #攻击倍率

#使用者:琪琪
class Flirt() :
    def __init__(self):
        self.name = "招蜂引蝶"                #技能名
        self.index = 6                       #技能索引
        self.explain = "一些莫名其妙的原因，就是受女孩子欢迎，不可抗力。（嘴角上扬的微笑给不受欢迎的人带来更高暴击）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.passivity    #技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率
        self.up_attr = [        # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度        
            150,             # 攻击范围
        ]

#使用者:琪琪
class Deadly_everyone() :
    def __init__(self):
        self.name = "群体嘲讽"                #技能名
        self.index = 7                       #技能索引
        self.explain = "我不是针对你，我只是想说在座的各位，都是。。。（群体伤害）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.whole        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率

#使用者:阿亮
class Chaos_hit() :
    def __init__(self):
        self.name = "混乱打击"                #技能名
        self.index = 8                       #技能索引
        self.explain = "。。。。。。。。（群体随机）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.rand        #优先攻击
        self.Number = 2                        #目标数量
        self.Multiple = 0.5                    #攻击倍率

#使用者:阿亮
class Accurate_hit() :
    def __init__(self):
        self.name = "精准打击"                #技能名
        self.index = 9                       #技能索引
        self.explain = "真的不知道吐槽什么好。。。。。。。。（单体血量最小者）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.hpLow        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 2                    #攻击倍率

#使用者:阿亮
class Deny() :
    def __init__(self):
        self.name = "秘籍：否认三连"                #技能名
        self.index = 10                       #技能索引
        self.explain = "不是我，我没有，别瞎说。 （对即将到来的灾难机智躲避，增加生存几率）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.passivity    #技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率
        self.up_attr = [        # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度        
            150,             # 攻击范围
        ]

#使用者:阿亮
class Double_Accurate_hit() :
    def __init__(self):
        self.name = "精准的混乱打击"                #技能名
        self.index = 11                       #技能索引
        self.explain = "其实就是1 2技能的结合版。。。。。。。。（群体血量最小者）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.hpLow        #优先攻击
        self.Number = 2                        #目标数量
        self.Multiple = 2                    #攻击倍率

#使用者:阿晓
class One_knife() :
    def __init__(self):
        self.name = "一刀"                #技能名
        self.index = 12                       #技能索引
        self.explain = "为什么都是普通攻击我比你们高？请看着我的手臂说话（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1.5                    #攻击倍率

#使用者:阿晓
class Force_knife() :
    def __init__(self):
        self.name = "用力一刀"                #技能名
        self.index = 13                       #技能索引
        self.explain = "还没死，挺能抗的，那我就用点力吧（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 2.5                    #攻击倍率

#使用者:阿晓
class Veteran () :
    def __init__(self):
        self.name = "身经百战"                #技能名
        self.index = 14                       #技能索引
        self.explain = "打架是个锻炼身体的好运动，你也要来一下吗 （整体属性提升）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.change_passivity  # 技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率
        self.condition = enum.skill_condition.hp_down # 被动变化条件
        self.buff_time = 1                  # buff持续时间
        self.up_attr = [        # 被动加成属性
            0, 0,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度        
            150,             # 攻击范围
        ]

#使用者:阿晓
class All_knife() :
    def __init__(self):
        self.name = "全力一刀"                #技能名
        self.index = 15                       #技能索引
        self.explain = "我要用两只手了（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 4                    #攻击倍率

#使用者:牛哥哥
class MyselfHp_up() :
    def __init__(self):
        self.name = "奶一口"                #技能名
        self.index = 16                       #技能索引
        self.explain = "能抗能奶才是好肉盾（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = -1                    #攻击倍率

#使用者:牛哥哥
class TeamHp_up() :
    def __init__(self):
        self.name = "你也要喝吗"                #技能名
        self.index =17                       #技能索引
        self.explain = "有我在，你死不了，但要是我先死了就没办法了（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.team    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = -0.5                #攻击倍率

#使用者:牛哥哥
class Sports_man () :
    def __init__(self):
        self.name = "体育生"                #技能名
        self.index = 18                       #技能索引
        self.explain = "锻炼是个好东西 （属性提升）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.passivity    #技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率
        self.up_attr = [        # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度        
            150,             # 攻击范围
        ]

#使用者:牛哥哥
class AllHp_up() :
    def __init__(self):
        self.name = "奶起来"                #技能名
        self.index = 19                       #技能索引
        self.explain = "哟哟，切克闹，干了这碗热翔，哦不，奶吧（群体回血）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.team        #技能目标
        self.first = enum.skill_first.whole        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = -0.5                #攻击倍率

#使用者:陆半仙
class Defy() :
    def __init__(self):
        self.name = "怜悯"                #技能名
        self.index = 20                       #技能索引
        self.explain = "和我作对是你这辈子最大的错误，但伟大的我给你机会，放弃抵抗吧（对，就是没有伤害那么任性）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 0                    #攻击倍率

#使用者:陆半仙
class One_finger() :
    def __init__(self):
        self.name = "仙人一指"                #技能名
        self.index = 21                       #技能索引
        self.explain = "凡人，这就是我们间的差距（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 3.5                    #攻击倍率

#使用者:路半仙
class Lead_halo () :
    def __init__(self):
        self.name = "主角光环"                #技能名
        self.index = 22                       #技能索引
        self.explain = "我可是第三次世界大战的主角 （全属性大提升）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.passivity    #技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率
        self.up_attr = [        # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度        
            150,             # 攻击范围
        ]

#使用者:陆半仙
class Tai_chi() :
    def __init__(self):
        self.name = "八卦像"                #技能名
        self.index = 23                       #技能索引
        self.explain = "因果律技能（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 6                    #攻击倍率

#使用者:舍长
class Ordinary_knife() :
    def __init__(self):
        self.name = "普通一刀"                #技能名
        self.index = 24                       #技能索引
        self.explain = "只是普普通通的一刀，他是个老实人（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率

#使用者:舍长
class Ordinary_force_knife() :
    def __init__(self):
        self.name = "普通用力一刀"                #技能名
        self.index = 25                       #技能索引
        self.explain = "只是普普通通用力一点的一刀，他真是个老实人（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 2                    #攻击倍率

#使用者:舍长
class Dormitory_head () :
    def __init__(self):
        self.name = "一舍之长"                #技能名
        self.index = 26                       #技能索引
        self.explain = "不把管家技能点满的胖子不是好舍长 （属性提升）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.passivity    #技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率
        self.up_attr = [        # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度        
            150,             # 攻击范围
        ]

#使用者:舍长
class Drunk_knife() :
    def __init__(self):
        self.name = "趁醉一击"                #技能名
        self.index = 27                       #技能索引
        self.explain = "虽然平时是老实人，但喝醉后就不是了，到处破坏（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 4                    #攻击倍率

#使用者:娘炮
class Electric() :
    def __init__(self):
        self.name = "电击"                #技能名
        self.index = 28                       #技能索引
        self.explain = "用电攻击（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率

#使用者:娘炮
class Electric_chain() :
    def __init__(self):
        self.name = "连锁电击"                #技能名
        self.index = 29                       #技能索引
        self.explain = "用电攻击（群体随机）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.rand        #优先攻击
        self.Number = 2                        #目标数量
        self.Multiple = 0.5                    #攻击倍率

#使用者:娘炮
class Knowledge () :
    def __init__(self):
        self.name = "知识就是力量"                #技能名
        self.index = 30                       #技能索引
        self.explain = "我真的很热爱学习的，不信我们讨论一下佐佐木明希，咦，你不知道，那长泽雅美，什么你还不知 （属性提升）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.passivity    #技能类型
        self.target = enum.skill_target.myself    #技能目标
        self.first = enum.skill_first.front        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率
        self.up_attr = [        # 被动加成属性
            200, 200,        # 最大生命值, 生命值
            25,    5,        # 攻击, 防御
            20,    0,        # 暴击, 抗暴
            0.4, 10,         # 攻击速度, 移动速度        
            150,             # 攻击范围
        ]

#使用者:娘炮
class Dark_matter() :
    def __init__(self):
        self.name = "暗物质攻击"                #技能名
        self.index = 31                       #技能索引
        self.explain = "我也不知道起什么名字好（单体）"    #说明
        self.minLevel = 1                    #使用等级
        self.m_type = enum.skill_type.hurt        #技能类型
        self.target = enum.skill_target.Enemy    #技能目标
        self.first = enum.skill_first.whole        #优先攻击
        self.Number = 1                        #目标数量
        self.Multiple = 1                    #攻击倍率

skill_tab = [   # 技能总表
    Claw_hit(), Claw_poison(), Insight_up(), Deadly_blow(),             # 0:爪击 1:毒爪 2:洞察提升 3:取敌首
    Despise(), Despise_rand(), Flirt(), Deadly_everyone(),              # 4:哼 5:哼哼 6:招蜂引蝶 7:群体嘲讽
    Chaos_hit(), Accurate_hit(), Deny(), Double_Accurate_hit(),         # 8:混乱打击 9:精准打击 10:秘籍：否认三连 11:精准的混乱打击
    One_knife(), Force_knife(), Veteran(), All_knife(),                 # 12:一刀 13:用力一刀 14:身经百战 15:全力一刀
    MyselfHp_up(), TeamHp_up(), Sports_man(), AllHp_up(),               # 16:奶一口 17:你也要喝吗 18:体育生 19:奶起来
    Defy(), One_finger(), Lead_halo(), Tai_chi(),                       # 20:怜悯 21:仙人一指 22:主角光环 23:八卦像
    Ordinary_knife(), Ordinary_force_knife(), Dormitory_head(), Drunk_knife(),# 24:普通一刀 25:普通用力一刀 26:一舍之长 27:趁醉一击
    Electric(), Electric_chain(), Knowledge(), Dark_matter(),           # 28:电击 29:连锁电击 30:知识就是力量 31:暗物质攻击
]
