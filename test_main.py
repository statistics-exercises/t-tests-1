import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) :
        for n in range(1,21) :
            mu = -10 +n
            bessel = 20*n / (20*n - 1)
            samples = np.random.normal(mu, 1.0, size=20*n )
            samplemean = sum(samples) / (20*n)
            sigma2 = bessel*( sum(samples*samples) / (20*n) - samplemean*samplemean )
            stat = ( samplemean - mu ) / np.sqrt(sigma2/(20*n))
            self.assertTrue( np.abs( stat - testStatistic( samples, mu) )<1e-7, "your function to calculate the test statistic is not working correctly" )
            
    def test_pvalue(self) :
         for n in range(1,21) :
             mu, sigma = -10 +n, 0.1*n
             samples = np.random.normal(mu, sigma, size=20*n )
             stat = testStatistic( samples, mu )
             pval = 1 - scipy.stats.norm.cdf(stat)
             self.assertTrue( np.abs( pval - pvalue( samples, mu ) )<1e-7, "your pvalue function does not return the correct value" )

         stat = testStatistic( data, 5 )
         pval = 1 - scipy.stats.norm.cdf(stat)
         self.assertTrue( np.abs( pval - pvalue( data, 5 ) )<1e-7, , "your pvalue function does not return the correct value" )
