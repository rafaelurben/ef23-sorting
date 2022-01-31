# 2022 - Rafael Urben

from tqdm import tqdm
import matplotlib.pyplot as plt
import time
import random


def random_list(length):
    l = list(range(length))
    random.shuffle(l)
    return l


class SortingAlgorithm():
    def __init__(self, sortingfunc):
        self.sortingfunc = sortingfunc

    def sort(self, data, **kwargs):
        "Apply the sorting algorithm"

        return self.sortingfunc(data, **kwargs)

    def analyze(self, lengths=5000, samples=10, **kwargs):
        "Create a plot with the sorting algorithm"

        print("Generating graph...")

        numberlist = range(1, lengths)
        timelist = []
        for listlength in tqdm(numberlist):
            unsortedlist = random_list(listlength)

            start = time.time()
            for _ in range(samples):
                sortedlist = self.sortingfunc(unsortedlist, **kwargs)
            end = time.time()

            wholetime = (end-start)
            timelist.append(wholetime/samples)

            plt.plot(timelist, "b.")
            plt.draw()
            plt.pause(0.0001)
            plt.clf()

        plt.plot(numberlist, timelist, "b.")
        plt.show()

        return numberlist, timelist

    def test(self, length, **kwargs):
        "Test the algorithm with a random list with length"

        l = random_list(length)

        return self.sortingfunc(l, **kwargs)
