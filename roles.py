# -*- coding: utf-8 -*-
import math
import random


class Role(object):
    """
    basic role class

    """
    blood = 100     
    arrow = 0       
    shield = 0      
    speed = 0       
    name0 = ''      
    role_members_num = 0 
    hitting_accuracy = 100 # hit rate
    # silent = False # 沉默状态标识
    # block = False  # 攻击封禁状态标识

    def __init__(self, arrow, shield, speed, name0, role_member):
        self.arrow = arrow
        self.shield = shield
        self.speed = speed
        self.name0 = name0
        self.role_member = role_member

    def normal_attack(self, role):
        """normal attack which has been considered of hit rate
         @:param role: the role to be attacked
        """
        damage = self.arrow - role.shield
        if random.randint(1, 10000) < self.hitting_accuracy * 100:
            role.under_attack(damage)

    def under_attack(self, damage, fire = 0):
        """self under attack, cause blood reducing
         @:param damage: physical damage
         @:param fire: element damage
        """
        if damage <= 0:
            damage = 0
        if fire <= 0:
            fire = 0
        self.blood = self.blood - damage - fire


class JiZi(Role):
    """
    姬子
    """
    def __init__(self):
        super().__init__(23, 9, 12, '姬子', 1)

    def attack(self, role, curr_round):
        """self attack role
         @:param role: the role will be attacked
         @:param curr_round: current round
        """
        self.love_never_die(role)
        self.cheer_friends(curr_round)
        self.normal_attack(role)

    def can_attack(self):
        """ tell whether I can attack
        TODO
        """
        return True

    def love_never_die(self,role):
        """skill1：love never die
        if counter with role which has more than 1 members, double the basic arrow
        @:param role: the person self counter with
        """
        if role.role_member > 1:
            self.arrow *= 2

    def cheer_friends(self,current_round):
        """skill2：cheer friends
        happens every 2 rounds, double self arrow but base hit rate reduced by 35%
        @:param current_round: current round
        """
        if current_round % 2 == 0:
            self.arrow *= 2
            self.hitting_accuracy *= 0.35


class DuYa(Role):
    """
    渡鸦
    """
    def __init__(self):
        super().__init__(23, 14, 14, '渡鸦', 1)

    def attack(self, role,current_round):
        self.not_aim_at_you(role)
        self.my_villa_island(current_round,role)
        self.normal_attack(role)

    def not_aim_at_you(self,role):
        """skill1：not aim at you
        cause 25% damage more on kiana, and other roles has 25% possibility to enhance basic damage
        @:param role: my enemy
        """
        if role.name0 == "琪亚娜":
            self.arrow *= 1.25
        else:
            if random.randint(1, 10000) < 2500:
                self.arrow *= 1.25

    def my_villa_island(self,current_round,role):
        """skill2：my villa island
        happens every 3 rounds, get my enemy 16 damages 7 times
        @:param current_round: current round
        @:param role: my enemy
        """
        if current_round % 3 == 0:
            damage = 16 - role.shield
            # here I consider about the effect of hit rate
            for _ in range(7):
                if random.randint(1, 10000) < self.hitting_accuracy * 100:
                    role.under_attack(damage)


class YingLianZu(Role):
    """
    樱莲组
    """
    def __init__(self):
        super().__init__(20, 9, 18, '樱莲组', 2)

    def attack(self, role,current_round):
        self.sakura_rice_cakes()
        self.kallen_rice_cakes(current_round,role)
        self.normal_attack(role)

    def sakura_rice_cakes(self):
        """skill1：not aim at you
        cause 25% damage more on kiana, and other roles has 25% possibility to enhance basic damage
        @:param role: my enemy
        """
        if random.randint(1, 10000) < 3000:
            self.blood += 25

    def kallen_rice_cakes(self,current_round,role):
        """skill2：my villa island
        happens every 3 rounds, get my enemy 16 damages 7 times
        @:param current_round: current round
        @:param role: my enemy
        """
        if current_round % 2 == 0:
            role.under_attack(0, 25)

class DeLiSha(Role):
    """
    德莉莎
    """
    def __init__(self):
        super().__init__(19, 12, 22, '德莉莎', 3)

    def attack(self, role,current_round):
        self.online_kicker(current_round,role)
        self.normal_attack(role)
        self.blood_judas_cutest(role)

    def blood_judas_cutest(self,role):
        """skill1：not aim at you
        cause 25% damage more on kiana, and other roles has 25% possibility to enhance basic damage
        @:param role: my enemy
        """
        if random.randint(1, 10000) < 3000:
            role.shield -= 5

    def online_kicker(self,current_round,role):
        """skill2：my villa island
        happens every 3 rounds, get my enemy 16 damages 5 times
        @:param current_round: current round
        @:param role: my enemy
        """
        if current_round % 3 == 0:
            damage = 16 - role.shield
            # here I consider about the effect of hit rate
            for _ in range(5):
                if random.randint(1, 10000) < self.hitting_accuracy * 100:
                    role.under_attack(damage)



# #class lilia:可怜的剑圣已经被淘汰了，就不写了==

# #丽塔子类 TODO
# class liTa(role):
#     #属性初始化
#     def __init__(self, num):
#         super().__init__(26, 11, 17, '丽塔')

#     def attack(self, role):
#         #没有被动技能，直接进行状态判断
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             return str(super().attack(role))+',沉默'
        
#         dam0=role.blood-role.onAttack(self, self.arrow-role.shield)
#         #女仆的温柔清理
#         if random.randint(1,10000)<=3500:
#             self.blood+=dam0
#             if self.blood>100:
#                 self.blood=100
#             #print('丽塔回血+',dam0)
#         #封禁对方攻击的技能
#         if random.randint(1,10000)>8000:
#             role.block=True
#             #print('丽塔使用了必杀，封锁了对手的进攻')
#         return self.arrow-role.shield

# #卡莲子类 TODO
# class kaLian(role):
#     #defence表示卡莲的减伤状态剩余几个回合
#     def __init__(self, num):
#         super().__init__(26, 6, 5, '卡莲')
#         self.defence = 0

#     def attack(self, role):
#         #如果处于减伤状态，每过一回合denfence-1，当其为0时，将对方的攻击力归还
#         if self.defence:
#             self.defence-=1
#             if self.defence==0:
#                 #print('对方的攻击力已恢复')
#                 role.arrow+=15

#         #状态判定
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             return str(super().attack(role))+',沉默'
#         #5%可能直接胜利
#         if random.randint(1, 10000) <= 500:
#             #print('卡莲的对手变成了废人')
#             role.blood = 0
#             return '∞，5%必杀'
#         #30%概率触发技能，对方攻击力减15
#         if random.randint(1, 10000) > 7000:
#             #print(role.name0+'攻击力下降')
#             #如果已经在减伤状态就不再减攻击了
#             if self.defence==0:
#                 role.arrow-=15
#             self.defence = 2
#         role.onAttack(self, self.arrow-role.shield)
#         return self.arrow-role.shield

# #符华子类 TODO
# class fuHua(role):
#     #charge是上仙的必杀技计数器
#     #defence表示进入锁血状态
#     def __init__(self, num):
#         super().__init__(27, 8, 5, '符华')
#         self.charge = 0
#         self.defence = False

#     def attack(self, role):
#         #计数器+1，状态判定
#         self.charge += 1
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             return str(super().attack(role))+',沉默'

#         #每3个回合触发必杀技，随机10-30元素伤害
#         if self.charge % 3 == 0:
#             temp = random.randint(10, 30)
#             #print('~赤鸢仙人发动必杀，随机元素伤害'+str(temp))
#             role.onAttack(self, 0, temp)
#             return temp
#         #普通攻击
#         role.onAttack(self, self.arrow-role.shield)
#         return self.arrow-role.shield

#     def onAttack(self, role, dam, fire=0):
#         #锁血状态下免疫元素伤害
#         if self.defence:
#             if fire:
#                 fire=0
#                 #print('~赤鸢已过滤元素伤害')
#             self.blood = self.blood-dam
#             return self.blood
#         #普通的受击判定
#         self.blood = self.blood-dam-fire
#         #受到致命伤害时开始锁血
#         if self.blood < 1 and self.defence == False:
#             #print('~符华开始锁血')
#             self.defence = True
#             self.blood = 1
#         return self.blood


# #布洛妮娅子类 TODO
# class buronia(role):
#     #charge是必杀技计数器
#     def __init__(self, num):
#         super().__init__(26, 8, 1, '布洛妮娅')
#         self.charge = 0

#     def attack(self, role):
#         #计数器增加，状态判定
#         self.charge += 1
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             return super().attack(role)
#         #普通攻击伤害计算
#         dam0 = self.arrow-role.shield
#         #每3个回合触发必杀技，随机造成1-100点物理伤害,伤害减对方防御
#         if self.charge % 3 == 0:
#             #print('~布洛妮娅必杀技发动')
#             dam0=random.randint(1,100)-role.shield
#             if dam0<0:
#                 dam0=0
#         role.onAttack(self,dam0)
#         return dam0
    
#     def onAttack(self, role, dam, fire=0):
#         #被动15%闪避攻击
#         if random.randint(1,10000)<=1500:
#             #print('~布洛妮娅触发了闪避')
#             #只免疫物理攻击，无法免疫纯元素攻击
#             if dam==0 and fire:
#                 self.blood = self.blood-fire
#             return self.blood
#         #不触发闪避则正常结算
#         self.blood = self.blood-dam-fire
#         return self.blood

# #八重樱子类 TODO
# class baChong(role):
#     #onFire是八重樱点燃状态的计数器
#     def __init__(self, num):
#         super().__init__(28, 7, 4, '八重樱')
#         self.onFire=0

#     def attack(self, role):
#         #状态判断
#         if self.block:
#             self.block = False
#             #点燃状态不受封禁或沉默影响
#             if self.onFire:
#                 self.onFire-=1
#                 #print(role.name0+'因为点燃受到了5点元素伤害')
#                 role.onAttack(self,0,5)
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             #点燃状态不受封禁或沉默影响
#             if self.onFire:
#                 self.onFire-=1
#                 #print(role.name0+'因为点燃受到了5点元素伤害')
#                 role.onAttack(self,0,5)
#             return str(super().attack(role))+',沉默'
        
#         #25%的概率造成的伤害（计算防御后）翻倍
#         dam0=self.arrow-role.shield
#         if random.randint(1,10000)<=2500:
#             #print('小八造成的伤害翻倍')
#             dam0=dam0*2

#         #20%的概率触发点燃，重复触发刷新持续时间
#         if random.randint(1,10000)<=2000:
#             #print('八重樱的攻击触发了点燃')
#             self.onFire=3
#         #如果对方被点燃，则要受到5点元素伤害
#         #这里选择调用一次对方的受击函数，确保符华的锁血技能、德丽莎的元素减伤等可以正确生效
#         if self.onFire:
#             self.onFire-=1
#             #print(role.name0+'因为点燃受到了5点元素伤害')
#             role.onAttack(self,0,5)

#         role.onAttack(self,dam0)
#         return dam0

# #芽衣姐姐的子类 TODO
# class yaYi(role):
#     def __init__(self, num):
#         super().__init__(26, 6, 3, '芽衣')

#     def attack(self, role):
#         #状态判定
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             return str(super().attack(role))+',沉默'

#         #一般状态下附加5点元素伤害
#         dam0 = self.arrow-role.shield
#         fire0 = 5
#         #触发必杀技时，附加20点元素伤害，将对方沉默
#         if random.randint(0, 10000) < 3000:
#             #print('芽衣将对方沉默')
#             fire0 = 20
#             role.silent = True
#         #print('芽衣的攻击附加元素伤害'+str(fire0))
#         role.onAttack(self, dam0, fire0)
#         return dam0+fire0

# #魔法少女德丽莎的子类 TODO
# class teriri(role):
#     #charge是必杀技计数器
#     def __init__(self, num):
#         super().__init__(24, 8, 2, '德丽莎')
#         self.charge = 0

#     def attack(self, role):
#         #计数器增加，状态判定
#         self.charge += 1
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             return super().attack(role)

#         #普通攻击伤害计算
#         dam0 = self.arrow-role.shield
#         fire0 = 0
#         #每两个回合触发必杀技，造成4次随机的元素伤害
#         if self.charge % 2 == 0:
#             a = random.randint(1, 16)
#             b = random.randint(1, 16)
#             c = random.randint(1, 16)
#             d = random.randint(1, 16)
#             #print('德丽莎发动必杀技：',a,b,c,d)
#             fire0 = a+b+c+d
#             #只造成一次攻击
#             #role.onAttack(self, 0, fire0)
#             #分别造成四次攻击
#             role.onAttack(self, 0, a)
#             role.onAttack(self, 0, b)
#             role.onAttack(self, 0, c)
#             role.onAttack(self, 0, d)
#             return fire0
#         role.onAttack(self, dam0, fire0)
#         return dam0+fire0

#     def onAttack(self, role, dam, fire=0):
#         #被动减元素伤害
#         self.blood = self.blood-dam-int(0.5*fire)
#         return self.blood


# #希儿子类 TODO
# class xiEr(role):
#     #属性初始化，charge是必杀技的计数器
#     def __init__(self, num):
#         super().__init__(23, 10, 5, '希儿')
#         self.charge = 0

#     def attack(self, role):
#         #每次进攻，回合数加1，立即触发被动技能，
#         # 随后判断当前是否被沉默，是否被封禁
#         self.charge += 1
#         #被动回血
#         self.blood+=7
#         if self.blood>100:
#             self.blood=100
#         #print('希儿回血+7')

#         #状态判断
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#             #如果被沉默，调用父类的攻击函数，即只进行普通攻击
#         if self.silent:
#             self.silent = False
#             return str(super().attack(role))+',沉默'

#         dam0 = self.arrow-role.shield
#         #每4个回合触发必杀技
#         if self.charge % 4 == 0:
#             dam0 = (100-role.shield)
#             if random.randint(1,10000)>2500:
#                 dam0=0

#         #计算好伤害值后，调用对方的onAttack函数进行伤害的结算，并便于触发对方的某些技能
#         role.onAttack(self, dam0)
#         if dam0:
#             return dam0
#         else:
#             return '0,Miss!'


# #罗莎莉亚子类 TODO
# class rosalia(role):
#     #属性初始化，charge为必杀技计数器，special为罗莎莉亚的特殊攻击倍率
#     def __init__(self, num):
#         super().__init__(30, 4, 4, '萝莎莉娅')
#         self.charge = 0
#         self.special = 1.0

#     def attack(self, role):
#         #计数器增加
#         self.charge += 1
#         #先进行伤害值的计算但并不进行攻击，因为倍率special接下来会发生变化
#         #普通攻击伤害计算
#         dam0 = (self.arrow-role.shield)*self.special
#         #必杀技伤害计算
#         if self.charge % 3 == 0:
#             dam0 = (15-role.shield)*(self.special*10)
#         #判断下回合的攻击倍率
#         self.special = 1.0
#         temp = random.randint(1, 10000)
#         if temp <= 3000:
#             self.special = 1.5
#         if temp > 7000:
#             self.special = 0.5

#         #判定状态
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             return str(super().attack(role))+',沉默'

#         #进行攻击，每三个回合自己的必杀技将对自己进行封锁
#         if self.charge % 3 == 0:
#             self.block = True
#         role.onAttack(self, int(dam0))

#         return int(dam0)



# #琪亚娜子类 TODO
# class qiYaNa(role):
#     #琪亚娜被动血量为120，charge为必杀技计数器
#     def __init__(self, num):
#         super().__init__(23, 11, 2, '琪亚娜')
#         self.blood = 120
#         self.charge = 0

#     def attack(self, role):
#         #回合数增加，状态判定
#         self.charge += 1
#         if self.block:
#             self.block = False
#             return '0，行动被封锁'
#         if self.silent:
#             self.silent = False
#             return super().attack(role)
#         #正常攻击
#         dam0 = self.arrow-role.shield
#         #每三回合触发必杀攻击
#         if (self.charge % 3 == 0):
#             dam0 = (12-role.shield)*8
#         role.onAttack(self, dam0)
#         return dam0
