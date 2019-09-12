# Quiz Module

#import random

questions = ["What command tells you your current directory?", "Command Checking your login", "What command for change directory?", "What command to move up one level?", "What command to list contents of directory?", "How do you get more detail with list command?", "What option do you use for help?", "What format to obtain a manual?", "How do search for a file?", "How do you find binaries?", "How do you find binaries in the PATH variable?", "What is a more powerful search?", "What is the format of the find command?"]

answers = ['pwd', 'whoami', 'cd', 'cd ..', 'ls', 'ls -la', '-h', 'man file', 'locate file', 'whereis', 'which', 'find', 'find directory options expression']

num = len(questions)

for i in range(num):
    #rand_index = random.randrange(num)

    print(questions[i])

    ans = input("Answer: ")

    if ans == answers[i]:
        print("Correct")
    else:
        print("No: " + (answers[i]))

