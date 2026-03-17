# Package Sorter

A function that dispatches packages to the correct stack based on their volume, dimensions, and mass.

## Rules

| Condition | Definition |
|---|---|
| **Bulky** | Volume ≥ 1,000,000 cm³ or any single dimension ≥ 150 cm |
| **Heavy** | Mass ≥ 20 kg |

| Stack | Criteria |
|---|---|
| `STANDARD` | Neither bulky nor heavy |
| `SPECIAL` | Bulky or heavy (but not both) |
| `REJECTED` | Both bulky and heavy |

## Usage

```python
from sort import sort

sort(10, 10, 10, 1)    # "STANDARD"
sort(100, 100, 100, 1) # "SPECIAL"  — bulky by volume
sort(150, 1, 1, 1)     # "SPECIAL"  — bulky by dimension
sort(10, 10, 10, 20)   # "SPECIAL"  — heavy
sort(100, 100, 100, 20) # "REJECTED" — both
```

## Running Tests

```bash
pip install pytest
pytest test_sort.py -v
```
