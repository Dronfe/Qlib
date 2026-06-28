import math
import random


def normal_distribution(sig, meu, x):
    """Return the Gaussian density values for a list of points."""
    if sig <= 0:
        raise ValueError("sig must be positive")

    values = []
    for value in x:
        exponent = -((value - meu) ** 2) / (2 * sig**2)
        density = (1 / (math.sqrt(2 * math.pi) * sig)) * math.exp(exponent)
        values.append(density)
    return values


def arithmetic_brownian_motion(n, s0=0.0, mu=0.0, sigma=1.0, dt=1.0, rng=None):
    """Simulate an arithmetic Brownian motion path for option-pricing work."""
    if n < 1:
        raise ValueError("n must be at least 1")
    if dt <= 0:
        raise ValueError("dt must be positive")
    if sigma < 0:
        raise ValueError("sigma must be non-negative")

    if rng is None:
        rng = random.Random()

    path = [float(s0)]
    for _ in range(n):
        shock = mu * dt + sigma * math.sqrt(dt) * rng.gauss(0.0, 1.0)
        path.append(path[-1] + shock)
    return path


def arithemetic_brownian_movement(n, s0=0.0, mu=0.0, sigma=1.0, dt=1.0, rng=None):
    """Backward-compatible wrapper for arithmetic Brownian motion."""
    return arithmetic_brownian_motion(n, s0=s0, mu=mu, sigma=sigma, dt=dt, rng=rng)

