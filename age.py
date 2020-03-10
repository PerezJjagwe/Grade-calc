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
    print("hey", Name,"F9")
elif Int_score < 20:
    print("Hello", Name ,"P8")
elif Int_score < 30:
    print("Hello",Name,"P7") 
elif Int_score < 40:
    print("Hello", Name,"C6")
elif Int_score < 50:
    print("Hello", Name,"C5")           
elif Int_score < 60:
    print("Hello", Name,"C4")
elif Int_score < 70:
    print("Hello", Name, "C3")
elif Int_score < 80:
    print("Hello", Name,"D2")
elif Int_score < 90:
    print("Hello", Name,"D1")         