a---
layout: NotesPage
title: Reasoning About Code Safety
permalink: /work_files/dev/cs/racs
prevLink: /work_files/dev/cs.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Magic Numbers and Exploitation](#content1)
  {: .TOC1}
  * [Reasoning About Memory Safety](#content2)
  {: .TOC2}
  * [Reasoning About Safety](#content3)
  {: .TOC3}
  * [Making C Safe [Alternatives of the Alternatives]](#content4)
  {: .TOC4}
  * [Software Security Issues and Testing](#content5)
  {: .TOC5}
  * [Working Towards Secure Systems](#content6)
  {: .TOC6}
  * [Approaches for Building Secure Software/Systems (Summary)](#content6)
  {: .TOC6}

</div>

***
***

## Magic Numbers and Exploitation
{: #content1}

1. **Exploit:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents11}
    :   An **Exploit** is a piece of software, a chunk of data, or a sequence of commands that takes advantage of a bug or vulnerability to cause unintended or unanticipated behavior to occur on computer software, hardware, or something electronic.

2. **Magic Numbers:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents12}
    :   Exploits are very _brittle_ in nature.  
        > Changing one number in an exploit (program) can render it useless.  
        > > Ex. Making sure the exploit runs on the right version.

3. **EXTRABACON:**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents13}
    :   Is an NSA exploit for Cisco ASA "Adaptive Security Appliances".
    :   * It had an exploitable stack-overflow vulnerability in the SNMP read operation.
        * But actual exploitation required two steps:  
            1. Query for the particular version (with an SMTP read).  
            2. Select the proper set of magic numbers for that version.

4. **ETERNALBLUE(screen):**{: style="color: SteelBlue  "}{: .bodyContents1 #bodyContents14}
    :    Another NSA exploit that got stolen by the same group ("ShadowBrokers") which stole EXTRABACON.
    :   * Eventually it was very robust.  
            * This was "god mode":  
            remote exploit Windows through SMBv1(Windows File sharing).
    :   * But initially it was jokingly called ETERNALBLUESCREEN:  
            * Because it would crash Windows computers more reliably than exploitation.

***

## Reasoning About Memory Safety
{: #content2}

1. **Memory Safety:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents21}
    :   No accesses to undefined memory.
        > "Undefined" is with respect to the semantics of the programming language.
    :   Undefined behavior is:  
            * **At Minimum:** is a bug.
            * **At Maximum:** is exploitable.

2. **Read Access:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents22}
    :   An attacker can read memory that he isn't supposed to.

3. **Write Access:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents23}
    :   An attacker can write memory that she isn't supposed to.

4. **Execute Access:**{: style="color: SteelBlue  "}{: .bodyContents2 #bodyContents24}
    :   An attacker can transfer control flow to memory that they isn't supposed to.

***

## Reasoning About Safety
{: #content3}

1. **How can we have confidence that our code executes in a safe fashion?:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents31}
    :   **Approach:** build up confidence on a function-by-function / module-by-module basis.

2. **Modularity:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents32}
    :   **Modularity** provides boundaries for our reasoning.
        * **Preconditions:** what must hold for function to operate correctly.  
        * **Postconditions:** what holds after function completes.  
            > These basically describe a contract for using the module.
    :   The notion of modularity apply to individual statements.  
        > Statement-1’s postcondition should logically imply Statement-2’s precondition.
    :   **Invariants:** conditions that always hold at a given point in a function.
        > This particularly matters for loops.

21. **How to Prove Memory-Safety?**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents321} \\
    1. Identify each point of memory access.  
    2. Write down precondition it requires.  
    3. Propagate requirement up to beginning of function.  

    * Complicated loops might need us to use induction to show invariants:  
        * _Base case:_ first entrance into loop.
        * _Induction:_ show that postcondition of last statement of loop, plus loop test condition, implies invariant.

        <button>Example.</button>{: .showText value="show"
        onclick="showTextPopHide(event);"}
        ![img](/main_files/cs/racs/All.png){: width="87%" hidden=""}

3. **Example 1:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents33}
    :   ```c
        int deref(int *p) {
            return *p;
        }
        ```
    :   * **The Pre-Condition:** requires ```p``` to not be NULL, and ```p``` a valid pointer.  
        $$ \implies \\ $$  
    :   ```c
        void *mymalloc(size_t n) {
            void *p = malloc(n);
            if (!p) { perror("malloc"); exit(1); }
            return p;
        }
        ```        
        * **The Post-Condition:** ensures that the return value is not NULL, and is a valid pointer.

4. **Example 2:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents34}
    :   ```c
        int sum(int a[], size_t n)  {
            int total = 0;
            for (size_t i=0; i<n; i++)
                total += a[i];
            return total;
        }
        ```
    :   * **The Pre-Condition:** requires ```p``` to not be NULL, and ```p``` a valid pointer.  

5. **Drawbacks:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents35}
    :   Unfortunately, the process descrived above is too tedius.  
        Thus, programers tend to _not_ safe-check their code.

6. **Alternative:**{: style="color: SteelBlue  "}{: .bodyContents3 #bodyContents36}
    :   Don't use C or C++.
    :   **Instead,** Use a _Safe_ language:  
            Turns "undefined" memory references into an immediate exception or program termination.
    :   Now you simply don't have to worry about buffer overflows and similar vulnerabilities.
    :   **Safe Languages:**  Python - JAVA - GO - RUST - SWIFT

***

## Making C Safe [Alternatives of the Alternatives]
{: #content4}
<p class="message">
The goal here is not to pervent all exploitaition. It is to raise the bar for the attackers. <br/>
We will aim for defense in depth. Ensuring that undefined behavior leads to crash.
</p>

1. **Stack Canaries:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents41}
    * **Goal:** protect the return pointer from being overwritten by a stack buffer.
    * **Defends-Against:** Stack Over-Flows.
    * **Method:** 
        1. When the program starts up, create a random value.
        2. When returning in a function, first check the canary against the stored value.
    * **Drawbacks:** (i.e. How to NOT kill the Canary?)  
        1. Find out what the canary is (e.g. via an [FSV](/work_files/dev/cs/ms#bodyContents36)) and then write its value back.
        2. Write around the canary. 
        3. Overflow the Heap.
    * **Properties:**  
        1. A simple stack overflow doesn’t work anymore.
        2. Minor and nearly negligible overhead.
        3. It requires a compiler flag to enable on Linux.

2. **Non-Executable Pages:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents42} \\
    * **Goal:** make pages in the TLB/Page-Table non-executable.
    * **Defends-Against:** Injections.
    * **Method:** 
        1. The TLB/Page-Table has three bits R(ead)/W(rite)/X(cute). 
        2. Maintain W xor X as a global propert.
            > Now, you can’t write code to the stack or heap.
    * **Drawbacks:** (i.e. How to NOT kill the Canary?)  
        1. Unfortunately, this is insufficient. There are multiple ways around it.
    * **Properties:**  
        1. A simple stack overflow doesn’t work anymore.
        2. Effectively no performance impact.
        3. Does break some code.
        4. Yet still often not ubiquitous on embedded systems.  
            > e.g. Cisco ASA
    * **Exploits that best this defending approach:**  
        * **Return into libc:**  set up the stack frame such that the "return" excutes the "excute" command.
        * **Return Oriented Programming:** 
            1. Given a code library, find a set of fragments (gadgets) that when called together execute the desired function.  
                > The "ROP Chain".  
            2. Inject onto the stack a sequence of saved "return addresses" that will invoke this.  
            
        > Unfortuntely, many such Exploits are available online.

3. **Address Space Layout Randomization:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents43} \\
    * **Goal:** Randomize the addresses of the excutables in memory.  
    * **Defends-Against:** Buffer Over-Flows.
    * **Method:** 
        1. Rather than deterministically allocating the process layout, the OS randomizes the starting base of each excutable section (text, data/BSS, heap, stack).
        2. Randomly relocate everything (Every library, the start of the stack & heap).
    * **Drawbacks:** (i.e. How to NOT kill the Canary?)  
        1. Find out what the canary is (e.g. via an [FSV](/work_files/dev/cs/ms#bodyContents36)) and then write its value back.
        2. Write around the canary. 
        3. Overflow the Heap.
    * **Properties:**  
        1. When combined with W^X, need an information leak to exploit.
            > A way to find the address of a function,   
              to find the magic offset needed to modify your ROP chain
        2. With 64b of space you have lots of entropy, making them harder to exploit.
        3. It requires a compiler flag to enable on Linux.

4. **Defense-in-Depth in Practice:**{: style="color: SteelBlue  "}{: .bodyContents4 #bodyContents44}
    :   * **Apple iOS** uses ASLR in the kernel and userspace, W^X whenever possible.
    :       > All applications are sandboxed to limit their damage: The kernel is the TCB.
    :   * **The ["Trident"](https://info.lookout.com/rs/051-ESQ-475/images/pegasus-exploits-technical-details.pdf) Exploit:** was used by a spyware vendor, the NSO group, to exploit iPhones of targets.  
            * To remotely exploit an iPhone, the NSO group's exploit had to:  
                1. Exploit Safari with a memory corruption vulnerability.
                    > Gains remote code execution within the sandbox: write to a R/W/X page as part of the JavaScript JIT.
                2. Exploit a vulnerability to read a section of the kernel stack.
                    > Saved return address & knowing which function called breaks the ASLR
                3. Exploits a vulnerability in the kernel to enable code execution

***

## Software Security Issues and Testing
{: #content5}

1. **Why does software have vulnerabilities?:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents51} \\
    1. Programmers are humans, and humans make mistakes.
        > Use Tools.
    2. Programmers often aren’t security-aware.
        > Learn about common types of security flaws.
    3. Programming languages aren’t designed well for security.
        > Use better languages (Java, Python, ...).

2. **What makes testing a program for security problems difficult?:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents52} \\
    1. We need to test for the absence of something.
        > Security is a negative property!
        > > "nothing bad happens, even in really unusual circumstances"
    2. Normal inputs rarely stress security-vulnerable code.

3. **How can we test more thoroughly?:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents53} \\
    1. Random inputs (fuzz testing)
    2. Mutation
    3. Spec-driven design.

4. **How do we tell when we’ve found a problem?:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents54}
    :   When we have found a crash or other deviant behavior.

5. **How do we tell when we’ve found a problem?:**{: style="color: SteelBlue  "}{: .bodyContents5 #bodyContents55}
    :   This is a very hard task but _code-coverage tools_ can help.

## Working Towards Secure Systems
{: #content6}

1. **Patching:**{: style="color: SteelBlue  "}{: .bodyContents6 #bodyContents61}
    :   Along with securing individual components, we need to _keep them up to date_.
    :   * **What's hard about patching?:**  
            1. Can require restarting production systems.
            2. Can break crucial functionality.
            3. Management burden:
                * It never stops (the "patch treadmill").
                * It can be difficult to track just what’s needed where.

3. **Vulnerability scanning:**{: style="color: SteelBlue  "}{: .bodyContents6 #bodyContents63}
    :   Probe your systems/networks for known flaws.

4. **Penetration testing ("pen-testing"):**{: style="color: SteelBlue  "}{: .bodyContents6 #bodyContents64}
    :   Pay someone to break into your systems.
            > Provided they take excellent notes about how they did it!

## Approaches for Building Secure Software/Systems (Summary)
{: #content7}

1. **Run-time checks:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents71} \\
    1. Automatic bounds-checking (overhead).
    2. What do you do if check fails?.

2. **Address randomization:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents72} \\
    1. Make it hard for attacker to determine layout.
    2. But they might get lucky / sneaky.

3. **Non-executable stack, heap:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents73} \\
    1. May break legacy code.
    2. See also Return-Oriented Programming (ROP).

4. **Monitor code for run-time misbehavior:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents74} \\
    1. E.g., illegal calling sequences.
    2. But again: what do you if detected?.

5. **Program in checks / “defensive programming”:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents75} \\
    1. E.g., check for null pointer even though sure pointer will be valid.
    2. Relies on programmer discipline.

6. **Use safe libraries:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents76} \\
    1. E.g. strlcpy, not strcpy; snprintf, not sprintf.
    2. Relies on discipline or tools.

7. **Bug-finding tools:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents77} \\
    1. Excellent resource as long as not many false positives.

8. **Code review:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents78} \\
    1. Can be very effective but expensive..

9. **Use a safe language:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents79} \\
    1. E.g., Java, Python, C#, Go, Rust.
    2. Safe = memory safety, strong typing, hardened libraries.
    3. Installed base? Programmer base? Performance?.

10. **Structure user input:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents710} \\
    1. Constrain how untrusted sources can interact with the system.
    2. Perhaps by implementing a reference monitor.

11. **Contain potential damage:**{: style="color: SteelBlue  "}{: .bodyContents7 #bodyContents711} \\
    1. E.g., run system components in jails or VMs.
    2. Think about privilege separation.
