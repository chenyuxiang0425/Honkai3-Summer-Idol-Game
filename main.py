import simulation
import roles
import pandas
from pandas import DataFrame

def main():
    role_list = {"Buronia": roles.Buronia,
                 "Alin": roles.Alin,
                 "YaYi": roles.YaYi,
                 "YingLianZu": roles.YingLianZu,
                 "DeLiSha": roles.DeLiSha,
                 "JiZi": roles.JiZi,
                 "XiEr": roles.XiEr,
                 "DuYa": roles.DuYa,
                 "LiTa": roles.LiTa,
                 "Durandel": roles.Durandel,
                 "FuHua": roles.FuHua,
                 "Kiana": roles.Kiana
    }

    winning_probability = {"name": list(role_list.keys())}
    for role, role_class in role_list.items():
        winning_probability[role] = []

    for attacker, attacker_class in role_list.items():
        for defender, defender_class in role_list.items():
            fight_times = 10000
            if attacker == defender:
                winning_probability[attacker].append(-1)
            else:
                winner_dict = simulation.redict_winner(attacker_class, defender_class, fight_times)
                winning_probability.get(attacker).append(winner_dict.get(attacker, 0)/fight_times)
    print(winning_probability)
    DataFrame(winning_probability).to_csv(".\\result.csv", index=False)


def test_Alin_Jizi():

    fight_times = 1000
    winner_dict = simulation.redict_winner(roles.Alin, roles.JiZi, fight_times)
    # print(winning_probability)
    print(winner_dict)

def test_LiTa_XiEr():

    fight_times = 1000
    winner_dict = simulation.redict_winner(roles.LiTa, roles.XiEr, fight_times)
    # print(winning_probability)
    print(winner_dict)


def test_DuYa_Kiana():

    fight_times = 10000
    winner_dict = simulation.redict_winner(roles.DuYa, roles.Kiana, fight_times)
    # print(winning_probability)
    print(winner_dict)


if __name__ == '__main__':
    main()

