"""EIP-137 namehash test vectors (verified against pycryptodome + eth-ens-namehash)."""

from namehash import namehash, ZERO_NODE

VECTORS = {
    "": 0x0000000000000000000000000000000000000000000000000000000000000000,
    "eth": 0x93CDEB708B7545DC668EB9280176169D1C33CFD8ED6F04690A0BCC88A93FC4AE,
    "foo.eth": 0xDE9B09FD7C5F901E23A3F19FECC54828E9C848539801E86591BD9801B019F84F,
}

assert ZERO_NODE == b"\x00" * 32
for name, expected in VECTORS.items():
    got = namehash(name)
    assert got == expected.to_bytes(32, "big"), f"namehash({name!r}) mismatch"
print(f"OK: {len(VECTORS)} EIP-137 vectors verified")
