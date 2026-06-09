from bot.client import BinanceFuturesClient

def execute_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Compiles programmatic system orders down to formal endpoint API payload requests."""
    client = BinanceFuturesClient()
    
    payload = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
    }
    
    if order_type.upper() == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"  
        
    # Maps directly to the uniform demo trading pipeline order book
    return client.send_signed_request("POST", "/api/v3/order", payload)