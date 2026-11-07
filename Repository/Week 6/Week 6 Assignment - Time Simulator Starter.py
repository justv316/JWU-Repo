# Timer Simulation Program Starter

# 1. Ask the user how many seconds to count
count_limit = int(input("Enter the number of seconds for your timer: "))

# 2. Define a function to display the countdown
def countdown(second):
    print(f"Time: {second} second(s)")

# 3. Use a loop to simulate the countdown
## Use the reversed built-in function on the original range to reverse its order.
for second in reversed(range(1, count_limit + 1)):
    countdown(second)

# Optional Challenge:
# Add a message at the end: "Time's up!"
print("Times up!")