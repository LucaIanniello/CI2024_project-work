# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

#SAFE OPERATOR USED

def safe_divide(a, b):
    return np.divide(a, b, out=np.zeros_like(a), where=b!=0)

def safe_log(x):
    return np.log(np.where(x > 0, x, 1))

def safe_sqrt(x):
    return np.sqrt(np.where(x >= 0, x, 0))

def safe_tan(x):
    return np.tan(np.where(np.abs(np.cos(x)) > 1e-6, x, 0))

def safe_exp(x, max_value=700):
    # Exponentially large values can overflow, so we clamp the input
    result = np.exp(np.clip(x, -max_value, max_value))
    return np.clip(result, -1e10, 1e10)


def safe_power(base, exponent, max_value=700, max_exponent=3):
    # Handle bases less than or equal to 0 when the exponent is fractional
    safe_base = np.where(base > 0, base, 1)
    exponent = np.clip(exponent, -max_exponent, max_exponent)
    result = np.power(safe_base, exponent)

    # Handle edge cases: If base is 0 and exponent is non-positive
    result = np.where((base == 0) & (exponent <= 0), 1, result)

    return result

def safe_arcsin(x):
    # Clip the input to the range [-1, 1] to avoid invalid values
    x_clipped = np.clip(x, -1, 1)
    return np.arcsin(x_clipped)

def safe_arccos(x):
    # Clip the input to the range [-1, 1] to avoid invalid values
    x_clipped = np.clip(x, -1, 1)
    return np.arccos(x_clipped)


def safe_arctan(x, max_value=1000):
    # Clip the input to a reasonable range to avoid extreme values
    x_clipped = np.clip(x, -max_value, max_value)
    return np.arctan(x_clipped)


#RESULT FUNCTION USED

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])


def f2(x: np.ndarray) -> np.ndarray:
    # Constants
    A = 9.6042 * 6.8333 * 6.4375  # = 423.0609
    B = 6.0417 * A * 9.2083  # = 23500.21
    D = 0.8958 * (7.2292 * 8.0208)  # = 51.9353
    
    sqrt_term = safe_sqrt(4.0625 - x[1])
    division_term = safe_divide(x[0], 4.8542) 
    
    term1 = B
    term2 = division_term * sqrt_term * A
    result = D * x[0] * (term1 + term2)
    
    return result


def f3(x: np.ndarray) -> np.ndarray:
    # First group of terms
    group1 = 22.0833 - 8.625 * x[1] - 4.0625 * safe_sqrt(x[2])
    
    # Second group of terms
    inner_sin1 = np.sin(x[2] / 10.0)
    inner_sin2 = np.sin(3.6667 + (7.2292 - x[0]))
    outer_sin = np.sin(inner_sin1 - inner_sin2)
    tan_term = np.tan(outer_sin)
    group2 = tan_term + 6.0417 * x[1]

    expression = group1 - group2
    
    return expression


def f4(x: np.ndarray) -> np.ndarray: 
    inner_value = 0.6702 + np.cos(x[1])
    arcsin_term = safe_arcsin(inner_value)
    
    result = np.exp(arcsin_term + np.cos(x[1]))
    return result


def f5(x: np.ndarray) -> np.ndarray: 
    log_cos_value = safe_log(
                        np.cos(
                            safe_arccos(
                                safe_arcsin(
                                    np.sin(
                                        safe_log(2.0 - x[1])
                                    )
                                )
                            )
                        )
                    )

    # Compute the second block of the expression
    tan_value = safe_tan(
                    safe_tan(
                        np.cos(
                            safe_arcsin(4.25)
                        )
                    ) ** 0.875
                ) ** 0.875

    # Final result
    result = log_cos_value * tan_value
    return result


def f6(x: np.ndarray) -> np.ndarray: 
    exp_value = safe_exp((x[0] / 2.1379310344827585) - x[1] - 1.1551724137931034)
    sqrt_value = safe_sqrt(exp_value)
    arctan_value = safe_arctan(sqrt_value)
    
    # Final expression
    result = x[1] + (x[1] + arctan_value - x[0])
    return result


def f7(x: np.ndarray) -> np.ndarray:
    arctan_term = safe_arctan(x[1] - 4.25)
    exp_term = 2 * np.exp((x[0] * x[1]) + 0.875)
    
    result = arctan_term + exp_term
    return result


def f8(x: np.ndarray) -> np.ndarray: 
    exp_value = safe_exp(2.9375 + x[5])
    power_value = 3.125**2.9375
    result = exp_value - (x[5] + (power_value - x[0]))
    return result
