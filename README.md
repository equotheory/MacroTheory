Amphire Lang
=======
Amphire is a Python-like programming language. In this project by MS9, we have fixed some aspects we belived lacking in python. Scroll to the bottom to find the core idea.

The project contains:

- Regular expression based lexer
- Top-down recursive descent parser
- AST-walking interpreter
- REPL of the code

Amphire doesn't require any third-party libraries.

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

#### To run: python3 -m amphire file.abr

## Amphire - Run through AmpCLI - New
Run `python3 AmpCLI/cli.py` to run
```
# Make sure to enter correct name with extension
# To run a .abr amphire file:
$ amp setup
# or if a heavy file
$ amp -render:first:setup
```
## Extra Commands In AmpCLI
```
$ amp load pip
$ amp create pip
--
$ amp load abr
# custom name
$ amp load abr -n
```

## Why so mixed with python?
You may have noticed that a lot of this code and modules work with python and sometimes only with  python and not Amphire becuase of the core idea of the project:
> The core idea of Amphire is for not to replace Python but to work alongside it as an extention to patch certain parts that don't live up to modern-day workflows. This might mean creating Amphire and it might mean creating python packages.
## Whats Next
Amphire is a project with no limits.
We want to, after the basic ecosystem is set, improve Amphire so that .abr files can work with or include Python.
## Versions Roadmap
This symbol *, means done and the next version or patch is in dev.
| Version      | Patches |
| ----------- | ----------- |
| 1 *     | X       |
| 2*   | Y, Z, N        |
|3*| V, B, O|
|RE|1*, 2*, 3|
|XER|Qf*, Qm*, Qe*|
|Fal|Xr*, Xf*, Xm*, Xe|