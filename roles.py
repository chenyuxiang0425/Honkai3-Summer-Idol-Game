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
    not_numbness = True
    not_fainting = True
    revitalization = False

    def __init__(self, arrow, shield, speed, name0, role_member):
        self.arrow = arrow
        self.shield = shield
        self.speed = speed
        self.name0 = name0
        self.role_member = role_member

    def attack(self, role, current_round):
        if not self.not_fainting:
            self.not_fainting = True
            return
        if self.not_numbness:
            self.normal_attack(role)

    def normal_attack(self, role):
        """normal attack which has been considered of hit rate
         @:param role: the role to be attacked
        """
        damage = self.arrow - role.shield
        if random.randint(1, 10000) < self.hitting_accuracy * 100:
            role.under_attack(damage)

    def under_attack(self, damage, fire=0):
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
        if not self.not_fainting:
            self.not_fainting = True
            return
        if self.not_numbness:
            self.love_never_die(role)
            self.cheer_friends(curr_round)
            self.normal_attack(role)

    def love_never_die(self, role):
        """skill1：love never die
        if counter with role which has more than 1 members, double the basic arrow
        @:param role: the person self counter with
        """
        if role.role_member > 1:
            self.arrow *= 2

    def cheer_friends(self, current_round):
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

    def attack(self, role, current_round):
        if not self.not_fainting:
            self.not_fainting = True
            return
        if self.not_numbness:
            self.not_aim_at_you(role)
            self.my_villa_island(current_round, role)
            if current_round % 3 != 0:
                self.normal_attack(role)

    def not_aim_at_you(self, role):
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

    def attack(self, role, current_round):
        if not self.not_fainting:
            self.not_fainting = True
            return
        if self.not_numbness:
            self.sakura_rice_cakes()
            self.kallen_rice_cakes(current_round, role)
            if current_round % 2 != 0:
                self.normal_attack(role)

    def sakura_rice_cakes(self):
        """skill1：sakura_rice_cakes
        has 30% possibility to obtain 25 blood
        @:param role: my enemy
        """
        if random.randint(1, 10000) < 3000:
            self.blood += 25

    def kallen_rice_cakes(self, current_round, role):
        """skill2：kallen_rice_cakes
        happens every 2 rounds, get my enemy 25 fire 7 times
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

    def attack(self, role, current_round):
        if not self.not_fainting:
            self.not_fainting = True
            return
        if self.not_numbness:
            self.online_kicker(current_round, role)
            if current_round % 3 != 0:
                self.normal_attack(role)
                self.blood_judas_cutest(role)

    def blood_judas_cutest(self, role):
        """skill1：not aim at you
        cause 25% damage more on kiana, and other roles has 25% possibility to enhance basic damage
        @:param role: my enemy
        """
        if random.randint(1, 10000) < 3000:
            role.shield -= 5

    def online_kicker(self, current_round, role):
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


# 芽衣
class YaYi(Role):
    def __init__(self):
        super().__init__(22, 12, 30, '芽衣', 1)

    def attack(self, role, current_round):
        if not self.not_fainting:
            self.not_fainting = True
            return
        if self.not_numbness:
            self.dragon_maid(current_round,role)
            if current_round % 2 != 0:
                self.normal_attack(role)
                self.singer_of_the_falling_world(role)

    def singer_of_the_falling_world(self, role):
        """skill1：has 30% to skip enemy's round
        @:param role: my enemy
        """
        if random.randint(1, 10000) < 3000:
            role.not_numbness = False

    def dragon_maid(self, current_round, role):
        """skill2：dragon_maid
        happens every 2 rounds, get my enemy 3 fires 5 times
        @:param current_round: current round
        @:param role: my enemy
        """
        if current_round % 2 == 0:
            for _ in range(5):
                role.under_attack(0, 3)


#琪亚娜
class Kiana(Role):
    def __init__(self):
        super().__init__(24, 11, 23, '琪亚娜', 1)

    def attack(self, role, current_round):
        if not self.not_fainting:
            self.not_fainting = True
            return
        if self.not_numbness:
            self.take_a_spear(current_round, role)
            if current_round % 2 != 0:
                self.normal_attack(role)

    def take_a_spear(self, current_round, role):
        """skill1：take_a_spear
        happens every 2 rounds, get my enemy my arrow plus double role's shield damage
        @:param role: my enemy
        """
        if current_round % 2 == 0:
            damage = self.arrow + role.shield * 2
            role.under_attack(damage)
            self.too_load()

    def too_load(self):
        """skill2：too_load
        30% possibility to get fainting
        """
        if random.randint(1, 10000) < 3000:
            self.not_fainting = False


#阿琳姐妹
class Alin(Role):
    def __init__(self):
        super().__init__(18, 10, 10, '阿琳姐妹', 2)
        self.revitalization = True

    def attack(self, role, current_round):
        if self.blood < 0:
            self.life_water()
            if self.blood > 0:
                self.become_star(role)
            return
        if not self.not_fainting:
            self.not_fainting = True
            return
        if self.not_numbness:
            self.normal_attack(role)

    def life_water(self):
        """skill1：life_water
        not die if blood less than 0, and become 20 blood
        """
        if self.blood < 0:
            self.blood = 20
            self.revitalization = False

    def become_star(self, role):
        """skill2：become_star
        50% possibility to attack 233 or 50
        @:param role: my enemy

        """
        if random.randint(1, 10000) < 5000:
            role.under_attack(233)
        else:
            role.under_attack(50)


# 幽兰戴尔

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


