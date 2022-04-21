'''
HackerRank training
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Sample input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample output: 
    Berry
    Harry
'''

if __name__ == '__main__':
    students = [] 
    names = []
    scores = []
    
    print("Awaiting input data...")
    for _ in range(int(input())): # Number of students
        name = input()
        score = float(input())

        scores.append(score)
        students.append([name, score])
    
    # Ordered list of unique scores
    scores = sorted(set(scores))
    # 2nd lowest
    secLowest = scores[1]
    
    names = [ a[0] for a in students if a[1] == secLowest ]

    print(f"\n{'-'*10} Students with the second lowest score are:")
    for n in sorted(names):
        print(n)
