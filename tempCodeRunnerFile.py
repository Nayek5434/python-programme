from vpython import *

print("3D Object Menu")
print("1. Curve\n2. Sphere\n3. Cone\n4. Arrow\n5. Ring\n6. Cylinder")
choice = int(input("Enter your choice: "))

if choice == 1:
    curve(pos=[vector(0,0,0), vector(1,1,0), vector(2,0,0)], radius=0.1)
elif choice == 2:
    sphere(radius=1, color=color.red)
elif choice == 3:
    cone(radius=1, length=2, color=color.green)
elif choice == 4:
    arrow(axis=vector(2,0,0), color=color.blue)
elif choice == 5:
    ring(radius=1, thickness=0.2, color=color.orange)
elif choice == 6:
    cylinder(radius=1, length=2, color=color.purple)
else:
    print("Invalid choice")