import numpy as np
student_scores = np.random.randint(50, 101, size=(32, 4))
subject_averages = np.mean(student_scores, axis=0)
highest_avg_subject_index = np.argmax(subject_averages)
subjects = ["Math", "Science", "English", "History"]
highest_avg_subject = subjects[highest_avg_subject_index]
print("Subject averages:", subject_averages)
print("Subject with the highest average score:", highest_avg_subject)
