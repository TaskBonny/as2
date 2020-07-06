age = input("What is your age: ")
cigarette = input("Are you a cigarette addict,answer Yes/No:")
immune= input("Is your immune system too weak, answer Yes/No:")
chronic = input("Do you have a serve chronic disease, answer Yes/No:")
limit_age= 75
if int(age) > limit_age:
    age= True
else:
    age=False
if cigarette.capitalize() =="Yes":
    cigarette = True
elif cigarette.capitalize() =="No":
    cigarette = False
if chronic.capitalize() == "Yes":
    chronic = True
elif chronic.capitalize() == "No":
    chronic = False
if immune.capitalize() == "Yes":
    immune = True
elif immune.capitalize == "No":
    immune = False

risky="You are in risky group"
notrisky="You are not in risky group"
if age and cigarette == True:
    print(risky)
elif chronic or immune == True:
    print(risky)
elif cigarette or age and immune or chronic == True:
    print(risky)
else:
    print(notrisky)
