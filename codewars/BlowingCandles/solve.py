"""

Condition: Given a certain sets fo candles (have strength)

Target: return moves needed to blow the candles, 1 blow can decrease candle's strength by 1

"""

def blow_candles(st):
    a, b, res = 0, 0, 0
    for x in map(int, st):
        a, b = max(x - a - b, 0), a
        res += a
    return res
