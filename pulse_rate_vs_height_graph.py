import matplotlib.pyplot as plt

n = int(input("Enter number of people: "))
pulse = [float(input(f"Pulse rate of person {i+1}: ")) for i in range(n)]
height = [float(input(f"Height of person {i+1}: ")) for i in range(n)]

plt.scatter(pulse, height)
plt.title("Pulse Rate vs Height")
plt.xlabel("Pulse Rate")
plt.ylabel("Height")
plt.show()