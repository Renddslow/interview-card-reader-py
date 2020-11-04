from test import Test
from card_reader import get_invalid_logs

def test_one(suite):
    suite.is_true(
        isinstance(get_invalid_logs([]), tuple),
        "returns an Array"
    )

def test_two(suite):
    input = [
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Mary", "scan": "enter" },
        { "employee": "Mary", "scan": "exit" },
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "exit" },
    ]
    expected = (["Paul"], [])

    (exits, entries) = get_invalid_logs(input)

    exits.sort()
    entries.sort()

    actual = (exits, entries)
    suite.is_deep_equal(
        actual,
        expected,
        "returns faulty exits when present",    
    )

def test_three(suite):
    input = [
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Mary", "scan": "enter" },
        { "employee": "Mary", "scan": "exit" },
        { "employee": "Gregory", "scan": "exit" },
        { "employee": "Mary", "scan": "enter" },
        { "employee": "Mary", "scan": "exit" },
        { "employee": "Gregory", "scan": "enter" },
        { "employee": "Gregory", "scan": "exit" },
    ]
    expected = ([], ['Gregory', 'Paul'])

    (exits, entries) = get_invalid_logs(input)

    exits.sort()
    entries.sort()
    
    actual = (exits, entries)
    suite.is_deep_equal(
        actual,
        expected,
        "returns faulty entries when present",
    )

def test_four(suite):
    input = [
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Mary", "scan": "enter" },
        { "employee": "Mary", "scan": "exit" },
        { "employee": "Ignatius", "scan": "exit" },
        { "employee": "Benedict", "scan": "enter" },
        { "employee": "Benedict", "scan": "enter" },
        { "employee": "Benedict", "scan": "exit" },
        { "employee": "Mary", "scan": "enter" },
        { "employee": "Mary", "scan": "exit" },
        { "employee": "Ignatius", "scan": "enter" },
    ]
    expected = (
        ['Benedict', 'Ignatius'],
        ['Ignatius', 'Paul'],
    )

    (exits, entries) = get_invalid_logs(input)

    exits.sort()
    entries.sort()
    
    actual = (exits, entries)
    suite.is_deep_equal(
        actual,
        expected,
        "returns faulty exits and entries when present",
    )

def test_five(suite):
    input = [
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "enter" },
    ]
    expected = (['Paul'], [])

    (exits, entries) = get_invalid_logs(input)

    exits.sort()
    entries.sort()
    
    actual = (exits, entries)
    suite.is_deep_equal(
        actual,
        expected,
        "returns only one faulty exit per employee when present",
    )

def test_six(suite):
    input = [
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "exit" },
    ]
    expected = ([], ['Paul'])

    (exits, entries) = get_invalid_logs(input)

    exits.sort()
    entries.sort()
    
    actual = (exits, entries)
    suite.is_deep_equal(
        actual,
        expected,
        "returns only one faulty entry per employee when present",
    )

def test_seven(suite):
    input = [
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "enter" },
        { "employee": "Paul", "scan": "exit" },
        { "employee": "Paul", "scan": "enter" },
    ]
    expected = (['Paul'], ['Paul'])

    (exits, entries) = get_invalid_logs(input)

    exits.sort()
    entries.sort()
    
    actual = (exits, entries)
    suite.is_deep_equal(
        actual,
        expected,
        "returns only one faulty entry and exit per employee when present",
    )

if __name__ == "__main__":
    suite = Test("get_invalid_logs")

    test_one(suite)
    test_two(suite)
    test_three(suite)
    test_four(suite)
    test_five(suite)
    test_six(suite)
    test_seven(suite)

    suite.run()
