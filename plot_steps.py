import matplotlib.pyplot as plt
import csv 
import glob
import sys
import numpy as np

def main():
    argvs = sys.argv[1:]
    # file_pattern = "res/steps/SubGoalFourrooms-v0*steps.csv"
    n_episodes = 2000
    mean_y = []
    sum_y = []
    for i, file_pattern in enumerate(argvs):
        # import pdb; pdb.set_trace()
        mean_y.append([0] * n_episodes)
        sum_y.append([0] * n_episodes)
        for run, file_path in enumerate(glob.glob(file_pattern+'*')):
            with open(file_path, "r", encoding='utf-8') as f:
                reader = csv.reader(f)
                for step, row in enumerate(reader):
                    mean_y[i][step] = 1/(1+run) * (run * mean_y[i][step] + int(row[0]))
                    sum_y[i][step] += int(row[0])
        plt.plot(list(range(n_episodes)), mean_y[i], label=file_pattern)
    plt.legend()
    plt.show()
    # plt.savefig(file_path.split('/')[-1] + '.png')

if __name__ == "__main__":
    main()