# ens-namehash

ENS **namehash** ([EIP-137](https://eips.ethereum.org/EIPS/eip-137)) in pure Python — zero dependencies.

Namehash turns a human-readable ENS name like `vitalik.eth` into the fixed 32-byte
node identifier that ENS smart contracts use on-chain. It preserves hierarchy:
from `namehash('eth')` you can derive `namehash('foo.eth')`, but never the reverse.

## How it works

```
namehash('')        = 0x00…00
namehash('eth')     = keccak256(namehash('')  + keccak256('eth'))
namehash('foo.eth') = keccak256(namehash('eth') + keccak256('foo'))
```

Labels are processed right-to-left; each step hashes the parent node concatenated
with the label's own keccak256 (`labelhash`).

## Usage

```bash
python3 namehash.py vitalik.eth foo.eth
# namehash('vitalik.eth') = 0xee6c4522aab0003e8d14cd40a6af439055fd2577951148c14b6cea9a53475835
# namehash('foo.eth')     = 0xde9b09fd7c5f901e23a3f19fecc54828e9c848539801e86591bd9801b019f84f
```

```python
from namehash import namehash, labelhash

labelhash("eth")   # single label hash -> bytes
namehash("alice.eth").hex()
```

## Files

- `namehash.py` — `namehash()` / `labelhash()` + CLI demo
- `keccak.py` — self-contained pure-Python Keccak-256 (the sponge Ethereum uses)
- `tests.py` — EIP-137 test vectors (`""`, `"eth"`, `"foo.eth"`)

```bash
python3 tests.py   # OK: 3 EIP-137 vectors verified
```
