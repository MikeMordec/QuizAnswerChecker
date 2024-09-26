'''
Created on Apr 28, 2022

@author: michaelmordec
'''

def main():
    answers = ['A','C','A','A','D',
               'B','C','A','C','B',
               'A','D','C','A','D',
               'C','B','B','D','A']    
    file = open("students.txt",'r') 
    i = 0
    correct = 0
    incorrect = 0

    studentAnswers = []
    incorrectQuestion= []
    for line in file:
        studentAnswers.append(line.strip()) 
    
    for studentAnswer in studentAnswers:
        correctAnswer = answers[i]
        #print(studentAnswer,correctAnswer)
        if(studentAnswer==correctAnswer):
            correct = correct + 1
        else:
            incorrect = incorrect + 1
            incorrectQuestion.append(i)
        i=i+1
    file.close()
    
    
    if(correct >=15):
        print("You passed!")
    else:
        print("You failed!")
    print("Total Number Correct:",correct)
    print("Total Number Incorrect:",incorrect)
    print("Incorrect question numbers:",incorrectQuestion)
main()