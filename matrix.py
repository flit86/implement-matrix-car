import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
def dot_product(vector_one, vector_two):
    """
    Returns the dot product of two vectors
    """
    dot_prod = 0
    for i in range(len(vector_one)):
        dot_prod += vector_one[i]*vector_two[i]
    return dot_prod  

def get_row(matrix, row):
    """
        Get full row from a matrix
    """
    return matrix[row]
    

def get_column(matrix, column_number):
    """
    Get full column from a matrix
    """
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column  





class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h == 1:
            return self.g[0]
        if self.h == 2:
            return self.g [0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]
        # TODO - your code here

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
       
        count = 0
        for i in range(self.w):
            count += self.g[i][i]
        return count
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        inverse = []
        
        if self.w == 1:
            inverse.append([1 / self.g[0][0]])
        
        if self.w == self.h == 2:
                
                inverse = [[0, 0],[0,0]]
                a = self[0][0]
                b = self[0][1]
                c = self[1][0]
                d = self[1][1]
            
                factor = 1 / self.determinant()
            
                inverse[0][0] = d * factor
                inverse[0][1] = -b * factor
                inverse[1][0] = -c * factor
                inverse[1][1] = a * factor
    
        return Matrix(inverse)
        
        # TODO - your code here

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row.append(self.g[j][i])
            matrix_transpose.append(row)
        return Matrix(matrix_transpose)
        
        
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #
        matrix_Add = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            matrix_Add.append(row)
        
        return Matrix(matrix_Add)   
        # TODO - your code here
        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        matrix_Neg = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                matrix = (-1 * self.g[i][j])
                row.append(matrix)
            matrix_Neg.append(row)
        return Matrix(matrix_Neg)
        
        #   
        # TODO - your code here
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        
        matrix_Sub = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other.g[i][j])
            matrix_Sub.append(row)
        
        return Matrix(matrix_Sub)
        #   
        # TODO - your code here
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        m_rows = self.h
        p_columns = other.w
        
        
        matrix_Mul = []
        for i in range(m_rows):
            row = []
            for j in range(p_columns):
                
                dot_prod = dot_product(get_row(self.g,i), get_column(other.g,j))
                row.append(dot_prod)
            matrix_Mul.append(row)
        
        return Matrix(matrix_Mul)
        
        #   
        # TODO - your code here
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
             #   
            # TODO - your code here
            #
            
            
            new_matrix = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other * self.g[i][j])
                new_matrix.append(row)
            return Matrix(new_matrix)
        
            
            
            
           
            