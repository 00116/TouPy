# 牌の種類などを管理する
class Hai:
    KIND = {0: '萬', 1: '筒', 2: '索', 3: '東', 4: '南', 5: '西', 6: '北', 7: '白', 8: '発', 9: '中'}
    AKADORA = {16: '赤5萬', 52: '赤5筒', 88: '赤5索'}

    # number0to135に0から135の整数を入力するとその牌の内容が生成される
    # self.kindは0~3までありそれぞれ萬子筒子索子字牌を表す
    # self.numberは数牌では数字(-1)を表し、字牌では0から順に東南西北白発中を表す
    # self.akaariは赤ドラが存在するゲームの際に全ての牌においてTrueとなる
    # self.akahaiはその牌自体が赤ドラの際にTrueとなる
    def __init__(self, number0to135, aka=False):
        self.number0to135 = number0to135
        self.akaari = aka
        self.akahai = False

        # 数牌の場合の処理
        if self.number0to135 < 108:
            self.kind = self.number0to135 // 36
            self.number = self.number0to135 // 4 - self.kind * 9
            if aka and self.number0to135 in self.AKADORA:
                self.str = self.AKADORA[self.number0to135]
                self.akahai = True
            else:
                self.str = str(self.number + 1) + self.KIND[self.kind]

        # 字牌の場合の処理
        else:
            self.kind = 3
            self.number = (self.number0to135 - 108) // 4
            self.str = self.KIND[self.kind + self.number]