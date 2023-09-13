from fractions import Fraction

n = int(input())
m = int(input())

def ReduceFraction(n, m):
	a = Fraction(n, m)
	return a.numerator, a.denominator


answer = ReduceFraction(n, m)
print(f'{answer[0]} {answer[1]}')
