# input(): ユーザの入力した値（文字列）を取得する

# age = input("何歳ですか？")
# print("あなたは{}歳です".format(age))

#　challenge1

age = int(input("カジノへようこそ！年齢を入力してください！"))
casino_age = 18
if age >= casino_age:
    print("あなたは{}歳ですね！ご利用いただけます。".format(age))
else:
    print("あなたは18歳未満なので、ご利用いただけません。")

# challenge2
print("カジノへようこそ！ゲームを以下から選んでください")
game_text = """
1:ルーレット
2:ブラックジャック
3:ポーカー
"""
game = input(game_text)
if game == "1":
    print("ルーレットへようこそ")
elif game == "2":
    print("ブラックジャックへようこそ")
elif game == "3":
    print("ポーカーへようこそ")
else:
    print("1:ルーレット"
          "2:ブラックジャック"
          "3:ポーカー"
          "のなかからお選びください")


