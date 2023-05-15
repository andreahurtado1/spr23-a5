#!/usr/bin/env python3
from calculator_adapter import run


### STUDENT TESTS
# checks that program runs for subtraction
assert run("4 - 2").output == "2"
# checks that program runs for division
assert run("10 / 2").output == "5"
# checks if mod is real
assert run("2 % 2").exit_status != 0

###

print("All tests passed!")
