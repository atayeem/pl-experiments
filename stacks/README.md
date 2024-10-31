# Stacks
This program language works by having every single operation either push to or pull from a stack. The stack is not the only place to store data, as values can be assigned to letters.

Here are some basic operations:

Push the integer 2 to the stack.
`2`

Push the string "Hello" and the float 2.3 to the stack.
`"Hello"2.3`

Push the integers 2 and 3 to the stack.
`2 3`

Assign the value 2 to the variable x, which is undefined. The assignment operation pops the last item off the stack and stores it into a variable
`2x`

Now if you write x, it will push 2 to the stack, and will not be reassigned unless you do this:
`3$x`

Otherwise, if you wrote
`3x`
it would push 3, followed by 2.

Push 2, then 3, then pop both of them and add 5 to the stack.
`2,3+`

Push a function which adds 1 to the last element on the stack to the stack.
`[1+]`

Pushing a function doesn't do anything except appending to the stack. To call it, you can do this:
`[1+]ff`
The first f consumes the function from the stack, and the second one calls it.

If instead you want to push a function to the stack, you can do this:
`.f`
This will not call the function, and instead push it to the stack.

Nested function declarations are also supported.
`[[1+][2-]]ffAB`
What this does is call a function to push two functions to the stack, then assigns them to A and B respectively. After this operation, A becomes `[2-]` and B becomes `[1+]`.

Basic arithmetic and logical operations are supported, including:
`+, -, *, /, %, =, <, >, &, |, ^, !, ~ (negative of the previous number)`

There are also some stack operations:
`N` (nothing), which does nothing.
`D` (dump), which prints the whole stack as it is.
`o` (output), which prints the last element on the stack and pops it.

Some operations take arguments:
`c` (copy), which pops a number from the stack, and copies that number of elements from the stack.
Ex: `1,2,3,3c`, which turns the stack to `1, 2, 3, 1, 2, 3`
Ex: `1,2,3,2c`, which turns the stack to `1, 2, 3, 2, 3`

`d` (delete), which pops a number from the stack, and deletes that number of elements from the stack.
Ex: `1, 2, 3, 2d`, which turns the stack to `1`

`G` (grab), which pops a number from the stack, and adds the number that is that far behind to the stack.
Ex: `1, 2, 3, 2g`, which turns the stack to `1, 2, 3, 2`
Ex: `1, 2, 3, 3g`, which turns the stack to `1, 2, 3, 1`
Note: `4G` is equivalent to `4c3d`, and this is in the examples, as G was not implemented yet.

`g` (get), which takes user input. The element it pops from the stack determines the type of the input.
Ex: `0go`, take in a string as input and print the string.
Ex: `1g1+o`, take in an integer as input and print the integer + 1.
Ex: `2g3.2+`, take in a float as input and print the float + 1.

Some operations take functions as arguments:
`i` (if), which pops a boolean, then two functions off the stack. 
An if statement looks like this:
`[else condition] [if condition] [boolean] i`
Ex: `.g.f2,3=i`, which executes f if 2 equals 3, else it executes g.
Ex: `[1c0>.N.~3gi]f`, which defines a function f that takes the absolute value of the top item on the stack.
This one's a little complex, so here's how to interpret it.
```
[-2]
1c 
[-2, -2]
0
[-2, -2, 0]
> (Note that the operands are backwards, this is doing 0 > -2)
[-2, True]
.N
[-2, True, {do nothing}]
.~
[-2, True, {do nothing}, {negate}]
i (i eats the top three elements and executes negate)
[2]
```

`r` (repeat), which repeats the function 2g 1g times.
It is of the form: `[function] [repetitions] r`
Note: -1 makes the loop go forever.
Ex: `["Hello, world!\n"o]1~r`, which prints Hello World forever.
Note: The same behavior can be implemented with recursion:
Ex: `[1+1cof]ff`, which prints increasing numbers.
However, you quickly run into the call stack limit.
