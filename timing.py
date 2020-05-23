import time


def timing(function, inputs):
    start = time.time()
    for i in inputs:
        _ = function(i)
    stop = time.time()
    elapsed = (stop - start) * 1000 * 1000  # milliseconds
    return elapsed
