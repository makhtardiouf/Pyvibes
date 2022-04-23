'''
HackerRank training
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Implemented in two ways.

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
#from timeit import timeit

def processWithLists():
    names, scores, students = [], [], []
    
    for _ in range(int(input())): # Number of students
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])
    
    print(students)

    # Ordered list of unique scores
    scores = sorted(set(scores))
    secLowest = scores[1] # 2nd lowest
    names = [ a[0] for a in students if a[1] == secLowest ]
    return names


def processWithDict():
    students = []
    for _ in range(int(input())):
        students.append( {'name': input(), 'score': float(input())} )
    
    # Sort by score & name
    students.sort(key=lambda s: (s['score'], s['name']))
    print(students)
    #breakpoint()

    scores = list(set([s['score'] for s in students]))
    secLowest = scores[1]
    names = [ print(s['name']) for s in students if s['score'] == secLowest ]
    return names


if __name__ == '__main__':
    print("Awaiting input data...")
    names = processWithDict()
    #names = processWithLists()

    print(f"\n{'-'*10} Students with the second lowest score are:")
    for n in sorted(names):
        print(n)
