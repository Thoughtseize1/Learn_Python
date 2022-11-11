from itertools import combinations


def all_sub_lists1(data):
    subs = []
    for i in range(0, len(data)):
        temp = [list(x) for x in combinations(data, i)]
        if len(temp) > 0:
            subs.extend(temp)
    return subs


def all_sub_lists(data):
    new_list = [[]]
    a = range(len(data) + 1)
    for item in a:
        for i in range(item):
            print(data[i:item])
            new_list.append(data[i:item])
    new_list.sort(key=len)
    return new_list


l1 = [4, 6, 1, 3]
print(all_sub_lists(l1))

