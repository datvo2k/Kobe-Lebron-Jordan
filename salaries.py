import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle, islice
from matplotlib import cm


sns.set(font_scale=2)
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sns.set_context("paper", rc={"font.size": 15, "axes.titlesize": 15, "axes.labelsize": 15})


def convert_currency(val):
    """
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',', '').replace('$', '')
    return int(new_val)


def all_salary(input_csv):
    kobe = input_csv[input_csv["Player"] == "Kobe Bryant"]
    kobe.reset_index(inplace=True, drop=True)
    kobe_salary = kobe['Salary'].apply(convert_currency)

    lebron = input_csv[input_csv["Player"] == "Lebron James"]
    lebron.reset_index(inplace=True, drop=True)
    lebron_salary = lebron['Salary'].apply(convert_currency)

    MJ = input_csv[input_csv["Player"] == "Michael Jordan"]
    MJ.reset_index(inplace=True, drop=True)
    MJ_salary = MJ['Salary'].apply(convert_currency)

    fig, axs = plt.subplots(nrows=3)
    fig.suptitle('Salary', fontsize=20)

    sns.lineplot(x=MJ['Season'], y=MJ_salary, data=MJ, ax=axs[0], hue=MJ['Player'])
    axs[0].ticklabel_format(style='plain', axis='y')
    sns.lineplot(x=kobe['Season'], y=kobe_salary, data=kobe, ax=axs[1], hue=kobe['Player'])
    axs[1].ticklabel_format(style='plain', axis='y')
    sns.lineplot(x=lebron['Season'], y=lebron_salary, data=lebron, ax=axs[2], hue=lebron['Player'])
    axs[2].ticklabel_format(style='plain', axis='y')

    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35)
    plt.show()


if __name__ == '__main__':
    salaries = pd.read_csv('D:/DATA/MJ_LB_KB/salaries.csv')
    all_salary(salaries)
