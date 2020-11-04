import unittest

class Test:
    def __init__(self, name):
        self.name = name
        self.cases = []

    def _add_case(self, name, value):
        self.cases.append({
            "name": name,
            "value": value,
        })

    def is_true(self, value, name):
        self._add_case(name, value)

    def is_deep_equal(self, a, b, name):
        self._add_case(name, a == b)

    def run(self):
        for i in range(len(self.cases)):
            correct = bool(self.cases[i]["value"])
            pass_string = "\x1b[32mpassed!\x1b[39m" if correct else "\x1b[31mfailed :(\x1b[39m"
            print(str(i + 1) + ". " + self.name + " - " + self.cases[i]["name"] + " " + pass_string)