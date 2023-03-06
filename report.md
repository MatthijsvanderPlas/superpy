# Report SuperPy

## 1. Argparse

I feel I have chosen a simple but effective way of implementing the parsing of arguments. Because I am using the:

```python
instruction = parser.add_subparsers(
        metavar="Subcommands",
        )
```

It helps to have a large portion of the input checks done by Argeparse and allows for a lot nice parsing if you ask me. Furthermore by using below code:

```python
buy.add_argument("buy", action="store_true", default=False)
```

One can use the following line to let the program know we are going to be using the 'buy' command. There is no need to add any additional parameters.

```bash
python main.py buy
```

It makes it easy for main.py to implement the flow logic of the program by checking if **`parsed`** has a certain attribute.

```python
if hasattr(parsed, "buy"):
        handleBuy(parsed)
```

## 2. DRY

By having a lot of the basic functions inside de utils.py it makes it easy to reuse them where needed and keeps the code DRY and easier to refactor in the future if needed. 

A Good example is the **`getDateFromFile()`** function which is used everywhere in the code to retrieve the current date from a simple .txt file. We use this file to keep the internal clock of the program.

```python
def getDateFromFile(type):

    if type == "str":

        with open("./day/day.txt") as f:
            line = "".join(f.readline().split("-"))
            date = datetime.strptime(line, "%d%m%Y").date()
            day = datetime.strftime(date, "%d-%m-%Y")
        return day

    if type == "date":

        with open("./day/day.txt") as f:
            line = "".join(f.readline().split("-"))
            day = datetime.strptime(line, "%d%m%Y").date()
        return day
```

We can now use this function everywhere in our program and either get a `_Date` object or a `str` returned with the current date for the program.

## 3. Structure

I feel that the overall stucture of the program (altough it can be optimized) is easy to follow along. I tried to keep most files short so it is easy to read through. I tried to keep the buisness logic and presentation seperate from each other. With using very descriptive (sometimes long) function names I think it makes it way more readable as the HOW a function does something is usually not all that interresting as your reading through a logic flow of the program.