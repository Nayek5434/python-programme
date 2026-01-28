import matplotlib.pyplot as plt

n = int(input("Enter number of integers: "))
data = [int(input(f"Enter integer {i+1}: ")) for i in range(n)]

plt.hist(data, bins=range(min(data), max(data)+2), edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()