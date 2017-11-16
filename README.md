# groestlcoin-hash-python

This package implements the hashing algorithm used by Groestlcoin.

## Usage

```python
    import groestlcoin_hash
    data = '\x00'
    digest = groestlcoin_hash.getHash(data, len(data))
```
