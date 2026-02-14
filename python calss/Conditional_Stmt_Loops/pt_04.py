#python cricet game
import random
print("Welcome to the Cricket Game")
target = random.randint(50, 150)
print(f"Target to win: {target} runs")
score = 0
while score < target:
    run = int(input("Enter runs scored in this ball (0-6): "))
    if run < 0 or run > 6:
        print("Invalid input! Please enter a number between 0 and 6.")
        continue
    score += run
    print(f"Current Score: {score}/{score//10}")