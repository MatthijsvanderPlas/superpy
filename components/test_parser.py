from components.inputParser import create_parser
import sys

sys.path.insert(0, "./components")


def test_input():
    def setUp(self):
        self.parser = create_parser()

    def test_input(self):
        parsing = self.parser.parse.args
        self.assertEqual(parsing(["buy"]).Instruction, "buy")
        assert parsing(["report", "inventory"]) == [
            "report",
            "inventory",
        ]

    def test_input2(self):
        parsing = self.parser.parse.args
        assert parsing("sell") == "sell"
