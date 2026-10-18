
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 25, 15, 30, 20])

categories = ["Python", "C++", "Java", "SQL", "Excel"]
values = [85, 70, 65, 90, 75]

# Create a figure with 15 subplots
fig, axes = plt.subplots(5, 3, figsize=(18, 22))
fig.suptitle("Matplotlib: Different Types of Graphs",
             fontsize=20, fontweight="bold")

axes = axes.flatten()

# 1. Line Graph
axes[0].plot(x, y, marker="o")
axes[0].set_title("1. Line Graph")

# 2. Bar Chart
axes[1].bar(categories, values)
axes[1].set_title("2. Bar Chart")
axes[1].tick_params(axis="x", rotation=45)

# 3. Horizontal Bar Chart
axes[2].barh(categories, values)
axes[2].set_title("3. Horizontal Bar Chart")

# 4. Scatter Plot
axes[3].scatter(x, y)
axes[3].set_title("4. Scatter Plot")

# 5. Pie Chart
axes[4].pie(values, labels=categories, autopct="%1.1f%%")
axes[4].set_title("5. Pie Chart")

# 6. Histogram
data = np.random.normal(50, 10, 500)
axes[5].hist(data, bins=20, edgecolor="black")
axes[5].set_title("6. Histogram")

# 7. Box Plot
axes[6].boxplot([values, y])
axes[6].set_title("7. Box Plot")

# 8. Area Chart
axes[7].fill_between(x, y, alpha=0.5)
axes[7].plot(x, y)
axes[7].set_title("8. Area Chart")

# 9. Stacked Bar Chart
first = [10, 20, 15, 25, 18]
second = [15, 10, 20, 15, 12]
axes[8].bar(categories, first, label="Group A")
axes[8].bar(categories, second, bottom=first, label="Group B")
axes[8].set_title("9. Stacked Bar Chart")
axes[8].tick_params(axis="x", rotation=45)
axes[8].legend()

# 10. Stem Plot
axes[9].stem(x, y)
axes[9].set_title("10. Stem Plot")

# 11. Step Plot
axes[10].step(x, y, where="mid")
axes[10].set_title("11. Step Plot")

# 12. Error Bar Chart
axes[11].errorbar(x, y, yerr=3, marker="o", capsize=5)
axes[11].set_title("12. Error Bar Chart")

# 13. Violin Plot
axes[12].violinplot([values, y], showmeans=True)
axes[12].set_title("13. Violin Plot")

# 14. Hexbin Plot
hx = np.random.randn(500)
hy = 2 * hx + np.random.randn(500)
axes[13].hexbin(hx, hy, gridsize=20)
axes[13].set_title("14. Hexbin Plot")

# 15. Polar Plot
theta = np.linspace(0, 2 * np.pi, 100)
radius = 2 + np.sin(5 * theta)
ax = fig.add_subplot(5, 3, 15, projection="polar")
ax.plot(theta, radius)
ax.set_title("15. Polar Plot")

# Improve layout
for ax in axes[:14]:
    ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.97])

# Save the graph collection
plt.savefig("matplotlib_all_graphs.png", dpi=300, bbox_inches="tight")

# Display all graphs
plt.show()
