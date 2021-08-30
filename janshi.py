import rule
from mahjong.constants import EAST, SOUTH, WEST, NORTH

# 雀士クラス 雀士の手牌、河、自風、ツモの管理
# 向聴数計算、点数計算、打牌の選択を行う
class Janshi:
    # play=Trueとした場合, その雀士は自動で牌を切らずに入力された牌を切る
    def __init__(self, play=False):
        self.name = ''

        self.jikaze = EAST
        self.jikaze_str = '東家'

        self.tehai = []
        self.kawa = []
        self.tenbou = 25000

        self.riichi = False
        self.tenpai =False

        self.play = play

    # 配牌をとる
    def haipai(self, yama):
        self.tehai =  yama[0:13]
        del yama[0:13]

    # ツモを行う
    def tsumo(self, yama):
        hai = yama[0]
        del yama[0]
        self.tehai.append(hai)
        return hai

    # リーパイを行う
    def riipai(self):
        self.tehai = sorted(self.tehai, key = lambda t: t.number0to135)

    # 点棒を受け取る
    def get_tenbou(self, tensuu):
        self.tenbou += int(tensuu)

    # 点棒を支払う
    def lost_tenbou(self, tensuu):
        self.tenbou -= int(tensuu)

    # 打牌を行う
    def dahai(self, sutehai=13):
        # 立直状態での処理
        if self.riichi == True:
                hai = self.tehai[13]
                del self.tehai[13]
                return hai

        # プレイヤーが操作する場合の処理
        if self.play:
            hai = self.tehai[sutehai]
            del self.tehai[sutehai]
            self.kawa.append(hai)

        # NPCの場合の処理
        else:
            shantenvalue = [i for i in range(len(self.tehai))]
            for i in range(len(self.tehai)):
                shantenvalue[i] = rule.Rule.shantensuu(self.tehai[:i] + self.tehai[i + 1:])
            hai = self.tehai[shantenvalue.index(min(shantenvalue))]
            del self.tehai[shantenvalue.index(min(shantenvalue))]
            self.kawa.append(hai)
        return hai