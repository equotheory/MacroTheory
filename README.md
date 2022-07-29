Abros Language
=======
Abros is a Python-like programming language. In this project by Qazzain, we have fixed some aspects we belived lacking in python. Scroll to the bottom to find the core idea.

The project contains:

- Regular expression based lexer
- Top-down recursive descent parser
- AST-walking interpreter
- REPL of the code

Abros doesn't require any third-party libraries.

What the language looks like:



    func map(arr, fn):
        r = []
        for val in arr:
            r = r + [fn(val)]
        r

    func factorial(n):
        if n <= 1:
            1
        else:
            n * factorial(n - 1)

    print(map(1...10, factorial))


You can find more examples in ``tests`` directory.

#### To run: python3 -m abros file.abr

## Extra Commands In AbsCLI
```
$ abs load pip
$ abs create pip
```

## Why so mixed with python?
You may have noticed that a lot of this code and modules work with python and sometimes only with python and not Abros becuase of the core idea of the project:
> The core idea of Abros is for not to replace Python but to work alongside it as an extention to patch certain parts that don't live up to modern-day workflows. This might mean creating Abros and it might mean creating python packages.
## Whats Next
Abros is a project with no limits.
We want to, after the basic ecosystem is set, improve Abros so that .abr files can work with or include Python.
## Versions Roadmap
* = Done
^ = nexr
1*, 1.2^, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9