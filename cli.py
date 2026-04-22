import argparse
from orders import place_order

def main():

    parser = argparse.ArgumentParser(description="Mock Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)   # BUY / SELL
    parser.add_argument("--type", required=True)   # MARKET / LIMIT
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        print("\n🚀 Placing Order...\n")

        response = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("✅ ORDER SUCCESS")
        print("----------------------")
        print("Order ID:", response["orderId"])
        print("Symbol:", response["symbol"])
        print("Side:", response["side"])
        print("Type:", response["type"])
        print("Status:", response["status"])
        print("Executed Qty:", response["executedQty"])
        print("Avg Price:", response["avgPrice"])
        print("----------------------")

    except Exception as e:
        print("❌ ERROR:", str(e))

if __name__ == "__main__":
    main()
