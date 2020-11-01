# Hypothesis tests with unknown variances

In last weeks exercises we introduced the following new flowchart to describe how we perform these hypothesis tests:

![](hypo-tests.003.jpeg)

We discussed how by reporting the p-value rather than simply stating whether there was sufficient evidence to reject the null hypothesis or not we are giving stakeholders a better sense of our result.  We can of course still write that, "_the null hypothesis is rejected in favour of the alternative_" if we see that the p-value is less than 5% or "_there is insufficient evidence to reject the null hypothesis_," if the p-value is greater than this threshold.  By also reporting the p-value, however, we are giving stakeholders a better sense of the reason for our decision on what to write.  They can thus way up the evidence themselves and choose whether to reject the null hypothesis or not.

In last week's exercises, I also explained that when we perform these hypothesis tests we are usually not given the variance of the distribution.  In last week tasks, I thus showed you how when you perform the hypothesis test:

__Null hypothesis__: the expectation of the distribution that the data in `mydata.dat` is sampled from is 5
__Alternative hypothesis__: the expectation for the distribution that the data in `mydata.dat` is sampled from is greater than 5

you can use an estimate of the sample variance:

![](https://render.githubusercontent.com/render/math?math=s^2=\frac{n}{n-1}\left[\frac{1}{n}\sum_{i=1}^nX_i^2-\left(\frac{1}{n}\sum_{i=1}^nX_i\right)^2\right])

when you compute the test statistic:

![](https://render.githubusercontent.com/render/math?math=T=\frac{\frac{1}{n_1}\sum_{i=1}^{n_1}X_i-\frac{1}{n_2}\sum_{j=1}^{n_2}Y_j-\theta_0}{\sqrt{\frac{\sigma_1^2}{n_1}%2B\frac{\sigma_2}{n_2}}})

You are probably already guessing the task here.  __I want you to complete the code in the cell on the right, which tests whether or not the data in the file `mydata.dat` is a series of samples from a distribution with an expectation of 5__.  To complete the exercise you will need to complete the following functions:

1. `testStatistic` - this function takes two arguments in input an NumPy array called `data` that contains the samples and a scalar called `mu0` which is the expectation of the distribution that is assumed under the null hypothesis.  This function should return the test statistic, T, that is defined using the formula above.  You will need to compute the sample variance within this function.
2. `pvalue` - this function takes two arguments in input an NumPy array called `data` that contains the samples and a scalar called `mu0` which is the expectation of the distribution that is assumed under the null hypothesis.  To complete this function you need to call `testStatistic` and you then need to calculate and return the __p-value__ based on the value of the __statistic__ that is returned by this function.
