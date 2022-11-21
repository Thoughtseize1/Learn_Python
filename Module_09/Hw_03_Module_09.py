def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache.get(n)
        else:
            if n < 2:
                return n
            else:
                cache[n] = fibonacci(n-1)+fibonacci(n-2)
                return cache[n]
    return fibonacci


a = caching_fibonacci()
print(a(10))
print(a(11))
print(a(12))
print(a(13))
