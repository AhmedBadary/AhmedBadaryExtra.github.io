---
layout: hw
title: HW 4
permalink: /work_files/research/conv_opt/hw/hw4
prevLink: /work_files/research/conv_opt.html
date: 22/12/1996
course: EE 227A
number: 4
---



## Q.1)

1. Trivially, assume $$\exists$$ optimial point $$p_1^\ast \in \chi_1$$ and assume that $$p_1^\ast$$ is also optimal for $$\chi_2$$. Now, since $$\chi_2$$ is bigger than $$\chi_1$$, assume $$\exists p_2' \in \chi_2 : p_2' < p_1 , \: \forall p_1 \in \chi_1$$. Now, pick that point $$p_2'$$, notice that $$p_2' < p_1\ast$$ ; thus, contradiction, since $$p_1\ast$$ was supposed to be optimal. Thus, any optimal point in $$\chi_1$$ must be bigger than or equal to the optimal point in $$\chi_2$$ since it is contained in it.

2. Notice that $$\chi_1 \subseteq \chi_2 \implies \chi_1 \cap \chi_3 \subseteq \chi_2 \cap \chi_3$$. Now since (1) above is true, we know that $$p_2^\ast = p_1^\ast = p_{13}^\ast \geq p_{23}^\ast$$. We, also, know that, since $$\chi_1 \cap \chi_3 \subseteq \chi_2$$, then $$p_{23}^\ast \geq p_2^\ast = p_{13}^\ast$$.  
    From the points above we conclude that $$p_{23}^\ast = p_{13}^\ast$$.

3. Notice that if $$p_1^\ast = p_2^\ast$$ then by uniquness of the optimal we know that the points that attained them must be equal. The same is true for the points attianing $$p_{23}^\ast$$ and $$p_2^\ast$$; since $$p_{23}^\ast = p_2^\ast$$.  
    Thus, all the points that attain $$p_1^\ast, p_2^\ast, $$ and $$ p_{23}^\ast$$ are the equal.  
    Thus, the point attaing $$p_1^\ast \in \chi_1 \cap \chi_2 \implies p_1^\ast = f_0(x_1^\ast) \geq f_0(x_{13}^\ast) = p_{13}^\ast$$, where we assume that $$x_1^ast$$ and $$x_{13}^\ast$$ are the points that attain $$p_1^\ast$$ and $$p_{13}^\ast$$ respectively.  
    Now, $$\chi_1 \cap \chi_2 \subseteq \chi_2 \cap \chi_3 \implies p_{13}^\ast \geq p_{23}^\ast =p_2^\ast = p_1^\ast$$.  
    Thus we can fianlly conclude that $$p_1^\ast = p_{13}^\ast$$. 


## Q.2)

We write the standard form,  
$$p^\ast = \min_{x\in \mathbf{R}^n} -\sum \alpha_i ln(x_i) : (-x) \leq 0, \vec{1}^Tx - c = $$.  
Now, we write the lagrangian $$\mathcal{L} = - \sum \alpha_i ln(x_i) - \lambda (\vec{1}^Tx - c)$$.  
$$(1) \delta_x \mathcal{L} = -\sum_i^n \alpha_i/x_i - n\lambda$$.  
$$(2) \delta_\lambda \mathcal{L} = -\sum_i^n x_i + c\lambda$$.   
We set them both equal to zero and we solve for $$x$$ to get  
$$x_i = \dfrac{c}{\sum_i^n \alpha_i} * \alpha_i$$.   
We plug in to find the optimal value,  
$$p^\ast = (\sum_i^n \alpha_i ) * (ln( c / (\sum_i^n \alpha_i) * \alpha_i ) = \alpha ln(c/\alpha) +n*\sum_{i=1}^n \alpha_i ln(\alpha_i)$$.


## Q.3)

1. We construct a decision vector $$x \in \{0,1\}^n$$, where $$x_i = 1$$ if item $$i$$ is sold, and $$ = 0$$ otherwise.  
    Thus, the Total revenue is obviosuly $$s^Tx$$, and the Total Transaction cost is $$ 1 + c^Tx$$. 

2. Notice that for any $$t \geq 0$$,  
     $$f(x) \leq t$$ for every $$x \in \{0,1\}^n$$ $$\iff \forall x \in \{0,1\}^n \: : \: s^Tx \leq t(1+c^Tx)$$,  
     Equivalently, $$t \geq \max_{x\in \{0,1\}^n} (s-ct)^T x = \vec{1}^T(s-ct)_+$$.  
     Thus, it holds.  

3. The constraint is active at the optimum.  
    Thus, $$ t^\ast = \max_{x\in \{0,1\}^n} (s - ct^\ast)^T x$$.  
    Thus, $$\exists x \in \{0,1\}^n : \max_{x\in \{0,1\}^n} (s-ct)^T x = (s - ct^\ast)^Tx^\ast =t^\ast$$.  
    We know that $$x^\ast$$ achives the maximum value $$ t^\ast = \dfrac{s^Tx^\ast}{1+ c^Tx^\ast}$$.  
    Now, we only need $$x^\ast$$ to be feasible which it is.  
    NOtice now that, we let $$\forall i \in \{1, \cdots, m\} \: : \: x_i^\ast = 1$$, if $$s_i >  t^\ast c_i$$, or $$0$$ otherwise. 



## Q.4)

1. $$ 
    \begin{align}
    y &= \dfrac{\beta_1x}{(\beta_2 + x)} \\
    \iff y(\beta_2+x) &= \beta_1x \\
    \iff \beta_2y + xy &= \beta_1x \\
    \iff \beta_2 + x &= \beta_1 \dfrac{x}{y} \\
    \iff \beta_2 &= \left(\dfrac{\beta_1}{y} - 1\right) x \\
    \iff \dfrac{\beta_2}{x} &= \dfrac{\beta_1}{y} - 1 \\
    \iff \dfrac{1}{y} &= \left(\dfrac{\beta_2}{\beta_1}\right)\left(\dfrac{1}{x} + \dfrac{1}{\beta_2} \right) \\
    \iff \dfrac{1}{y} &= \left(\dfrac{\beta_2}{\beta_1}\right)\dfrac{1}{x} + \dfrac{1}{\beta_1}
    \end{align}
    $$


2. We write the problem $$ \min_w \| X^Tw - z \|_2$$, where $$z = (\dfrac{1}{y_1}, \cdots, \dfrac{1}{y_m}),$$ and  
    $$ X = \left\{
     {\begin{array}{ccc}
   1/x_1 & \cdots & 1/x_m \\
   1 & \cdots & 1 
  \end{array} } \right\} $$.  
  Now, just set $$\beta^\ast  = (1/w_1^\ast, w_2^\ast/w_1^\ast)$$, where $$w^\ast$$ is determined.
