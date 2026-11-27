"""Tests for the demo shop payments module."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shop.payments import charge, refund  # noqa: E402


class TestPayments(unittest.TestCase):
    def test_charge_positive(self):
        self.assertEqual(charge(1000)["status"], "ok")

    def test_charge_negative_rejected(self):
        with self.assertRaises(ValueError):
            charge(-500)

    def test_refund(self):
        self.assertEqual(refund(100)["status"], "ok")


if __name__ == "__main__":
    unittest.main()
