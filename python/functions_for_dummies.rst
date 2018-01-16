
Functions
=========

-  What is a function?
-  Why use functions?
-  How to define and call functions?
-  Keyword Arguments
-  Default Argument Values
-  Local vs global variables

What is a function?
-------------------

A function is a **block of organized, reusable code** that is used to
**perform a single, specific task**. It performs actions on input data
(arguments) and returns a result if necessary.

Why use functions?
------------------

-  **Reusability**: functions are reusable blocks of code and allow to
   avoid copy/paste which is a dangerous practice and pollutes the code.

-  **Organization**: functions help to organize your model. As a model
   grows in complexity, having all the code live inside a "main" script
   becomes increasingly complicated. Using functions allows to divide
   complicated tasks into smaller, simpler ones, and reduce the overall
   complexity of your model.

-  **Abstraction**: Functions can be used as "black boxes", you don't
   need to know what's inside to use them. To use a function, you just
   need to know its name (= what it is supposed to do), the input
   arguments and the optional output.

How to define and call functions?
---------------------------------

How to define functions?
~~~~~~~~~~~~~~~~~~~~~~~~

-  Function blocks begin with the keyword **def** followed by the
   **function name** and parentheses **( )**.
-  Input **arguments** are placed within these parentheses. They are
   optional.
-  The code block within every function starts with a colon (**:**) and
   is indented.
-  A function can optionally start by its **documentation**: string
   written between triple quotes """ (mutiple lines documentation is
   allowed).
-  The optional statement **return [variable(s) or expression]** exits a
   function and returns output result(s).

Syntax:

.. code:: python

    def function_name(arguments):
        """function documentation = docstring (optional)"""
        <function code>
        # optional
        return [variable(s) or expression]

Let's begin with a simple function with no input arguments and returning
nothing:

.. code:: ipython3

    def it_helpdesk():
        """Print universal solution to any computer problem"""
        print("Have you try to turn it off and on again?")

Function with an input argument:

.. code:: ipython3

    def it_helpdesk(problem):
        """Print universal solution to any computer problem"""
        print("Hello, IT")
        print(problem)
        print("Have you try to turn it off and on again?")

Function returning something:

.. code:: ipython3

    # (case 1) function returning an expression
    def it_helpdesk():
        """Return universal solution to any computer problem"""
        return "Have you try to turn it off and on again?"
    
    # (case 2) function returning a variable
    def it_helpdesk():
        """Return universal solution to any computer problem"""
        answer = "Have you try to turn it off and on again?"
        return answer

More complicated: a function with an input argument and returning
something:

.. code:: ipython3

    def it_helpdesk(problem):
        """Return universal solution to any computer problem"""
        print("Hello, IT")
        print(problem)
        return "Have you try to turn it off and on again?"

How to call functions?
~~~~~~~~~~~~~~~~~~~~~~

-  To call a function, simply type its name followed by parentheses ().
-  If the function defines input arguments, pass them inside the
   parentheses. Passed arguments can be values or variables.
-  If the function returns a result, precedes it with a new variable and
   the symbol =.

Syntax:

.. code:: python

    # function with no input argument and returning nothing
    function_name()
    # function with input arguments and returning nothing
    function_name(arguments)
    # function with input arguments and returning a result
    res = function_name(arguments)

Function with no input arguments:

.. code:: ipython3

    def it_helpdesk():
        """Print universal solution to any computer problem"""
        print("Have you try to turn it off and on again?")
    
    # call and execute function "it_helpdesk()"
    it_helpdesk()


.. parsed-literal::

    Have you try to turn it off and on again?


Function with an input argument:

.. code:: ipython3

    def it_helpdesk(problem):
        """Print universal solution to any computer problem"""
        print("Hello, IT")
        print(problem)
        print("Have you try to turn it off and on again?")
        
    # call function "it_helpdesk" and pass a string as input argument
    it_helpdesk("My computer smells weird and is very hot")
    
    print("\n10 minutes later...\n")
    
    # call function "it_helpdesk" and a variable 
    # (!) the name of the passed variable can be different from the name of the input argument
    my_problem = "My computer is on fire!"
    it_helpdesk(my_problem)


.. parsed-literal::

    Hello, IT
    My computer smells weird and is very hot
    Have you try to turn it off and on again?
    
    10 minutes later...
    
    Hello, IT
    My computer is on fire!
    Have you try to turn it off and on again?


Function returning something:

.. code:: ipython3

    def it_helpdesk():
        """Return universal solution to any computer problem"""
        return "Have you try to turn it off and on again?"
    
    # call function "it_helpdesk"
    answer = it_helpdesk()
    print(answer)


.. parsed-literal::

    Have you try to turn it off and on again?


More complicated: a function with an input argument and returning
something:

.. code:: ipython3

    def it_helpdesk(problem):
        """Return universal solution to any computer problem"""
        print("Hello, IT")
        print(problem)
        return "Have you try to turn it off and on again?"
    
    # call function "it_helpdesk" and pass a string as input argument
    answer = it_helpdesk("My computer smells weird and is very hot")
    print(answer)
    
    print("\n10 minutes later...\n")
    
    # call function "it_helpdesk" and a variable 
    # (!) the name of the passed variable can be different from the name of the input argument
    my_problem = "My computer is on fire!"
    answer = it_helpdesk(my_problem)
    print(answer)


.. parsed-literal::

    Hello, IT
    My computer smells weird and is very hot
    Have you try to turn it off and on again?
    
    10 minutes later...
    
    Hello, IT
    My computer is on fire!
    Have you try to turn it off and on again?


**Note**: it is allowed to return several values:

.. code:: ipython3

    # Note: this function already exists in Python
    def divmod(a, b):
        """Return the quotient and the remainder of the division of two numbers"""
        return a // b, a % b
    
    quotient, remainder = divmod(25, 3)
    print(quotient, remainder)


.. parsed-literal::

    8 1


Keyword Arguments
-----------------

Default Argument Values
-----------------------

Local vs global variables
-------------------------

In Python, you can use two kinds of variables: - **global variables**:
defined outside functions. They are accessible everywhere inside the
module (module = file with .py extension). - **local variables**:
created inside functions. They are accessible only inside the function
in which they are created.

**WARNING**: a global and a local variable can have the same name!

Python variables
~~~~~~~~~~~~~~~~

.. figure:: attachment:python_global_local_vars.png
   :alt: python\_global\_local\_vars.png

   python\_global\_local\_vars.png

**Rule 1**: functions have access to global variables:

.. code:: ipython3

    global_var = "I'm a global variable"
    
    def my_function():
        # a function can access to variables defined outside them
        print(global_var)
        
    my_function()


.. parsed-literal::

    I'm a global variable


**Rule 2**: variable assignments (i.e. using operator =) in a function
create or act on local variables.

**Rule 3**: if a local variable has the same name as a global one,
Python will access the local variable (*variable shadowing*).

.. code:: ipython3

    var = "I'm a global variable"
    
    def my_function():
        # create a local variable named 'var' 
        var = "I'm a local variable"
        # if a local variable has the same name as a global one, Python will access the local variable
        print(var)
        
    my_function()
    # the global variable has not been modified
    print(var)


.. parsed-literal::

    I'm a local variable
    I'm a global variable


**Rule 4**: input arguments behave like global variables:

.. code:: ipython3

    var = "I'm a global variable"
    
    def my_function(var):
        # input arguments behave like global variables
        # remember: variable assignments (i.e. using operator =) in a function create or act on local variables
        var = "I'm a local variable"
    
    # pass the global variable to function and try to modify it
    my_function(var)
    # the global variable has not been modified
    print(var)


.. parsed-literal::

    I'm a global variable


Don't want to lose your modifications? Use **return**:

.. code:: ipython3

    var = "I'm a global variable"
    
    def my_function(var):
        # variable assignments (i.e. using operator =) in a function create or act on local variables
        var = var + " and I have been modified"
        # Don't want to lose your modifications? Use return
        return var
    
    # set new content to variable 'var'
    var = my_function(var)
    # the variable 'var' has been modified
    print(var)


.. parsed-literal::

    I'm a global variable and I have been modified


End of story? Nope.

Python is vicious as a snake...

**Rule 5**: Modifying elements of a list, dictionary, array or any
"composed" variable does not create new local variables:

.. code:: ipython3

    from larray import *
    
    array_1 = LArray([1, 2, 3, 4, 5], 'a=a0..a4')
    array_2 = LArray([1, 2, 3, 4, 5], 'b=b0..b4')
    
    def my_function():
        # assigning the whole array creates a local array
        array_1 = LArray([6, 7, 8, 9, 10], 'a=a0..a4')
        # assigning subset of an array does not create local array
        array_2['b1:b4'] = LArray([7, 8, 9, 10], 'b=b1..b4')
    
    my_function()
    print("array_1 has not been modified:")
    print(array_1)
    print("array_2 has been modified:")
    print(array_2)


.. parsed-literal::

    array_1 has not been modified:
    a  a0  a1  a2  a3  a4
        1   2   3   4   5
    array_2 has been modified:
    b  b0  b1  b2  b3  b4
        1   7   8   9  10


What if want to modify the whole content of an array?

Simply add **[:]** next to the array you want to modify:

.. code:: ipython3

    from larray import *
    
    array_1 = LArray([1, 2, 3, 4, 5], 'a=a0..a4')
    
    def my_function():
        # trick: to change to whole content of an array, add [:] next to the array
        array_1[:] = LArray([6, 7, 8, 9, 10], 'a=a0..a4')
    
    my_function()
    print("array_1 has been modified:")
    print(array_1)


.. parsed-literal::

    array_1 has been modified:
    a  a0  a1  a2  a3  a4
        6   7   8   9  10


What to remember?
~~~~~~~~~~~~~~~~~

1. **Functions have access to global variables**.
2. **Variable assignments (i.e. using operator =) in a function create
   or act on local variables**.
3. **If a local variable has the same name as a global one, Python will
   access the local variable (variable shadowing)**.
4. **Input arguments behave like global variables**.
5. **Modifying elements of a list, dictionary, array or any "composed"
   variable does not create new local variables**.
6. **To change the whole content of an array without creating a new
   local one, add [:] next to the array (e.g. pop[:] = 0)**.

**TIPS**:

Global variables may be dangerous. When it's possible, write functions
as **independent** blocks of code and pass any external variables you
need to work with as input arguments.

When you have to deal with many external variables (arrays), passing all
of them as arguments may become cumbersome. In that case, remember that
modifying global variables inside functions is allowed in Python but
must be done carefully.

More infos on defining functions?
---------------------------------

See the `official documentation of Python
(3.5) <https://docs.python.org/3.5/tutorial/controlflow.html#defining-functions>`__
