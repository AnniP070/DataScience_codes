#4. Create a line plot and bar chart to visualize categorical data using Matplotlib. Use all the possible operations on graphs.
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 10, 5]

plt.figure(figsize=(10, 5))

# Bar chart
plt.bar(categories, values, color='skyblue')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# line plot
plt.plot(categories, values, marker='o',color='orange')
plt.title('Line Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()