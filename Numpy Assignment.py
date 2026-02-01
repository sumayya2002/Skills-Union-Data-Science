import numpy as np

# Student test scores for 3 subjects (math, science, english)
scores = np.array([
    [85, 92, 78],
    [90, 88, 95],
    [75, 70, 85],
    [88, 95, 92],
    [65, 72, 68],
    [95, 88, 85],
    [78, 85, 82],
    [92, 89, 90]
])

# Student names
names = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'])

# Random 4x4 matrix for linear algebra operations
matrix_A = np.random.randint(1, 10, size=(4, 4))
matrix_B = np.random.randint(1, 10, size=(4, 4))

#Task 1.1 Average Scores per Student
average_score = np.mean(scores, axis=1)
print("Average Scores: ", average_score)
print('Average scores for each student:')

all_avgs = dict(zip(names, average_score))
for name, avg in all_avgs.items():
    print(f"{name}:{avg:.2f}")


#Task 1.2 Highest Scores in each subject
high_scores = np.max(scores,axis=0)
# print(high_scores)
print('The highest scores in each subjects are:')
print('The highest score in Math is ' + str(high_scores[0]) + ".")
print('The highest score in Science is ' + str(high_scores[1]) + ".")
print('The highest score in English is ' + str(high_scores[2]) + ".")


#Task 1.3 Select all students who scored above 90 in any subject
all_scores = dict(zip(names, scores))
# print(all_scores)
list_above90 = []
for name, score in all_scores.items():
    if (score >90).any():
        list_above90.append(name)
print("The students that scored atleast one subject over 90 are: "+ str(list_above90) )


#Task 1.4 Create a boolean mask to find students who passed all subjects (passing score is 70)
students_passed = []
for name, score in all_scores.items():
    if (score >= 70).all():
        students_passed.append(name)
print("The students that passed all subjects are :" + str(students_passed) )


# Task 2.1 Reshape the scores array to be 12x2

new_array_scores = scores.reshape(12,2)
print(new_array_scores)


# Task 2.2 Create a new array with standardized scores (subtract mean and divide by std dev)

mean = np.mean(scores)
print("Mean is" +str(mean))

standard = np.std(scores)
print('Standard deviation is '+str(standard))

standardised = (scores - mean)/standard
print("Standardised scores array:")
print(standardised)


# Task 2.3 Sort the students by their average score in descending order
sorted_students = sorted(all_avgs.items(),key=lambda item: item[1], reverse = True)
# print (sorted_students)
print("Students sorted by average score (Highest to Lowest):")
for name, avg in sorted_students:
    print(f"{name}: {avg:.2f}")

    
# Task 2.4 Use array methods to find min, max and mean for each subject
subject_min = scores.min(axis=0)
subject_max = scores.max(axis = 0)
subject_mean = scores.mean(axis = 0)
subjects = ["Math", "Science", "English"]
print("Subject min, max and mean:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: Min = {subject_min[i]}, Max = {subject_max[i]}, Mean = {subject_mean[i]}")


# Task 3.1 Multiply matrix_A and matrix_B using matrix multiplication
matrix_mul = matrix_A.dot(matrix_B)
print(matrix_mul)

# Task 3.2 Calculate the determinant of matrix_A
determinant = np.linalg.det(matrix_A)
print(determinant)

# Task 3.3 Find the inverse of matrix_A (if it exists)
inverse = np.linalg.inv(matrix_A)
print(inverse)

# Task 3.4 Calculate the eigenvalues of matrix_A
eig = np.linalg.eig(matrix_A)
print(eig)

# Task 4.1 Use broadcasting to add 5 points to all math scores (first column)
added_5 = scores[:,:1] + 5
print("Math scores, 5 added:")
print(added_5)

# Task 4.2 Find unique scores across all subjects
unique = np.unique(scores)
print("Unique Scores:")
print(unique)

# Task 4.3 Use boolean indexing to find students who scored above average in all subjects

above_avg = scores > subject_mean
# print(above_avg)
mask = np.all(above_avg, axis =1)

above_avg_students = names[mask]
print("Students above average in all subjects:", above_avg_students)