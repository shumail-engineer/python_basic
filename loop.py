# 1. Using a for loop to print numbers from 1 to 5
print("1. For loop (1 to 5):")
for i in range(1, 6):
    print(i)

# 2. Using a while loop to print even numbers less than 10
print("\n2. While loop (even numbers < 10):")
num = 2
while num < 10:
    print(num)
    num += 2

# 3. Looping through a list
print("\n3. Looping through a list of fruits:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# 4. Using break and continue inside a loop
print("\n4. For loop with break and continue:")
for i in range(1, 10):
    if i == 3:
        print("Skipping 3 using continue")
        continue
    if i == 7:
        print("Breaking at 7")
        break
    print(i)
