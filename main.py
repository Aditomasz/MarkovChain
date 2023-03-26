import random
import matplotlib.pyplot as plt
import numpy as np
import cv2

k = 0.4
p = 0.3
n = 0.3

last = "x"
player = "x"
ai = "x"
Z = np.ones(9)
balance = 0
stats = []
stats.append(balance)

print("Kamien(k), papier(p) czy nozyce(n)?:")
ai = np.random.choice(['k', 'p', 'n'], p=[k, p, n])
player = input()
if ai == "k":
    print("kamien")
    if player == "k":
        print("DRAW")
    elif player == "p":
        print("YOU WIN")
        balance = balance + 1
    else:
        print("YOU LOSE")
        balance = balance - 1
elif ai == "p":
    print("papier")
    if player == "k":
        print("YOU LOSE")
        balance = balance - 1
    elif player == "p":
        print("DRAW")
    else:
        print("YOU WIN")
        balance = balance + 1
elif ai == "n":
    print("nozyce")
    if player == "k":
        print("YOU WIN")
        balance = balance + 1
    elif player == "p":
        print("YOU LOSE")
        balance = balance - 1
    else:
        print("DRAW")
last = player
stats.append(balance)
while True:
    print("Do you want to play again? Y/N")
    player = input()
    if player == "N":
        break
    print("Kamien(k), papier(p) czy nozyce(n)?:")

    player = input()

    if last == "k":
        sum = Z[0] + Z[1] + Z[2]
        k = Z[2] / sum
        p = Z[0] / sum
        n = Z[1] / sum
        ai = np.random.choice(['k', 'p', 'n'], p=[k, p, n])
        if player == "k":
            Z[0] = Z[0] + 1
        if player == "p":
            Z[1] = Z[1] + 1
        if player == "n":
            Z[2] = Z[2] + 1
    if last == "p":
        sum = Z[3] + Z[4] + Z[5]
        k = Z[5] / sum
        p = Z[3] / sum
        n = Z[4] / sum
        ai = np.random.choice(['k', 'p', 'n'], p=[k, p, n])
        if player == "k":
            Z[3] = Z[3] + 1
        if player == "p":
            Z[4] = Z[4] + 1
        if player == "n":
            Z[5] = Z[5] + 1
    if last == "n":
        sum = Z[6] + Z[7] + Z[8]
        k = Z[8] / sum
        p = Z[6] / sum
        n = Z[7] / sum
        ai = np.random.choice(['k', 'p', 'n'], p=[k, p, n])
        if player == "k":
            Z[6] = Z[6] + 1
        if player == "p":
            Z[7] = Z[7] + 1
        if player == "n":
            Z[8] = Z[8] + 1

    if ai == "k":
        print("kamien")
        if player == "k":
            print("DRAW")
        elif player == "p":
            print("YOU WIN")
            balance = balance + 1
        else:
            print("YOU LOSE")
            balance = balance - 1
    elif ai == "p":
        print("papier")
        if player == "k":
            print("YOU LOSE")
            balance = balance - 1
        elif player == "p":
            print("DRAW")
        else:
            print("YOU WIN")
            balance = balance + 1
    elif ai == "n":
        print("nozyce")
        if player == "k":
            print("YOU WIN")
            balance = balance + 1
        elif player == "p":
            print("YOU LOSE")
            balance = balance - 1
        else:
            print("DRAW")
    last = player
    stats.append(balance)

Z = Z.reshape(3, 3)
print(Z)
plt.plot(stats)
plt.show()

