p = [-1] * 2
print(p)
# class NQueenProblem:
#     def __init__(self, n):
#         self.n = n
#         self.board = [-1] * n
#         self.result = []

#     def is_valid(self, row, col):
#         for i in range(row):
#             if self.board[i] == col or abs(row - i) == abs(col - self.board[i]):
#                 return False
#         return True

#     def solve(self, row=0):
#         if row == self.n:
#             self.result.append(self.board[:])
#         else:
#             for col in range(self.n):
#                 if self.is_valid(row, col):
#                     self.board[row] = col
#                     self.solve(row + 1)


# n = 8
# problem = NQueenProblem(n)
# problem.solve()

# print(len(problem.result))


# def can_add(fwd, square):
#     tx = square % 8
#     ty = square // 8

#     # 縦の確認
#     if tx in fwd:
#         return False
#     # 横の確認
#     if fwd[ty] != -1:
#         return False
#     # 斜めの確認
#     if tx + ty in [fwd[i] + i for i in range(8) if fwd[i] != -1] \
#             or tx - ty in [fwd[i] - i for i in range(8) if fwd[i] != -1]:
#         return False
#     return True


# def solve(fwd, square):

#     if -1 not in fwd:
#         return 1

#     ans = 0
#     for i in range(square, 64):
#         if can_add(fwd, i):
#             ty = i // 8
#             fwd[ty] = i % 8
#             ans += solve(fwd, i + 1)
#             fwd[ty] = -1

#     return ans


# def main():
#     fwd = [-1 for _ in range(8)]
#     print(solve(fwd, 0))


# main()
