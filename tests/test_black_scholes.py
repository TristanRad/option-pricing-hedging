"""Tests for pricer.black_scholes."""


from pricer.black_scholes import price_option
import numpy as np
import pytest
# Paramètres du brief
S0, K, T, r, q, sigma = 100.0, 100.0, 1.0, 0.03, 0.0, 0.20


def test_put_call_parity():
    call = price_option(S0, K, T, r, q, sigma, "call")
    put = price_option(S0, K, T, r, q, sigma, "put")
    assert abs((call - put) - (S0 * np.exp(-q * T) - K * np.exp(-r * T))) < 1e-10


def test_call_bounds():
    call = price_option(S0, K, T, r, q, sigma, "call")
    lower = max(S0 * np.exp(-q * T) - K * np.exp(-r * T), 0.0)
    upper = S0 * np.exp(-q * T)
    assert lower - 1e-12 <= call <= upper + 1e-12


def test_zero_maturity_raises():
    with pytest.raises(ValueError):
            price_option(S0, K, 0.0, r, q, sigma, "call")

