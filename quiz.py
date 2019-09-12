# Quiz Module

#import random

questions = ["What is 1+0", "What is 2+0", "What is 3+0", "What is 4+0"]

answers = ['1', '2', '3', '4']

total_questions = len(questions)
''' Will need to create text files to track the totals and dump at the beginning of each run so that totals can be added from current session.
May also consider using this to track and them adjust each time program is run instead of creating files to track individual quizzes. '''

# Create a list with full range
right_count = [0] * total_questions

with open('right_count.csv', 'r') as f:
    lines = f.readlines()
    #header = lines[0]
    #field_names = header.strip().split(',')
    #print(field_names)
    for row in lines:
        right = row.strip().split(',')

# Use for loop to load downloaded file into right list
for i in range(len(right)):
    right_count[i] = right[i]

# Create a list with full range
wrong_count = [0] * total_questions

with open('wrong_count.csv', 'r') as w:
    lines = w.readlines()
    #header = lines[0]
    #column_names = header.strip().split(',')
    #print(column_names)
    for row in lines:
        wrong = row.strip().split(',')


# Use for loop to load downloaded file into wrong list
for i in range(len(wrong)):
    wrong_count[i] = wrong[i]


#start accumulator for the total correct answers on quiz
cor_ans = 0


for i in range(total_questions + 1):
    #rand_index = random.randrange(total_questions)
    print(str(i+1) + ") " + questions[i])

    ans = input("Answer: ")

    if ans == answers[i]:
        print("Correct")
        cor_ans += 1
        right_count[i] = int(right_count[i]) + 1
        #f.write('1\n')
        #d.write('0\n')
    else:
        print("No: " + (answers[i]))
        wrong_count[i] = int(wrong_count[i]) + 1
        #d.write('1\n')
        #f.write('0\n')

# Moves right_count values to a file and stores them in a txt file.
#for i in right_count:

#   f.write(str(i))

#for i in wrong_count:
#    f.write(str(i))

#f.close()
#d.close()
with open('right_count.csv', 'w') as f:
    f.write(right_count)

with open('wrong_count.csv', 'w') as w:
    w.write(wrong_count)

print(f"You got {cor_ans} out of {total_questions} correct.")
