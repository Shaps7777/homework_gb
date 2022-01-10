# Ежики работают как распаковщики и запаковщики
# Один ежик - списки и кортежи
def func(a, b, c):
    print(a, b, c)


date = [10, 20, 30]
func(*date)


# Два ежика - словари
def func_2(a, b, c):
    print(a, b, c)


date = {'a': 10, 'b': 20, 'c': 30}
func_2(**date)

def func_3(** kwargs):
    print(kwargs)


date = {'a': 10, 'b': 20, 'c': 30}
func_3(**date)

