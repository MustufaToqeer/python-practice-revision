# # # def greet():
# # #     print("Hello")


# # # greet()

# # # say_hello = greet
# # # say_hello()


# # # def get_greet():
# # #     def greet_2():
# # #         print("Hi")

# # #     return greet_2


# # # get_greet()()


# # # def decorator(func):
# # #     def wrapper(*args, **kwargs):
# # #         print("Before function")
# # #         result = func(*args, **kwargs)
# # #         print("After function")
# # #         return result

# # #     return wrapper


# # # new_function = decorator(greet)
# # # new_function()


# # # @decorator
# # # def greet_3():
# # #     print("Greet 3")


# # # greet_3()


# # # def greet_4():
# # #     print("Greet 4")


# # # greet_4()

# # # greet_4 = decorator(greet_4)
# # # greet_4()


# # import time
# # import logging
# # from functools import wraps

# # logger = logging.getLogger()


# # def timer(function):
# #     @wraps(function)
# #     def wrapper(*args, **kwargs):
# #         start_time = time.time()
# #         result = function(*args, **kwargs)
# #         end_time = time.time()
# #         print(f"{function.__name__} took total time : {end_time - start_time} seconds.")
# #         return result

# #     return wrapper


# # @timer
# # def add(a, b):
# #     return a + b


# # print(add(1, 2))

# # print(add.__name__)  # without functools.wraps → "wrapper"
# # print(add.__name__)  # with functools.wraps    → "add"

# # Q1 — Write from scratch
# # Write a decorator called @logger that prints this every time the function is called:
# # Calling: add | Args: (2, 3) | Kwargs: {}
# # Apply it to a function add(a, b) that returns a + b.

# import logging
# from functools import wraps

# log = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO)


# def logger(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         log.info(f"Calling: {func.__name__} | Args: {args} | Kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# @logger
# def add(a, b):
#     return a + b


# print(add(1, 2))

# """
# Q2 — Debug this
# This code has a bug. Find it and fix it without running the code first — just by reading:

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def greet(name):
#     print(f"hello {name}")

# greet("Rahul")
# """


# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result

#         return wrapper

#     return decorator


# @repeat(3)
# def greet(name):
#     print(f"hello {name}")


# greet("Rahul")


# import functools


# def double_run(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)

#     return wrapper


# def shout(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(">>>")
#         func(*args, **kwargs)
#         print("<<<")

#     return wrapper


# @double_run
# @shout
# def say(msg):
#     print(msg)


# say("hello")

"""
@double_run
@shout
def say(msg):
    print(msg)

say = double_run(shout(say))
"""

# import logging
# from functools import wraps

# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO)


# def retry(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for index in range(1, 4):
#             try:
#                 result = func(*args, **kwargs)
#                 return result
#             except Exception as exception:
#                 if index == 3:
#                     raise exception
#                 logging.info(f"Attempt {index} failed, retrying ...")

#     return wrapper


# def decorator_a():
#     pass


# def decorator_b():
#     pass


# @decorator_a
# @decorator_b
# def func():
#     pass


# func = decorator_b(func)
# func = decorator_a(func)
# func()
