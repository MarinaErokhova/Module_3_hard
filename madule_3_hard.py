data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    summa = 0
    for i in args:
        if isinstance(i, int):
            summa = summa + i
        elif isinstance(i, str) and len(i) > 0:
            summa = summa + len(i)
        elif isinstance(i, list):
            summa = summa + calculate_structure_sum(*i)
        elif isinstance(i, tuple):
            summa = summa + calculate_structure_sum(*i)
        elif isinstance(i, set):
            summa = summa + calculate_structure_sum(*i)
        elif isinstance(i, dict):
            summa = summa + calculate_structure_sum(*i.keys())
            summa = summa + calculate_structure_sum(*i.values())
    return summa

result = calculate_structure_sum(data_structure)
print(result)