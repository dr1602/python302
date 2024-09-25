from set_array import Array

class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
            
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ''
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + ' '
                
            result += '\n'
                
        return str(result)
            
if __name__ == '__main__':
    from grid import Grid
    
    matrix = Grid(3, 3)
    print(matrix.__str__())

    for row in range(matrix.get_height()):
        for column in range(matrix.get_width()):
            matrix[row][column] = row * column
            
    print(matrix)
    
    print(matrix.get_height())
    # 3
    
    print(matrix.get_width())
    # 3
    
    print(matrix.__getitem__(1))
    # [0, 1, 2]
    
    print(matrix.__getitem__(1)[2])
    # 2
    
    print(matrix.__str__())