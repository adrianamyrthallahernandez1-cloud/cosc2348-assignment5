#!/usr/bin/env python3
from example_tests import run


### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "5" for input of "2 + 3"
assert run("2 + 3").output == "5"

# Checks that the program outputs "6" for input of "10 - 4"
assert run("10 - 4").output == "6"

# Checks that the program exits successfully for input "2 + 3"
assert run("2 + 3").exit_status == 0

# Checks that the program fails correctly for invalid input "2 @ 3"
assert run("2 @ 3").exit_status != 0


print("All tests passed!")#!/usr/bin/env python3
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

#!/usr/bin/env python3
from example_tests import run


### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "5" for input of "2 + 3"
assert run("2 + 3").output == "5"

# Checks that the program outputs "6" for input of "10 - 4"
assert run("10 - 4").output == "6"

# Checks that the program exits successfully for input "2 + 3"
assert run("2 + 3").exit_status == 0

# Checks that the program fails correctly for invalid input "2 @ 3"
assert run("2 @ 3").exit_status != 0


print("All tests passed!")
