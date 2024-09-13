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
            if isinstance(i, str):
                counter += len(i)
            if isinstance(i, dict):
                for key in i.keys():
                    if isinstance(key, int):
                        counter += key
                    else:
                        counter += len(key)
                for value in i.values():
                    if isinstance(value, int):
                        counter += value
                    else:
                        counter += len(value)
            if isinstance(i, (list, tuple, set)):
                counter += calculate_structure_sum(*i)

        return counter

result = calculate_structure_sum(*data_structure)
print(result)
