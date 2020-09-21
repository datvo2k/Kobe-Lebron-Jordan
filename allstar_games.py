import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle, islice
from matplotlib import cm

'''
PTS-TRB-AST-FG%-3P%-FT%-TOV-PF
'''
sns.set(font_scale=1)
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sns.set_context("paper", rc={"font.size": 15, "axes.titlesize": 15, "axes.labelsize": 15})


def players_index(input_csv, input_string):
    player_index = input_csv[input_csv["Player"] == input_string]
    player_index.reset_index(inplace=True, drop=True)
    fig, axs = plt.subplots(ncols=3, nrows=3)
    fig.suptitle('{0} in All-Star Game'.format(input_string), fontsize=20)

    sns.barplot(x=player_index['PTS'], y=player_index['Season'], data=player_index, color='r', ax=axs[0][0])
    sns.barplot(x=player_index['AST'], y=player_index['Season'], data=player_index, color='r', ax=axs[0][1])
    sns.barplot(x=player_index['TRB'], y=player_index['Season'], data=player_index, color='r', ax=axs[0][2])
    sns.barplot(x=player_index['STL'], y=player_index['Season'], data=player_index, color='r', ax=axs[1][0])
    sns.barplot(x=player_index['BLK'], y=player_index['Season'], data=player_index, color='r', ax=axs[1][1])
    sns.barplot(x=player_index['TOV'], y=player_index['Season'], data=player_index, color='r', ax=axs[1][2])
    sns.barplot(x=player_index['FG%'] * 100, y=player_index['Season'], data=player_index, color='r', ax=axs[2][0])
    sns.barplot(x=player_index['3P%'] * 100, y=player_index['Season'], data=player_index, color='r', ax=axs[2][1])
    sns.barplot(x=player_index['FT%'] * 100, y=player_index['Season'], data=player_index, color='r', ax=axs[2][2])

    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35)
    plt.show()


if __name__ == '__main__':
    allstar_games = pd.read_csv('D:/DATA/MJ_LB_KB/allstar_games_stats.csv')
    print(" 1: Kobe Bryant \n 2: Lebron James \n 3: Michael Jordan")
    players_index(allstar_games, 'Michael Jordan')
