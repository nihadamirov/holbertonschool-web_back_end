# Async Comprehension

![image](https://github.com/user-attachments/assets/f6824591-f422-4a54-9f40-909809420c9c)


## Master

**By:** Emmanuel Turlay, Staff Software Engineer at Cruise  
**Weight:** 1  
**Migrated to checker v2:** Yes  
**Note:** Your score will be updated as you progress.

## Concepts

For this project, we expect you to look at these concepts:

- Python - Asynchronous execution
- Python - Asynchronous Programming

## Resources

Read or watch:

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.x)
- The length of your files will be tested using `wc`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your functions should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## tasks 

| Number | Name                               | Short Description                                                                                                                                              | Filename                     |
|--------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| 0      | Async Generator                    | Write a coroutine called `async_generator` that loops 10 times, asynchronously waits 1 second, and yields a random number between 0 and 10.                     | `0-async_generator.py`       |
| 1      | Async Comprehensions               | Write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`, then returns them.          | `1-async_comprehension.py`   |
| 2      | Run time for four parallel comprehensions | Write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`, measuring and returning the runtime. | `2-measure_runtime.py`        |
