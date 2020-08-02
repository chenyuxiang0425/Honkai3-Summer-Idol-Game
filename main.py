import simulation
import roles

def main():
    for _ in range(50):
        fight_times = 100000
        winer_dict = simulation.redict_winner(fight_times)
        for key, value in winer_dict.items():
            print(key, "的胜率为", value/fight_times)


if __name__ == '__main__':
    main()

