import pytest
from grades import letter_grade

def test_letter_grade_A():
    assert letter_grade(80) == "A"
    assert letter_grade(100) == "A"

def test_letter_grade_B():
    assert letter_grade(70) == "B"
    assert letter_grade(79) == "B"

def test_letter_grade_C():
    assert letter_grade(60) == "C"
    assert letter_grade(69) == "C"

def test_letter_grade_F():
    assert letter_grade(0) == "F"
    assert letter_grade(59) == "F"

def test_letter_grade_out_of_bounds():
    with pytest.raises(ValueError, match="Score must be 0-100"):
        letter_grade(-1)
    with pytest.raises(ValueError, match="Score must be 0-100"):
        letter_grade(101)