import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('student_grades.csv')

# Display basic information
print(df.info())
print(df.describe())

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Fill missing grades with the mean
df['Grade'].fillna(df['Grade'].mean(), inplace=True)

# Remove duplicates
duplicates_before = df.duplicated().sum()
df.drop_duplicates(inplace=True)
duplicates_after = df.duplicated().sum()
print(f'Duplicates before removal: {duplicates_before}, after removal: {duplicates_after}')

# Ensure data types are correct
df['Name'] = df['Name'].astype(str)
df['Grade'] = df['Grade'].astype(float)

# Descriptive statistics
print(df.describe())

# Histogram of grades
sns.histplot(df['Grade'], bins=10)
plt.title('Grade Distribution')
plt.xlabel('Grades')
plt.ylabel('Frequency')
plt.show()

# Calculate average, max, and min grades
average_grade = df['Grade'].mean()
max_grade = df['Grade'].max()
min_grade = df['Grade'].min()

print(f'Average Grade: {average_grade:.2f}')
print(f'Maximum Grade: {max_grade}')
print(f'Minimum Grade: {min_grade}')

# Bar chart of grades
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Name'], df['Grade'], color='skyblue')
plt.title('Student Grades')
plt.xlabel('Students')
plt.ylabel('Grades')
plt.xticks(rotation=45)

# Annotate mean, max, and min
plt.text(x=0, y=average_grade + 1, s=f'Mean: {average_grade:.2f}', color='red')
plt.text(x=0, y=max_grade + 1, s=f'Max: {max_grade}', color='green')
plt.text(x=0, y=min_grade - 1, s=f'Min: {min_grade}', color='blue')

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
