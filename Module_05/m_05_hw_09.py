def formatted_numbers():
    formatted_list = []
    formatted_list.append(
        "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
    for i in range(16):
        formatted_list.append(
            "|{0:<10}|{1:^10}|{2:>10}|".format(i, "{:x}".format(i), "{:b}".format(i)))
    return formatted_list


for el in formatted_numbers():
    print(el)
