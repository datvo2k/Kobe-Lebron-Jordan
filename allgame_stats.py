import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from itertools import cycle
import numpy as np

cycol = cycle('bgrcmk')
sns.set(font_scale=1)
sns.set_context("paper", rc={"font.size": 15, "axes.titlesize": 15, "axes.labelsize": 15})
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
matplotlib.rcParams['font.weight'] = 'normal'


def show_attack(input_csv, input_string, option):
    # option: 0: regular season, 1: playoff
    player_index = input_csv[input_csv["Player"] == input_string]
    player_index.reset_index(inplace=True, drop=True)

    regular_season = player_index[player_index["RSorPO"] == 'Regular Season']
    regular_season.reset_index(inplace=True, drop=True)

    playoffs_season = player_index[player_index["RSorPO"] == 'Playoffs']
    playoffs_season.reset_index(inplace=True, drop=True)
    print(player_index)

    if option == 0:
        # show regular season
        fig, ax = plt.subplots(figsize=(16, 8), dpi=120)
        ax.plot(regular_season['Season'], regular_season['PTS'], label='PTS', c=next(cycol))
        ax.plot(regular_season['Season'], regular_season['AST'], label='AST', c=next(cycol))
        ax.plot(regular_season['Season'], regular_season['TRB'], label='TRB', c=next(cycol))
        ax.set_xticklabels(regular_season['Season'], rotation=45, ha="right", c=next(cycol))
        ax.legend()

        plt.title('{0} in Regular Season'.format(input_string))
        plt.xlabel('Season', fontsize=16)
        fig.tight_layout()
        plt.show()

    else:
        fig, ax = plt.subplots(figsize=(16, 8), dpi=120)
        ax.plot(playoffs_season['Season'], playoffs_season['PTS'], label='PTS', c=next(cycol))
        ax.plot(playoffs_season['Season'], playoffs_season['AST'], label='AST', c=next(cycol))
        ax.plot(playoffs_season['Season'], playoffs_season['TRB'], label='TRB', c=next(cycol))
        ax.set_xticklabels(playoffs_season['Season'], rotation=45, ha="right")
        ax.legend()

        plt.title('{0} in Playoffs'.format(input_string))
        plt.xlabel('Season', fontsize=16)
        fig.tight_layout()
        plt.show()


def convert_time(val):
    new_val = val.replace(':', '')
    new_val = int(new_val)
    new_val = new_val / 100
    return float(new_val)


def PTS_and_minutes(input_csv):
    kobe_index = input_csv[input_csv["Player"] == 'Kobe Bryant']
    kobe_index.reset_index(inplace=True, drop=True)
    lebron_index = input_csv[input_csv["Player"] == 'Lebron James']
    lebron_index.reset_index(inplace=True, drop=True)
    jordan_index = input_csv[input_csv["Player"] == 'Michael Jordan']
    jordan_index.reset_index(inplace=True, drop=True)

    fig, axs = plt.subplots(nrows=3)
    sns.scatterplot(kobe_index['MP'].apply(convert_time), kobe_index['GmSc'], data=kobe_index, color='r', ax=axs[0])
    axs[0].set_ylabel("Game Score", fontsize=14)
    axs[0].set_xlabel('')
    axs[0].set_title('Kobe Bryant')

    sns.scatterplot(lebron_index['MP'].apply(convert_time), lebron_index['GmSc'],
                    data=lebron_index, color='g', ax=axs[1])
    axs[1].set_ylabel("Game Score", fontsize=14)
    axs[1].set_xlabel('')
    axs[1].set_title('Lebron James')

    sns.scatterplot(jordan_index['MP'].apply(convert_time), jordan_index['GmSc'],
                    data=jordan_index, color='b', ax=axs[2])
    axs[2].set_xlabel("Minutes Played", fontsize=14)
    axs[2].set_ylabel("Game Score", fontsize=14)
    axs[2].set_title('Michael Jordan')

    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35)
    plt.show()


def total_PTS(input_csv):
    table = input_csv[['Player', 'PTS', 'AST', 'TRB']]
    total_point = table.groupby(['Player'], as_index=False)['TRB'].sum()
    print(total_point)

    f, ax = plt.subplots(figsize=(16, 8))
    sns.barplot(x=total_point['TRB'], y=total_point['Player'], data=total_point)
    ax.set_title('Total rebounds in their career', fontsize=14)
    ax.set_xlabel('Rebounds', fontsize=14)
    ax.set_ylabel('')
    plt.show()


def win_loss(input_csv):
    table = input_csv[['Player', 'Result']]
    print(table)

    kobe_index = table[table["Player"] == 'Kobe Bryant']
    kobe_index.reset_index(inplace=True, drop=True)
    lebron_index = table[table["Player"] == 'Lebron James']
    lebron_index.reset_index(inplace=True, drop=True)
    jordan_index = table[table["Player"] == 'Michael Jordan']
    jordan_index.reset_index(inplace=True, drop=True)

    kobe_win = kobe_index[kobe_index['Result'] == 'W'].count() / \
               (kobe_index[kobe_index['Result'] == 'W'].count() + kobe_index[kobe_index['Result'] == 'L'].count())

    lebron_win = lebron_index[lebron_index['Result'] == 'W'].count() / \
                 (lebron_index[lebron_index['Result'] == 'W'].count() + lebron_index[
                     lebron_index['Result'] == 'L'].count())

    jordan_win = jordan_index[jordan_index['Result'] == 'W'].count() / \
                 (jordan_index[jordan_index['Result'] == 'W'].count() + jordan_index[
                     jordan_index['Result'] == 'L'].count())

    f, ax = plt.subplots(figsize=(16, 8))
    X = np.arange(1)
    ax.bar(X + 0.00, kobe_win[1] * 100, color='b', width=0.1, label='Kobe Bryant')
    ax.bar(X + 0.25, lebron_win[1] * 100, color='g', width=0.1, label='Lebron James')
    ax.bar(X + 0.50, jordan_win[1] * 100, color='r', width=0.1, label='Michael Jordan')
    ax.set_ylabel('% Win', fontsize=14)
    ax.set_xticklabels('')
    ax.set_title('All career', fontsize=14)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    pre_game = pd.read_csv('D:/DATA/MJ_LB_KB/per_game_stats.csv')
    all_games = pd.read_csv('D:/DATA/MJ_LB_KB/allgames_stats.csv')

    # show_attack(pre_game, 'Michael Jordan', 1)
    total_PTS(all_games)
