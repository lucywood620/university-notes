def pay(rate,hours):
    if hours>40:
        overtime=hours-40
        overtimecost=overtime*rate*1.5
        normalcost=40*rate
        return overtimecost+normalcost
    else:
        return rate*hours

print(pay(2,44))


