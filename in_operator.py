# in演算子  リストの中にあるかどうかをTrue,falseで返す
fruits = ['apple', 'peach', 'melon', 'grapes', 'banana']
# print('apple' in fruits)

# challenge
print(fruits)
Likefruits = input("あなたの好きなフルーツは何ですか？")

if Likefruits in fruits:
    print("{}ですね、差し上げますよ".format(Likefruits))
    fruits.remove(Likefruits)

else:
    print("{}ですね、仕入れました。".format(Likefruits))
    fruits.append(Likefruits)
print("今あるフルーツはこちらです.{}".format(fruits))
