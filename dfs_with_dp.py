class LongestPathInASquareMatrixOptimized:

    def __init__(self):
        # Open file and loads:
        # n : matrix size
        # matrix: the matrix
        # additionally we set dp to a zero matrix
        with open("./tests/test1.txt", "r") as test_file:
            self.n = int(test_file.readline())
            self.matrix = []
            lines = test_file.readlines()
            for line in lines:
                self.matrix.append([eval(i) for i in line.split(' ')])
            self.dp = [[0] * self.n for _ in range(self.n)]

    def __dfs(self, i, j, prev, path, longest_path):
        # Method for find the longest path with given conditions

        # Frontier conditions and second rule defined by PDR team
        if i < 0 or i >= self.n or j < 0 or j >= self.n or abs(prev - self.matrix[i][j]) != 1:
            return 0

        # If we've already calculated longest path for the cell, we return the value
        if self.dp[i][j] != 0:
            return self.dp[i][j]

        path.append((i, j))

        if len(path) > len(longest_path):
            longest_path[:] = path

        actual_matrix_value = self.matrix[i][j]

        # Move down (recursion)
        down_movement = self.__dfs(i, j + 1, actual_matrix_value, path, longest_path)
        # Move right (recursion)
        right_movement = self.__dfs(i + 1, j, actual_matrix_value, path, longest_path)

        # Set dp value for a non calculated path
        self.dp[i][j] = max(down_movement, right_movement) + 1
        path.pop()
        return self.dp[i][j]

    def __get_longest_path(self):
        # function driver to iterate over matrix to find different paths using the dfs function
        # only if we have not calculated longest path (using dp matrix)
        # and saves the longest path and the max length of the path
        max_length = 0
        longest_path_indexes = []
        for i in range(self.n):
            for j in range(self.n):
                if self.dp[i][j] == 0:
                    path = []
                    path_sum = self.__dfs(i, j, self.matrix[i][j] - 1, path, longest_path_indexes)
                    max_length = max(max_length, path_sum)

        return max_length, longest_path_indexes

    def __get_formatted_path(self, longest_path_indexes):
        # function to transform indexes list to a values list
        path_list = []
        for indexes in longest_path_indexes:
            path_list.append(str(self.matrix[indexes[0]][indexes[1]]))
        return '-'.join(path_list)

    def longest_line_dance(self):
        # prints out to console info
        path_length, longest_path_indexes = self.__get_longest_path()
        print("Longest Endavans Line Dance is : {}".format(self.__get_formatted_path(longest_path_indexes)))
        print("Length of Path is : {}".format(path_length))


longest_path = LongestPathInASquareMatrixOptimized()
longest_path.longest_line_dance()
