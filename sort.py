def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Dispatch a package to the correct stack based on its volume, dimensions, and mass.

    Args:
        width, height, length: package dimensions in cm (must be >= 0)
        mass: package mass in kg (must be >= 0)

    Returns:
        "STANDARD", "SPECIAL", or "REJECTED"

    Raises:
        TypeError: if any argument is not numeric
        ValueError: if any argument is negative
    """
    for name, val in {"width": width, "height": height, "length": length, "mass": mass}.items():
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric, got {type(val).__name__}")
        if val < 0:
            raise ValueError(f"{name} must be non-negative, got {val}")

    bulky = (width * height * length >= 1_000_000) or any(d >= 150 for d in (width, height, length))
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
