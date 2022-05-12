    * Function calls push new stack frames onto the stack.
    * A stack frame includes space for all the local variables used by that function, and other book-keeping information used by the compiler for this function invocation.
    * On Intel (x86) machines, the stack grows down.
    > This means that the stack grows towards smaller memory addresses.
    * There is a special register, called the stack pointer (SP), that points to the beginning of the current stack frame.
    * Thus, the stack extends from the address given in the SP until the end of memory, and pushing a new frame on the stack involves subtracting the length of that frame from SP.
    * Intel (x86) machines have another special register, called the instruction pointer (IP), that points to the next machine instruction to execute.
    * For most machine instructions, the machine reads the instruction pointed to by IP, executes that instruction, and then increments the IP.
    * Function calls cause the IP to be updated differently: the current value of IP is pushed onto the stack (this will be called the return address), and the program then jumps to the beginning of the function to be called.
    * The compiler inserts a function prologue—some automatically generated code that performs the above operations—into each function, so it is the first thing to be executed when the function is called.
    * The prologue pushes the current value of SP onto the stack and allocates stack space for local variables by decrementing the SP by some appropriate amount.
    * When the function returns, the old FP and return address are retrieved from the stack, and the stack frame is popped from the stack (by restoring the old FP value).
    * Execution continues from the return address.
