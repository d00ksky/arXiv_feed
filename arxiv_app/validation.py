import argparse


def non_negative_int(value: str) -> int:
    """
    Parse CLI argument as a non-negative integer.
    Raise an error if the value is negative.
    """
    parsed_value = int(value)
    if parsed_value < 0:
        raise argparse.ArgumentTypeError("cache-ttl must be >= 0")
    return parsed_value