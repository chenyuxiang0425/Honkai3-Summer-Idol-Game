# -*- coding: utf-8 -*-
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
    hitting_accuracy = 100  # hit rate
    not_numbness = True
    not_fainting = True
    revitalization = False
    charmed_counts = 0

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
        if self.charmed_counts > 0:
            self.charmed_counts -= 1
            self.normal_attack(role)
            return

    def normal_attack(self, role):
        """normal attack which has been considered of hit rate
         @:param role: the role to be attacked
        """
        damage = self.arrow
        if random.randint(1, 10000) < self.hitting_accuracy * 100:
            role.under_attack(causer=self, damage=damage)

    def under_attack(self, causer, damage, fire=0,is_skill_attack=False):
        """self under attack, cause blood reducing
         @:param causer: who cause the damage
         @:param damage: physical damage
         @:param fire: element damage
         @:param is_skill_attack: is it from a skill
        """
        damage = damage - self.shield
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
        super(JiZi, self).attack(role, curr_round)
        if self.not_numbness and self.charmed_counts <= 0:
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
        super(DuYa, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
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

    def my_villa_island(self, current_round, role):
        """skill2：my villa island
        happens every 3 rounds, get my enemy 16 damages 7 times
        @:param current_round: current round
        @:param role: my enemy
        """
        if current_round % 3 == 0:
            damage = 16
            # here I consider about the effect of hit rate
            for _ in range(7):
                if random.randint(1, 10000) < self.hitting_accuracy * 100:
                    role.under_attack(causer=self,damage=damage,fire=0,is_skill_attack=True)


class YingLianZu(Role):
    """
    樱莲组
    """
    def __init__(self):
        super().__init__(20, 9, 18, '樱莲组', 2)

    def attack(self, role, current_round):
        super(YingLianZu, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
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
            role.under_attack(causer=self,damage=0, fire=25, is_skill_attack=True)


class DeLiSha(Role):
    """
    德莉莎
    """
    def __init__(self):
        super().__init__(19, 12, 22, '德莉莎', 3)

    def attack(self, role, current_round):
        super(DeLiSha, self).attack(role,current_round)
        if self.not_numbness and self.charmed_counts <= 0:
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
            damage = 16
            # here I consider about the effect of hit rate
            for _ in range(5):
                if random.randint(1, 10000) < self.hitting_accuracy * 100:
                    role.under_attack(causer=self,damage=damage,is_skill_attack=True)


class YaYi(Role):
    """
    芽衣
    """
    def __init__(self):
        super().__init__(22, 12, 30, '芽衣', 1)

    def attack(self, role, current_round):
        super(YaYi, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
            self.dragon_maid(current_round, role)
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
                role.under_attack(causer=self,damage=0, fire=3,is_skill_attack=True)


class Kiana(Role):
    """
    琪亚娜
    """
    def __init__(self):
        super().__init__(24, 11, 23, '琪亚娜', 1)

    def attack(self, role, current_round):
        super(Kiana, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
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
            role.under_attack(causer=self,damage=damage, is_skill_attack=True)
            self.too_load()

    def too_load(self):
        """skill2：too_load
        30% possibility to get fainting
        """
        if random.randint(1, 10000) < 3000:
            self.not_fainting = False


class Alin(Role):
    """
    阿琳姐妹
    """
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
        if self.charmed_counts > 0:
            self.charmed_counts -= 1
            self.normal_attack(role)
            return
        if self.not_numbness and self.charmed_counts <= 0:
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
            role.under_attack(causer=self,damage=233, is_skill_attack=True)
        else:
            role.under_attack(causer=self,damage=50, is_skill_attack=True)


class Durandel(Role):
    """
    幽兰黛尔
    """
    def __init__(self):
        super().__init__(19, 10, 15, '幽兰黛尔', 1)

    def attack(self, role, current_round):
        super(Durandel, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
            self.the_joy_of_fishing()
            self.normal_attack(role)

    def the_joy_of_fishing(self):
        """skill1: the_joy_of_fishing
        increase arrow 3 point every time before attack
        """
        self.arrow += 3

    def under_attack(self, causer, damage, fire=0, is_skill_attack=False):
        """skill2: 16% possibility to ignore enemy skills and cause her 30 damage
        self under attack, cause blood reducing
         @:param damage: physical damage
         @:param fire: element damage
        """
        if is_skill_attack:
            if random.randint(1, 10000) < 1600:
                causer.blood -= 30
        else:
            damage = damage - self.shield
            if damage <= 0:
                damage = 0
            if fire <= 0:
                fire = 0
            self.blood = self.blood - damage - fire


class LiTa(Role):
    """
    丽塔
    """
    def __init__(self):
        super().__init__(26, 11, 17, '丽塔', 1)
        self.perfect_mind_done = False

    def attack(self, role, current_round):
        super(LiTa, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
            self.perfect_mind(role, current_round)
            if current_round % 4 != 0:
                self.gentle_cleaning_of_maid(role)

    def gentle_cleaning_of_maid(self, role):
        """skill1：gentle_cleaning_of_maid
        35% possibility to reduce current damage 3 points, and reduce enemy's arrow 4 points permanently
        @:param role: my enemy
        """
        if random.randint(1, 10000) < 3500:
            role.under_attack(causer=self, damage=self.arrow - 3, is_skill_attack=True)
            role.arrow -= 4
        else:
            role.normal_attack(self.arrow)

    def perfect_mind(self, role, current_round):
        """skill2：perfect_mind
        happens every 4 rounds, increase enemy 4 blood and make her charmed for 2 rounds which can not use skills
        make her damage reduce 60% forever
        @:param role: my enemy
        @:param current_round: current round
        """
        if current_round % 4 == 0:
            role.blood += 4
            role.charmed_counts = 2
            self.perfect_mind_done = True

    def under_attack(self, causer, damage, fire=0, is_skill_attack=False):
        """self under attack, cause blood reducing
        if perfect_mind has happened, the total damage reduce 60%
         @:param damage: physical damage
         @:param fire: element damage
        """
        damage = damage - self.shield
        if damage <= 0:
            damage = 0
        if fire <= 0:
            fire = 0
        if self.perfect_mind_done:
            self.blood = self.blood - (damage + fire) * (1 - 0.6)
        else:
            self.blood = self.blood - damage - fire


class Buronia(Role):
    """
    布洛妮娅
    """
    def __init__(self):
        super().__init__(21, 10, 20, '布洛妮娅', 1)

    def attack(self, role, current_round):
        super(Buronia, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
            self.angel_reconstruction(role)
            self.motorcycle_visitors(role, current_round)
            if current_round % 3 != 0:
                self.normal_attack(role)

    def angel_reconstruction(self, role):
        """skill1 angel_reconstruction
        after attack, 25% possibility to case 12 damage 4 times
        @:param role: my enemy
        """
        if random.randint(1, 10000) < 2500:
            damage = 12
            for _ in range(4):
                if random.randint(1, 10000) < self.hitting_accuracy * 100:
                    role.under_attack(causer=self,damage=damage, is_skill_attack=True)

    def motorcycle_visitors(self, role, current_round):
        """skill2：motorcycle_visitors
        happens every 3 rounds, cause element damage in 1~100
        @:param role: my enemy
        @:param current_round: current round
        """
        if current_round % 3 == 0:
            role.under_attack(causer=self,damage=0, fire=random.randint(1, 100), is_skill_attack=True)


class FuHua(Role):
    """
    符华
    """
    def __init__(self):
        super().__init__(17, 15, 16, '符华', 1)

    def attack(self, role, current_round):
        super(FuHua, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
            self.pen_and_ink(role, current_round)
            if current_round % 3 != 0:
                self.normal_attack(role)

    def normal_attack(self, role):
        """skill1: FuHua's normal attack is element attack
         @:param role: my enemy
        """
        fire = self.arrow
        if random.randint(1, 10000) < self.hitting_accuracy * 100:
            role.under_attack(causer=self, damage=0, fire=fire)

    def pen_and_ink(self, role, current_round):
        """skill2: pen_and_ink
        happens every 3 rounds, 18 damage and reduce enemy's hit rate by 0.25
         @:param role: my enemy
        """
        if current_round % 3 == 0:
            role.under_attack(causer=self,damage=0, fire=18, is_skill_attack=True)
            role.hitting_accuracy *= 0.25


class XiEr(Role):
    """
    希儿
    """
    def __init__(self):
        super().__init__(23, 13, 26, '希儿', 1)
        self.state = "white"

    def attack(self, role, current_round):
        super(XiEr, self).attack(role, current_round)
        if self.not_numbness and self.charmed_counts <= 0:
            self.change_myself()
            self.please_another_me()
            self.normal_attack(role)

    def change_myself(self):
        """skill1:change myself
        every time before attack,change my state
        """
        if self.state == "white":
            self.state = "black"
        else:
            self.state = "white"

    def please_another_me(self):
        """skill2: please_another_me"""
        if self.state == "white":
            self.blood += random.randint(1, 15)
            self.arrow -= 10
            self.shield += 5
        else:
            self.arrow += 10
            self.shield -= 5
