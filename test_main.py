import io
import sys
import random
from main import parse, fillInZeroes, q3, randomPoly, unParse, printDebugPretty, loop
from Term import Term

def run_tests():
    # Test Term class
    try:
        term = Term(3, 2)
        assert str(term) == "3x^2", "Term class test failed"
        term = Term(-5, 1)
        assert str(term) == "-5x", "Term class test failed"
        term = Term(7, 0)
        assert str(term) == "7", "Term class test failed"
        print("Term class tests passed")
    except AssertionError as e:
        print(e)

    # Test parse function
    try:
        result = parse("x^2 + 7x + 9")
        expected = [Term(1, 2), Term(7, 1), Term(9, 0)]
        assert all(result[i].arity == expected[i].arity and result[i].degree == expected[i].degree for i in range(len(result))), "parse function test failed"
        print("parse function tests passed")
    except AssertionError as e:
        print(e)

    # Test fillInZeroes function
    try:
        fx = [Term(1, 2), Term(7, 1), Term(9, 0)]
        result = fillInZeroes(fx, 3)
        expected = [Term(1, 2), Term(7, 1), Term(9, 0)]
        assert all(result[i].arity == expected[i].arity and result[i].degree == expected[i].degree for i in range(len(result))), "fillInZeroes function test failed"
        print("fillInZeroes function tests passed")
    except AssertionError as e:
        print(e)

    # Test q3 function
    try:
        captured_output = io.StringIO()
        sys.stdout = captured_output
        q3("x^2 + 7x + 9", "3x^2 + 2x + 5")
        sys.stdout = sys.__stdout__
        result = captured_output.getvalue().strip()
        # Check for expected result manually, as it requires specific polynomial convolution result
        # Replace the expected result with the correct polynomial convolution result of "x^2 + 7x + 9" and "3x^2 + 2x + 5"
        expected_result = "3x^4 + 23x^3 + 68x^2 + 64x + 45"
        if result != expected_result:
            print(f"q3 function test failed\nExpected: {expected_result}\nGot: {result}")
        assert result == expected_result, "q3 function test failed"
        print("q3 function tests passed")
    except AssertionError as e:
        print(e)

    # Test randomPoly function
    try:
        poly = randomPoly()
        assert len(poly) > 0, "randomPoly function test failed"
        assert all(isinstance(term, Term) for term in poly), "randomPoly function test failed"
        print("randomPoly function tests passed")
    except AssertionError as e:
        print(e)

    # Test unParse and unparseIndividual functions
    try:
        fx = [Term(1, 2), Term(7, 1), Term(9, 0)]
        gx = [Term(3, 2), Term(2, 1), Term(5, 0)]
        result = unParse(fx, gx)
        expected = ["1x^2 + 7x + 9", "3x^2 + 2x + 5"]
        assert result == expected, "unParse function test failed"
        print("unParse and unparseIndividual function tests passed")
    except AssertionError as e:
        print(e)

    # Test printDebugPretty function
    try:
        captured_output = io.StringIO()
        sys.stdout = captured_output
        printDebugPretty(22)
        sys.stdout = sys.__stdout__
        result = captured_output.getvalue().strip()
        expected = "-" * 22
        assert result == expected, "printDebugPretty function test failed"
        print("printDebugPretty function tests passed")
    except AssertionError as e:
        print(e)

    # Test loop function
    try:
        captured_output = io.StringIO()
        sys.stdout = captured_output
        loop(3, False)
        sys.stdout = sys.__stdout__
        result = captured_output.getvalue().strip()
        assert result, "loop function test failed"
        print("loop function tests passed")
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    run_tests()
