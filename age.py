#0-9 =F9
#10-19 - P8
#20-29 =P7
#30-39 =C6
#40-49 =C5
#50-59 =C4
#60-69 =C3
#70-79 =D2
#80-100 =D1

Name = input("What is your name?:")
Score = input("What was your score?:")
Int_score = int(Score)
if Int_score < 10:
    print("Hey", Name,"things must have been rough, you got an F9")
elif Int_score < 20:
    print("Hello", Name ,"imagine you survived on a thin line, you got a P8")
elif Int_score < 30:
    print("Hello",Name,"its not the end but ey, you got a P7") 
elif Int_score < 40:
    print("Hello", Name,"yooo lets fight, a C6 is what it was")
elif Int_score < 50:
    print("Hello", Name,"ey man not a bad run but you got a C5")           
elif Int_score < 60:
    print("Hello", Name,"almost their fam, its a C4")
elif Int_score < 70:
    print("Hello", Name, "eh you just missed it by a whisker , you got a C3")
elif Int_score < 80:
    print("Hello", Name,"we are almost hitting the bulls eye, you got a D2")
elif Int_score > 90:
    print("Hello", Name,"your the nigga your at the top of the food chain, you pocketed a D1")         