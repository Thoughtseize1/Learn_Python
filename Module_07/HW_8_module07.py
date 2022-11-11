def token_parser(s: str):
    temp_int = ''
    count = len(s)
    leksema_list = []
    for sym in s:
        if sym.isdigit():
            temp_int += sym
            if count == 1:
                leksema_list.append(temp_int)
        elif sym in ('+', '-', '*', '/', '(', ')'):
            if temp_int:
                leksema_list.append(temp_int)
            leksema_list.append(sym)
            temp_int = ''
        count -= 1
    return leksema_list


print(token_parser('(2++    3) *4 - 5 * 3)+47'))
