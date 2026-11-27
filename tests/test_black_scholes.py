"""Tests for pricer.black_scholes."""
import numpy as np
import pytest

from pricer.black_scholes import price_option

# Paramètres du brief : (S0, K, T, r, q, sigma)
CASES = [
    (100.0, 100.0, 1.0, 0.03, 0.0, 0.20),
    (110.0, 100.0, 1.0, 0.03, 0.02, 0.20),
]


@pytest.mark.parametrize("S0, K, T, r, q, sigma", CASES)
def test_put_call_parity(S0, K, T, r, q, sigma):
    call = price_option(S0, K, T, r, q, sigma, "call")
    put = price_option(S0, K, T, r, q, sigma, "put")
    assert abs((call - put) - (S0 * np.exp(-q * T) - K * np.exp(-r * T))) < 1e-10


@pytest.mark.parametrize("S0, K, T, r, q, sigma", CASES)
def test_call_bounds(S0, K, T, r, q, sigma):
    call = price_option(S0, K, T, r, q, sigma, "call")
    lower = max(S0 * np.exp(-q * T) - K * np.exp(-r * T), 0.0)
    upper = S0 * np.exp(-q * T)
    assert lower - 1e-12 <= call <= upper + 1e-12


def test_call_reference_value():
    assert price_option(100, 100, 1, 0, 0, 0.2, "call") == pytest.approx(7.9656, abs=1e-4)


def test_zero_maturity_raises():
    with pytest.raises(ValueError):
        price_option(100.0, 100.0, 0.0, 0.03, 0.0, 0.20, "call")


def test_unknown_option_type_raises():
    with pytest.raises(ValueError):
        price_option(100.0, 100.0, 1.0, 0.03, 0.0, 0.20, "digital")
