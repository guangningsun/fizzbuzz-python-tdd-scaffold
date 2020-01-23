#!/usr/bin/python
import sys
import getopt


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        print_fizzbuzz(int(args[0]))
    except EOFError:
        sys.exit(0)


def print_fizzbuzz(input_num):
    for i in range(1, input_num+1):
        if fizzbuzz(i) != "pass":
            print("%s %s" % (i, fizzbuzz(i)))


def fizzbuzz(input_num):
    if input_num % 3 == 0 and input_num % 5 != 0:
        return ("fizz")
    elif input_num % 3 != 0 and input_num % 5 == 0:
        return ("buzz")
    elif input_num % 3 == 0 and input_num % 5 == 0:
        return ("fizz buzz")
    else:
        return "pass"


if __name__ == "__main__":
    main()
