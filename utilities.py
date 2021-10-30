from random import expovariate


def exp_rv(mean):
    """Return an exponential random variable with the given mean."""
    return expovariate(1 / mean)
