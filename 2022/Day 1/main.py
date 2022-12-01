inputList = open('./input.txt', 'r').readlines()
input = "".join(inputList)

elfCalories = input.split('\n\n')

perElfCalories = []

for elf in elfCalories:
    calories = elf.split('\n')
    totalCaloriesPerElf = 0
    for calorie in calories:
        totalCaloriesPerElf += int(calorie)
    perElfCalories.append(totalCaloriesPerElf)

perElfCalories.sort()

print(perElfCalories)

# puzzle 1
print(perElfCalories[-1])

print(perElfCalories[-1] + perElfCalories[-2] + perElfCalories[-3])
