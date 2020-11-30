# a function from the end of the sim notebook is needed earlier so instead of inserting it above
# without explanation it's reasonably clean to just quickly import it and explain it later...
from mpmath import mp
ticks_per_day = 24000
av_chance_per_tick = 3/4096 * (0.96 * 1/500 + 0.04 * 1)
def binompdf(n, p, k):
	return mp.binomial(n, k) * p**k * (1 - p)**(n - k)
def binomcdf(n, p, k):
	return sum([binompdf(n, p, x) for x in range(k + 1)])
def prob_hatch_by_day(i):
	return 1 - binomcdf(i * ticks_per_day, av_chance_per_tick, 2)
