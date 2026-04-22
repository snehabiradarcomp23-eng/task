from client import place_mock_order
from logger import logger

def place_order(symbol, side, order_type, quantity, price=None):

    logger.info(f"REQUEST -> {symbol}, {side}, {order_type}, {quantity}, {price}")

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order requires price")

    response = place_mock_order(symbol, side, order_type, quantity, price)

    logger.info(f"RESPONSE -> {response}")

    return response
