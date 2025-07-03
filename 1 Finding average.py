import numpy as np

student_scores = np.array([
    [85, 90, 78, 92],
    [88, 76, 85, 80],
    [90, 85, 88, 86],
    [70, 80, 75, 85]
])

subjects = ['Math', 'Science', 'English', 'History']
avg = np.mean(student_scores, axis=0)
print("Average scores:", avg)
print("Highest average subject:", subjects[np.argmax(avg)])
