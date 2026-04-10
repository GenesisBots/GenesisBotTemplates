import json
from pathlib import Path
from datetime import datetime
from typing import List
import pandas as pd


class BrokerClient:
    def __init__(self, broker: str, mode: str):
        self.broker = broker
        self.mode = mode
        self._init_keys()

    def _init_keys(self):
        if self.mode == "paper":
            print("[INFO] Running in PAPER mode. No real orders will be sent.")
        else:
            print("[INFO] Running in LIVE mode. Make sure your keys and risk settings are correct.")

    def get_historical_data(self, symbol: str, timeframe: str, lookback_bars: int) -> pd.DataFrame:
        print(f"[MOCK] Fetching {lookback_bars} bars of {timeframe} data for {symbol}")
        idx = pd.date_range(end=datetime.utcnow(), periods=lookback_bars, freq="H")
        return pd.DataFrame({"close": range(lookback_bars)}, index=idx)

    def get_position(self, symbol: str) -> float:
        return 0.0

    def place_order(self, symbol: str, qty: float, side: str):
        if self.mode == "paper":
            print(f"[PAPER] {side.upper()} {qty} {symbol}")
        else:
            print(f"[LIVE] {side.upper()} {qty} {symbol}")


def load_config() -> dict:
    cfg_path = Path(__file__).parent / "config.example.json"
    with open(cfg_path, "r", encoding="utf-8") as f:
        return json.load(f)


def example_signal(prices: pd.Series, entry_threshold: float, exit_threshold: float) -> str:
    returns = prices.pct_change().dropna()
    momentum = returns.mean()

    if momentum > entry_threshold / 100.0:
        return "long"
    elif momentum < -entry_threshold / 100.0:
        return "short"
    elif abs(momentum) < exit_threshold / 100.0:
        return "flat"
    return "hold"


def run():
    cfg = load_config()
    mode = cfg.get("mode", "paper")
    broker_name = cfg.get("broker", "alpaca")

    broker = BrokerClient(broker_name, mode)

    symbols: List[str] = cfg.get("symbols", [])
    timeframe = cfg.get("timeframe", "1h")
    lookback = cfg.get("strategy", {}).get("lookback_bars", 50)
    entry_th = cfg.get("strategy", {}).get("entry_threshold", 1.5)
    exit_th = cfg.get("strategy", {}).get("exit_threshold", 0.5)

    for symbol in symbols:
        data = broker.get_historical_data(symbol, timeframe, lookback)
        signal = example_signal(data["close"], entry_th, exit_th)
        position = broker.get_position(symbol)

        print(f"[{symbol}] signal={signal}, position={position}")

        if signal == "long" and position <= 0:
            broker.place_order(symbol, qty=1, side="buy")
        elif signal == "short" and position >= 0:
            broker.place_order(symbol, qty=1, side="sell")
        elif signal == "flat" and position != 0:
            side = "sell" if position > 0 else "buy"
            broker.place_order(symbol, qty=abs(position), side=side)


if __name__ == "__main__":
    run()
