def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return True

    if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
        return True
    elif len(flowerbed) == 1 and flowerbed[0] == 1 and n > 1:
        return False

    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 1 or flowerbed[i + 1] == 1:
            continue
        if flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1

    return n <= 0


print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
