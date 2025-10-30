# ex9.py
import math

def factorial(n: int) -> int:
    """Iterative factorial (n!). n must be >= 0."""
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def exp_series(x: float, terms: int) -> float:
    """
    Approximate e^x using the first `terms` Maclaurin terms:
      e^x ≈ Σ_{k=0}^{terms-1} x^k / k!
    """
    if terms <= 0:
        raise ValueError("terms must be a positive integer")
    total = 0.0
    for k in range(terms):
        total += (x ** k) / factorial(k)
    return total

def ln1p_series(x: float, terms: int) -> float:
    """
    Approximate ln(1 + x) using the first `terms` of the alternating series:
      ln(1+x) ≈ Σ_{k=1}^{terms} (-1)^{k+1} * x^k / k
    Converges for -1 < x ≤ 1 (best near 0).
    """
    if terms <= 0:
        raise ValueError("terms must be a positive integer")
    if not (-1.0 < x <= 1.0):
        # series won’t converge well (or at all) outside this range
        raise ValueError("ln(1+x) series requires -1 < x ≤ 1")
    total = 0.0
    sign = 1.0  # (-1)^(k+1) starts + for k=1
    for k in range(1, terms + 1):
        total += sign * (x ** k) / k
        sign = -sign
    return total

if __name__ == "__main__":
    # demo: compute e^x and ln(1+x) for comparison (optional)
    x = float(input("Enter x: "))
    n = int(input("Enter number of terms (positive int): "))

    # e^x via series
    try:
        approx_exp = exp_series(x, n)
        print(f"e^{x} (series, {n} terms) = {approx_exp}")
        # Optional reference using math for sanity-check (not required by exercise):
        print(f"e^{x} (math.exp) = {math.exp(x)}")
    except ValueError as e:
        print("exp_series error:", e)

    # ln(1+x) via series (only meaningful for -1 < x ≤ 1)
    try:
        approx_ln1p = ln1p_series(x, n)
        print(f"ln(1+{x}) (series, {n} terms) = {approx_ln1p}")
        # Optional reference:
        print(f"ln(1+{x}) (math.log1p) = {math.log1p(x)}")
    except ValueError as e:
        print("ln1p_series error:", e)