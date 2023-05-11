import time


# queenを置けるかどうかの判定をする関数
def judgment(board, row, col, n):
    # 同じ列をチェック
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 左上方向をチェック
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 右上方向をチェック
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# queenを配置する処理
def solve_queens_placement(board, row, n):
    # n-queen問題を解く事ができたら
    if row == n:
        # 全てのクイーンが配置された場合は解を出力
        print_board(board)
        return True

    for col in range(n):
        if judgment(board, row, col, n):
            board[row][col] = 1
            if solve_queens_placement(board, row + 1, n):
                return True
            board[row][col] = 0

    return False


def solve_queens(n):
    # 処理の実行時間の計測・開始
    start = time.time()
    # 初期化
    board = [[0] * n for _ in range(n)]

    # 第一引数に盤面の情報　第二引数に開始の行　第三引数に長さ
    if not solve_queens_placement(board, 0, n):
        print("解が存在しません")

    # 処理の実行時間の計測・終了
    end = time.time()
    elapsed_time = end - start
    print("n:", n)
    print("処理時間:", elapsed_time, "秒")


def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()


# n-queen問題を解く
n = 8
solve_queens(n)
