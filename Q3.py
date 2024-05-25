import json
questions = { }
scores = 0
number=1
r = open("questions.txt",'r')
questions = json.load(r)
r.close()
print("python quiz programm")
print("Enter t for True or f for False")
name = input("Enter your full name: ")
for ques in questions.keys():
    print("Question",number,": ", ques)
    ans = input("The answer is ")
    #testing the result
    if ans.upper() == questions[ques].upper():
        scores = scores + 1
        print("Correct ")
    else:
        print ("Wrong")
    number = number + 1

#write the name and the score is a separate file
result={name:scores}
m = open("score.txt",'w')
result = json.dump(result,m)
m.close()