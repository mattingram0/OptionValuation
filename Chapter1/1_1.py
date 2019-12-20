import numpy as np
import matplotlib.pyplot as plt


def main():
    # Input Data
    k1 = int(input("Strike Price 1: "))
    k2 = int(input("Strike Price 2: "))
    x = np.linspace(0, 6, 100)

    # Bull Spread: Buy a call with strike k1, sell a call with strike k2,
    # with k1 < k2
    y = np.maximum(x - k1, 0) - np.maximum(x - k2, 0)

    # Plot the data
    fig = plt.figure(figsize=(12.8, 9.6), dpi=250)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Bull Spread")
    ax.set_xlim([0, 6])
    ax.set_ylim([0, 6])
    ax.set_xlabel("S(T)")
    ax.set_ylabel("Payout")
    ax.plot(x, y)
    plt.show()


main()
