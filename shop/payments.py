"""Payments module for the demo shop."""


def charge(amount_cents: int) -> dict:
    """Charge a customer. Negative amounts are rejected."""
    if amount_cents < 0:
        raise ValueError("amount must not be negative")
    return {"charged": amount_cents, "status": "ok"}


def refund(amount_cents: int) -> dict:
    """Refund a previous charge. Negative amounts are rejected."""
    if amount_cents < 0:
        raise ValueError("amount must not be negative")
    return {"refunded": amount_cents, "status": "ok"}
