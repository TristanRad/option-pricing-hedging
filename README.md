# Option Pricing & Delta Hedging

*Work in progress.*

Prices European, up-and-out barrier and arithmetic Asian options under the Black-Scholes model with three independent methods (closed form, Monte Carlo, Crank-Nicolson PDE), checks that they agree, and simulates the delta hedging of a short call.

## Setup

```bash
pip install -e ".[dev]"
pytest
```
