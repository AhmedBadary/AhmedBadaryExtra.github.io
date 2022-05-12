---
layout: NotesPage
title: Reinforcement Learning
permalink: /work_files/research/rl
prevLink: /work_files/research/
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Intro - Reinforcement Learning](#content1)
  {: .TOC1}
  * [SECOND](#content2)
  {: .TOC2}
  * [THIRD](#content3)
  {: .TOC3}
</div>

***
***


[Deep RL WS1](https://sites.google.com/view/deep-rl-bootcamp/lectures)  
[Deep RL WS2](https://sites.google.com/view/deep-rl-workshop-nips-2018/home)  
[Deep RL Lec CS294 Berk](http://rail.eecs.berkeley.edu/deeprlcourse/)  
[Reinforcement Learning Course Lectures UCL](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)  
[RL CS188](https://inst.eecs.berkeley.edu/~cs188/fa18/)  
[Deep RL (CS231n Lecture)](https://www.youtube.com/watch?v=lvoHnicueoE)  
[Deep RL (CS231n Slides)](http://cs231n.stanford.edu/slides/2019/cs231n_2019_lecture14.pdf)  
* [An Outsider's Tour of Reinforcement Learning (Ben Recht!!!)](http://www.argmin.net/2018/06/25/outsider-rl/)  
* [Reinforcement Learning Series (Tutorial + Code (vids))](https://www.youtube.com/playlist?list=PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv)  
* [A step-by-step Policy Gradient algorithms Colab + Pytorch tutorial](https://www.reddit.com/r/MachineLearning/comments/defiac/p_a_stepbystep_policy_gradient_algorithms_colab/)  
* [Pathmind: Reinforcement Learning Simulations (Code)](https://pathmind.com/)  
* [Reinforcement Learning Tutorial (Sentdex)](https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/)  



## Intro - Reinforcement Learning
{: #content1}

1. **Reinforcement Learning:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    
    ![img](https://cdn.mathpix.com/snip/images/KD106EKeWa3NIEqKiMNXELeZ6beGrRAXTkyVo1Iq2sc.original.fullsize.png){: width="80%"}  

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}

3. **Mathematical Formulation of RL - Markov Decision Processes:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    __Markov Decision Process__  
    
    Defined by $$(\mathcal{S}, \mathcal{A}, \mathcal{R}, \mathbb{P}, \gamma)$$:  
    {: #lst-p}
    * $$\mathcal{S}$$: set of possible states
    * $$\mathcal{A}$$: set of possible actions
    * $$\mathcal{R}$$: distribution of reward given (state, action) pair
    * $$\mathbb{P}$$: transition probability i.e. distribution over next state given (state, action) pair
    * $$\gamma$$: discount factor  

    __MDPs Algorithm/Idea:__  
    {: #lst-p}
    - At time step $$\mathrm{t}=0,$$ environment samples initial state $$\mathrm{s}_ {0} \sim \mathrm{p}\left(\mathrm{s}_ {0}\right)$$
    - Then, for $$\mathrm{t}=0$$ until done:
        - Agent selects action $$a_t$$ 
        - Environment samples reward $$\mathrm{r}_ {\mathrm{t}} \sim \mathrm{R}\left( . \vert \mathrm{s}_{\mathrm{t}}, \mathrm{a}_ {\mathrm{t}}\right)$$
        - Environment samples next state $$\mathrm{s}_ {\mathrm{t}+1} \sim \mathrm{P}\left( . \vert \mathrm{s}_ {\mathrm{t}}, \mathrm{a}_ {\mathrm{t}}\right)$$
        - Agent receives reward $$\mathrm{r}_ {\mathrm{t}}$$ and next state $$\mathrm{s}_ {\mathrm{t}+1}$$

    \- A policy $$\pi$$ is a _function_ from $$S$$ to $$A$$ that specifies what action to take in each state  
    \- Objective: find policy $$\pi^{\ast}$$ that maximizes cumulative discounted reward:  
    <p>$$\sum_{t \geq 0} \gamma^{t} r_{t}$$</p>  


    __Optimal Policy $$\pi^{\ast}$$:__{: style="color: red"}  
    We want to find optimal policy $$\mathbf{n}^{\ast}$$ that maximizes the sum of rewards.  
    We handle __randomness__  (initial state, transition probability...) by __Maximizing the *expected sum of rewards*__.  
    __Formally__,  
    <p>$$\pi^{* }=\arg \max _{\pi} \mathbb{E}\left[\sum_{t \geq 0} \gamma^{t} r_{t} | \pi\right] \quad$ \text{ with } $s_{0} \sim p\left(s_{0}\right), a_{t} \sim \pi\left(\cdot | s_{t}\right), s_{t+1} \sim p\left(\cdot | s_{t}, a_{t}\right)$$</p>  



    __The Bellman Equations:__{: style="color: red"}  
    Definition of “optimal utility” via expectimax recurrence gives a simple one-step lookahead relationship amongst optimal utility values.  
    The __Bellman Equations__ <span>_characterize_ optimal values</span>{: style="color: purple"}:    
    <p>$$\begin{aligned} V^{ * }(s) &= \max _{a}\left(s^{*}(s, a)\right. \\
                     Q^{ * }(s, a) &= \sum_{s^{\prime}} T\left(s, a, s^{\prime}\right)\left[R\left(s, a, s^{\prime}\right)+\gamma V^{ * }\left(s^{\prime}\right)\right] \\
                     V^{ * }(s) &= \max _{a} \sum_{s^{\prime}} T\left(s, a, s^{\prime}\right)\left[R\left(s, a, s^{\prime}\right)+\gamma V^{ * }\left(s^{\prime}\right)\right] \end{aligned}$$</p>  

    __Value Iteration Algorithm:__{: style="color: red"}  
    The __Value Iteration__ algorithm <span>_computes_ the optimal values</span>{: style="color: purple"}:  
    <p>$$V_{k+1}(s) \leftarrow \max _{a} \sum_{s^{\prime}} T\left(s, a, s^{\prime}\right)\left[R\left(s, a, s^{\prime}\right)+\gamma V_{k}\left(s^{\prime}\right)\right]$$</p>   
    \- Value iteration is just a fixed point solution method.  
    \- It is repeated bellman equations.  

    __Convergence:__  
    <button>Convergence</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/fTeplubG_bAgJuyrStw26Y1K9Tms89dphOrOcNseKzY.original.fullsize.png){: width="100%" hidden=""}  

    __Issues:__  
    {: #lst-p}
    * Problem 1: It’s slow – $$O(S^2A)$$ per iteration
    * Problem 2: The “max” at each state rarely changes
    * Problem 3: The policy often converges long before the values  
    * Problem 4: Not scalable. Must compute $$Q(s, a)$$ for every state-action pair. If state is e.g. current game state pixels, computationally infeasible to compute for entire state space  


    __Policy Iteration:__{: style="color: red"}  
    It is an Alternative approach for optimal values:  
    __Policy Iteration algorithm:__  
    {: #lst-p}
    * Step \#1 __Policy evaluation:__ calculate utilities for some fixed policy (not) of to
    utilitiesl until convergence
    * Step #2: __Policy improvement:__ update policy using one-step look-ahead with resulting (but not optimall) utilities af future values  
    * Repeat steps until policy converges  

    * __Evaluation:__  
        For fixed current policy $$\pi$$, find values with policy evaluation:  
        * Iterate until values converge:  
            <p>$$V_{k+1}^{\pi_{i}}(s) \leftarrow \sum_{s^{\prime}} T\left(s, \pi_{i}(s), s^{\prime}\right)\left[R\left(s, \pi_{i}(s), s^{\prime}\right)+\gamma V_{k}^{\pi_{i}}\left(s^{\prime}\right)\right]$$</p>  
    * __Improvement:__  
        For fixed values, get a better policy using policy extraction:  
        * One-step look-ahead:  
            <p>$$\pi_{i+1}(s)=\arg \max _{a} \sum_{s^{\prime}} T\left(s, a, s^{\prime}\right)\left[R\left(s, a, s^{\prime}\right)+\gamma V^{\pi_{i}}\left(s^{\prime}\right)\right]$$</p>  

    __Properties:__  
    {: #lst-p}
    * It's still __optimal__
    * Can can converge (much) faster under some conditions  


    __Comparison - Value Iteration vs Policy Iteration:__  
    <button>Comparison</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/yoH-nwG1Hunddc_DcRunAFYup5Nf6kcspI44gQ7tujw.original.fullsize.png){: width="100%" hidden=""}  


    __Q-Learning \| Solving for Optimal Policy:__{: style="color: red"}  
    A problem with __value iteration__ was: It is Not scalable. Must compute $$Q(s, a)$$ for every state-action pair.  
    __Q-Learning__ solves this by using a function approximator to estimate the action-value function:  
    <p>$$Q(s, a ; \theta) \approx Q^{* }(s, a)$$</p>  
    __Deep Q-learning:__ the case where the function approximator is a deep neural net.  

    __Training:__  
    ![img](https://cdn.mathpix.com/snip/images/Ppeh18nh-ofk-A0puhgN4__m90utYwRBYO9KTtpYDwg.original.fullsize.png){: width="80%"}  

    <button>Example Network - Learning Atari Games</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/H9XsqlC8tNbJo2VJUdZvjZkFzpCwFjhsXcd4EUgX1I0.original.fullsize.png){: width="100%" hidden=""}  

    __Experience Replay__  
    ![img](https://cdn.mathpix.com/snip/images/v_zXml9JyIzF83-gfy-07iBEQt65M22vCc5qqVLs95s.original.fullsize.png){: width="60%"}  

    __Deep Q-learning with Experience Replay - Algorithm:__  
    <button>Algorithm</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/uco5J96x_Bnz6KA8VE3XMUF2OM6rRfOsI399USWjDms.original.fullsize.png){: width="70%" hidden=""}  


    <br>
    __Policy Gradients:__{: style="color: red"}  
    An alternative to learning a Q-function.  
    Q-functions can be very complicated.  
    > Example: a robot grasping an object has a very high-dimensional state => hard to learn exact value of every (state, action) pair.  

    \- Define a __class of parameterized policies__:  
    <p>$$\Pi=\left\{\pi_{\theta}, \theta \in \mathbb{R}^{m}\right\}$$</p>  
    \- For each policy, define its __value__:  
    <p>$$J(\theta)=\mathbb{E}\left[\sum_{t \geq 0} \gamma^{t} r_{t} | \pi_{\theta}\right]$$</p>  
    \- Find the __optimal policy__ $$\theta^{ * }=\arg \max _ {\theta} J(\theta)$$ by __gradient ascent on *policy parameters*__ (__REINFORCE Algorithm__)   

    __REINFORCE Algorithm:__{: style="color: red"}  
    __Expected Reward:__  
    <p>$$\begin{aligned} J(\theta) &=\mathbb{E}_{\tau \sim p(\tau ; \theta)}[r(\tau)] \\ &=\int_{\tau} r(\tau) p(\tau ; \theta) \mathrm{d} \tau \end{aligned}$$</p>  
    where $$r(\tau)$$ is the reward of a trajectory $$\tau=\left(s_{0}, a_{0}, r_{0}, s_{1}, \dots\right)$$.  
    __The Gradient:__  
    <p>$$\nabla_{\theta} J(\theta)=\int_{\tau} r(\tau) \nabla_{\theta} p(\tau ; \theta) \mathrm{d} \tau$$</p>  
    \- The Gradient is __Intractable__. Gradient of an expectation is problematic when $$p$$ depends on $$\theta$$.  
    \- __Solution:__  
    * __Trick:__  
        <p>$$\nabla_{\theta} p(\tau ; \theta)=p(\tau ; \theta) \frac{\nabla_{\theta} p(\tau ; \theta)}{p(\tau ; \theta)}=p(\tau ; \theta) \nabla_{\theta} \log p(\tau ; \theta)$$</p>  
    * __Injecting Back:__  
        <p>$$\begin{aligned} \nabla_{\theta} J(\theta) &=\int_{\tau}\left(r(\tau) \nabla_{\theta} \log p(\tau ; \theta)\right) p(\tau ; \theta) \mathrm{d} \tau \\ &=\mathbb{E}_{\tau \sim p(\tau ; \theta)}\left[r(\tau) \nabla_{\theta} \log p(\tau ; \theta)\right] \end{aligned}$$</p>  
    * __Estimating the Gradient:__ Can estimate with *__Monte Carlo sampling__*.  
        * The gradient does NOT depend on _transition probabilities:_  
            * $$p(\tau ; \theta)=\prod_{t \geq 0} p\left(s_{t+1} | s_{t}, a_{t}\right) \pi_{\theta}\left(a_{t} | s_{t}\right)$$  
            * $$\log p(\tau ; \theta)=\sum_{t \geq 0} \log p\left(s_{t+1} | s_{t}, a_{t}\right)+\log \pi_{\theta}\left(a_{t} | s_{t}\right)$$  
                $$\implies$$ 
            * $$\nabla_{\theta} \log p(\tau ; \theta)=\sum_{t \geq 0} \nabla_{\theta} \log \pi_{\theta}\left(a_{t} | s_{t}\right)$$  
        * Therefore when sampling a trajectory $$\tau,$$ we can estimate $$J(\theta)$$ with:  
            <p>$$\nabla_{\theta} J(\theta) \approx \sum_{t \geq 0} r(\tau) \nabla_{\theta} \log \pi_{\theta}\left(a_{t} | s_{t}\right)$$</p>  
    * __Gradient Estimator__:  
        <p>$$\nabla_{\theta} J(\theta) \approx \sum_{t \geq 0} r(\tau) \nabla_{\theta} \log \pi_{\theta}\left(a_{t} | s_{t}\right)$$</p>  
        * __Intuition/Interpretation__:  
            * If $$\mathrm{r}(\tau)$$ is high, push up the probabilities of the actions seen
            * If $$\mathrm{r}(\tau)$$ is low, push down the probabilities of the actions seen
        Might seem simplistic to say that if a trajectory is good then all its actions were good. But in expectation, it averages out!  
        * __Variance__:  
            * __Issue__: This also suffers from __high variance__ because credit assignment is really hard.  
            * __Variance Reduction - Two Ideas__:  
                1. Push up probabilities of an action seen, only by the cumulative future reward from that state:  
                    <p>$$\nabla_{\theta} J(\theta) \approx \sum_{t \geq 0}\left(\sum_{t^{\prime} \geq t} r_{t^{\prime}}\right) \nabla_{\theta} \log \pi_{\theta}\left(a_{t} | s_{t}\right)$$</p>  
                2. Use discount factor $$\gamma$$ to ignore delayed effects  
                    <p>$$\nabla_{\theta} J(\theta) \approx \sum_{t \geq 0}\left(\sum_{t^{\prime} \geq t} \gamma^{t^{\prime}-t} r_{t^{\prime}}\right) \nabla_{\theta} \log \pi_{\theta}\left(a_{t} | s_{t}\right)$$</p>  

                \- __Problem:__ The raw value of a trajectory isn’t necessarily meaningful. For example, if rewards are all positive, you keep pushing up probabilities of actions.  
                \- __What is important then:__ Whether a reward is better or worse than what you expect to get.  
                \- __Solution:__ Introduce a __baseline function__ dependent on the state.  
                \-Concretely, estimator is now:  
                <p>$$\nabla_{\theta} J(\theta) \approx \sum_{t \geq 0}\left(\sum_{t^{\prime} \geq t} \gamma^{t^{\prime}-t} r_{t^{\prime}}-b\left(s_{t}\right)\right) \nabla_{\theta} \log \pi_{\theta}\left(a_{t} | s_{t}\right)$$</p>  
                * __Choosing a Baseline__:  
                    * __Vanilla REINFORCE__:  
                        A simple baseline: constant moving average of rewards experienced so far from all trajectories.  
                    * __Actor-Critic__:  
                        We want to push up the probability of an action from a state, if this action was better than the __expected value of what we should get from that state__.  
                        Intuitively, we are happy with an action $$a_{t}$$ in a state $$s_{t}$$ if $$Q^{\pi}\left(s_{t}, a_{t}\right)-V^{\pi}\left(s_{t}\right)$$ is large. On the contrary, we are unhappy with an action if it's small.  
                        Now, the estimator:  
                        <p>$$\nabla_{\theta} J(\theta) \approx \sum_{t \geq 0}\left(Q^{\pi_{\theta}}\left(s_{t}, a_{t}\right)-V^{\pi_{\theta}}\left(s_{t}\right)\right) \nabla_{\theta} \log \pi_{\theta}\left(a_{t} | s_{t}\right)$$</p>  
                        * __Learning $$Q$$ and $$V$$__:  
                            We learn $$Q, V$$ using the __Actor-Critic Algorithm__.  

    __Actor-Critic Algorithm:__{: style="color: red"}  
    An algorithm to learn $$Q$$ and $$V$$.  
    We can combine Policy Gradients and Q-learning by training both:  
    * __Actor:__ the policy, and 
    * __Critic:__ the Q-function  

    __Details:__  
    - The actor decides which action to take, and the critic tells the actor how good its action was and how it should adjust
    - Also alleviates the task of the critic as it only has to learn the values of (state, action) pairs generated by the policy
    - Can also incorporate Q-learning tricks e.g. experience replay
    - Remark: we can define by the advantage function how much an action was better than expected  

    __Algorithm:__  
    <button>Algorithm</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](https://cdn.mathpix.com/snip/images/oRVXry6DNumat6k3h_a3IYPz4Qjb-3_iiCg1ShkjwSk.original.fullsize.png){: width="80%" hidden=""}  


    <br>
    __Summary:__{: style="color: red"}  
    {: #lst-p}
    - __Policy gradients:__ very general but suffer from high variance so
    requires a lot of samples. Challenge: sample-efficiency
    - __Q-learning:__ does not always work but when it works, usually more
    sample-efficient. Challenge: exploration  

    - __Guarantees:__  
        - __Policy Gradients:__ Converges to a local minima of J(𝜃), often good enough!
        - __Q-learning:__ Zero guarantees since you are approximating Bellman equation with a complicated function approximator



<!-- 4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18} -->

***

<!-- ## SECOND
{: #content2}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23} -->