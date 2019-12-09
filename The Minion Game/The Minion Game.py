def minion_game(string):
   
    #!/usr/bin/env python
    n = len(string)
    stuart = 0 # consonannts
    kevin = 0 # vowels
    vowels = ('A', 'E', 'I', 'O', 'U')
    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)