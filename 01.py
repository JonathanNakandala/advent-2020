from data.data_01 import expenses

solution = []
for i, expense1 in enumerate(expenses):
    for expense2 in expenses[i:]:
        total = expense1 + expense2
        if total == 2020:
            solution.append(expense1)
            solution.append(expense2)

print(f"The two expenses that total 2020 are: {solution}")

multiplied = solution[0]*solution[1]

print(f"Their multiplication is {multiplied}")