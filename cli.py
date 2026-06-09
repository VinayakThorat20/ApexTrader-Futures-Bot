import argparse
import sys
from bot.logging_config import setup_logging
from bot.validators import validate_inputs
from bot.orders import execute_order

def main():
    setup_logging()
    
    parser = argparse.ArgumentParser(description="ApexTrader CLI - Advanced Algorithmic Interface Gateway")
    
    parser.add_argument("--symbol", type=str, required=True, help="Target pair ticker asset (e.g. BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL", "buy", "sell"])
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT", "market", "limit"])
    parser.add_argument("--quantity", type=float, required=True, help="Order asset quantity sizing allocation")
    parser.add_argument("--price", type=float, default=None, help="Target valuation price (Required for limit operations only)")

    args = parser.parse_args()

    # Sanitization
    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)
    except ValueError as val_err:
        print(f"\n❌ Operational Validation Blocked: {str(val_err)}")
        sys.exit(1)

    # Overview Output Print Screen
    print("\n" + "⚡" * 20)
    print(" 🛠️  APEXTRADER PIPELINE TRANSACTION SUMMARY")
    print(f" 🔹 Instrument Pair: {args.symbol.upper()}")
    print(f" 🔹 Strategy Action: {args.side.upper()}")
    print(f" 🔹 Strategy Intent: {args.type.upper()}")
    print(f" 🔹 Target Quantity: {args.quantity}")
    if args.price:
        print(f" 🔹 Base Trigger Target Value: ${args.price}")
    print("⚡" * 20)

    print("\nAuthorizing signature pathways and establishing connection channels...")
    result = execute_order(args.symbol, args.side, args.type, args.quantity, args.price)

    # Process Final Response Structure
    print("\n" + "=" * 40)
    if "error" in result:
        print(f"❌ EXECUTION ATTEMPT ROUTING FAILURE: {result['message']}")
    else:
        print("🚀 API NODE RESPONSE STATUS: TRANSACTION SUCCESSFUL")
        print(f" ▪️ Unique ID:       {result.get('orderId')}")
        print(f" ▪️ Pool Status:     {result.get('status')}")
        print(f" ▪️ Filled Quantity: {result.get('executedQty')}")
        print(f" ▪️ Realized Price:  ${result.get('avgPrice', 'N/A')}")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    main()