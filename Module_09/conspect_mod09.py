# Карирование
def greeting(mod):
    if mod.lower() == 'h':
        return hi_func
    else:
        return other_hi


def hi_func(name: str):
    print(f'Hi {name}')


def other_hi(name: str):
    print(f'Hello {name}')


a = greeting('H')

a('Nikita')


# Замыкание
def outer():
    cache = {}

    def inner_function(y):
        if y not in cache:
            acumulator = 0
            for i in range(1, y+1):
                acumulator += i
            cache[y] = acumulator
            print(cache[y])
        return cache.get(y)
    return inner_function


inner = outer()
inner(10)
inner(10)
