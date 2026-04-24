result = (lambda per : print("Grade A" if (per >= 90) else "Grade B" if (per >= 80) else
    "Grade C" if (per >= 70) else 
    "Fail"))

result(20)
result(70)
result(88)