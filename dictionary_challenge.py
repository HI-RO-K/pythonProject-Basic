age = int(input("カジノへようこそ！年齢を入力してください！"))
casino_age = 18
game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー', '4': 'ダーツ'}
if age >= casino_age:
    print("あなたは{}歳ですね！ご利用いただけます。".format(age))
    while True:
        print("プレイするゲームを選択してください。")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(" :")
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました。")
            break
        else:
            print("1~3からお選びください")
else:
    print(f"あなたは{casino_age}歳未満なので、ご利用いただけません。")
