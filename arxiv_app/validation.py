import argparse


def non_negative_int(value: str) -> int:
    ivalue = int(value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError("cache-ttl must be >= 0")
    return ivalue