import roles


def is_fight_ended(role1, role2):
    """if role1 or role2's blood down to zero, the fight is end
    @:param role1: one role
    @:param role2: another role
    :return true if any of them's blood down to zero
    """
    return (role1.blood < 1 or role2.blood < 1) and role1.revitalization is False and role2.revitalization is False


def get_winner(role1, role2):
    """if role1 or role2's blood down to zero, the other role is winner
    @:param role1: one role
    @:param role2: another role
    :return role who wins
    """
    if role1.blood < 1:
        return role2
    if role2.blood < 1:
        return role1


def fight(role1, role2):
    """two roles fight, return the name of winner
    @:param role1: one role
    @:param role2: another role
    :return winner's name
    """
    winner = "None"
    currend_round = 0
    fast_role,slow_role = role1,role2
    if role1.speed < role2.speed: # make sure the fastest is the first role to attack
        fast_role,slow_role = role2,role1

    while winner == "None":
        fast_role.not_numbness, slow_role.not_numbness = True, True
        currend_round += 1
        fast_role.attack(slow_role,currend_round)
        if is_fight_ended(fast_role, slow_role):
            winner = get_winner(fast_role, slow_role)
            break
        slow_role.attack(fast_role, currend_round)
        if is_fight_ended(fast_role, slow_role):
            winner = get_winner(fast_role, slow_role)
            break
    return winner.name0


def redict_winner(fight_times=100000):
    """two roles fight, return a dictionary of battle history
    @:param role1: one role
    @:param role2: another role
    :return winner's name
    """
    win_times = {}
    for _ in range(fight_times):
        role1 = roles.Alin()
        role2 = roles.Kiana()
        winner = fight(role1, role2)
        if not winner in win_times:
            win_times[winner] = 1
        else:
            win_times[winner] += 1
    return win_times


# #打印战报的战斗函数
# def fightRe(role1, role2):
#     winner = '0'
#     print('战斗开始')
#     print(role1.name0+' '+role2.name0)
#     #保证速度值高的选手先发
#     if (role1.speed < role2.speed):
#         temp = role1
#         role1 = role2
#         role2 = temp
#     #进入战斗，当有选手血量降为0，比赛停止
#     #在每次循环中，两位选手轮流调用自身的attack()成员函数进行攻击
#     print(role1.name0+'血量'+str(role1.blood))
#     print(role2.name0+'血量'+str(role2.blood)+' |')
#     while (winner == '0'):
#         dam1 = role1.attack(role2)
#         print(role1.name0+'进攻，伤害为'+str(dam1))
#         print(role2.name0+'血量'+str(role2.blood)+'。')
#         if (role1.blood < 1):
#             winner = role2.name0
#             break
#         if role2.blood < 1:
#             winner = role1.name0
#             break
#         dam2 = role2.attack(role1)
#         print(role2.name0+'进攻，伤害为'+str(dam2))
#         print(role1.name0+'血量'+str(role1.blood)+' |')
#         if (role1.blood < 1):
#             winner = role2.name0
#         if role2.blood < 1:
#             winner = role1.name0
#     print(winner+'胜利\n')
#     return winner
