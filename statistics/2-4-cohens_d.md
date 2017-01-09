[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> We follow the code given in the book essentially verbatim:
```  
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
```     
and then use the function in the book called CohenEffectSize() with  firsts['totalwgt_lb']
and others['totalwgt_lb'] as arguments. We find that the effect size is .088672927072602 (with others as our X_1). This indicates that first pregnancies tend to have slightly smaller birth weights. This is possibly explained by a finding earlier in the chapter, that first pregnancies tend to be slightly shorter.
