
import pygame

#配置
#_________________________图片配置
# 场景
class Screen():
    screen_size = [720, 800]# 场景尺寸

# 角色的图片
class Actor_image():
    actor_size = [100, 110] # 角色的尺寸
    battle_count = 4        # 战斗图片帧数

# 生命条
class Hp_bar():
    bar_color = (0, 100, 0) # 血条颜色
    width = 90              # 宽度
    height = 16             # 高度

#__________________________绘图配置
# 字体
class Font():
    font = pygame.font.SysFont('SimHei', 16)# 字体
    font_color = (0, 0, 0)          # 字体颜色

#__________________________角色配置
class Actor():
    Max_row = 5             # 行数
    Max_col = 5             # 列数
    actor_space = 120       # 角色间的间隔
    x_aline = 50            # 校准
    y_aline = 300           
    move_time = 0.1         # 移动的间隔时间
    attack_time = 0.2       # 攻击的时间间隔（额外添加的）
    defense_coefficient = 1 # 防御系数
    team = 0                # 队友
    enemy = 1               # 敌人


#___________________________技能配置
class Skill():
    count = 4               # 每个角色的技能数量
    image_time = 1          # 技能特效持续时间


#总的配置
class Config():
    screen = Screen()               # 场景
    actor_image = Actor_image()     # 图片配置
    hp_bar = Hp_bar()               # 生命条
    font = Font()                   # 字体
    actor = Actor()                 # 角色
    skill = Skill()                 # 技能

config = Config()   #s实例化
