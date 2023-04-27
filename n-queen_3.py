"""
〜パラメータ〜
n:ボードの一辺のマス
x:横のマス
y:縦のマス
positions:n×nの二次元配列・-1はqueenが置けることを表す・０は他のクイーンの可動領域・１は
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


def solve_queens(n):
    # 初期化：全てのクイーンは-1行にあると仮定する(リスト内包表記)
    positions = [[-1] * n for i in range(n)]

    for y in range(n):
        for x in range(n):
            if positions[x][y] == -1:
                positions[x][y] == 1
                break
            


# n-queen問題を解く
solve_queens(8)
