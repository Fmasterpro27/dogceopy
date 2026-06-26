# 🐶 DogCEOPy

> A lightweight, modern Python wrapper for the **Dog CEO API**.

[![PyPI version](https://img.shields.io/pypi/v/DogCEOPy.svg)](https://pypi.org/project/DogCEOPy/)
[![Python versions](https://img.shields.io/pypi/pyversions/DogCEOPy.svg)](https://pypi.org/project/DogCEOPy/)
[![License](https://img.shields.io/pypi/l/DogCEOPy.svg)](LICENSE)

DogCEOPy provides a simple and Pythonic interface for retrieving dog breeds, sub-breeds, and dog images without dealing with raw HTTP requests.

## Features

- 🚀 Simple and intuitive API
- 🐕 Fetch all dog breeds
- 🦴 Fetch sub-breeds
- 🖼️ Get random dog images
- 📷 Get multiple random images
- 🐶 Get breed and sub-breed images
- 📝 Fully type hinted
- 🔄 Context manager support
- ⚡ Lightweight with minimal dependencies

## Installation

```bash
pip install DogCEOPy
```

## Quick Start

```python
from dogceopy import DogCEO

dog = DogCEO()

print(dog.random.image())
```

Example output:

```text
https://images.dog.ceo/breeds/husky/n02110185_14597.jpg
```

---

## Breed Information

### List all breeds

```python
from dogceopy import DogCEO

dog = DogCEO()

print(dog.breeds.list())
```

### List all breeds with sub-breeds

```python
print(dog.breeds.list_all())
```

### List sub-breeds

```python
print(
    dog.breeds.sub_breeds("bulldog")
)
```

Output:

```python
["boston", "english", "french"]
```

### Check if a breed exists

```python
print(
    dog.breeds.exists("husky")
)
```

Output:

```python
True
```

---

## Random Images

### One random dog image

```python
print(
    dog.random.image()
)
```

### Multiple random dog images

```python
print(
    dog.random.images(5)
)
```

---

## Breed Images

### Random Husky image

```python
print(
    dog.images.random("husky")
)
```

### Five random Husky images

```python
print(
    dog.images.random_many(
        "husky",
        5
    )
)
```

### All Husky images

```python
print(
    dog.images.all("husky")
)
```

---

## Sub-Breed Images

English Bulldog is a sub-breed of Bulldog.

### Random English Bulldog image

```python
print(
    dog.images.sub_random(
        "bulldog",
        "english"
    )
)
```

### Five random English Bulldog images

```python
print(
    dog.images.sub_random_many(
        "bulldog",
        "english",
        5
    )
)
```

### All English Bulldog images

```python
print(
    dog.images.sub_all(
        "bulldog",
        "english"
    )
)
```

---

## Using a Context Manager

```python
from dogceopy import DogCEO

with DogCEO() as dog:
    print(
        dog.random.image()
    )
```

The HTTP session is automatically closed when the block exits.

---

## API Overview

### `random`

| Method          | Description                    |
| --------------- | ------------------------------ |
| `image()`       | Get one random dog image       |
| `images(count)` | Get multiple random dog images |

### `breeds`

| Method                  | Description                          |
| ----------------------- | ------------------------------------ |
| `list()`                | List all breeds                      |
| `list_all()`            | List all breeds and sub-breeds       |
| `sub_breeds(breed)`     | Get sub-breeds                       |
| `exists(breed)`         | Check whether a breed exists         |
| `has_sub_breeds(breed)` | Check whether a breed has sub-breeds |

### `images`

| Method                                     | Description                            |
| ------------------------------------------ | -------------------------------------- |
| `random(breed)`                            | Random image for a breed               |
| `random_many(breed, count)`                | Multiple random images                 |
| `all(breed)`                               | All images for a breed                 |
| `sub_random(breed, sub_breed)`             | Random image for a sub-breed           |
| `sub_random_many(breed, sub_breed, count)` | Multiple random images for a sub-breed |
| `sub_all(breed, sub_breed)`                | All images for a sub-breed             |

---

## Requirements

- Python 3.8+
- requests

---

## Running Tests

```bash
pytest
```

---

## Author

Developed and maintained by **JackMa**

GitHub: https://github.com/Fmasterpro27

---

## License

Licensed under the Apache License 2.0.

---

## Acknowledgements

This library is an unofficial Python wrapper for the Dog CEO API and is not affiliated with Dog CEO.

Powered by the Dog CEO Dog API.
