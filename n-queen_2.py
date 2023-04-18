class NQueenProblem:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.result = []

    def is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col or abs(row - i) == abs(col - self.board[i]):
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            self.result.append(self.board[:])
        else:
            for col in range(self.n):
                if self.is_valid(row, col):
                    self.board[row] = col
                    self.solve(row + 1)


n = 10
problem = NQueenProblem(n)
problem.solve()

print(len(problem.result))
