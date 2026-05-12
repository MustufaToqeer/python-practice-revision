# def generate_number_upto_5():
#     for i in range(1, 6):
#         yield i


# def squares_of_numbers():
#     for i in range(1, 11):
#         yield i**2


# squares_generator = (i**2 for i in range(1, 11))  # () instead of [] otherwise it becomes list

# print(list(generate_number_upto_5()))
# print(list(squares_of_numbers()))
# print(squares_generator)
# print(list(squares_generator))


# def regular_function():
#     print("Starting of function")
#     data = [1, 2, 3]
#     print("End of function")
#     return data


# def generator_function():
#     print("Start of generator function")
#     yield 1
#     print("Middle of generator function")
#     yield 2
#     print("Ending of generator function")
#     yield 3


# print(regular_function())
# print(generator_function())
# print(next(generator_function()))  # Prints 1
# print(next(generator_function()))  # This also prints 1 because new generator function is initialised

# gen = generator_function()
# print(next(gen))  # Prints 1
# print(next(gen))  # Prints 2
# print(next(gen))  # Prints 3
# # print(next(gen))  # Stop Iteration Error

# gen = generator_function()
# print(gen.__iter__())  # returns itself
# print(gen.__next__())  # same as next(gen)

# print("=" * 10)
# for val in generator_function():
#     print(val)

# print("=" * 10)
# # The above code is similar to the below code
# gen = generator_function()
# while True:
#     try:
#         value = next(gen)
#         print(value)
#     except StopIteration:
#         print("END")
#         break


# list — loads everything into memory immediately. 1_000_000 == 1000000  # True
# numbers = [i for i in range(1_000_000)]  # 8MB in memory right now

# # generator — computes one value at a time, uses almost no memory
# numbers = (i for i in range(1_000_000))  # barely any memory


# def read_file_bad(path):
#     with open(path) as f:
#         return f.readlines()


# print(read_file_bad("fake_file.text"))


# def read_file_good_method(path):
#     with open(path) as f:
#         for line in f:
#             yield line.strip()


# for line in read_file_good_method("fake_file.text"):
#     print(line)


# def first():
#     yield 1
#     yield 2


# def second():
#     yield 3
#     yield 4
#     yield 5


# def combined():
#     yield from first()
#     yield from second()


# print(list(combined()))

# TEST
# Q1 - A generator function fibonacci() that yields fibonacci numbers infinitely — no list, no limit


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Q2 - A generator function read_in_chunks(filepath, chunk_size) that reads a file in chunks of n bytes at a time using yield


def read_in_chunks(filepath, chunk_size):
    with open(filepath, "rb") as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data


# Q3 - A function pipeline() that chains two generators together using yield from — first yields even numbers 1–20, second yields their squares


def generate_even_numbers():
    for i in range(0, 21, 2):
        yield i


def generate_squares(numbers):
    for i in numbers:
        yield i**2


def pipeline():
    evens = generate_even_numbers()
    yield from generate_squares(evens)
