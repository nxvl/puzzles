"""
Solves: http://www.spotify.com/es/jobs/tech/best-before/
Author:
    Nicolas Valcarcel <nvalcarcel@gmail.com>

"""
import sys
import unittest
from datetime import date
from itertools import permutations


def read_input(raw_in):
    if len(raw_in) > 1:
        print "Malformed Input: Valid input \"A{1,4}/B{1,4}/C{1,4}\""
        sys.exit(1)
    else:
        return tuple([int(x) for x in raw_in[0].split("/")])


def half_date(tup, year):
    today = date.today()
    if today.year > year:
        ret = None
    else:
        a = date(year, tup[0], tup[1])
        b = date(year, tup[1], tup[0])
        if (a > b) and (b > today):
            ret = b
        elif a > today:
            ret = a
        else:
            ret = None

    return ret


def full_date(tup):
    today = date.today()
    ret = None
    for x in permutations(tup):
        try:
            curr = date(x[0] + 2000, x[1], x[2])
        except ValueError:
            continue

        if (curr > today) and ((ret and (curr < ret)) or (not ret)):
            ret = curr

    return ret


def get_bestbefore(tup):
    tmp = list(tup)
    half = False

    for x in tup:
        if x > 2000:
            tmp.remove(x)
            ret = half_date(tuple(tmp), x)
            half = True

    if not half:
        ret = full_date(tup)

    if ret:
        return ret.isoformat()
    else:
        return "%d/%d/%d is illegal" % tup


# Tests
class ModuleTests(unittest.TestCase):
    def setUp(self):
        self.ina = "02/4/67"
        self.outa = "2067-02-04"
        self.tupa = (02, 4, 67)

        self.inb = "31/9/73"
        self.outb = "31/9/73 is illegal"
        self.tupb = (31, 9, 73)

    def test_read_input(self):
        self.assertEqual(read_input([self.ina]), self.tupa)
        self.assertEqual(read_input([self.inb]), self.tupb)

    def test_half_date(self):
        self.assertEqual(half_date((10, 04), 2013), date(2013, 04, 10))
        self.assertEqual(half_date((10, 04), 2000), None)

    def test_full_date(self):
        self.assertEqual(full_date(self.tupa), date(2067, 02, 04))
        self.assertEqual(full_date(self.tupb), None)
        self.assertEqual(full_date((10, 04, 13)), date(2013, 04, 10))
        self.assertEqual(full_date((10, 04, 00)), None)

    def test_get_bestbefore(self):
        self.assertEqual(get_bestbefore(self.tupa), self.outa)
        self.assertEqual(get_bestbefore(self.tupb), self.outb)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        sys.argv.pop(1)
        unittest.main()
    elif len(sys.argv) == 1:
       tup = read_input(sys.stdin.readlines())
       print get_bestbefore(tup)
    else:
        print "Usage: %s [test]" % sys.argv[0]
