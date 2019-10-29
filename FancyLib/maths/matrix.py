class Matrix:

    def __init__(self):
        self.inner_dict = {}
        self.rows = []
        self.cols = []
        self.default_val = ''


    def is_square(self):
        """
        Whether the matrix is a square matrix

        :return: bool
        """
        rows_len = len(self.rows)
        cols_len = len(self.cols)
        return rows_len != 0 and cols_len != 0 and rows_len == cols_len


    def set(self, row, col, val):
        """
        Insert or update a value in the matrix given row key and column key

        :param row: The row key
        :param col: The column key
        :param val: The value to be set
        """
        if row not in self.rows:
            self.insert_key_into_rows_cols(row, True)
            self.inner_dict[row] = {}
        if col not in self.cols:
            self.insert_key_into_rows_cols(col, False)
        self.inner_dict[row][col] = val
        self.auto_adjust(row, col)


    def insert_key_into_rows_cols(self, row_or_col, is_row: bool):
        """
        Update row or column key list by inserting new key into the correct position to ensure the order

        :param row_or_col: Row or column key
        :param is_row: Whether to insert into row key list (True) or column key list (False)
        """
        if is_row:
            row_str = str(row_or_col)
            rows_len = len(self.rows)
            for i in range(rows_len):
                if row_str < str(self.rows[i]):
                    self.rows.insert(i, row_or_col)
                    return
            self.rows.append(row_or_col)
        else:
            col_str = str(row_or_col)
            cols_len = len(self.cols)
            for i in range(cols_len):
                if col_str < str(self.cols[i]):
                    self.cols.insert(i, row_or_col)
                    return
            self.cols.append(row_or_col)


    def auto_adjust(self, row, col):
        """
        Fill in default values on given row and column

        :param row: The row key
        :param col: The column key
        """
        for r in self.rows:
            if col not in self.inner_dict[r]:
                self.inner_dict[r][col] = self.default_val
        for c in self.cols:
            if c not in self.inner_dict[row]:
                self.inner_dict[row][c] = self.default_val


    def auto_eliminate(self):
        """
        Remove rows or columns which is full of default values
        """
        tmp_rows = list(self.rows)
        for row in tmp_rows:
            if all((x == self.default_val for x in self.inner_dict[row].values())):
                self.eliminate_row(row)
        tmp_cols = list(self.cols)
        for col in tmp_cols:
            if all((x == self.default_val for x in (self.inner_dict[y][col] for y in self.rows))):
                self.eliminate_col(col)



    def get(self, row, col):
        """
        Get a value from matrix given row key and column key

        :param row: The row key
        :param col: The column key

        :return: (T) value
        """
        if row not in self.rows:
            raise Exception(f'Invalid row {row}')
        if col not in self.cols:
            raise Exception(f'Invalid col {col}')
        return self.inner_dict[row][col]


    def shape(self):
        """
        Get the shape of the matrix (row length and column length)

        :return: Tuple(row_length, column_length)
        """
        return (len(self.rows), len(self.cols))


    def get_row_vector(self, row):
        """
        Enumerate objects from a matrix row of a given row key

        :param row: The row key

        :return: (generator) values of the given row key
        """
        if row not in self.rows:
            raise Exception(f'Invalid row {row}')
        for col in self.cols:
            yield self.inner_dict[row][col]


    def get_col_vector(self, col):
        """
        Enumerate objects from a matrix column of a given column key

        :param col: The column key

        :return: (generator) values of the given column key
        """
        if col not in self.cols:
            raise Exception(f'Invalid column {col}')
        for row in self.rows:
            yield self.inner_dict[row][col]


    def eliminate_row(self, row):
        """
        Elimate a row from the matrix

        :param row: The row key
        """
        if row not in self.rows:
            raise Exception(f'Invalid row {row}')
        self.inner_dict.pop(row, None)
        self.rows.remove(row)


    def eliminate_col(self, col):
        """
        Elimate a column from the matrix

        :param col: The col key
        """
        if col not in self.cols:
            raise Exception(f'Invalid col {col}')
        for row in self.rows:
            if row in self.inner_dict:
                self.inner_dict[row].pop(col, None)
        self.cols.remove(col)


    def transpose(self):
        """
        Transpose the matrix
        """
        tmp = {}
        for col in self.cols:
            tmp[col] = {}
            for row in self.rows:
                tmp[col][row] = self.inner_dict[row][col]
        self.inner_dict = tmp
        tmp = None
        tmp = self.rows
        self.rows = self.cols
        self.cols = tmp
        tmp = None


    def output(self, print_with_row_col_labels: bool = True):
        """
        Print the matrix in a visualizable way

        :param print_with_row_col_labels: Whether to print row and column titles (default = True)
        """
        if print_with_row_col_labels:
            print('', end='\t')
            for col in self.cols:
                print(f'[{repr(col)}]', end='\t')
        print()
        for row in self.rows:
            if print_with_row_col_labels:
                print(f'[{repr(row)}]', end='\t')
            for col in self.cols:
                # repr(object): return a string containing a printable representation of an object
                # e.g. a string object will be printed with quates
                print(repr(self.inner_dict[row][col]), end='\t')
            print()
        print(self.rows)
        print(self.cols)


    def scale(self, new_rows:list, new_cols:list, auto_fill: bool = True):
        """
        Scale up or scale down the matrix using given row and col

        :param new_rows: A new row key list to scale up/down the current matrix's rows
        :param new_cols: A new column key list to scale up/down the current matrix's columns

        :return: A new Matrix instance after scaling
        """
        if not new_rows:
            new_rows = self.rows
        if not new_cols:
            new_cols = self.cols
        tmp_matrix = Matrix()
        for row in new_rows:
            if row in self.inner_dict or auto_fill:
                for col in new_cols:
                    if col in self.inner_dict[row]:
                        tmp_matrix.set(row, col, self.inner_dict[row][col])
                    elif auto_fill:
                        tmp_matrix.set(row, col, self.default_val)
        return tmp_matrix



m = Matrix()

m.set(4,5, 'v45')
m.set(0,10, 'v010')
m.set(0,5,'v05')
m.set(0,'20','v05')
m.set(0,0, 'v00')
m.set(0,1,'v01')
m.set(1,0,'v10')
m.set(1,1,'v11')
m.set(9,8,100)
print(m.cols)

m.output()
print()

# m.transpose()
# m.output()
# t = m.scale([1,9],[0,10,'20'])
# t.output()
m.eliminate_row(0)
m.eliminate_col(5)
m.output()
print()
m.auto_eliminate()
m.output()