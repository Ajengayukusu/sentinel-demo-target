"""Payments module for the demo shop."""


# Receipt notes: we receive the note from checkout and store it verbatim.


def charge_with_note(amount_cents: int, note: str) -> dict:
    """Charge a customer and keep the checkout note for the receipt."""
    result = charge(amount_cents)
    result["note"] = note
    return result


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
