# whileループ
# count = 0
# while count < 10:
#     print(count)
#     count += 1
#
# # break continue
# while True:
#     age = int(input("あなたは何歳ですか？"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくありません")
#         continue
#     else:
#         print(f"あなたは{age}歳です")
#         break

# Challenge1
age = int(input("カジノへようこそ！年齢を入力してください！"))
casino_age = 18
if age >= casino_age:
    print("あなたは{}歳ですね！ご利用いただけます。".format(age))
else:
    print("あなたは18歳未満なので、ご利用いただけません。")

print("カジノへようこそ！ゲームを以下から選んでください")
game_text = """
1:ルーレット
2:ブラックジャック
3:ポーカー
"""
while True:
    game = input(game_text)
    if game == "1":
        print("ルーレットへようこそ")
        break
    elif game == "2":
        print("ブラックジャックへようこそ")
        break
    elif game == "3":
        print("ポーカーへようこそ")
        break
    else:
        print("1~3からお選びください")
        continue
