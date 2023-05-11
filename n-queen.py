"""
〜パラメータ〜
n:ボードの一辺のマス
x:横のマス
y:縦のマス
positions:n×nの二次元配列・-1はqueenが置けることを表す・０は他のクイーンの効き筋の領域・１は
クイーンが置かれている状態


〜処理の流れ〜
solve_queenにn×nのnを渡す
盤面：positionsを生成し全て-1に初期化
外のfor文でボードの縦方向を走査する
内のfor文でボードの横方向を走査する
クイーンを置けるか調べる
    →左から順に走査し、置く事ができるマス（-1）を見つける。
    →その行で置けなかったら次の行へ
クイーンを配置する
?positionsの情報を更新（置けないマスを０に更新する処理）
今いる行のfor文をスキップし、次の行のfor文の処理を行う
上記を繰り返し、終了したら結果表示

"""
import time


def prohibit(positions, n, col, row):
    # queenを置いた列に配置を禁止する処理(0に変える)
    for y in range(col + 1, n):  # col+1から始めることで、同じ列は変更しない(上書きを避ける)
        positions[y][row] = 0

    # 右下にかけて
    for i in range(1, min(n - col, n - row)):
        positions[col + i][row + i] = 0

    # 左下にかけて
    for i in range(1, min(n - col, row + 1)):
        positions[col + i][row - i] = 0


def solve_queens(n):
    # 処理の実行時間の計測・開始
    start = time.time()
    # 初期化：-1だったらクイーンを置く事ができる(リスト内包表記)
    positions = [[-1] * n for _ in range(n)]

    # 判定処理
    for col in range(n):
        for row in range(n):
            if positions[col][row] == -1:
                # queenを配置
                positions[col][row] = 1
                # 聞き筋のマスに置く事ができないようにする処理
                prohibit(positions, n, col, row)
                # 配置したので次の行の進む処理
                break
    # 処理の実行時間の計測・終了
    end = time.time()
    elapsed_time = end - start
    print("n:", n)
    print("処理時間:", elapsed_time, "秒")
    # print(positions)


# n-queen問題を解く・1万が限界
n = 8
solve_queens(n)
