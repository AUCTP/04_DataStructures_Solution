# Modify the code to build a program that calculates the average grade for each class instead of each student

grades = {
    'Mike': {
        'Finance': 12,
        'Marketing': 3,
        'Math': 0,
        'Economics': 10
    },
    'Sara': {
        'Finance': 10,
        'Programming': 12,
        'Econometrics': 3
    },
    'Julia': {
        'Marketing': 12,
        'Accounting': -3,
        'Programming': 10,
        'Finance': 7
    },
    'John': {
        'Project Management': 7,
        'Math': 12,
        'Economics': 3,
        'Econometrics': 10
    }
}

subjectCounts = {}
subjectGrades = {}

for grades in grades.values():
    for subject in grades.keys():
        subjectCounts[subject] = subjectCounts.get(subject, 0) + 1
        subjectGrades[subject] = subjectGrades.get(subject, 0) + grades[subject]

for subject in subjectCounts.keys():
    averageGrade = subjectGrades[subject]/subjectCounts[subject]
    print(f'{subject}: {averageGrade}')