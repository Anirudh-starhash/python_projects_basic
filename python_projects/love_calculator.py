print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
count1=0
count2=0
for x in ['t','r','u','e']:
  if(x in name1 or x in name2):
    count1+=name1.count(x)+name2.count(x)
for x in ['l','o','v','e']:
  if(x in name1 or x in name2):
    count2+=name1.count(x)+name2.count(x)
score=int(str(count1)+str(count2))
if(score<10 or score>90):
  print(F"Your score is {score},you go together like coke and mentos.")
elif(score>=40 and score<=50):
    print(F"Your score is {score},you are alright together.")
else:
    print(F"Your score is {score}.")
