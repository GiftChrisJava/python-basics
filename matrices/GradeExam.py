def main() :
    # Students' answers to the questions
    answers = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']
    ]
    
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    
    for row in range(len(answers)):
        # count tracker has to be 0
        countCorrect = 0
        
        # count correct answers
        for i in range(len(answers[row])):
            if keys[i] == answers[row][i]:
                countCorrect += 1
                
        # print student and the grade
        print("Student", row, "'s correct count is", countCorrect, "representing", round(( countCorrect / len(keys) * 100), 0), "%")

main()