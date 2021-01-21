from decimal import Decimal

from rest_framework.fields import DecimalField


def decimal_to_str(value: Decimal) -> str:
    return DecimalField(
        max_digits=20,
        decimal_places=2
    ).to_representation(value)


d2s = decimal_to_str
