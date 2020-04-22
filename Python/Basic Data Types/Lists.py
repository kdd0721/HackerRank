#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            eval('l.{0}{1}'.format(cmd,tuple(map(int,args))))
        else:
            print(l)