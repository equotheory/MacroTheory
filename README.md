MacroTheory Language
=======
MacroTheory is a Python-like programming language. In this project by EquoTheory, we have fixed some aspects we belived lacking in python. Scroll to the bottom to find the core idea.

The project contains:

- Regular expression based lexer
- Top-down recursive descent parser
- AST-walking interpreter
- REPL of the code

MacroTheory doesn't require any third-party libraries.

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

# Run Command
Running a MacroTheory file is very easy.
```python3 -m macro fileName.abr```
In MCLI: 
```
$ mc run
>> Dir+File: # If in same dir, just enter {filename}.abr, if not then customize to folder/file.abr
```

## Extra Commands In MCLI (MacroCLI)
```
$ mc set tool=pip # Set pip as default; will download. If installed, skip.
$ mc pkg get
>> Package Name: 
$ mc pkg get+ver # For specific version
```

## Why so mixed with python?
You may have noticed that a lot of this code and modules work with python and sometimes only with python and not MacroTheory becuase of the core idea of the project:
> The core idea of MacroTheory is for not to replace Python but to work alongside it as an extention to patch certain parts that don't live up to modern-day workflows. This might mean creating MacroTheory and it might mean creating python packages.
## Whats Next
MacroTheory is a project with no limits.
We want to, after the basic ecosystem is set, improve MacroTheory so that .abr files can work with or include Python.

## Versions Guide

Version can be found in MacroTheory/src/macro/__ init __ .py

Anything version with A as a prefix is in alpha.

B --> Beta
P - Pre-Release - We are here.
Z - Release 1 - 3 Versions
X - 1-10 Versions 