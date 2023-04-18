def solve_queens(n):
    # 初期化：全てのクイーンは-1行にあると仮定する
    positions = [-1] * n
    # 解の数をカウントする変数を初期化する
    count = 0
    # 列の選択

    def backtrack(row, col):
        nonlocal count  # 外部の変数を更新するためにnonlocalを使用する
        # 行の終了条件
        if row == n:
            count += 1  # 解の数を1つ増やす
            print_board(positions)  # 解の盤面を出力する
            return
        for i in range(col, n):
            # 同じ列にクイーンがないことを確認する
            if is_valid(row, i, positions):
                positions[row] = i
                backtrack(row + 1, col)
                positions[row] = -1
    # 盤面を出力する関数

    def print_board(positions):
        for row in range(n):
            line = ""
            for col in range(n):
                if positions[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")
    # クイーンの配置が可能かどうかを確認する関数

    def is_valid(row, col, positions):
        for i in range(row):
            if positions[i] == col or positions[i] - i == col - row or positions[i] + i == col + row:
                return False
        return True
    backtrack(0, 0)
    print("Total number of solutions:", count)  # 解の数を出力する


# 8クイーン問題を解く
solve_queens(8)
