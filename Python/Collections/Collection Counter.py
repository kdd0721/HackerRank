#https://www.hackerrank.com/challenges/collections-counter/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
from collections import Counter

n = int(input())
shoes = Counter(map(int, input().split()))
c_num = int(input())

income = 0

for i in range(c_num):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        shoes[size]-=1
        income+=price

print(income)