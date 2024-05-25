import json
questions = { }
s = 0
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
    if ans.upper() == questions[ques].upper():
        s = s + 1
        print("Correct ")
    else:
        print ("Wrong")
    number = number + 1
result={name:s}
m = open("score.txt",'w')
result = json.dump(result,m)
m.close()