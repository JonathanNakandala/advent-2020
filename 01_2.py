from data.data_01 import expenses

solution = []
for i, expense1 in enumerate(expenses):
    for j, expense2 in enumerate(expenses[i:]):
        for expense3 in expenses[j:]:

            total = expense1 + expense2 + expense3
            if total == 2020:
                solution.append(expense1)
                solution.append(expense2)
                solution.append(expense3)

print(f"The two expenses that total 2020 are: {solution}")

multiplied = solution[0]*solution[1]*solution[2]

print(f"Their multiplication is {multiplied}")