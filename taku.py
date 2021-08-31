import hai
from mahjong.constants import EAST, SOUTH, WEST, NORTH

# 卓クラス 山, 局数, 場風, ドラ表示牌の管理
class Taku:
    def __init__(self, aka=False):
        self.bakaze = EAST
        self.kyoku = 1
        self.hai = []
        self.aka = aka

        self.hai = [hai.Hai(i, self.aka) for i in range(136)]

        self.yama = self.hai.copy()

        self.kancounter = 0
        self.dora_hyouji = []
        self.dora_hyouji.append(self.yama[-(6 + self.kancounter * 2)])

        # 場に出たリー棒をカウントする
        self.riibou = 0

    # カンした際に実行 カンドラが増える(カン自体は未実装)
    def kan(self):
        self.kancounter += 1
        self.dora_hyouji.append(self.yama[-(6 + self.kancounter * 2)])