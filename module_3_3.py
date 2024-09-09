def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = (3, 'стул', False)
values_dict = {'a': 7, 'b': True, 'c': 'вафля'}
values_list_2 = [37.18, 'СоРоКа']


print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(5, False)
print_params(5, c = 5)
print_params(b = 3, )
print_params(values_dict)
print_params(values_list)
print_params(*values_dict)
print_params(**values_dict)
print_params(*values_list)
print_params(*values_list_2, 42)
print_params(42, *values_list_2)

