# Imports
from components.inputParser import create_parser
from components.buy import handleBuy
import sys
from console import console, err_console

sys.path.insert(0, "./components")


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    # Accept arguments from argparse
    parser = create_parser()
    parsed = parser.parse_args()
    # Buy command was given and now parsed
    if parsed.buy:
        console.print(
            f"[blue bold]Product: {parsed.name_product}, Price: {parsed.price}, Amount: {parsed.amount}"
        )
     
        handleBuy(parsed.name_product, parsed.price, parsed.amount, parsed.expiration)


if __name__ == "__main__":
    main()
