from collections.abc import Hashable
object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
object_list = [objects for objects in object_list if isinstance(objects, Hashable)]
index = [0 for i in range(len(object_list))]
for i in range(len(object_list)):
    for j in range(len(object_list)):
        if hash(object_list[i]) == hash(object_list[j]) and i != j:
            index[j] = 1
            index[i] = 1

print(sum(index))
# from collections.abc import Hashable
# newdic = {}
# for i in object_list:
#     if isinstance(i, Hashable):
#         newdic[hash(i)] = object_list.count(i)
# result = sum(ii for ii in newdic.values() if ii > 1)
# print(result)
