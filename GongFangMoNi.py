import roles

def is_fight_end(role1, role2):
    return role1.blood < 1 or role2.blood < 1

def get_winner(role1, role2):
    if role1.blood < 1:
        return role2
    if role2.blood < 1:
        return role1

def fight(role1, role2):
    winner = '0'
    currend_round = 0
    fast_role,slow_role = role1,role2
    #保证速度值高的选手先发
    if role1.speed < role2.speed:
        fast_role,slow_role = role2,role1
    #进入战斗，当有选手血量降为0，比赛停止
    #在每次循环中，两位选手轮流调用自身的attack()成员函数进行攻击
    while winner == '0':
        currend_round += 1
        fast_role.attack(slow_role,currend_round)
        if is_fight_end(fast_role, slow_role):
            winner = get_winner(fast_role, slow_role)
            break
        slow_role.attack(fast_role,currend_round)
        if is_fight_end(fast_role, slow_role):
            winner = get_winner(fast_role, slow_role)
            break
    return winner.name0

def main():
    for _ in range(10):
        win_times = {}
        for _ in range(100000):
            role1,role2 = roles.JiZi(),roles.DuYa()
            winner = fight(role1, role2)
            if not winner in win_times:
                win_times[winner] = 1
            else:
                win_times[winner] += 1
        print(win_times)



if __name__ == '__main__':
    main()


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



    
    # win = {
        # '姬子': 0,
        # '符华': 0,
        # '卡莲': 0,
        # '琪亚娜': 0,
        # '芽衣': 0,
        # '德丽莎': 0,
        # '萝莎莉娅':0,
        # '莉莉娅':0,
        # '布洛妮娅':0,
        # '希儿':0,
        # '丽塔':0,
        # '八重樱':0
    # }
    # i = 0
    # while i < 100000:
        # role1 = roles.buronia(0)
        # role2 = roles.kaLian(0)
        # #每场比赛交换位置，如果速度相同可以实现换发，
        # # 速度不同的会在fight函数中再次交换，使得速度值高的为role1
        # if i%2:
            # temp=role1
            # role1=role2
            # role2=temp
        # #win[fightRe(role1, role2)] += 1
        # win[fight(role1, role2)] += 1
        # i += 1
    # print('最终结果\n'+role1.name0+'胜利'+str(win[role1.name0])+'次')
    # print(role2.name0+'胜利'+str(win[role2.name0])+'次\n')
    
    # win = {
        # '姬子': 0,
        # '符华': 0,
        # '卡莲': 0,
        # '琪亚娜': 0,
        # '芽衣': 0,
        # '德丽莎': 0,
        # '萝莎莉娅':0,
        # '莉莉娅':0,
        # '布洛妮娅':0,
        # '希儿':0,
        # '丽塔':0,
        # '八重樱':0
    # }
    # i = 0
    # while i < 100000:
        # role1 = roles.fuHua(0)
        # role2 = roles.baChong(0)
        # #每场比赛交换位置，如果速度相同可以实现换发，
        # # 速度不同的会在fight函数中再次交换，使得速度值高的为role1
        # if i%2:
            # temp=role1
            # role1=role2
            # role2=temp
        # #win[fightRe(role1, role2)] += 1
        # win[fight(role1, role2)] += 1
        # i += 1
    # print('最终结果\n'+role1.name0+'胜利'+str(win[role1.name0])+'次')
    # print(role2.name0+'胜利'+str(win[role2.name0])+'次\n')
    
    # win = {
        # '姬子': 0,
        # '符华': 0,
        # '卡莲': 0,
        # '琪亚娜': 0,
        # '芽衣': 0,
        # '德丽莎': 0,
        # '萝莎莉娅':0,
        # '莉莉娅':0,
        # '布洛妮娅':0,
        # '希儿':0,
        # '丽塔':0,
        # '八重樱':0
    # }
    # i = 0
    # while i < 100000:
        # role1 = roles.fuHua(0)
        # role2 = roles.kaLian(0)
        # #每场比赛交换位置，如果速度相同可以实现换发，
        # # 速度不同的会在fight函数中再次交换，使得速度值高的为role1
        # if i%2:
            # temp=role1
            # role1=role2
            # role2=temp
        # #win[fightRe(role1, role2)] += 1
        # win[fight(role1, role2)] += 1
        # i += 1
    # print('最终结果\n'+role1.name0+'胜利'+str(win[role1.name0])+'次')
    # print(role2.name0+'胜利'+str(win[role2.name0])+'次\n')
    # input()

