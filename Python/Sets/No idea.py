n, m = input().split()
my_list = input().split()
A = set(input().split())
B = set(input().split())

print(sum([(i in A)-(i in B) for i in my_list]))