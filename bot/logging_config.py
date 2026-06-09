import logging

def setup_logging():
    """Configures structured application logging to console and text file."""
    log_format = "%(asctime)s - [%(levelname)s] - %(message)s"
    
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler("trading_bot.log"),
            logging.StreamHandler()
        ]
    )