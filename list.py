# リスト（lists）:　複数のオブジェクトを順序づけて保持するデータ型
# []で括って、カンマ（、）で各オブジェクトを区切る
#            0         1       2         3     index
fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['string', 1, 3.4, True, fruits]

# print(hetro_list)
# print(fruits[0])
# print(fruits[-3])
# print(hetro_list[-1][-1])
# print("hello world"[3])

# .append: 新しいオブジェクトを追加する
print(fruits)
fruits.append('banana')
print(fruits)

# .insert: 指定したindexに指定したオブジェクトを追加する
fruits.insert(3, 'lemon')
print(fruits)
# .remove: マッチした最初のオブジェクトをのぞく
fruits.remove('peach')
print(fruits)
# .sort:　　昇順に並び替える
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# .len():  リストの要素数を取得する
print(len(fruits))
print(len("hello world"))
