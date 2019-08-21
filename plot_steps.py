import matplotlib.pyplot as plt
import csv 
import glob
import sys
import pandas as pd
import seaborn as sns

def plot_state_values(file_path):
    plt.figure()
    state_values = []
    with open(file_path, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            state_values.append(list(map(float, row)))
    # import pdb; pdb.set_trace()    
    sns.heatmap(state_values, annot=True)
    plt.savefig("res/state_values.png")
    plt.close()
    # TODO show
    


def main():
    argvs = sys.argv[1:]
    # file_pattern = "res/steps/SubGoalFourrooms-v0*steps.csv"
    n_episodes = 2001
    mean_y = []
    for i, file_pattern in enumerate(argvs):
        mean_y.append([0] * n_episodes)
        # import pdb; pdb.set_trace()
        for file_path in glob.glob(file_pattern+'*'):
            with open(file_path, "r", encoding='utf-8') as f:
                reader = csv.reader(f)
                for step, row in enumerate(reader):
                    mean_y[i][step] = 1/(1+step) * (step * mean_y[i][step] + int(row[0]))
        plt.figure()
        plt.plot(list(range(n_episodes)), mean_y[i], label=file_pattern)
        plt.legend()
        # plt.show()
        plt.savefig(file_path.split('/')[-1] + '.png')
        plt.close()
    plot_state_values("res/Fourrooms-v0-0-values.csv")

if __name__ == "__main__":
    main()