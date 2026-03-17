import subprocess
import sys
from sort import sort

examples = [
    (10,  10,  10,  1,  "STANDARD"),
    (100, 100, 100, 1,  "SPECIAL"),   # bulky by volume
    (150, 1,   1,   1,  "SPECIAL"),   # bulky by dimension
    (10,  10,  10,  20, "SPECIAL"),   # heavy
    (100, 100, 100, 20, "REJECTED"),  # both
]

print("=== sort() demo ===\n")
for width, height, length, mass, expected in examples:
    result = sort(width, height, length, mass)
    status = "OK" if result == expected else "FAIL"
    print(f"  sort({width}, {height}, {length}, {mass}) => {result} [{status}]")

print("\n=== pytest ===\n")
subprocess.run([sys.executable, "-m", "pytest", "test_sort.py", "-v"])
