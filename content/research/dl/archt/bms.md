---
layout: NotesPage
title: Boltzmann Machines
permalink: /work_files/research/dl/archits/bms
prevLink: /work_files/research/dl.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Boltzmann Machines](#content1)
  {: .TOC1}
  * [Restricted Boltzmann Machines (RBMs)](#content2)
  {: .TOC2}
  * [Deep Boltzmann Machines (DBNs)](#content3)
  {: .TOC3}
  <!-- * [FOURTH](#content4)
  {: .TOC4} -->
</div>

***
***

__Resources:__{: style="color: red"}  
{: #lst-p}
* [A Thorough Introduction to Boltzmann Machines](http://willwolf.io/2018/10/20/thorough-introduction-to-boltzmann-machines/)  
* [RBMs Developments (Hinton Talk)](https://www.youtube.com/watch?v=VdIURAu1-aU&t=0s)  
* [A Tutorial on Energy-Based Learning (LeCun)](http://yann.lecun.com/exdb/publis/pdf/lecun-06.pdf)  
* [DBMs (paper Hinton)](http://proceedings.mlr.press/v5/salakhutdinov09a/salakhutdinov09a.pdf)  
* [Generative training of quantum Boltzmann machines with hidden units (paper)](https://arxiv.org/abs/1905.09902)  
* [Binary Stochastic Neurons in TF](https://r2rt.com/binary-stochastic-neurons-in-tensorflow.html)  
* [Geometry of the Restricted Boltzmann Machine (paper)](https://arxiv.org/pdf/0908.4425.pdf)  


## Preliminaries
{: #content9}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91} -->

2. **The Boltzmann Distribution:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92}  
    The __Boltzmann Distribution__ is a probability distribution (or probability measure) that gives the _probability that a system will be in a certain state_ as a function of that _state's energy_ and the _temperature of the system_:  
    <p>$$p_{i} = \dfrac{1}{Z} e^{-\frac{\varepsilon_{i}}{k_B T}}$$</p>  
    where $$p_{i}$$ is the probability of the system being in state $$i$$, $$\varepsilon_{i}$$ is the energy of that state, and a constant $$k_B T$$ of the distribution is the product of __Boltzmann's constant__ $$k_B$$ and __thermodynamic temperature__ $$T$$, and $$Z$$ is the __partition function__.    

    The distribution shows that <span>states with __*lower* energy__ will always have a __*higher* probability__ of being occupied</span>{: style="color: goldenrod"}.  
    The __*ratio* of probabilities of two states__ (AKA __Boltzmann factor__) only depends on the states' energy difference (AKA __Energy Gap__):{: #bodyContents92BF}  
    <p>$$\frac{p_{i}}{p_{j}}=e^{\frac{\varepsilon_{j}-\varepsilon_{i}}{k_B T}}$$</p>  

    __Derivation:__{: style="color: red"}  
    The Boltzmann distribution is the distribution that __maximizes the entropy__:  
    <p>$$H\left(p_{1}, p_{2}, \cdots, p_{M}\right)=-\sum_{i=1}^{M} p_{i} \log_{2} p_{i}$$</p>  
    subject to the constraint that $$\sum p_{i} \varepsilon_{i}$$ equals a particular mean energy value.  

    [This is a simple __Lagrange Multipliers__ maximization problem (can be found here).](https://bouman.chem.georgetown.edu/S98/boltzmann/boltzmann.htm)  


    __Applications in Different Fields:__{: style="color: red"}  
    {: #lst-p}
    * __Statistical Mechanics__{: style="color: purple"}  
        The __canonical ensemble__ is a probability distribution with the form of the Boltzmann distribution.  
        It gives the probabilities of the various possible states of a closed system of fixed volume, in thermal equilibrium with a heat bath.  
    * __Measure Theory__{: style="color: purple"}  
        The Boltzmann distribution is also known as the __Gibbs Measure__.  
        The __Gibbs Measure__ is a probability measure, which is a generalization of the canonical ensemble to infinite systems.  
    * __Statistics/Machine-Learning__{: style="color: purple"}  
        The Boltzmann distribution is called a __log-linear model__.  
    * __Probability Theory/Machine-Learning__{: style="color: purple"}  
        The Boltzmann distribution is known as the __softmax function__.  
        The __softmax function__ is used to represent a __categorical distribution__.  
    * __Deep Learning__{: style="color: purple"}  
        The Boltzmann distribution is the [__sampling distribution__](https://en.wikipedia.org/wiki/Sampling_distribution) of __stochastic neural networks__ (e.g. RBMs).  



    <br>

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents93}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents94}


***
***


## Boltzmann Machines
{: #content1}

1. **Boltzmann Machines (BMs):**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    A __Boltzmann Machine (BM)__ is a type of <span>stochastic recurrent neural network</span>{: style="color: purple"} and <span>Markov Random Field (MRF)</span>{: style="color: purple"}.    

    __Goal - What do BMs Learn:__{: style="color: red"}  
    Boltzmann Machines were originally introduced as a general **_“connectionist”_ approach** to learning <span> arbitrary probability distributions over binary vectors</span>{: style="color: goldenrod"}.  
    They are capable of learning <span>internal representations of data</span>{: style="color: goldenrod"}.  
    They are also able to <span>represent and solve (difficult) combinatoric problems</span>{: style="color: goldenrod"}.  

    __Structure:__{: style="color: red"}  
    ![img](https://cdn.mathpix.com/snip/images/GcOUC--gwjuIgl1bAzFcW77LqLOD3siTNaol-pbyhV8.original.fullsize.png){: width="20%"}
    {: #lst-p}
    * __Input__:  
        BMs are defined over a $$d$$-dimensional __binary random vector__ $$\mathrm{x} \in\{0,1\}^{d}$$.  
    * __Output__:  
        The units produce __binary results__.  
    * __Units:__  
        * __Visible__ Units: $$\boldsymbol{v}$$  
        * __Hidden__ Units: $$\boldsymbol{h}$$  
    * __Probabilistic Model__:  
        It is an __energy-based model__; it defines the __joint probability distribution__ using an __energy function__:  
        <p>$$P(\boldsymbol{x})=\frac{\exp (-E(\boldsymbol{x}))}{Z}$$</p>    
        where $$E(\boldsymbol{x})$$ is the energy function and $$Z$$ is the partition function.  
    * __The Energy Function:__  
        * With only __visible units__:  
            <p>$$E(\boldsymbol{x})=-\boldsymbol{x}^{\top} \boldsymbol{U} \boldsymbol{x}-\boldsymbol{b}^{\top} \boldsymbol{x}$$</p>  
            where $$U$$ is the "weight" matrix of model parameters and $$\boldsymbol{b}$$ is the vector of bias parameters.  
        * With both, __visible and hidden units__:  
            <p>$$E(\boldsymbol{v}, \boldsymbol{h})=-\boldsymbol{v}^{\top} \boldsymbol{R} \boldsymbol{v}-\boldsymbol{v}^{\top} \boldsymbol{W} \boldsymbol{h}-\boldsymbol{h}^{\top} \boldsymbol{S} \boldsymbol{h}-\boldsymbol{b}^{\top} \boldsymbol{v}-\boldsymbol{c}^{\top} \boldsymbol{h}$$</p>  


    __Approximation Capabilities:__{: style="color: red"}  
    A BM with only __visible units__ is limited to modeling <span>linear relationships</span>{: style="color: purple"} between variables as described by the weight matrix[^2].  
    A BM with __hidden units__ is a <span>universal approximator of probability mass functions over discrete variables</span>{: style="color: goldenrod"} _(Le Roux and Bengio, 2008)_.  


    __Relation to Hopfield Networks:__{: style="color: red"}  
    A Boltzmann Machine is just a <span>__Stochastic__ Hopfield Network with __Hidden Units__</span>{: style="color: purple"}.  
    BMs can be viewed as the __stochastic__, __generative__ counterpart of Hopfield networks.  

    <button>Comparison and Discussion</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    <div markdown="1">
    It is important to note that although Boltzmann Machines bear a strong resemblance to Hopfield Networks, they are actually nothing like them in there functionality.  
    {: #lst-p}
    * __Similarities__:  
        * They are both networks of __binary units__.  
        * They both are __energy-based__ models with the same __energy function__ 
        * They both have the same __update rule/condition__ (of estimating a unit’s output by the sum of all weighted inputs).  
    * __Differences__:  
        * __Goal:__ BMs are NOT memory networks. They are not trying to store things. Instead, they employ a [different computational role](/work_files/research/dl/archits/hopfield#bodyContents18dcr); they are trying to learn <span>__latent representations__ of the data</span>{: style="color: purple"}.  
            The goal is __representation learning__.   
        * __Units__: BMs have an extra set of units, other than the visible units, called __hidden units__. These units represent __latent variables__ that are not observed but learned from the data.  
            These are necessary for representation learning.  
        * __Objective__: BMs have a different objective; instead of minimizing the energy function, they <span>minimize the error (__KL-Divergence__) between the *"real"* distribution over the data and the *model* distribution over global states</span>{: style="color: purple"} (marginalized over hidden units).  
            Interpreted as the error between the input data and the reconstruction produced by the hidden units and their weights.  
            This is necessary to capture the training data probability distribution.  
        * __Energy Minima__: energy minima were useful for Hopfield Nets and served as storage points for our input data (memories). However, they are very harmful for BMs since there is a _global objective_ of finding the best distribution that approximates the real distribution.  
            This is necessary to capture the training data probability distribution "well".   
        * __Activation Functions__: the activation function for a BM is just a *__stochastic__* version of the __binary threshold__ function. The unit would still update to a binary state according to a threshold value but with the <span>update to the unit state being governed by a probability distribution (__Boltzmann distribution__)</span>{: style="color: purple"}.  
            This is necessary (important$$^{ * }$$) to escape energy minima.  
    </div>


    __Relation to the Ising Model:__{: style="color: red"}  
    The global energy $$E$$ in a Boltzmann Machine is identical in form to that of the Ising Model.  




    __Notes:__{: style="color: red"}  
    {: #lst-p}
    * __Factor Analysis__ is a <span>__Causal__ Model</span>{: style="color: purple"} with _continuous_ variables.  
    <br>


2. **Unit-State Probability:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}  
    * The __units__ in a BM are *__binary units__*.  
    * Thus, they have __*two* states__ $$s_i \in \{0,1\}$$ to be in:  
        1. __On__: $$s_i = 1$$   
        2. __Off__: $$s_i = 0$$  
    * The __probability that the $$i$$-th unit will be *on* ($$s_i = 1$$)__ is:  
        <p>$$p(s_i=1)=\dfrac{1}{1+ e^{-\Delta E_{i}/T}}$$</p>  
        where the scalar $$T$$ is the __temperature__ of the system.  
        * The RHS is just the __logistic function__. Rewriting the probability:  
        <p>$$p(s_i=1)=\sigma(\Delta E_{i}/T)$$</p>  

        <button>Derivation</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        * Using the [__Boltzmann Factor__](#bodyContents92BF) (ratio of probabilities of states):  
            <p>$$\begin{align}
                \dfrac{p(s_i=0)}{p(s_i=1)} &= e^{\frac{E\left(s_{i}=0\right)-E\left(s_{i}=1\right)}{k T}} \\
                \dfrac{1 - p(s_i=1)}{p(s_i=1)} &= e^{\frac{-(E\left(s_{i}=1\right)-E\left(s_{i}=0\right))}{k T}} \\
                \dfrac{1}{p(s_i=1)} - 1 &= e^{\frac{-\Delta E_i}{k T}} \\ 
                p(s_i=1) &= \dfrac{1}{1 + e^{-\Delta E_i/T}} 
                \end{align}
                $$</p> 
            where we absorb the Boltzmann constant $$k$$ into the artificial Temperature constant $$T$$.   
            {: hidden=""}  

    


3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}

***

## Restricted Boltzmann Machines (RBMs)
{: #content2}

1. **Restricted Boltzmann Machines (RBMs):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    __Restricted Boltzmann Machines (RBMs)__ 

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}

***

## Deep Boltzmann Machines (DBNs)
{: #content3}

1. **Deep Boltzmann Machines (DBNs):**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    __Deep Boltzmann Machines (DBNs)__ 

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}

[^1]: The unit deep within the network is doing the same thing, but with different boundary conditions.  
[^2]: Specifically, the probability of one unit being on is given by a linear model (__logistic regression__) from the values of the other units.  