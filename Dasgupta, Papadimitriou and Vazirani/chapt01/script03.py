# Functions

def division(x: int, y: int):
    """
    Division.
    """
    if x == 0:
        return (0, 0)

    q, r = division(int(x/2), y)

    q *= 2
    r *= 2

    if x % 2 == 1:
        r += 1

    if r >= y:
        r -= y
        q += 1

    return (q, r)

# Execution

if __name__ == '__main__':
    print(division(100, 5))
    print(division(999, 2))
