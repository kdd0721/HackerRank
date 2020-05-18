def minion_game(s):
    # your code goes here
    vowel = "AEIOU"
    stuart = 0
    kevin = 0
    for i in range(len(s)):
        if s[i] in vowel:
            kevin += len(s)-i
        else:
            stuart += len(s)-i
    
    if stuart > kevin:
        print("Stuart",stuart)
    elif stuart < kevin:
        print("Kevin",kevin)
    else:
        return "Draw"

if __name__ == '__main__':
    minion_game("BANANA")