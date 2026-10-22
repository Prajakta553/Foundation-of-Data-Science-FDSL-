import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Load Dataset
# ---------------------------------------------------------

df = pd.read_csv('Attendance_Prediction.csv')

print("First 5 records:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())


# ---------------------------------------------------------
# 2. Line Plot
# Graph Name: Average Attendance by Age
# ---------------------------------------------------------

age_attendance = df.groupby('age')['attendance'].mean() * 100

plt.figure(figsize=(8, 5))
plt.plot(
    age_attendance.index,
    age_attendance.values,
    marker='o'
)

plt.title('Line Plot - Average Attendance by Age')
plt.xlabel('Age')
plt.ylabel('Attendance (%)')
plt.grid(True)
plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 3. Bar Plot
# Graph Name: Average Attendance by Course
# ---------------------------------------------------------

course_attendance = df.groupby('course')['attendance'].mean() * 100

plt.figure(figsize=(8, 5))
plt.bar(
    course_attendance.index,
    course_attendance.values
)

plt.title('Bar Plot - Average Attendance by Course')
plt.xlabel('Course')
plt.ylabel('Attendance (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 4. Histogram
# Graph Name: Distribution of Study Hours
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df['study_hours'],
    bins=10,
    edgecolor='black'
)

plt.title('Histogram - Distribution of Study Hours')
plt.xlabel('Study Hours')
plt.ylabel('Number of Students')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 5. Scatter Plot
# Graph Name: Study Hours vs Sleep Hours
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df['study_hours'],
    df['sleep_hours'],
    alpha=0.5
)

plt.title('Scatter Plot - Study Hours vs Sleep Hours')
plt.xlabel('Study Hours')
plt.ylabel('Sleep Hours')
plt.grid(True)
plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 6. Box Plot
# Graph Name: Distribution of Travel Time
# ---------------------------------------------------------

plt.figure(figsize=(7, 5))

plt.boxplot(
    df['travel_time_minutes']
)

plt.title('Box Plot - Distribution of Travel Time')
plt.ylabel('Travel Time (Minutes)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 7. Pie Chart
# Graph Name: Attendance Status Distribution
# ---------------------------------------------------------

attendance_counts = df['attendance'].value_counts().sort_index()

labels = ['Absent', 'Present']

plt.figure(figsize=(7, 7))

plt.pie(
    attendance_counts.values,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Pie Chart - Attendance Status Distribution')
plt.show()


# ---------------------------------------------------------
# 8. Heatmap
# Graph Name: Correlation Heatmap
# ---------------------------------------------------------

numeric_data = df[
    [
        'age',
        'study_hours',
        'sleep_hours',
        'travel_time_minutes',
        'attendance'
    ]
]

correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))

plt.imshow(
    correlation,
    cmap='coolwarm',
    interpolation='none'
)

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45,
    ha='right'
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title('Heatmap - Correlation of Numerical Variables')

# Show correlation values inside the heatmap
for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(
            j,
            i,
            round(correlation.iloc[i, j], 2),
            ha='center',
            va='center'
        )

plt.tight_layout()
plt.show()