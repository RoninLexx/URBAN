data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
] # БУДЕШЬ СПИСЫВАТЬ - НИЧЕМУ НЕ НАУЧИШЬСЯ !

def calculate_structure_sum(*args):
        counter = 0
        for i in args:
            if isinstance(i, int):
                counter += i
            if isinstance(i, str):
                counter += len(i)
            if isinstance(i, dict):
                for key in i.keys():
                    counter += calculate_structure_sum(key)
                for value in i.values():
                    counter += calculate_structure_sum(value)
            if isinstance(i, (list, tuple, set)):
                counter += calculate_structure_sum(*i)

        return counter

result = calculate_structure_sum(*data_structure)
print(result)
