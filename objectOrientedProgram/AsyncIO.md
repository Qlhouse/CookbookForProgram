+ subroutine
Also use the term “function”, “method” or “procedure”. Denote bits of code that can be called by other code.

+ coroutine

+ yield

+ generator

+ stack
stack (run time stack) 

Stack includes two kinds of things - call frames and storage for local variables:

1. call frames—one for each function call

A call frame is just an area of memory that is set aside to keep track of a function call in progress. Call frames are born when a function is called, and they die when a function returns.

Call frames are kept on the run time stack:

calling a function adds a call frame at the top

returning from a function deletes the top frame

Each call frame contains the name of the function that was called, and "where to pick up from" (as a line number) when the function call returns.



2. storage for local variables.

+ frame

+ Corunctine class & object

+ async def
Declare an asynchronous coroutine function

+ await

+ CPU-bound VS. IO-bound
