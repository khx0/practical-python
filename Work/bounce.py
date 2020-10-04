# Exercise 1.5
# file: bounce.py 
# date: 2020-10-04

initial_height = 100.0

n_bounces = 10

height = initial_height

for i in range(n_bounces):

    height *= 3.0 / 5.0

    # print(i + 1, height)
    print(i + 1, round(height, 4))
