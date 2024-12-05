import logging

# iterators
def generator_pair(n):
    for _ in range(n):
        if _ % 2 == 0:
            yield _
q = generator_pair(10)
print(list(q))



def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
fib = fibonacci_generator(1)
for _ in range(10):
    print(fib)


# generators
def iterator_revers(rand_list):
    for _ in reversed(rand_list):
        yield _

my_rand_list = [1, 2, 3, 4, 5]
for num in iterator_revers(my_rand_list):
    print(num)



def iterator_pair(rand_list):
    for _ in rand_list:
        if _ % 2 == 0:
            yield _

my_rand_list2 = [1, 2, 3, 4, 5]
print(list(iterator_pair(my_rand_list2)))


# # decorators
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Test {func.__name__} executed with result: {result}")
        return result
    return wrapper

@log_decorator
def add(a,b):
    return a + b

result_add = add(2, 3)



def validate_params_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(f"Function error {func.__name__}: {e}")
            return f"An error occurred {e}"
    return wrapper


@validate_params_decorator
def divide(a, b):
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, '2'))
print(divide(10, 0))