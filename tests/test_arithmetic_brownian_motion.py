import random
import unittest

from distlib import arithmetic_brownian_motion


class ArithmeticBrownianMotionTests(unittest.TestCase):
    def test_zero_volatility_gives_drift_line(self):
        path = arithmetic_brownian_motion(
            3,
            s0=10.0,
            mu=0.2,
            sigma=0.0,
            dt=1.0,
            rng=random.Random(0),
        )

        self.assertAlmostEqual(path[0], 10.0)
        self.assertAlmostEqual(path[1], 10.2)
        self.assertAlmostEqual(path[2], 10.4)
        self.assertAlmostEqual(path[3], 10.6)

    def test_returns_length_n_plus_one(self):
        path = arithmetic_brownian_motion(
            5,
            s0=1.0,
            mu=0.0,
            sigma=0.5,
            dt=0.25,
            rng=random.Random(2),
        )

        self.assertEqual(len(path), 6)


if __name__ == "__main__":
    unittest.main()
