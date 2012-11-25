"""
Solves: http://www.spotify.com/es/jobs/tech/ticket-lottery/
Author:
    Nicolas Valcarcel <nvalcarcel@gmail.com>

"""
import sys
import unittest
from math import ceil


def read_input(raw_in):
    if len(raw_in) > 1:
        print "Malformed Input: Valid input \"m n t p\""
        sys.exit(1)
    else:
        (m, n, t, p) = [int(x) for x in raw_in[0].strip().split()]
        if (m < 1) or (m > 1000):
            print "m needs to be between 1 and 1000"
            sys.exit(1)
        if (n < 1) or (n > m):
            print "n needs to be between 1 and m"
            sys.exit(1)
        if (t < 1) or (t > 100):
            print "t needs to be between 1 and 100"
            sys.exit(1)
        if (p < 1) or (p > m):
            print "p needs to be between 1 and m"
            sys.exit(1)
        return (m, n, t, p)


def get_needed_winners(t, p):
    if t >= p:
        return 1
    elif p % t == 0:
        return p / t
    else:
        return ceil(p / t)


def get_bc(a, b):
    """
    Binomial Coefficient
    http://en.wikipedia.org/wiki/Binomial_coefficient
    """
    if b > (a - b):
        b = a - b

    ret = 1
    for i in xrange(1, b + 1):
        ret *= a - (b - i)
        ret /= i
    print "a = %d, b = %d, ret = %d" % (a, b, ret)
    return ret


def get_probability(m, n, p, x):
    """
    http://en.wikipedia.org/wiki/hypergeometric_distribution
    """
    a = 0
    for i in xrange(x, p + 1):
        a += (1.0 * get_bc(p, i) * get_bc(m - p, n - i)) / get_bc(m, n)

    return round(a, 10)


# Tests
class ModuleTests(unittest.TestCase):
    def setUp(self):
        self.ina = "100 10 2 1"
        self.tupa = (100, 10, 2, 1)
        self.outa = "0.1"

        self.inb = "100 10 2 2"
        self.tupb = (100, 10, 2, 2)
        self.outb = "0.1909090909"

        self.inc = "10 10 5 1"
        self.tupc = (10, 10, 5, 1)
        self.outc = "1.0"

    def test_read_input(self):
        self.assertEqual(read_input([self.ina]), self.tupa)
        self.assertequal(read_input([self.inb]), self.tupb)
        self.assertEqual(read_input([self.inc]), self.tupc)

    def test_get_needed_winners(self):
        self.assertEqual(get_needed_winners(self.tupa[2], self.tupa[3]), 1)
        self.assertEqual(get_needed_winners(self.tupb[2], self.tupb[3]), 1)
        self.assertEqual(get_needed_winners(self.tupc[2], self.tupc[3]), 1)

    def test_get_bc(self):
        self.assertEqual(get_bc(5, 4), 5)
        self.assertEqual(get_bc(45, 6), 8145060)
        self.assertEqual(get_bc(50, 10), 10272278170)

    def test_get_propability(self):
        self.assertEqual(
            get_probability(self.tupa[0], self.tupa[1], self.tupa[3], 1),
            float(self.outa)
        )
        self.assertEqual(
            get_probability(self.tupb[0], self.tupb[1], self.tupb[3], 1),
            float(self.outb)
        )
        self.assertEqual(
            get_probability(self.tupc[0], self.tupc[1], self.tupc[3], 1),
            float(self.outc)
        )


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        sys.argv.pop(1)
        unittest.main()
    elif len(sys.argv) == 1:
        (m, n, t, p) = read_input(sys.stdin.readlines())
        x = get_needed_winners(t, p)
        print get_probability(m, n, p, x)
    else:
        print "Usage: %s [test]" % sys.argv[0]
