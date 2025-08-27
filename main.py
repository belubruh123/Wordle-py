import random

answer = ''

with open('word.txt', 'r') as f:
    lines = f.readlines()
    answer = lines[random.randint(1,14855)]

with open('word.txt','r') as f:
    for i in range(6):
        output = ''
        UserIn = input('Enter you word: ')
        valid = False
        for line in f:
            if UserIn in line:
                valid = True
                break
        if (valid == False):
            print('Not word in list!')
            i -= 1
            continue
        for a in range(5):
            if (UserIn[a] in answer):
                if (UserIn[a] == answer[a]):
                    output += '🟩'
                else:
                    output += '🟨'
            else:
                output += '⬛'
        if output == '🟩🟩🟩🟩🟩':
            print('You win!')
        else:
            print(UserIn + '\n' + output)
            if (i == 5):
                print('You failed :(')