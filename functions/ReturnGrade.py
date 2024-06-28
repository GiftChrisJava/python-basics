def printGrade(score):
    if score >= 90.0 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    else :
        return "F"
    
def main():
    score = eval(input("Enter a score : "))
    print("The grade is", printGrade(score))


main()