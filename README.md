# ApexTrader-Futures-Bot 🚀

An enterprise-ready, modular algorithmic order-routing terminal written in Python 3.x designed to interact with the Binance Futures USDT-M Testnet Exchange. 

This platform implements a robust decoupled multi-tier directory architecture that cleanly isolates system entry-points from underlying network connection layers. It features built-in multi-endpoint connection fallbacks, real-time input sanitization pipelines, and comprehensive multi-handler session logging to maintain complete execution trace history.

## Core Structural Highlights
* **Decoupled System Architecture:** Implements a strict separation of concerns across input parameter validation (`validators.py`), configuration management (`logging_config.py`), execution routing logic (`orders.py`), and cryptographic HTTP clients (`client.py`).
* **Resilient Network Layer:** Built with a fallback execution mechanism that loops through active network endpoints to minimize transaction routing failures caused by upstream exchange downtime.
* **Pre-Flight Input Sanitization:** Rejects malformed requests (e.g., fractional limits, improper sides, invalid price references) locally before network overhead or API signature compute occurs.
* **Dual-Sink Audit Logging:** Seamlessly broadcasts transactions to the active CLI terminal interface while simultaneously appending high-fidelity structured logs to `trading_bot.log`.

## Directory Structure
```text
ApexTrader-Futures-Bot/
├── bot/
│   ├── __init__.py          # Marks folder as a modular package
│   ├── client.py            # Signature engines & cryptographic HTTP client
│   ├── logging_config.py    # Multi-handler system logging setup
│   ├── orders.py            # Order parameter compiler & router
│   └── validators.py        # Input sanitation & rule enforcement
├── cli.py                   # User-facing CLI runtime gateway interface
├── requirements.txt         # Package dependency index
├── .env                     # Private application credential configurations
├── .gitignore               # Excludes sensitive data from version control
└── README.md                # System documentation manual