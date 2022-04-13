def benchmark(function):
    import time

    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = function(*args, **kwargs)
        end = time.perf_counter_ns()
        return f"Result: {result}\nTime benchmark: {end-start} sec"
    return wrapper


@benchmark
def number_power(number, power):
    return number ** power
