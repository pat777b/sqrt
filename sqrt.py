# sqrt takes in two positive integers. One integer is a number we want to take the square root of. The other number is the desired precision. It returns an approximate
# square root as a string as its output.


def sqrt(num1, precision):
    i: int = 0
    p: int = 0
    x: int = 9
    c: int = 0
    numstr: str = str(num1)
    if (len(numstr) % 2 == 1) and (len(numstr) > 2):
        c = 10*c + int(numstr[0])
        while (x * (x + 20 * p)) > c:
            x -= 1
        y = x * (x + (20 * p))
        c -= y
        p = 10*p + x
        x = 9
        numstr = numstr[1:]
    while len(numstr) > 0:
        if len(numstr) < 2:
            c = 10*c + int(numstr[0])
            while (x * (x + (20 * p))) > c:
                x -= 1
            y = x * (x + (20 * p))
            c -= y
            p = 10*p + x
            x = 9
            numstr = numstr[1:]
        else:
            c = 100*c + 10*int(numstr[0]) + int(numstr[1])
            while (x * (x + 20 * p)) > c:
                x -= 1
            y = x * (x + (20 * p))
            c -= y
            p = 10*p + x
            x = 9
            numstr = numstr[2:]
    ans = str(p) + '.'
    while i < precision:
        c = 100*c
        while (x * (x + (20 * p))) > c:
            x -= 1
        y = x * (x + (20 * p))
        c -= y
        p = 10*p + x
        ans = ans + str(x)
        x = 9
        i += 1
    return ans


print(sqrt(2, 1000000))

