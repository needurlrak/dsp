[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> First we convert inches to cm: 6'1" is approximately 185.42 cm and 5'10" is approximately 177.8 cm. Now, we calculate

scipy.stats.norm.cdf(185.42, loc = 178, scale = 7.7) - scipy.stats.norm.cdf(177.8, loc = 178, scale = 7.7) =0.34274683763147368

So roughly 34.2% of the US male population is between 5'10" and 6'1".
