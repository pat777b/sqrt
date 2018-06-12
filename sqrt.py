# sqrt takes in two positive integers. One integer is a number we want to take the square root of. The other number is the desired precision. It returns an approximate
# square root as a string as its output.


def sqrt(num1,precision):
    i: int = 0
    p: str = '0'
    y: int = 0
    x: int = 9
    c: str = ''
    rem: int = 0
    numstr: str = str(num1)
    while len(numstr) > 0:
        if len(numstr) < 2:
            c = c + numstr[0]
            k = int(c)
            p_int = int(p)
            while (x * (x + (20 * p_int))) > k:
                x -= 1
            y = x * (x + (20 * p_int))
            k -= y
            c = str(k)
            p = p + str(x)
            x = 9
            numstr = numstr[1:]
        else:
            c = c + numstr[0] + numstr[1]
            k = int(c)
            p_int = int(p)
            while (x * (x + 20 * p_int)) > k:
                x -= 1
            y = x * (x + (20 * p_int))
            k -= y
            c = str(k)
            p = p + str(x)
            x = 9
            numstr = numstr[2:]
    ans = p[1:] + '.'
    while i < precision:
        c = c + '00'
        k = int(c)
        p_int = int(p)
        while (x * (x + (20 * p_int))) > k:
            x -= 1
        y = x * (x + (20 * p_int))
        k -= y
        c = str(k)
        p = p + str(x)
        ans = ans + str(x)
        x = 9
        i += 1
    return ans


print(sqrt(2,100))