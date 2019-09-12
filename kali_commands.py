# Quiz Module

#import random

questions = ["What command tells you your current directory?", "Command Checking your login", "What command for change directory?", "What command to move up one level?", "What command to list contents of directory?", "How do you get more detail with list command?", "What option do you use for help?", "What format to obtain a manual?", "How do search for a file?", "How do you find binaries?", "How do you find binaries in the PATH variable?", "What is a more powerful search?", "What is the format of the find command?", "What command displays processes?", "What switch follows 'ps' to display running processes?", "Which command filters in linux?", "Which symbol is for piping?", "Create a file with cat.", "How do you exit the prompt in Linux?", "How do you read a file in Linux?", "How do you append a file in Linux?", "How do you overwrite a file?", "How do you create a file with touch?", "How do you create a directory?", "How do you copy a file?", "How do you rename a file?", "How do you remove a file?", "How do you remove empty directory?", "What switch will remove directory and all files permanently?"]

answers = ['pwd', 'whoami', 'cd', 'cd ..', 'ls', 'ls -la', '-h', 'man file', 'locate file', 'whereis', 'which', 'find', 'find directory options expression', 'ps', 'aux', 'grep', '|', 'cat > file', 'CTRL-D', 'cat file', 'cat >> file', 'cat > file', 'touch file', 'mkdir directory', 'cp oldfile newfile', 'mv file file2', 'rm file', 'rmdir directory', 'rm -r directory']

num = len(questions)

cor_ans = 0
total_questions = num

for i in range(num):
    #rand_index = random.randrange(num)

    print(questions[i])

    ans = input("Answer: ")

    if ans == answers[i]:
        print("Correct")
        cor_ans += 1

    else:
        print("No: " + (answers[i]))

print(f"You got {cor_ans} out of {total_questions} correct.")
