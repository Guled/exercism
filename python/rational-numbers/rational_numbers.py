from __future__ import division

# //Implment generation the prime number that multiple (find the first ones)
# // https://www.dummies.com/education/math/pre-algebra/how-to-reduce-a-fraction-to-its-lowest-terms/

# //How to generate prime numbers https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19
class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
         return (self.numer * other.denom + self.denom * other.numer) / (other.numer * other.denom)

    def __sub__(self, other):
        return (self.numer * other.denom - self.denom * other.numer) / (other.numer * other.denom)

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass


# The difference of two rational numbers r1 = self.numer/other.numer and r2 = self.denom/other.denom is r1 - r2 = self.numer/other.numer - self.denom/other.denom = (self.numer * other.denom - self.denom * other.numer) / (other.numer * other.denom).
#
# The product (multiplication) of two rational numbers r1 = self.numer/other.numer and r2 = self.denom/other.denom is r1 * r2 = (self.numer * self.denom) / (other.numer * other.denom).
#
# Dividing a rational number r1 = self.numer/other.numer by another r2 = self.denom/other.denom is r1 / r2 = (self.numer * other.denom) / (self.denom * other.numer) if self.denom * other.numer is not zero.
#
# Exponentiation of a rational number r = a/b to a non-negative integer power n is r^n = (a^n)/(b^n).
#
# Exponentiation of a rational number r = a/b to a negative integer power n is r^n = (b^m)/(a^m), where m = |n|.
#
# Exponentiation of a rational number r = a/b to a real (floating-point) number x is the quotient (a^x)/(b^x), which is a real number.
#
# Exponentiation of a real number x to a rational number r = a/b is x^(a/b) = root(x^a, b), where root(p, q) is the qth root of p.
