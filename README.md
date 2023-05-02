# Chinese Poetry Query

A database for querying Chinese poetry.

## Usage

* Clone this repo with submodules:

```bash
    git clone https://github.com/T0nyX1ang/chinese-poetry-query --recurse-submodules
```

* Generate database (with automatic conversion for tradition Chinese characters):

```bash
    py -3 generate_database.py  # Windows
    python3 generate_database.py  # *nix
```

* Query database:

```bash
    py -3 query_database.py ...   # Windows
    python3 query_database.py ...   # *nix
```

## License

* [MIT](./LICENSE)
