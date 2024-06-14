# bounce.py
#
# Exercise 1.5

distance = 100

for bounce in range(1, 10+1):
    distance = (3/5) * distance
    print(f'{bounce} {round(distance, 4)}')