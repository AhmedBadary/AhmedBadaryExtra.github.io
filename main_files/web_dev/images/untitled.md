---
layout: NotesPage
title: HW 1
permalink: /work_files/dev/cs/hw
prevLink: /work_files/dev/cs.html
---

## Q.1)

a) True
b) False
c) False
d) False
e) False

There are no "slip days".


\\

\\

\\

\\

\\

\\

\\

\\


\\

***

## Q.5)

    a) MAC.
    b) Confidentiality.

## Q.2)

a) Yes. 
    So, here, Mallory knows the Cyphertext and she also knows the IV. So, all she had to do was xor the planetext {no / yes} and then compare that to the cybercypher. 


b) NO.  
    So, here, Mallory has noway of knowing what the key is for encryption. And since the key has high entropy bruteforcing it is computationally infeasible.

***

## Q.3)

Mary can create a message by concatenating M with T_1 xor M. Which once you invoke AES on that you xor T_1 with itself and then with M (T_3=AES (T_1 xor T_1 xor M_1) = T_1).



## Q.4)

a) We define the Encryption-Scheme E(x) and the Hash Function H(x) and use them in the function:  
    F(x) = E(H(x)).  
    we just use E_k(X)=AES-CTR_k(X), with a predetermined value for IV.  
    Now, we do $$x_i^\ast = F(x_i)$$.

b) All the numbers generated are determinstic and that means that the inputs determins the output completely, so any (x=y) => (x*=y*).

c) AES and ECB are invertible. And Notice that our hash is secure so no collision is produced from that.

d) Two hashes will have same first 16b is very very unlikely 1/2^128, The hash, now, conceals the identity of the block.


## Q.5)

a) $$S^3 = M \text{mod } n$$.

b) She can just S=M=1, by noticing $$1 = 1 \text{mod } n$$.

c) $$4^3 \times M^{3d} = 4^3 \times M\text{ mod } n$$.

d) Notice that, in b we can't figure out that message that was outputted by H because H doesn't decrypt. C fails for the same reason to get a message 64* The hash.

## Q.5)


a) MAC: Mainly because this is a symmetric key system.  
    It uses a secret key to make specific tags, and the messages associated prove the original message. 

    Authenticity: Well, it appears that the text said nothing about the other two traits. Authenticity is established through identity verification.

b) The attackers can compute the Hash of the filename and put it in the link. So, we want to make it hard to generate this.
b)