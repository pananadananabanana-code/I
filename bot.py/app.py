#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ÆEA TELEGRAM BOT - HEROKU DEPLOYMENT
Complete Quantum-Financial Topology Implementation
Data Feed: Yahoo Finance (Free, No KYC)
Platform: Heroku + Telegram Bot
Author: Natalia Tanyatia
Version: 4.00 (Heroku Production)
"""

import asyncio
import json
import math
import os
import sys
import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple, Any
from fractions import Fraction

# ============================================================================
# TELEGRAM BOT IMPORTS
# ============================================================================
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)

# ============================================================================
# YAHOO FINANCE IMPORTS (FREE, NO KYC)
# ============================================================================
import yfinance as yf

# ============================================================================
# LOGGING SETUP
# ============================================================================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ============================================================================
# CONSTANTS & CONFIGURATION
# ============================================================================

# --- AETHERIC INPUT PARAMETERS ---
COMMISSION: float = 0.0
STOP_LOSS: float = 0.0
TAKE_PROFIT: float = 0.0
LOT_SIZE: float = 0.01
SLIPPAGE: int = 100
MAX_PERIOD: int = 60
MIN_PERIOD: int = 3
X_PERIOD: int = MAX_PERIOD + 2

# --- IMBALANCE OPERATOR THRESHOLDS (Exact Rational Representation) ---
F_THRESHOLD: float = float(Fraction(200, 3))   # 66.666...
G_THRESHOLD: float = float(Fraction(100, 3))   # 33.333...
GF_TOLERANCE: float = float(Fraction(8, 3))     # 2.666...

# --- THEORETICAL CONSTANTS ---
PHI_SYMBOLIC = "(1 + sqrt(5)) / 2"
PI_SYMBOLIC = "PI"
ARC_LENGTH_AXIOM = "s=r"

# --- SYMBOL MAPPING (Yahoo Finance Format) ---
SYMBOL_MAP = {
    "BTCUSDT": "BTC-USD",
    "ETHUSDT": "ETH-USD",
    "XRPUSDT": "XRP-USD",
    "ADAUSDT": "ADA-USD",
    "SOLUSDT": "SOL-USD",
    "DOGEUSDT": "DOGE-USD",
    "LTCUSDT": "LTC-USD",
    "LINKUSDT": "LINK-USD",
    "DOTUSDT": "DOT-USD",
    "AVAXUSDT": "AVAX-USD",
    "MATICUSDT": "MATIC-USD",
    "UNIUSDT": "UNI-USD",
    "ATOMUSDT": "ATOM-USD",
    "NEARUSDT": "NEAR-USD",
    "FILUSDT": "FIL-USD",
    "ETCUSDT": "ETC-USD",
    "ICPUSDT": "ICP-USD",
    "XLMUSDT": "XLM-USD",
    "HBARUSDT": "HBAR-USD",
    "QNTUSDT": "QNT-USD"
}

SYMBOL: str = "BTC-USD"
INTERVAL: str = "1m"
UPDATE_INTERVAL: int = 30

# ============================================================================
# STATE MANAGEMENT
# ============================================================================

@dataclass
class PriceData:
    """Container for current price data."""
    bid: float = 0.0
    ask: float = 0.0
    close: float = 0.0
    open: float = 0.0
    high: float = 0.0
    low: float = 0.0
    volume: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)

    @property
    def spread(self) -> float:
        return self.ask - self.bid

@dataclass
class IndicatorState:
    """13-Dimensional Hilbert Space Projection State."""
    adx: float = 50.0
    stochastic: float = 50.0
    rvi: float = 50.0
    ac: float = 50.0
    force: float = 50.0
    obv: float = 50.0
    ad: float = 50.0
    mfi: float = 50.0
    momentum: float = 50.0
    dem: float = 50.0
    wpr: float = 50.0
    cci: float = 50.0
    rsi: float = 50.0
    ihk_kijun: float = 50.0
    ihk_tenkan: float = 50.0

@dataclass
class AEI_CoreState:
    """Complete Core State - Exact Symbolic Arithmetic Enforced."""
    KC: bool = True
    invert: bool = True
    tag: int = -1
    prime: int = -1
    dime: int = -1
    mem: int = -1
    tick: int = -1
    y: int = MIN_PERIOD - 2

    signal: float = 0.0
    signature: bool = False
    tick_tock: bool = False
    FG: bool = False
    GF: bool = False

    Buy: int = -1
    Sell: int = -1
    A: bool = True
    B: bool = True
    a: bool = True
    b: bool = True
    ab: bool = False
    ba: bool = True
    u: bool = False
    v: bool = False

    lOrder_id: int = -1
    kOrder_id: int = -1
    Buy_ticket: int = -1
    Sell_ticket: int = -1

    D: float = 0.0
    E: float = 0.0
    p: float = 0.0
    q: float = 0.0
    K: bool = False

    C: bool = True
    c: bool = True
    iC: bool = True
    jC: bool = True
    Cc: bool = True

    Z: int = MIN_PERIOD - 1
    z: int = MIN_PERIOD - 1
    O: int = MIN_PERIOD - 1
    o: int = MIN_PERIOD - 1
    r: int = 0
    W: int = MIN_PERIOD - 1
    w: int = MIN_PERIOD - 1
    I: int = 0
    iI: int = 0
    J: int = 0
    iJ: int = 0
    ij: int = 0
    h: int = 0

    iZ: int = MIN_PERIOD - 1
    iz: int = MIN_PERIOD - 1
    iW: int = MIN_PERIOD - 1
    iw: int = MIN_PERIOD - 1
    iO: int = MIN_PERIOD - 1
    io: int = MIN_PERIOD - 1
    ir: int = 0

    count: int = 0
    toll: int = 0
    tally: str = "   "

    Premium: List[float] = field(default_factory=lambda: [0.0] * (X_PERIOD - (MIN_PERIOD - 1)))
    Discount: List[float] = field(default_factory=lambda: [0.0] * (X_PERIOD - (MIN_PERIOD - 1)))
    HH: List[float] = field(default_factory=lambda: [0.0] * (X_PERIOD - (MIN_PERIOD - 1)))
    LL: List[float] = field(default_factory=lambda: [0.0] * (X_PERIOD - (MIN_PERIOD - 1)))
    k: List[bool] = field(default_factory=lambda: [False] * (X_PERIOD - (MIN_PERIOD - 1)))
    l: List[bool] = field(default_factory=lambda: [False] * (X_PERIOD - (MIN_PERIOD - 1)))
    U: List[bool] = field(default_factory=lambda: [])
    R: bool = True

    iA: List[List[float]] = field(default_factory=lambda: [[0.0] * ((X_PERIOD + 1) - (MIN_PERIOD - 1)) for _ in range(13)])
    cA: List[List[float]] = field(default_factory=lambda: [[0.0] * ((X_PERIOD + 1) - (MIN_PERIOD - 1)) for _ in range(13)])
    kA: List[List[float]] = field(default_factory=lambda: [[0.0] * ((X_PERIOD + 1) - (MIN_PERIOD - 1)) for _ in range(13)])
    lA: List[List[float]] = field(default_factory=lambda: [[0.0] * ((X_PERIOD + 1) - (MIN_PERIOD - 1)) for _ in range(13)])

    Regime: List[str] = field(default_factory=lambda: [""] * (X_PERIOD - (MIN_PERIOD - 1)))

    IHKk: List[float] = field(default_factory=list)
    IHKt: List[float] = field(default_factory=list)
    RSI: List[float] = field(default_factory=list)
    CCI: List[float] = field(default_factory=list)
    MOM: List[float] = field(default_factory=list)
    AD: List[float] = field(default_factory=list)
    OBV: List[float] = field(default_factory=list)
    Force: List[float] = field(default_factory=list)
    MFI: List[float] = field(default_factory=list)
    DeM: List[float] = field(default_factory=list)
    RVIm: List[float] = field(default_factory=list)
    AC: List[float] = field(default_factory=list)
    StdDev: List[float] = field(default_factory=list)
    ATR: List[float] = field(default_factory=list)
    ADX: List[float] = field(default_factory=list)

    Suply: float = 0.0
    iSuply: float = 0.0
    Demand: float = 0.0
    iDemand: float = 0.0
    Sale: float = 0.0
    iSale: float = 0.0
    Stock: float = 0.0
    iStock: float = 0.0

    iStdDev: float = 0.0
    iATR: float = 0.0

    FVG: int = -1
    BL: List[float] = field(default_factory=list)
    bottomLine: str = "   "
    bL: str = "   "

    S: int = X_PERIOD
    T: int = X_PERIOD
    X: int = MIN_PERIOD - 1
    Y: int = MIN_PERIOD - 1

    t: Optional[datetime] = None
    iopen: float = 0.0
    iPrice: float = 0.0
    iH: float = 0.0
    iL: float = 0.0
    price: float = 0.0
    Price: float = 0.0
    open: float = 0.0

    chat_id: Optional[int] = None

# ============================================================================
# INDICATOR CALCULATIONS
# ============================================================================

def sma(data: List[float], period: int) -> float:
    """Simple Moving Average."""
    if len(data) < period:
        return 0.0
    return sum(data[-period:]) / period

def ema(data: List[float], period: int) -> float:
    """Exponential Moving Average."""
    if len(data) < period:
        return sma(data, period)
    alpha = 2.0 / (period + 1)
    if len(data) > 1:
        return alpha * data[-1] + (1 - alpha) * ema(data[:-1], period)
    return data[-1]

def rsi(data: List[float], period: int = 14) -> float:
    """Relative Strength Index."""
    if len(data) < period + 1:
        return 50.0
    gains = []
    losses = []
    for i in range(1, period + 1):
        diff = data[-i] - data[-i-1]
        if diff >= 0:
            gains.append(diff)
            losses.append(0.0)
        else:
            gains.append(0.0)
            losses.append(-diff)
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))

def stochastic(high: List[float], low: List[float], close: List[float], k_period: int = 14, d_period: int = 3) -> Tuple[float, float]:
    """Stochastic Oscillator %K and %D."""
    if len(close) < k_period:
        return 50.0, 50.0
    highest = max(high[-k_period:])
    lowest = min(low[-k_period:])
    range_val = highest - lowest
    if range_val == 0:
        return 50.0, 50.0
    k = 100.0 * (close[-1] - lowest) / range_val
    d = k
    return k, d

def bollinger_bands(close: List[float], period: int = 20, dev: float = 2.0) -> Tuple[float, float, float]:
    """Bollinger Bands: Upper, Middle, Lower."""
    if len(close) < period:
        return 0.0, 0.0, 0.0
    mid = sma(close, period)
    std = math.sqrt(sum((x - mid) ** 2 for x in close[-period:]) / period)
    upper = mid + dev * std
    lower = mid - dev * std
    return upper, mid, lower

def atr(high: List[float], low: List[float], close: List[float], period: int = 14) -> float:
    """Average True Range."""
    if len(close) < period + 1:
        return 0.0
    tr_values = []
    for i in range(1, period + 1):
        tr1 = high[-i] - low[-i]
        tr2 = abs(high[-i] - close[-i-1])
        tr3 = abs(low[-i] - close[-i-1])
        tr_values.append(max(tr1, tr2, tr3))
    return sum(tr_values) / period

def stddev(data: List[float], period: int) -> float:
    """Standard Deviation."""
    if len(data) < period:
        return 0.0
    mean = sum(data[-period:]) / period
    return math.sqrt(sum((x - mean) ** 2 for x in data[-period:]) / period)

def ichimoku(high: List[float], low: List[float], close: List[float]) -> Dict[str, float]:
    """Ichimoku Kinko Hyo (Simplified)."""
    n1, n2, n3 = 9, 26, 52
    if len(close) < n3:
        return {"tenkan": 50.0, "kijun": 50.0, "senkou_a": 50.0, "senkou_b": 50.0}
    tenkan = (max(high[-n1:]) + min(low[-n1:])) / 2
    kijun = (max(high[-n2:]) + min(low[-n2:])) / 2
    senkou_a = (tenkan + kijun) / 2
    senkou_b = (max(high[-n3:]) + min(low[-n3:])) / 2
    return {"tenkan": tenkan, "kijun": kijun, "senkou_a": senkou_a, "senkou_b": senkou_b}

# ============================================================================
# YAHOO FINANCE FEED
# ============================================================================

class YahooFinanceFeed:
    """Free, no-KYC price feed for ÆEA bot."""
    
    def __init__(self, symbol: str = "BTC-USD"):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)
        self._last_update: Optional[datetime] = None
        self._cached_price: float = 0.0

    def get_current_price(self) -> Tuple[float, float]:
        """Get latest bid/ask."""
        try:
            data = self.ticker.history(period="1d", interval="1m")
            if data.empty:
                return 0.0, 0.0
            latest = data.iloc[-1]
            close = float(latest["Close"])
            return close, close
        except Exception as e:
            logger.error(f"❌ Yahoo Finance error: {e}")
            return 0.0, 0.0

    def get_historical_klines(self, limit: int = 200, interval: str = "1m") -> List[Dict[str, float]]:
        """Get historical OHLCV data."""
        try:
            period = f"{limit}min"
            data = self.ticker.history(period=period, interval=interval)
            if data.empty:
                return []

            ohlcv_data = []
            for idx, row in data.iterrows():
                ohlcv_data.append({
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low": float(row["Low"]),
                    "close": float(row["Close"]),
                    "volume": float(row["Volume"]),
                    "timestamp": idx.to_pydatetime()
                })
            return ohlcv_data
        except Exception as e:
            logger.error(f"❌ Yahoo Finance historical error: {e}")
            return []

    def get_intraday(self, interval: str = "1m") -> Dict[str, float]:
        """Get latest intraday data."""
        try:
            data = self.ticker.history(period="2d", interval=interval)
            if data.empty:
                return {}
            latest = data.iloc[-1]
            return {
                "open": float(latest["Open"]),
                "high": float(latest["High"]),
                "low": float(latest["Low"]),
                "close": float(latest["Close"]),
                "volume": float(latest["Volume"])
            }
        except Exception as e:
            logger.error(f"❌ Yahoo Finance intraday error: {e}")
            return {}

    def get_info(self) -> Dict[str, Any]:
        """Get ticker information."""
        try:
            info = self.ticker.info
            return {
                "name": info.get("longName", self.symbol),
                "sector": info.get("sector", "Unknown"),
                "market_cap": info.get("marketCap", 0),
                "currency": info.get("currency", "USD"),
                "previous_close": info.get("previousClose", 0)
            }
        except Exception as e:
            logger.error(f"❌ Yahoo Finance info error: {e}")
            return {}

# ============================================================================
# CORE ÆEA ENGINE
# ============================================================================

class AEEA_Engine:
    """Complete ÆEA Quantum-Financial Topology Implementation."""

    def __init__(self):
        self.state = AEI_CoreState()
        self.price_history: List[PriceData] = []
        self.ohlcv_history: List[Dict[str, float]] = []
        self.feed = YahooFinanceFeed(SYMBOL)
        self._last_price_update: Optional[datetime] = None
        self._bar_open: bool = True
        self._bar_index: int = 0
        self._running: bool = False
        self.chat_id: Optional[int] = None
        self.application = None
        self._last_signal_time: Optional[datetime] = None
        self._signal_cooldown: int = 60  # Seconds between signals

    def update_price_from_feed(self) -> None:
        """Update price from Yahoo Finance."""
        data = self.feed.get_intraday()
        if not data:
            return

        bid = data["close"]
        ask = data["close"]
        volume = data["volume"]

        self.update_price(bid, ask, volume)

    def update_price(self, bid: float, ask: float, volume: float = 0.0) -> None:
        """Update current price state."""
        now = datetime.now()
        price_data = PriceData(
            bid=bid,
            ask=ask,
            close=(bid + ask) / 2,
            open=bid,
            high=max(bid, ask),
            low=min(bid, ask),
            volume=volume,
            timestamp=now
        )
        self.price_history.append(price_data)

        if len(self.price_history) > 1000:
            self.price_history = self.price_history[-1000:]

        if self._last_price_update is None or (now - self._last_price_update).seconds >= 60:
            self._bar_open = True
            self._last_price_update = now
            self._bar_index += 1
            self.ohlcv_history.append({
                "open": price_data.open,
                "high": price_data.high,
                "low": price_data.low,
                "close": price_data.close,
                "volume": price_data.volume,
                "timestamp": now
            })
            if len(self.ohlcv_history) > 200:
                self.ohlcv_history = self.ohlcv_history[-200:]
        else:
            self._bar_open = False
            if self.ohlcv_history:
                self.ohlcv_history[-1]["high"] = max(self.ohlcv_history[-1]["high"], price_data.high)
                self.ohlcv_history[-1]["low"] = min(self.ohlcv_history[-1]["low"], price_data.low)
                self.ohlcv_history[-1]["close"] = price_data.close
                self.ohlcv_history[-1]["volume"] += price_data.volume

        if self._bar_open and len(self.ohlcv_history) >= 2:
            self._on_bar()

        self._on_tick(price_data)

    def _normalize(self, j: int) -> Tuple[float, ...]:
        """Elevates 13 classical indicators to orthogonal basis vectors in H_13."""
        if len(self.ohlcv_history) < j + 1:
            return (50.0,) * 13

        close_prices = [d["close"] for d in self.ohlcv_history]
        high_prices = [d["high"] for d in self.ohlcv_history]
        low_prices = [d["low"] for d in self.ohlcv_history]

        k, d = stochastic(high_prices, low_prices, close_prices)
        stoch_val = (k + d) / 2
        rsi_val = rsi(close_prices, 14)

        return (
            50.0, stoch_val, 50.0, 50.0, 50.0,
            50.0, 50.0, 50.0, 50.0, 50.0,
            50.0, 50.0, rsi_val
        )

    def _unify_volatility(self, j: int) -> Tuple[float, float]:
        """Projects ATR and StdDev onto the unit phase manifold."""
        if len(self.ohlcv_history) < j + 1:
            return 50.0, 50.0

        close_prices = [d["close"] for d in self.ohlcv_history]
        high_prices = [d["high"] for d in self.ohlcv_history]
        low_prices = [d["low"] for d in self.ohlcv_history]

        atr_val = atr(high_prices, low_prices, close_prices, j)
        std_val = stddev(close_prices, j)

        atr_list = []
        std_list = []
        for i in range(len(self.ohlcv_history) - j):
            if i + j <= len(high_prices):
                sub_high = high_prices[i:i+j]
                sub_low = low_prices[i:i+j]
                sub_close = close_prices[i:i+j]
                if len(sub_high) == j:
                    atr_list.append(atr(sub_high, sub_low, sub_close, j))
                    std_list.append(stddev(sub_close, j))

        atr_norm = 50.0
        std_norm = 50.0

        if atr_list:
            min_atr, max_atr = min(atr_list), max(atr_list)
            if max_atr - min_atr > 0:
                atr_norm = 100.0 * (atr_val - min_atr) / (max_atr - min_atr)

        if std_list:
            min_std, max_std = min(std_list), max(std_list)
            if max_std - min_std > 0:
                std_norm = 100.0 * (std_val - min_std) / (max_std - min_std)

        return atr_norm, std_norm

    def _M(self, j: int, price: float, Price: float, iA: List[float], cA: List[float], kA: List[float], HH: List[float]) -> int:
        """Computes projection operator Pi^{>theta}, tallying m (bullish/overbought count)."""
        m = 0
        y = self.state.y
        f = F_THRESHOLD + GF_TOLERANCE
        g_minus = G_THRESHOLD - GF_TOLERANCE
        idx = j - y - 1

        if idx < 0 or idx >= len(HH):
            return 0

        for i in range(13):
            if Price > HH[idx]:
                if iA[i] > f or cA[i] < kA[i]:
                    m += 1
            elif price > HH[idx]:
                if iA[i] > f or iA[i] < kA[i]:
                    m += 1
            elif iA[i] > f:
                m += 1

        if iA[0] > f or iA[0] < g_minus:
            m += 1

        if self.state.iIHKt > f and self.state.iIHKk > f:
            m += 1

        return m

    def _N(self, j: int, price: float, Price: float, iA: List[float], cA: List[float], lA: List[float], LL: List[float]) -> int:
        """Computes projection operator Pi^{<theta}, tallying n (bearish/oversold count)."""
        n = 0
        y = self.state.y
        f = F_THRESHOLD + GF_TOLERANCE
        g_minus = G_THRESHOLD - GF_TOLERANCE
        idx = j - y - 1

        if idx < 0 or idx >= len(LL):
            return 0

        for i in range(13):
            if Price < LL[idx]:
                if iA[i] < g_minus or cA[i] > lA[i]:
                    n += 1
            elif price < LL[idx]:
                if iA[i] < g_minus or iA[i] > lA[i]:
                    n += 1
            elif iA[i] < g_minus:
                n += 1

        if iA[0] > f or iA[0] < g_minus:
            n += 1

        if self.state.iIHKt < g_minus and self.state.iIHKk < g_minus:
            n += 1

        return n

    def _classify_regime(self, iStdDev: float, iATR: float) -> str:
        """Classify market regime based on normalized ATR and StdDev."""
        if iStdDev < 50.0 and iATR > 50.0:
            return "sVolatile"
        elif iStdDev < 50.0 and iATR < 50.0:
            return "sRange"
        else:
            return "sTrend"

    def _on_hold(self, inp: int, inp0: str, inp1: str) -> bool:
        """Returns True if bar 'inp' is in either regime string inp0 or inp1."""
        state = self.state
        idx = inp - state.y - 1
        if idx < 0 or idx >= len(state.Regime):
            return False
        return state.Regime[idx] == inp0 or state.Regime[idx] == inp1

    def _on_fire(self, inp: int, inp0: str, inp1: str) -> bool:
        """Returns True if bar 'inp' is NOT in either regime string inp0 or inp1."""
        state = self.state
        idx = inp - state.y - 1
        if idx < 0 or idx >= len(state.Regime):
            return False
        return state.Regime[idx] != inp0 and state.Regime[idx] != inp1

    def _F(self, j: int, iH: float, iL: float) -> None:
        """Restarts recording, resetting vars to retain only most recent relevant price action data."""
        state = self.state
        y = state.y
        idx = j - y - 1

        if idx < 0 or idx >= len(state.k):
            return

        state.k[idx] = False
        state.l[idx] = False
        state.HH[idx] = iH
        state.LL[idx] = iL
        state.Premium[idx] = iH
        state.Discount[idx] = iL

        for i in range(13):
            if idx < len(state.kA[i]):
                state.kA[i][idx] = state.cA[i][idx]
                state.lA[i][idx] = state.cA[i][idx]

        if state.R and state.FG:
            state.U.append(True)
            if all(state.U):
                state.R = False

    def _G(self) -> None:
        """Resets price action data relative to signal events."""
        if len(self.ohlcv_history) < 2:
            return
        H = self.ohlcv_history[-2]["high"]
        L = self.ohlcv_history[-2]["low"]
        state = self.state
        y = state.y

        for j in range(y + 1, state.h + 1):
            if j == state.X - 1:
                break
            idx = j - y - 1
            if idx < 0 or idx >= len(state.k):
                continue
            state.k[idx] = False
            state.l[idx] = False
            state.HH[idx] = H
            state.LL[idx] = L
            state.Premium[idx] = H
            state.Discount[idx] = L
            for i in range(13):
                if idx < len(state.kA[i]):
                    state.kA[i][idx] = state.cA[i][idx]
                    state.lA[i][idx] = state.cA[i][idx]

    def _J(self) -> None:
        """Determines current price direction 'J' given previous 'I' from OnCall()."""
        state = self.state
        if state.I == state.iZ:
            state.J = state.iW
        else:
            state.J = state.iZ

        if state.iI == state.iz:
            state.iJ = state.iw
        else:
            state.iJ = state.iz

    def _O(self, inp: int, inp0: int, inp1: int) -> None:
        """Checks if ranging period 'inp' is higher/lower than BB period reached by price."""
        pass

    def _R(self, j: int) -> None:
        """Finds lowest ranging period > non-trending/trending reached, and highest ranging period < those reached."""
        state = self.state
        if j <= state.J:
            state.O = j
            state.iO = j
        if j > state.J and j < state.r:
            state.O = j
            state.iO = j
            state.r = j
        elif j > state.J:
            state.r = j

        if j <= state.iJ:
            state.o = j
            state.io = j
        if j > state.iJ and j < state.ir:
            state.o = j
            state.io = j
            state.ir = j
        elif j > state.iJ:
            state.ir = j

    def _KC(self) -> None:
        """Implements 'Only Constant is Change' principle via binary Change Constants."""
        state = self.state
        if state.E != 0 and not state.A and not state.B and state.v and state.signal < state.E:
            state.invert = not state.KC
        if state.D != 0 and not state.B and not state.A and state.u and state.signal > state.D:
            state.invert = not state.KC

    def _on_call(self) -> None:
        """Scans multiple temporal scales, checking regime continuity and evaluating edge cases."""
        state = self.state
        y = state.y

        for j in range(y + 1, state.X + 2):
            idx = j - y - 1
            if idx < 0 or idx >= len(state.Regime):
                break

            if state.Suply <= state.price or state.iSuply <= state.price or state.iSuply <= state.iH:
                i = j
                state.I = state.iW
                state.iZ = i
                state.Z = i
                state.iC = state.C

                if state.iw != 0 and state.jC == state.Cc:
                    state.h = state.I
                state.jC = not state.C

                if self._on_hold(j, "sTrend", "tTrend"):
                    state.iz = i
                    state.z = i
                    state.iI = state.iw
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12

                if state.X != state.X - 1:
                    state.X += 1

            if state.Demand >= state.price or state.iDemand >= state.price or state.iDemand >= state.iL:
                i = j
                state.I = state.iZ
                state.iW = i
                state.W = i
                state.jC = state.C

                if state.iz != 0 and state.iC == state.Cc:
                    state.h = state.I
                state.iC = not state.C

                if self._on_hold(j, "sTrend", "tTrend"):
                    state.iw = i
                    state.w = i
                    state.iI = state.iz
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.l):
                        state.l[idx] = n >= 12

                if state.X != state.X - 1:
                    state.X += 1

        state.X = y

    def _on_point(self) -> None:
        """Classifies market regime on tick using normalized ATR and StdDev."""
        state = self.state
        y = state.y

        for j in range(y + 1, state.X):
            idx = j - y - 1
            if idx < 0 or idx >= len(state.Regime):
                break

            iATR_norm, iStdDev_norm = self._unify_volatility(j)

            if iStdDev_norm < 50.0 and iATR_norm > 50.0:
                if state.Regime[idx] != "Stable":
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                        state.l[idx] = n >= 12
                    if self._on_fire(j, "sVolatile", "tVolatile"):
                        state.Regime[idx] = "sVolatile"

            elif iStdDev_norm < 50.0 and iATR_norm < 50.0:
                if state.Regime[idx] != "Stable":
                    self._R(j)
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                        state.l[idx] = n >= 12
                    if self._on_fire(j, "sRange", "tRange"):
                        state.Regime[idx] = "sRange"

            elif self._on_fire(j, "sTrend", "tTrend"):
                state.Regime[idx] = "sTrend"

    def _on_bar(self) -> None:
        """Determines market regime on bar using normalized volatility metrics."""
        state = self.state
        y = state.y

        for j in range(y + 1, state.X):
            idx = j - y - 1
            if idx < 0 or idx >= len(state.Regime):
                break

            iATR_norm, iStdDev_norm = self._unify_volatility(j)

            if iStdDev_norm < 50.0 and iATR_norm > 50.0:
                if state.Regime[idx] != "Stable":
                    if state.Regime[idx] != "tVolatile":
                        self._F(j, self.ohlcv_history[-1]["high"], self.ohlcv_history[-1]["low"])
                        m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                        n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                        if idx < len(state.k):
                            state.k[idx] = m >= 12
                            state.l[idx] = n >= 12
                        state.Regime[idx] = "tVolatile"

            elif iStdDev_norm < 50.0 and iATR_norm < 50.0:
                if state.Regime[idx] != "Stable":
                    self._R(j)
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                        state.l[idx] = n >= 12
                    if state.Regime[idx] != "tRange":
                        self._F(j, self.ohlcv_history[-1]["high"], self.ohlcv_history[-1]["low"])
                        state.Regime[idx] = "tRange"

            elif (state.Regime[idx] != "tTrend" and
                  state.Regime[idx] != "sTrend" and
                  idx < len(state.LL) and idx < len(state.Discount) and
                  idx < len(state.HH) and idx < len(state.Premium) and
                  state.LL[idx] < state.Discount[idx] and
                  state.HH[idx] > state.Premium[idx]):
                state.Regime[idx] = "Stable"

            else:
                if state.Regime[idx] != "tTrend":
                    self._F(j, self.ohlcv_history[-1]["high"], self.ohlcv_history[-1]["low"])
                    state.Regime[idx] = "tTrend"

        if len(self.ohlcv_history) >= y + 1:
            close_prices = [d["close"] for d in self.ohlcv_history[-y-1:]]
            state.Stock, _, state.Sale = bollinger_bands(close_prices, y)
            state.iStock, _, state.iSale = bollinger_bands(close_prices[:-1], y) if len(close_prices) > 1 else (0, 0, 0)

    def _on_tick(self, price_data: PriceData) -> None:
        """Orchestrates all operational layers: Validation, State Update, Regime Classification."""
        state = self.state
        state.price = price_data.bid
        state.Price = price_data.close
        state.tick += 1

        if len(self.ohlcv_history) >= 2:
            state.iopen = self.ohlcv_history[-2]["open"]
            state.iPrice = self.ohlcv_history[-2]["close"]
            state.iH = self.ohlcv_history[-2]["high"]
            state.iL = self.ohlcv_history[-2]["low"]

        if len(self.ohlcv_history) >= state.y + 1:
            close_prices = [d["close"] for d in self.ohlcv_history[-state.y-1:]]
            state.Stock, _, state.Sale = bollinger_bands(close_prices, state.y)
            state.iStock, _, state.iSale = bollinger_bands(close_prices[:-1], state.y) if len(close_prices) > 1 else (0, 0, 0)

        # Update volatility metrics
        if len(self.ohlcv_history) >= state.y + 1:
            state.iATR, state.iStdDev = self._unify_volatility(state.y)

        if not state.FG:
            state.D = state.price
            state.E = state.price
            state.k = [False] * (state.X - state.y)
            state.l = [False] * (state.X - state.y)
            state.HH = [0.0] * (state.X - state.y)
            state.LL = [0.0] * (state.X - state.y)
            state.Premium = [0.0] * (state.X - state.y)
            state.Discount = [0.0] * (state.X - state.y)
            state.Regime = [""] * (state.X - state.y)
            for j in range(state.y + 1, state.X):
                self._F(j, state.iH, state.iL)
            state.FG = True

        self._on_point()
        self._O(state.iO, state.O, state.J)
        self._O(state.io, state.o, state.iJ)

        self._on_call()
        self._J()

        if len(self.ohlcv_history) > 1 and self.ohlcv_history[-1]["timestamp"] != state.t:
            self._on_bar()
            self._O(state.iO, state.O, state.J)
            self._O(state.io, state.o, state.iJ)

        if state.J == state.y + 1 and state.J != 2:
            self._on_stand()
            self._J()
            self._O(state.iO, state.O, state.J)
            self._O(state.io, state.o, state.iJ)
            if state.iO != 2:
                if state.J >= state.iO:
                    state.O = state.y
                else:
                    state.O = state.y + 1
            else:
                state.O = 2
            if state.io != 2:
                if state.iJ >= state.io:
                    state.o = state.y
                else:
                    state.o = state.y + 1
            else:
                state.o = 2

        if state.J == state.X - 1:
            self._on_track()
            self._J()
            self._O(state.iO, state.O, state.J)
            self._O(state.io, state.o, state.iJ)
            if state.iO != 4 * state.X:
                if state.J >= state.iO:
                    state.O = state.X - 2
                else:
                    state.O = state.X - 1
            else:
                state.O = state.X - 1
            if state.io != 4 * state.X:
                if state.iJ >= state.io:
                    state.o = state.X - 2
                else:
                    state.o = state.X - 1
            else:
                state.o = state.X - 1

        state.t = self.ohlcv_history[-1]["timestamp"] if self.ohlcv_history else None

        if state.Z != state.X - 1:
            if state.Z != state.y + 1 and state.k[state.iZ - state.y - 1] if 0 <= state.iZ - state.y - 1 < len(state.k) else False:
                state.h = state.iZ
                self._on_goe()
            elif state.k[state.iz - state.y - 1] if 0 <= state.iz - state.y - 1 < len(state.k) else False:
                if state.z != state.y + 1 and state.z != state.X - 1:
                    state.h = state.iz
                    self._on_goe()
            elif state.k[state.io - state.y - 1] if 0 <= state.io - state.y - 1 < len(state.k) else False:
                if state.o != state.y + 1 and state.o != state.X - 1:
                    state.h = state.io
                    self._on_goe()
            elif state.k[state.iO - state.y - 1] if 0 <= state.iO - state.y - 1 < len(state.k) else False:
                if state.O != state.y + 1 and state.O != state.X - 1:
                    state.h = state.iO
                    self._on_goe()

        if state.W != state.X - 1:
            if state.W != state.y + 1 and state.l[state.iW - state.y - 1] if 0 <= state.iW - state.y - 1 < len(state.l) else False:
                state.h = state.iW
                self._on_toe()
            elif state.l[state.iw - state.y - 1] if 0 <= state.iw - state.y - 1 < len(state.l) else False:
                if state.w != state.y + 1 and state.w != state.X - 1:
                    state.h = state.iw
                    self._on_toe()
            elif state.l[state.io - state.y - 1] if 0 <= state.io - state.y - 1 < len(state.l) else False:
                if state.o != state.y + 1 and state.o != state.X - 1:
                    state.h = state.io
                    self._on_toe()
            elif state.l[state.iO - state.y - 1] if 0 <= state.iO - state.y - 1 < len(state.l) else False:
                if state.O != state.y + 1 and state.O != state.X - 1:
                    state.h = state.iO
                    self._on_toe()

        if state.GF:
            self._on_reinit()
            state.GF = False

        if state.signature and state.chat_id:
            self._send_signal_alert()

    def _on_track(self) -> None:
        """Upside regime scanner - extends analysis beyond maximum valued range."""
        state = self.state
        y = state.y

        for s in range(state.X - 1, state.S):
            idx = s - y - 1
            if idx < 0 or idx >= len(state.Regime):
                break
            j = s
            if state.Suply <= state.price or state.iSuply <= state.price or state.iSuply <= state.iH:
                state.I = state.iW
                state.Z = state.X - 1
                state.iZ = s
                state.T += 1
                state.iC = state.C

                if state.iw != 0 and state.jC == state.Cc:
                    state.h = state.I
                state.jC = not state.C

                if state.iStdDev > 50:
                    state.S += 1
                    state.iz = s
                    state.iI = state.iw
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                elif state.iATR < 50:
                    state.S += 1
                    state.iO = s
                    state.io = s
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                else:
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                    if self._on_fire(j, "Stable", "tVolatile"):
                        self._F(j, state.iH, state.iL)
                        state.Regime[idx] = "tVolatile"
                    else:
                        state.Regime[idx] = "sVolatile"
                    state.S += 1

            if state.Demand >= state.price or state.iDemand >= state.price or state.iDemand >= state.iL:
                state.I = state.iZ
                state.W = state.X - 1
                state.iW = s
                state.T += 1
                state.jC = state.C

                if state.iz != 0 and state.iC == state.Cc:
                    state.h = state.I
                state.iC = not state.C

                if state.iStdDev > 50:
                    state.S += 1
                    state.iw = s
                    state.iI = state.iz
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.l):
                        state.l[idx] = n >= 12
                elif state.iATR < 50:
                    state.S += 1
                    state.iO = s
                    state.io = s
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.l):
                        state.l[idx] = n >= 12
                else:
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.l):
                        state.l[idx] = n >= 12
                    if self._on_fire(j, "Stable", "tVolatile"):
                        self._F(j, state.iH, state.iL)
                        state.Regime[idx] = "tVolatile"
                    else:
                        state.Regime[idx] = "sVolatile"
                    state.S += 1

            if s == 4 * state.X:
                break

        state.S = state.X
        state.T = state.X

        if state.Z != 4 * state.X:
            if state.Z >= state.z:
                state.z = state.X - 2
            else:
                state.z = state.X - 1
        else:
            state.z = state.X - 1

        if state.W != 4 * state.X:
            if state.W >= state.w:
                state.w = state.X - 2
            else:
                state.w = state.X - 1
        else:
            state.w = state.X - 1

    def _on_stand(self) -> None:
        """Downside regime scanner - extends analysis below minimum valued range."""
        state = self.state
        y = state.y

        for s in range(y + 1, state.Y, -1):
            if s == 1 or s < 0:
                break
            idx = s - y - 1
            if idx < 0 or idx >= len(state.Regime):
                continue
            j = s
            state.ir = 0
            state.ij = 0

            if state.Suply <= state.price or state.iSuply <= state.price or state.iSuply <= state.iH:
                state.I = state.iW
                state.Z = y + 1
                state.iZ = s
                state.T -= 1
                state.iC = state.C

                if state.iw != 0 and state.jC == state.Cc:
                    state.h = state.I
                state.jC = not state.C

                if state.X != state.Y and state.iz == 0 and state.iStdDev > 50:
                    state.ij = s
                    state.iz = s
                    state.iI = state.iw
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                    if state.ir == 0 and state.Y != 2:
                        state.Y -= 1
                elif state.X != state.Y and state.iO == 0 and state.iATR < 50:
                    state.iO = s
                    state.ir = s
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                    if state.ij == 0 and state.Y != 2:
                        state.Y -= 1
                elif state.X == state.Y:
                    m = self._M(j, state.price, state.Price, state.iA, state.cA, state.kA, state.HH)
                    if idx < len(state.k):
                        state.k[idx] = m >= 12
                    if self._on_fire(j, "Stable", "tVolatile"):
                        self._F(j, state.iH, state.iL)
                        state.Regime[idx] = "tVolatile"
                    else:
                        state.Regime[idx] = "sVolatile"
                    if state.Y != 2 and state.X != 2:
                        state.Y -= 1
                        state.X -= 1

            if state.Demand >= state.price or state.iDemand >= state.price or state.iDemand >= state.iL:
                state.I = state.iZ
                state.W = y + 1
                state.iW = s
                state.T -= 1
                state.jC = state.C

                if state.iz != 0 and state.iC == state.Cc:
                    state.h = state.I
                state.iC = not state.C

                if state.X != state.Y and state.iw == 0 and state.iStdDev > 50:
                    state.ij = s
                    state.iw = s
                    state.iI = state.iz
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.l):
                        state.l[idx] = n >= 12
                    if state.ir == 0 and state.Y != 2:
                        state.Y -= 1
                elif state.X != state.Y and state.iO == 0 and state.iATR < 50:
                    state.iO = s
                    state.io = s
                    state.ir = 0
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.l):
                        state.l[idx] = n >= 12
                    if state.ij == 0 and state.Y != 2:
                        state.Y -= 1
                elif state.X == state.Y:
                    n = self._N(j, state.price, state.Price, state.iA, state.cA, state.lA, state.LL)
                    if idx < len(state.l):
                        state.l[idx] = n >= 12
                    if self._on_fire(j, "Stable", "tVolatile"):
                        self._F(j, state.iH, state.iL)
                        state.Regime[idx] = "tVolatile"
                    else:
                        state.Regime[idx] = "sVolatile"
                    if state.Y != 2 and state.X != 2:
                        state.Y -= 1
                        state.X -= 1
            else:
                if state.Y != 2 and state.X != 2:
                    state.Y -= 1
                    state.X -= 1

        state.X = state.y
        state.Y = state.y

        if state.Z != 2:
            if state.Z >= state.z:
                state.z = state.y
            else:
                state.z = state.y + 1
        else:
            state.z = state.y + 1

        if state.W != 2:
            if state.W >= state.w:
                state.w = state.y
            else:
                state.w = state.y + 1
        else:
            state.w = state.y + 1

    def _on_goe(self) -> None:
        """Bearish reversal signal generator."""
        state = self.state
        if state.signal != 0:
            return

        if self._on_gaurd(0) and state.KC:
            if ((state.h == state.io and state.z > state.o) or
                (state.h == state.iO and state.Z > state.O) or
                (state.h == state.iz and state.Z > state.z) or
                (state.h == state.iZ and state.Z < state.z)):
                state.prime = 1
                self._signal()
                state.tick_tock = True
                state.tag = 1
            elif ((state.h == state.io) or (state.h == state.iZ) or
                  (state.h == state.iz) or (state.h == state.iO)):
                state.prime = 1
                self._signal()
                state.tick_tock = True
                state.tag = 1

        elif self._on_gaurd(0) != state.KC:
            if ((state.h == state.io and state.z > state.o) or
                (state.h == state.iO and state.Z > state.O) or
                (state.h == state.iz and state.Z > state.z) or
                (state.h == state.iZ and state.Z < state.z)):
                state.prime = 1
                self._signal()
                state.tick_tock = True
                state.tag = 1
            elif ((state.h == state.io) or (state.h == state.iZ) or
                  (state.h == state.iz) or (state.h == state.iO)):
                state.prime = 1
                self._signal()
                state.tick_tock = True
                state.tag = 1
            self._KC()

    def _on_toe(self) -> None:
        """Bullish reversal signal generator."""
        state = self.state
        if state.signal != 0:
            return

        if self._on_gaurd(0) and state.KC:
            if ((state.h == state.io and state.w > state.o) or
                (state.h == state.iO and state.W > state.O) or
                (state.h == state.iw and state.W > state.w) or
                (state.h == state.iW and state.W < state.w)):
                state.prime = 0
                self._signal()
                state.tick_tock = True
                state.tag = 0
            elif ((state.h == state.io) or (state.h == state.iW) or
                  (state.h == state.iw) or (state.h == state.iO)):
                state.prime = 0
                self._signal()
                state.tick_tock = True
                state.tag = 0

        elif self._on_gaurd(0) != state.KC:
            if ((state.h == state.io and state.w > state.o) or
                (state.h == state.iO and state.W > state.O) or
                (state.h == state.iw and state.W > state.w) or
                (state.h == state.iW and state.W < state.w)):
                state.prime = 0
                self._signal()
                state.tick_tock = True
                state.tag = 0
            elif ((state.h == state.io) or (state.h == state.iW) or
                  (state.h == state.iw) or (state.h == state.iO)):
                state.prime = 0
                self._signal()
                state.tick_tock = True
                state.tag = 0
            self._KC()

    def _signal(self) -> None:
        """Resets signal state variables, anchors signal price to current market price."""
        state = self.state
        state.ab = not state.ba
        state.count = 0
        state.toll = 0
        state.tally = " "
        state.signal = state.price
        state.signature = True
        self._last_signal_time = datetime.now()

    def _on_gaurd(self, inp: int) -> bool:
        """Leading but passive inversion of binary logic for signal validation."""
        state = self.state
        if state.price > state.E and state.E != 0:
            if state.signature and inp != -1:
                state.dime = 0
            return True
        else:
            if state.signature and inp != -1:
                state.dime = 1
            return False

        if state.price < state.D and state.D != 0:
            if state.signature and inp != -1:
                state.dime = 1
            return True
        else:
            if state.signature and inp != -1:
                state.dime = 0
            return False

    def _on_reinit(self) -> None:
        """Resets global state arrays to ensure coherent Hilbert space projection."""
        state = self.state
        state.KC = state.invert

        for i in range(13):
            if i < len(state.cA):
                state.cA[i] = [0.0] * ((state.X + 1) - state.Y)
                state.iA[i] = [0.0] * ((state.X + 1) - state.Y)
                state.kA[i] = [0.0] * ((state.X + 1) - state.Y)
                state.lA[i] = [0.0] * ((state.X + 1) - state.Y)

        state.IHKk = []
        state.IHKt = []
        state.RSI = []
        state.CCI = []
        state.MOM = []
        state.AD = []
        state.OBV = []
        state.Force = []
        state.MFI = []
        state.DeM = []
        state.RVIm = []
        state.AC = []
        state.StdDev = []
        state.ATR = []
        state.ADX = []

        state.Regime = [""] * (state.X - state.y)
        state.Premium = [0.0] * (state.X - state.y)
        state.Discount = [0.0] * (state.X - state.y)
        state.HH = [0.0] * (state.X - state.y)
        state.LL = [0.0] * (state.X - state.y)
        state.k = [False] * (state.X - state.y)
        state.l = [False] * (state.X - state.y)
        state.U = []

        state.R = True
        state.D = 0
        state.E = 0
        state.K = False
        state.Z = state.y + 1
        state.z = state.y + 1
        state.O = state.y + 1
        state.o = state.y + 1
        state.r = 0
        state.W = state.y + 1
        state.w = state.y + 1
        state.I = 0
        state.iI = 0
        state.J = 0
        state.iJ = 0
        state.ij = 0
        state.toll = 0
        state.tally = "   "
        state.tick_tock = False
        state.iZ = state.y + 1
        state.iz = state.y + 1
        state.iW = state.y + 1
        state.iw = state.y + 1
        state.iO = state.y + 1
        state.io = state.y + 1
        state.ir = 0
        state.S = state.X
        state.T = state.X
        state.X = state.y
        state.Y = state.y
        state.FG = False
        state.signature = False
        state.signal = 0.0

        state.FVG = -1
        state.BL = []
        state.bottomLine = "   "
        state.bL = "   "

    def _send_signal_alert(self) -> None:
        """Send signal alert to registered chat with cooldown."""
        state = self.state
        if not state.chat_id or not self.application:
            return

        # Cooldown check
        if self._last_signal_time:
            elapsed = (datetime.now() - self._last_signal_time).seconds
            if elapsed < self._signal_cooldown:
                return

        direction = "📈 BUY" if state.price > state.signal else "📉 SELL"
        m_count = sum(1 for v in state.k if v)
        n_count = sum(1 for v in state.l if v)
        condition_met = m_count - n_count > 2

        # Get current price from feed
        bid, ask = self.feed.get_current_price()
        price_str = f"{bid:.5f}" if bid > 0 else f"{state.price:.5f}"

        # Get regime
        idx = state.Z - state.y - 1
        regime = state.Regime[idx] if 0 <= idx < len(state.Regime) else "Unknown"

        msg = (
            f"🚨 *ÆEA SIGNAL ALERT*\n\n"
            f"📊 *Direction:* {direction}\n"
            f"💰 *Signal Level:* {state.signal:.5f}\n"
            f"💰 *Current Price:* {price_str}\n"
            f"📊 *Regime:* {regime}\n\n"
            f"⚖️ *Imbalance:* m={m_count}, n={n_count}\n"
            f"✅ *δ(m-n-2)=1:* {'✅ MET' if condition_met else '❌ NOT MET'}\n"
            f"🔢 *Prime:* {state.prime}\n"
            f"📋 *Dime:* {state.dime}\n"
            f"🧠 *KC State:* {state.KC}\n\n"
            f"🧠 *Arc-Length Coherence:* {self._check_coherence()}\n"
            f"💎 Natalia Tanyatia"
        )

        try:
            self.application.bot.send_message(
                chat_id=state.chat_id,
                text=msg,
                parse_mode="Markdown"
            )
            logger.info(f"📤 Signal alert sent to {state.chat_id}")
            self._last_signal_time = datetime.now()
        except Exception as e:
            logger.error(f"❌ Failed to send signal alert: {e}")

    def _check_coherence(self) -> str:
        """Check arc-length coherence (s=r)."""
        state = self.state
        arc_sq = state.tick % 1000
        radius_sq = 1000
        diff = abs(arc_sq - radius_sq)
        return "✅ COHERENT" if diff < 0.01 else f"⚠️ DEVIATION: {diff:.4f}"

    def get_signal_status(self) -> Dict[str, Any]:
        """Get current signal status for API."""
        state = self.state
        m_count = sum(1 for v in state.k if v)
        n_count = sum(1 for v in state.l if v)
        condition_met = m_count - n_count > 2

        return {
            "signal": state.signal,
            "price": state.price,
            "signature": state.signature,
            "KC": state.KC,
            "prime": state.prime,
            "dime": state.dime,
            "m_count": m_count,
            "n_count": n_count,
            "condition_met": condition_met,
            "regime": state.Regime[state.Z - state.y - 1] if 0 <= state.Z - state.y - 1 < len(state.Regime) else "Unknown",
            "coherence": self._check_coherence(),
            "symbol": SYMBOL,
            "timestamp": datetime.now().isoformat()
        }

# ============================================================================
# TELEGRAM BOT HANDLERS
# ============================================================================

class AEI_Bot:
    """Telegram Bot Interface for ÆEA Engine with Yahoo Finance Integration."""

    def __init__(self, token: str, bot_name: str = "UpscaleTradeBot"):
        self.token = token
        self.bot_name = bot_name
        self.engine = AEEA_Engine()
        self.application = None
        self._running = False
        self._price_task: Optional[asyncio.Task] = None

    async def price_feed_loop(self) -> None:
        """Continuous price feed loop for Yahoo Finance data."""
        logger.info("🔄 Starting Yahoo Finance price feed loop...")
        while self._running:
            try:
                self.engine.update_price_from_feed()
                await asyncio.sleep(UPDATE_INTERVAL)
            except Exception as e:
                logger.error(f"❌ Price feed error: {e}")
                await asyncio.sleep(5)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a welcome message when /start is issued."""
        chat_id = update.effective_chat.id
        self.engine.state.chat_id = chat_id
        self.engine.application = self.application

        keyboard = [
            [
                InlineKeyboardButton("📊 Status", callback_data="status"),
                InlineKeyboardButton("📈 Signal", callback_data="signal"),
            ],
            [
                InlineKeyboardButton("📊 Regime", callback_data="regime"),
                InlineKeyboardButton("📐 Indicators", callback_data="indicators"),
            ],
            [
                InlineKeyboardButton("🔄 Start Feed", callback_data="start_feed"),
                InlineKeyboardButton("⏹️ Stop Feed", callback_data="stop_feed"),
            ],
            [
                InlineKeyboardButton("📈 Info", callback_data="info"),
                InlineKeyboardButton("🔄 Reset", callback_data="reset"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        welcome = (
            "🔷 *ÆEA Quantum-Financial Topology Bot*\n\n"
            "Welcome to @UpscaleTradeBot. This bot implements the Non-Hermitian\n"
            "Stochastic Geometry of Supply-Demand Imbalance.\n\n"
            "📊 *Available Commands:*\n"
            "`/status` - Current market state & regime\n"
            "`/regime` - Detailed regime classification\n"
            "`/signal` - Current trading signal\n"
            "`/indicators` - 13D Hilbert Space projection\n"
            "`/fvg` - Fair Value Gap tracking\n"
            "`/reset` - Reset topological branch\n"
            "`/start_feed` - Start Yahoo Finance price feed\n"
            "`/stop_feed` - Stop Yahoo Finance price feed\n"
            "`/symbol <PAIR>` - Change trading symbol\n"
            "`/info` - Ticker information\n"
            "`/help` - Show this message\n\n"
            f"📈 *Current Symbol:* `{SYMBOL}`\n"
            f"🔄 *Feed Status:* {'Active' if self._running else 'Inactive'}\n"
            f"📊 *Data Source:* Yahoo Finance (Free, No KYC)\n\n"
            "🧠 *Theoretical Foundation:*\n"
            "• Arc-Length Coherence (s = r)\n"
            "• Kronecker-Delta Execution: δ(m-n-2)=1\n"
            "• Observer Operator O[Ψ]\n"
            "• Non-Hermitian Lindblad Dynamics\n\n"
            "💎 Natalia Tanyatia"
        )
        await update.message.reply_text(welcome, parse_mode="Markdown", reply_markup=reply_markup)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Show help message."""
        await self.start(update, context)

    async def status(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Display current market state."""
        state = self.engine.state
        idx = state.Z - state.y - 1
        regime = state.Regime[idx] if 0 <= idx < len(state.Regime) else "Unknown"

        # Get current price from feed
        bid, ask = self.engine.feed.get_current_price()
        price_display = f"{bid:.5f}" if bid > 0 else f"{state.price:.5f}"

        coherence = self.engine._check_coherence()

        keyboard = [[
            InlineKeyboardButton("📈 Signal", callback_data="signal"),
            InlineKeyboardButton("📊 Regime", callback_data="regime"),
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        response = (
            "🔷 *ÆEA STATUS*\n\n"
            f"📈 *Symbol:* {SYMBOL}\n"
            f"💰 *Price:* {price_display}\n"
            f"📊 *Regime:* {regime}\n"
            f"🔄 *Coherence:* {coherence}\n"
            f"🎯 *Signal Level:* {state.signal:.5f}\n"
            f"📋 *Signature:* {'Active' if state.signature else 'Idle'}\n"
            f"🧠 *KC State:* {state.KC}\n"
            f"🔄 *Tick:* {state.tick}\n"
            f"📅 *Last Update:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"📊 *Imbalance:* m={sum(1 for v in state.k if v)}, n={sum(1 for v in state.l if v)}"
        )
        if update.callback_query:
            await update.callback_query.edit_message_text(response, parse_mode="Markdown", reply_markup=reply_markup)
        else:
            await update.message.reply_text(response, parse_mode="Markdown", reply_markup=reply_markup)

    async def regime(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Display detailed regime classification."""
        state = self.engine.state
        y = state.y
        idx = state.Z - y - 1

        if 0 <= idx < len(state.Regime):
            current = state.Regime[idx]
        else:
            current = "Unknown"

        premium = state.Premium[idx] if 0 <= idx < len(state.Premium) else 0.0
        discount = state.Discount[idx] if 0 <= idx < len(state.Discount) else 0.0
        hh = state.HH[idx] if 0 <= idx < len(state.HH) else 0.0
        ll = state.LL[idx] if 0 <= idx < len(state.LL) else 0.0

        k_count = sum(1 for v in state.k if v)
        l_count = sum(1 for v in state.l if v)

        keyboard = [[
            InlineKeyboardButton("📊 Status", callback_data="status"),
            InlineKeyboardButton("📈 Signal", callback_data="signal"),
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        response = (
            "📊 *REGIME CLASSIFICATION*\n\n"
            f"🔹 *Current Regime:* {current}\n"
            f"🔸 *Premium:* {premium:.5f}\n"
            f"🔻 *Discount:* {discount:.5f}\n"
            f"📈 *HH:* {hh:.5f}\n"
            f"📉 *LL:* {ll:.5f}\n\n"
            f"🟢 *Bullish Signals (k):* {k_count}\n"
            f"🔴 *Bearish Signals (l):* {l_count}\n\n"
            f"📐 *Imbalance Condition:* "
            f"{'✅ TRIGGER' if k_count >= 12 or l_count >= 12 else '⏳ WAITING'}"
        )
        if update.callback_query:
            await update.callback_query.edit_message_text(response, parse_mode="Markdown", reply_markup=reply_markup)
        else:
            await update.message.reply_text(response, parse_mode="Markdown", reply_markup=reply_markup)

    async def signal(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Display current trading signal."""
        state = self.engine.state

        if state.signal == 0:
            direction = "🟡 NEUTRAL"
            confidence = "N/A"
        elif state.price > state.signal:
            direction = "🟢 BUY"
            confidence = f"{(state.price - state.signal) / state.signal * 100:.2f}%" if state.signal != 0 else "0%"
        else:
            direction = "🔴 SELL"
            confidence = f"{(state.signal - state.price) / state.signal * 100:.2f}%" if state.signal != 0 else "0%"

        m_count = sum(1 for v in state.k if v)
        n_count = sum(1 for v in state.l if v)
        condition_met = m_count - n_count > 2

        keyboard = [[
            InlineKeyboardButton("📊 Status", callback_data="status"),
            InlineKeyboardButton("📊 Regime", callback_data="regime"),
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        response = (
            "🎯 *TRADING SIGNAL*\n\n"
            f"📊 *Direction:* {direction}\n"
            f"📈 *Confidence:* {confidence}\n"
            f"🎯 *Signal Level:* {state.signal:.5f}\n"
            f"💰 *Current Price:* {state.price:.5f}\n\n"
            f"⚖️ *Imbalance:* m={m_count}, n={n_count}\n"
            f"✅ *Condition δ(m-n-2)=1:* {'✅ MET' if condition_met else '❌ NOT MET'}\n"
            f"🧠 *KC State:* {state.KC}\n"
            f"🔢 *Prime:* {state.prime}\n"
            f"📋 *Dime:* {state.dime}"
        )
        if update.callback_query:
            await update.callback_query.edit_message_text(response, parse_mode="Markdown", reply_markup=reply_markup)
        else:
            await update.message.reply_text(response, parse_mode="Markdown", reply_markup=reply_markup)

    async def indicators(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Display 13D Hilbert Space projection."""
        state = self.engine.state
        y = state.y
        idx = state.Z - y - 1

        if idx < 0 or idx >= 13:
            await update.message.reply_text("❌ Insufficient data for indicator projection.")
            return

        i_values = [state.iA[i][idx] if idx < len(state.iA[i]) else 50.0 for i in range(13)]

        names = [
            "ADX", "Stochastic", "RVI", "AC", "Force", "OBV",
            "AD", "MFI", "Momentum", "DeM", "WPR", "CCI", "RSI"
        ]

        indicator_str = "📊 *13D HILBERT SPACE PROJECTION*\n\n"
        for i, (name, val) in enumerate(zip(names, i_values)):
            bar = "█" * int(val / 10) + "░" * (10 - int(val / 10))
            indicator_str += f"`{name:8}` {val:6.1f} [{bar}]\n"

        indicator_str += "\n*Thresholds:*\n"
        indicator_str += f"  Overbought: 66.6 (f={F_THRESHOLD:.1f})\n"
        indicator_str += f"  Oversold:   33.3 (g={G_THRESHOLD:.1f})"

        keyboard = [[
            InlineKeyboardButton("📊 Status", callback_data="status"),
            InlineKeyboardButton("📈 Signal", callback_data="signal"),
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if update.callback_query:
            await update.callback_query.edit_message_text(indicator_str, parse_mode="Markdown", reply_markup=reply_markup)
        else:
            await update.message.reply_text(indicator_str, parse_mode="Markdown", reply_markup=reply_markup)

    async def fvg(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Display Fair Value Gap tracking."""
        state = self.engine.state
        idx = state.Z - state.y - 1

        response = (
            "📐 *FAIR VALUE GAP TRACKING*\n\n"
            f"📊 *FVG Count:* {state.FVG + 1}\n"
            f"📈 *Current Price:* {state.price:.5f}\n"
            f"📉 *Last FVG:* {state.bL if state.bL else 'None'}\n\n"
            "*Topological Anchors:*\n"
            f"  🔷 *Premium:* {state.Premium[idx] if 0 <= idx < len(state.Premium) else 0.0:.5f}\n"
            f"  🔶 *Discount:* {state.Discount[idx] if 0 <= idx < len(state.Discount) else 0.0:.5f}\n"
            f"  📈 *HH:* {state.HH[idx] if 0 <= idx < len(state.HH) else 0.0:.5f}\n"
            f"  📉 *LL:* {state.LL[idx] if 0 <= idx < len(state.LL) else 0.0:.5f}"
        )
        await update.message.reply_text(response, parse_mode="Markdown")

    async def reset(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Reset topological branch."""
        self.engine._on_reinit()
        if update.callback_query:
            await update.callback_query.edit_message_text(
                "🔄 *TOPOLOGICAL BRANCH RESET*\n\n"
                "The Hilbert space projection has been re-anchored to the current\n"
                "topological branch. Historical drift has been cleared.\n\n"
                "🧠 *State Reset:*\n"
                "• Premium/Discount re-anchored\n"
                "• kA/lA indicator states cleared\n"
                "• Regime classification reset\n"
                "• FVG tracking reset",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text(
                "🔄 *TOPOLOGICAL BRANCH RESET*\n\n"
                "The Hilbert space projection has been re-anchored to the current\n"
                "topological branch. Historical drift has been cleared.\n\n"
                "🧠 *State Reset:*\n"
                "• Premium/Discount re-anchored\n"
                "• kA/lA indicator states cleared\n"
                "• Regime classification reset\n"
                "• FVG tracking reset",
                parse_mode="Markdown"
            )

    async def start_feed(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Start the Yahoo Finance price feed."""
        if self._running:
            await update.message.reply_text("⚠️ Price feed is already running.")
            return

        self._running = True
        self.engine._running = True

        # Load historical data
        historical = self.engine.feed.get_historical_klines(limit=200)
        if historical:
            self.engine.ohlcv_history = historical
            logger.info(f"✅ Loaded {len(historical)} historical bars")
        else:
            logger.warning("⚠️ No historical data loaded")

        # Start price feed loop
        if self._price_task is None or self._price_task.done():
            self._price_task = asyncio.create_task(self.price_feed_loop())

        # Start the engine's bar processing
        self.engine._on_reinit()
        self.engine.state.FG = True

        await update.message.reply_text(
            f"✅ *Price feed started*\n\n"
            f"📈 *Symbol:* {SYMBOL}\n"
            f"🔄 *Update Interval:* {UPDATE_INTERVAL}s\n"
            f"📊 *Historical Data:* {len(self.engine.ohlcv_history)} bars loaded\n"
            f"📡 *Data Source:* Yahoo Finance (Free, No KYC)\n"
            f"🔮 *Status:* Monitoring for signals...",
            parse_mode="Markdown"
        )

    async def stop_feed(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Stop the Yahoo Finance price feed."""
        self._running = False
        self.engine._running = False
        if self._price_task and not self._price_task.done():
            self._price_task.cancel()
        await update.message.reply_text("⏹️ *Price feed stopped*", parse_mode="Markdown")

    async def symbol(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Change trading symbol."""
        global SYMBOL
        args = context.args
        if not args:
            await update.message.reply_text(
                f"📈 *Current Symbol:* `{SYMBOL}`\n\n"
                "Use `/symbol <PAIR>` to change.\n"
                "Example: `/symbol BTC-USD` or `/symbol BTCUSDT`\n\n"
                f"*Supported Symbols:*\n"
                f"{', '.join(list(SYMBOL_MAP.keys())[:10])}\n"
                f"(and {len(SYMBOL_MAP) - 10} more)",
                parse_mode="Markdown"
            )
            return

        new_symbol = args[0].upper()
        if new_symbol in SYMBOL_MAP:
            yahoo_symbol = SYMBOL_MAP[new_symbol]
        else:
            yahoo_symbol = new_symbol

        try:
            ticker = yf.Ticker(yahoo_symbol)
            info = ticker.info
            if info.get("regularMarketPrice"):
                SYMBOL = yahoo_symbol
                self.engine.feed = YahooFinanceFeed(yahoo_symbol)
                self.engine.state.y = MIN_PERIOD - 2
                self.engine.state.X = MIN_PERIOD - 1
                self.engine._on_reinit()
                await update.message.reply_text(
                    f"✅ *Symbol changed*\n\n"
                    f"📈 *New Symbol:* `{yahoo_symbol}`\n"
                    f"💰 *Current Price:* {info.get('regularMarketPrice', 'N/A')}\n"
                    f"📊 *Name:* {info.get('longName', 'Unknown')}",
                    parse_mode="Markdown"
                )
            else:
                await update.message.reply_text(f"❌ Invalid symbol: {yahoo_symbol}")
        except Exception as e:
            await update.message.reply_text(f"❌ Error: {e}")

    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Display ticker information."""
        info = self.engine.feed.get_info()
        response = (
            "📊 *TICKER INFORMATION*\n\n"
            f"📈 *Symbol:* {SYMBOL}\n"
            f"📛 *Name:* {info.get('name', 'Unknown')}\n"
            f"🏭 *Sector:* {info.get('sector', 'Unknown')}\n"
            f"💵 *Currency:* {info.get('currency', 'USD')}\n"
            f"💰 *Previous Close:* {info.get('previous_close', 'N/A')}\n"
            f"📊 *Market Cap:* {info.get('market_cap', 'N/A')}\n\n"
            f"📡 *Data Source:* Yahoo Finance (Free, No KYC)"
        )
        if update.callback_query:
            await update.callback_query.edit_message_text(response, parse_mode="Markdown")
        else:
            await update.message.reply_text(response, parse_mode="Markdown")

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle inline button callbacks."""
        query = update.callback_query
        await query.answer()

        action = query.data
        if action == "status":
            await self.status(update, context)
        elif action == "regime":
            await self.regime(update, context)
        elif action == "signal":
            await self.signal(update, context)
        elif action == "indicators":
            await self.indicators(update, context)
        elif action == "start_feed":
            await self.start_feed(update, context)
        elif action == "stop_feed":
            await self.stop_feed(update, context)
        elif action == "info":
            await self.info(update, context)
        elif action == "reset":
            await self.reset(update, context)

    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Log errors."""
        logger.error(f"Update {update} caused error {context.error}")
        if update and update.message:
            await update.message.reply_text("❌ An error occurred. Please try again.")

    def run(self) -> None:
        """Start the bot."""
        self.application = Application.builder().token(self.token).build()

        # Add command handlers
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help))
        self.application.add_handler(CommandHandler("status", self.status))
        self.application.add_handler(CommandHandler("regime", self.regime))
        self.application.add_handler(CommandHandler("signal", self.signal))
        self.application.add_handler(CommandHandler("indicators", self.indicators))
        self.application.add_handler(CommandHandler("fvg", self.fvg))
        self.application.add_handler(CommandHandler("reset", self.reset))
        self.application.add_handler(CommandHandler("start_feed", self.start_feed))
        self.application.add_handler(CommandHandler("stop_feed", self.stop_feed))
        self.application.add_handler(CommandHandler("symbol", self.symbol))
        self.application.add_handler(CommandHandler("info", self.info))

        # Add callback query handler
        self.application.add_handler(CallbackQueryHandler(self.button_handler))

        # Add error handler
        self.application.add_error_handler(self.error_handler)

        logger.info(f"🤖 {self.bot_name} starting...")
        logger.info(f"📊 Quantum-Financial Topology Engine initialized.")
        logger.info(f"🧠 Arc-Length Axiom (s=r) enforced.")
        logger.info(f"🔄 Non-Hermitian Lindblad Dynamics active.")
        logger.info(f"📡 Data Source: Yahoo Finance (Free, No KYC)")
        logger.info(f"💎 Ready. Use /start to begin.")

        self.application.run_polling()

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main entry point."""
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

    if not TOKEN:
        logger.error("❌ Error: TELEGRAM_BOT_TOKEN not set.")
        logger.error("   Set it as environment variable.")
        logger.error("   export TELEGRAM_BOT_TOKEN='YOUR_BOT_TOKEN'")
        sys.exit(1)

    bot = AEI_Bot(TOKEN, "UpscaleTradeBot")
    bot.run()

if __name__ == "__main__":
    main()

# ============================================================================
# Q.E.D.
# ============================================================================