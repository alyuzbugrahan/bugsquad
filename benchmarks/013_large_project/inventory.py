STOCK = {"keyboard": 12, "mouse": 40, "monitor": 3, "cable": 100, "headset": 7}


def in_stock(name, quantity=1):
    return STOCK.get(name, 0) >= quantity
