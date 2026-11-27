"""Closed-form Black-Scholes prices, analytical Greeks and implied volatility."""
import numpy as np
from scipy.stats import norm


## 1 - cas d'étude de base

def d1(S0, K, T, r, q, sigma):
    return (np.log(S0 / K) + (r - q + sigma**2 / 2) * T) / (sigma * np.sqrt(T))


def d2(S0, K, T, r, q, sigma):
    return d1(S0, K, T, r, q, sigma) - sigma * np.sqrt(T)


def price_option(S0, K, T, r, q, sigma, option_type):

    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma should be positive")

    D1 = d1(S0, K, T, r, q, sigma)
    D2 = d2(S0, K, T, r, q, sigma)

    if option_type == "call":
        C0 = S0 * np.exp(-q * T) * norm.cdf(D1) - K * np.exp(-r * T) * norm.cdf(D2)
        return C0

    elif option_type == "put":
        P0 = K * np.exp(-r * T) * norm.cdf(-D2) - S0 * np.exp(-q * T) * norm.cdf(-D1)
        return P0


    else:
        raise ValueError("option_type doit être 'call' ou 'put'")


