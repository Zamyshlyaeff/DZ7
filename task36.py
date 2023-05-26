# Напишите функцию print_operation_table
# (operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число
# строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
# идет с единицы (подумайте, почему не с нуля).
num_rows=6
num_columns=6
operation=lambda x,y: x*y
def print_operation_table(operation, num_rows, num_columns):
     for x in range(1, num_rows + 1):
        for y in range(1, num_columns + 1):
            print(*list(map(operation, [x], [y])), end=' ')
        print()
    
    
            
print_operation_table(operation,num_rows, num_columns)



