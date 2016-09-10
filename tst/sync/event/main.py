#
# @file main.py
#
# @section License
# Copyright (C) 2016, Erik Moqvist
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# This file is part of the Pumbaa project.
#

from pumbaa import Event
import harness


def test_help():
    EVENT = Event()
    help(Event)
    help(EVENT)


def test_read_write():
    EVENT = Event()

    EVENT.write(0x6)
    assert EVENT.size() == 1
    assert EVENT.read(0x2) == 0x2
    assert EVENT.read(0x4) == 0x4


def test_bad_arguments():
    EVENT = Event()

    try:
        EVENT.read(None)
    except TypeError as e:
        assert str(e) == "can't convert NoneType to int"
    else:
        assert False

    try:
        EVENT.write(None)
    except TypeError as e:
        assert str(e) == "can't convert NoneType to int"
    else:
        assert False


def main():
    testcases = [
        (test_help, "test_help"),
        (test_read_write, "test_read_write"),
        (test_bad_arguments, "test_bad_arguments")
    ]
    harness.run(testcases)


if __name__ == '__main__':
    main()
