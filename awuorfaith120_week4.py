# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sm8dAqOYMQD3alQxEwLvojidcWQdI1mI
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading in our data
data = pd.read_csv("/content/scores.csv")
data.head(5)

"""a) Using the data from the csv file, select and plot any two of the subject scores with the student
names on the x-axis and scores on the y-axis.
"""

# Selecting two subject scores and student names
subject1 = "Math Score"
subject2 = "Science Score"

student_names = data["Name"]
subject1_scores = data[subject1]
subject2_scores = data[subject2]

# Plotting our graphs
plt.figure(figsize=(10, 6))

plt.plot(student_names, subject1_scores, color='indigo', label=subject1, marker = "o", linestyle = "-")

plt.xlabel('Student Names')
plt.ylabel('Scores')
plt.title('Subject Scores of Students')
plt.xticks(rotation=90)
plt.legend()

plt.tight_layout()
plt.grid(True)
plt.show()

plt.plot(student_names, subject2_scores, color= "green", label=subject2, marker = "o", linestyle = "-")

plt.xlabel('Student Names')
plt.ylabel('Scores')
plt.title('Subject Scores of Students')
plt.xticks(rotation=90)
plt.legend()

plt.tight_layout()
plt.grid(True)
plt.show()

"""b) Compute the mean score for each of the subjects and store the all the mean scores in a list."""

#Computing the mean score for each subject
mean_scores = data.mean()

#Extracting column names (subjects)
subjects = mean_scores.index.tolist()

# Creating a dictionary to associate each mean score with its corresponding subject
mean_scores_dict = dict(zip(subjects, mean_scores))

print("Mean scores for each subject:")
for subject, mean_score in mean_scores_dict.items():
    print(f"{subject}: {mean_score}")

#Converting the mean scores to a list
mean_scores_list = mean_scores.tolist()

print("Mean scores for each subject:", mean_scores_list)

"""c) Plot a histogram distribution of the mean scores with the subjects on the x-axis and the mean scores
on the y-axis.
"""

#Creating a bar plot
plt.figure(figsize=(10, 6))
plt.bar(subjects, mean_scores, color='skyblue', width=0.6)

#Adding labels and title
plt.xlabel('Subjects')
plt.ylabel('Mean Scores')
plt.title('Mean Scores Distribution by Subject')

#Displaying the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()