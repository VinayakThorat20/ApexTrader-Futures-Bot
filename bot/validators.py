def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Performs rigorous sanitation checks on parameter inputs before API transmission."""
    if not symbol.isalnum():
        raise ValueError("Market asset symbol format is invalid (e.g. use BTCUSDT).")
        
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Execution strategy order side must be either 'BUY' or 'SELL'.")
        
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order execution parameters type must be 'MARKET' or 'LIMIT'.")
        
    if quantity <= 0:
        raise ValueError("Order sizing target quantity must be strictly greater than 0.")
        
    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Limit execution paths require a target trigger price greater than 0.")
        
    return True