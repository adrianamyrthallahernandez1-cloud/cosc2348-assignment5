#!/usr/bin/env python3
import subprocess


def run_calculator(equation):
    result = subprocess.run(
        ["../calculator", "-q"] + equation.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result


### ADD AT LEAST TWO TESTS HERE!

# Test addition
result = run_calculator("2 + 3")
assert result.returncode == 0
assert "5" in result.stdout

# Test subtraction
result = run_calculator("10 - 4")
assert result.returncode == 0
assert "6" in result.stdout


print("All tests passed!")

