import random
import time

def place_mock_order(symbol, side, order_type, quantity, price=None):

    order_id = random.randint(100000, 999999)

    # simulate market price if not given
    if order_type == "MARKET":
        price = round(random.uniform(30000, 70000), 2)

    response = {
        "orderId": order_id,
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "status": "FILLED",
        "executedQty": quantity,
        "avgPrice": price,
        "timestamp": int(time.time() * 1000)
    }

    return response
