def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        sub = ''
        for a in s[i:i+k]:
            if a in sub:
                continue
            else:
                sub += a
        print(sub)
        sub=''   

if __name__ == '__main__':
    merge_the_tools('AABCAAADA', 3)