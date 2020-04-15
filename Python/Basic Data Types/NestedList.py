#https://www.hackerrank.com/challenges/nested-list/problem

arr = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]

second_score = sorted(list(set([score for name, score in arr])))[1]

for name, score in sorted(arr, key=lambda x: x[0]):
    if score==second_score:
        print(name)