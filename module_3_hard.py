data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
        counter = 0
        for i in args:
            if isinstance(i, int):
                counter += i
            elif isinstance(i, str):
                if i is not int:
                    counter += len(i)
            elif isinstance(i, dict):
                if i.keys() is not int:
                    counter += len(i.keys())
                    counter += len(i.values())
            elif isinstance(i, (list, tuple, set)):
                counter += calculate_structure_sum(*i)

        return counter

result = calculate_structure_sum(*data_structure)
print(result)
