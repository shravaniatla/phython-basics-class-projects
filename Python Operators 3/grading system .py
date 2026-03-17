hindi = 76
math = 78
social = 68
english = 79

total = (english + math + social + english)
percentage = (total/320)*100

if (percentage>=81)&(percentage<=100):
    print("grade A")
elif (percentage>=61)&(percentage<=80):
    print("Grade B")
elif (percentage>=41)&(percentage<=60):
    print("Grade C")
else:
    print("Grade F")