class Cell:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        return self.nums


    def __add__(self, other):
        return 'Sum of cells is ' + str(self.nums + other.nums)


    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'ячеек в первой клетке меньше или равно второй, вычитание невозможно'


    def __mul__(self, other):
        return 'Multiplay of cells is ' + str(self.nums * other.nums)


    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.nums / other.nums))


    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

cell_1 = Cell(10)
cell_2 = Cell(14)
print(cell_1 + cell_2)
print(cell_2.make_order(3))




