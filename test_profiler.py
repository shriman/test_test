import time


# ----------------------------------------------------------------------
def fast():
    """"""
    print("This is a very fast print statement")
    print("This is a print")
    print("I run fast!")


# ----------------------------------------------------------------------
def slow():
    """"""
    time.sleep(3)
    print("I run slow!")


# ----------------------------------------------------------------------
def medium():
    """"""
    time.sleep(0.5)
    print("I run a little slowly...")


# ----------------------------------------------------------------------
def main():
    """"""
    fast()
    slow()
    medium()


if __name__ == '__main__':
    main()
