#!/usr/bin/env python3
from sys import addaudithook
from os import _exit
from re import match


def safe_eval(exit, code):
    globals()['_exit'] = 123
    def hook(*a):
        print(a)
        print(exit)
        exit(0)

    def dummy():
        pass

    dummy.__code__ = compile(code, "<code>", "eval")
    addaudithook(hook)
    return dummy()

# 1+print(__import__('os').access("flag.txt", 4))
# 1+print(__import__('os').readlink("flag.txt"))

if __name__ == "__main__":
    expr = input("Math expression: ")
    if len(expr) <= 200 and match(r"[0-9+\-*/]+", expr):
        print(safe_eval(_exit, expr))
    else:
        print("Do you know what is a calculator?")
