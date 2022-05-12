(
* It is extremely hard to learn a model of the world without experiencing "enough examples", so the data is still extremely necessary.
* To capture an entire distribution over some data that should GENERALIZE well; is limited by how actually representative that data is of the true "data-generating" distribution, so "good" data is necessary
)


* Hypothesis: Deep CNNs have a tendency to learn superficial statistical regularities in the dataset rather than high level abstract concepts.  
* From the perspective of learning high level abstractions, Fourier image statistics can be superficial regularities, not changing object category.  
* So long as our machine learning models cheat, by relying only on superfcial statistical regularities, they remain vulnerable to out-of-distribution examples. 
* Humans generalize better than other animals thanks to a more accurate internal model of the __underlying causal relationships__.  
* 


__The need for predictive causal modeling: rare & dangerous states:__  
* Autonomous vehicles in near- accident situations.  
* Current supervised learning fails these cases because they are too rare.  
* Worse with RL (statistical inefficiency)  
* __Goal__: develop better predictive models of the world able to __generalize in completely unseen scenarios__, but it does not seem reasonable to model the sequence of future states in all their details.  
    * (Without) No need to die a thousand deaths

__Motivation:__  
* As we are deploying Machine Learning in the real world, what happens is that, the kind of data on which those systems will be used, is almost for sure are going to be statistically different from the kind of data on which it was trained.  
    * And as an example of this consider self driving cars or vehicles, for which would like them to behave well in these rare but dangerous states.  


__Invariance vs Disentangling:__{: style="color: red"}  
{: #lst-p}
* They are different concepts.  
* __Invariance__: is a property of an object/system being equal wrt. a certain change.  
    We seek to have invariant detectors, features, etc. to certain things we care about; but sensitive to other things (based on the domain).  
* __Disentangling__: 
    * __Motivation__:  
        * But if we're trying to explain the world around us, if we're trying to build machines that explain the world around them that understand their environment, we should be prudent about what aspects of the world we would like our systems to be invariant about. Maybe we want to capture everything.  
            And the most important aspect isn't what we get rid of or not, but rather how we can separate the different factors from each other.  
        * It helps us deal with __curse of dimensionality__.  


* __Good Representations (Bengio)__{: style="color: red"}  
    The idea is when we transform the data in the space, machine learning becomes easier.  
    So, in particular, the kind of complex dependencies that we see in them, say, the pixel space will become easy to model maybe with linear models or factorize models in that space.  

* __Latent Variables and Abstract Representations__{: style="color: red"}  
    ![img](https://cdn.mathpix.com/snip/images/U0kEzjna1M_8C9ghlUyWNx7gHhJ0MsSdTljBuGio8uA.original.fullsize.png){: width="60%"}  
    * __Encoder/decoder view__: maps between low $$\&$$ high-levels  
    * __Encoder does inference__: interpret the data at the abstract level 
    * __Decoder can generate new configurations__  
    * Encoder *__flattens__* and __disentangles__ the data __manifold__  
        Go from a _"spaghetti"_ of manifolds to, flat and separate manifolds.  
        * A big goal is: transform the _"curved"_ (data) manifold, into a *__flat__* manifold.  
            <button>Illustration</button>{: .showText value="show" onclick="showTextPopHide(event);"}
            ![img](https://cdn.mathpix.com/snip/images/5Vkr6YgW9bq1o0ZSp1nEGuD5U7iUDtyJFEIa5PLLHuQ.original.fullsize.png){: width="60%" hidden=""}  
        * __Checking that a manifold is *flat*__:  
            Simple Idea: Interpolate between two points on the manifold (average), if the middle point comes from the data distribution (e.g. image), then it is flat.  
            * Interpolating in h-space should give you e.g. either one image or the other, but not a blend (preserve identity).
            * Interpolating in X-space will give you e.g. a combination of the two images.  
            * <button>Illustration: from paper</button>{: .showText value="show" onclick="showTextPopHide(event);"}
                ![img](https://cdn.mathpix.com/snip/images/N0G8rIK-_pHhko9zKNfALbaaBQj6oLQkJf9F1XsH4V8.original.fullsize.png){: width="100%" hidden=""}  
    * Marginal independence in h-space


* __What's missing in DL:__{: style="color: red"}  
    <span>Deep Understanding</span>{: style="color: goldenrod"}.  
* __What is needed:__{: style="color: red"}  
    * __Generalizing Beyond i.i.d. Data__:  
        * The Learning _Theories_ need to be modified.  
        * Current ML theory is strongly dependent on the iid assumption  
        * Real-life applications often require generalizations in regimes not seen during training  
        * Humans can project themselves in situations they have never been (e.g. imagine being on another planet, or going through exceptional events like in many movies)  
        * __Solution__: <span>understanding explanatory/causal factors and mechanisms</span>{: style="color: goldenrod"}.  
            * __How:__ <span>_Clues_ to help __disentangle__ the underlaying causal factors (w/ regularization)</span>{: style="color: goldenrod"}.  

* __Humans Outperform Machines at *Autonomous Learning*:__{: style="color: red"}  
    * Humans are very good at unsupervised learning, e.g. a 2 year old knows intuitive physics  
    * Babies construct an approximate but sufficiently reliable model of physics.  
        * How do they manage that?  
            Note that they __interact with the world__, not just observe it.  
            * It is important to _act in the world_ to _acquire information_.  
                The basic tools for that come from __RL__.  
                It is not developed enough, as of now.  
                > Note: <span>the information gained/learned by an acting agent is *__subjective__* to his own capabilities/affordences</span>{: style="color: goldenrod"}.  
                    E.g. Adult vs Baby (bodies) interacting with the world.  