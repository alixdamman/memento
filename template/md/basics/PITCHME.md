---
@title[Why Python?]
## Why Python?

@ol
- open source
- easy to learn
- clean syntax
- large community
- easy to extend by building libraries
- lots of (scientific) libraries

---

## Presenting Code

---?code=template/src/say_hello_func.py&lang=python&title=Create a function in Python

@[1](declare a new function)
@[2-14](documentation)
@[3](description)
@[5-8](parameters)
@[10-13](examples (doctests))
@[15](body of the function)
@[17](call to the function)

---

## Simple types

```python
# int
i0 = -5
i1 = 5

# float
f0 = 5.05
f1 = 1.e3

# boolean
b0 = True
b1 = False

# string
s0 = 'string'  # simple quote '
s1 = "string"  # double quotes "
```

@[1-3]
@[5-7]
@[9-11]
@[13-15]

---

`new_var = old_var` creates a copy the variable `old_var`

![](template/img/simple_types.png)

[execute here](https://goo.gl/BzRbPV)

---

## Composed types

```python
# list
c = [5, 5.05]

# tuple
t = (5, 5.05)

# dictionary
d = {'int': 5, 'float': 5.05}
```

@[1-2]
@[4-5]
@[7-8]

---

`new_var = old_var` creates an 'alias' for the variable `old_var`

![](template/img/composed_types_alias.png)

[execute here](https://goo.gl/o6wBWc)

---

`new_var = old_var.copy()` creates a copy for the variable `old_var`

![](template/img/composed_types_copy.png)

[execute here](https://goo.gl/qDHtps)
