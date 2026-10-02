"""ENS namehash (EIP-137) and labelhash demo in pure Python.

namehash(name) builds a 32-byte node identifier for any ENS name,
recursively hashing labels from right to left:

    namehash('')        = 0x00..00
    namehash('eth')     = keccak256(namehash('') + keccak256('eth'))
    namehash('a.b')     = keccak256(namehash('b') + keccak256('a'))

Run:  python3 namehash.py [name ...]     (default: foo.eth)
"""

from keccak import keccak256

ZERO_NODE = b"\x00" * 32


def labelhash(label: str) -> bytes:
    """keccak256 of a single label, e.g. labelhash('eth')."""
    return keccak256(label.encode("utf-8"))


def namehash(name: str) -> bytes:
    """32-byte EIP-137 namehash of a dotted ENS name."""
    node = ZERO_NODE
    if name:
        for label in reversed(name.split(".")):
            node = keccak256(node + keccak256(label.encode("utf-8")))
    return node


def _demo(names):
    for name in names:
        print(f"namehash('{name}') = 0x{namehash(name).hex()}")


if __name__ == "__main__":
    import sys

    _demo(sys.argv[1:] or ["foo.eth"])
