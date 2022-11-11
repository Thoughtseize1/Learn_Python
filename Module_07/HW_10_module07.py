
# Usefull Article -  https://pyprog.pro/python/py/dict/dict_generators.html

def make_request(keys: list, values: list):
    if len(keys) != len(values):
        return {}
    else:
        return {x: y for x, y in zip(keys, values)}


print(make_request(['name', 'age', 'email'], ['Nick', '23', 'nick@test.com']))
