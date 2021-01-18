#!/usr/local/bin/python3.7
import sqlite3
import sys
import os

OK = 0
WA = 1
PE = 4
RE = 5
CF = 6

author_solution = "author_solution.sql"
os.rename('answer', 'answer.py')


def author(db_name):
    con = sqlite3.connect(db_name)
    solution = open(author_solution, "rt", encoding="utf8").read().strip()
    result = con.execute(solution).fetchall()
    con.close()
    result = [x[0] for x in result]
    return result


try:
    db_name = open('input', "rt", encoding="utf8").read().strip()
    user_result = [x.strip() for x in open('output', "rt", encoding="utf8").readlines()]
    author_result = author(db_name)
    for entry in zip(user_result, author_result):
        print(entry)
    check = author(db_name) == user_result
    if check:
        print('Correct answer')
        sys.exit(OK)
    else:
        print('Incorrect answer')
        sys.exit(WA)

except Exception as e:
    print(e)
    sys.exit(RE)
