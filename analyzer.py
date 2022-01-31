# 2022 - Rafael Urben

import time
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

def random_list(n):
    l = list(range(n))
    random.shuffle(l)
    return l

def generate_graph(algorithm, lengths=10000, samples=10):
    print("Generating graph...")

    numberlist = range(1, lengths)
    timelist = []
    for listlength in tqdm(numberlist):
        unsortedlist = random_list(listlength)

        start = time.time()
        for _ in range(samples):
            sortedlist = algorithm(unsortedlist)
        end = time.time()

        wholetime = (end-start)
        timelist.append(wholetime/samples)
        
        plt.plot(timelist, "b.")
        plt.draw()
        plt.pause(0.0001)
        plt.clf()

    plt.plot(numberlist, timelist, "b.")
    plt.show()

if __name__ == '__main__':
    print("Don't run this file directly!")
