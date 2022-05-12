---
layout: NotesPage
title: CNNs <br /> Convolutional Neural Networks
permalink: /work_files/research/dl/archits/convnets
prevLink: /work_files/research/dl/cv.html
---

<div markdown="1" class = "TOC">
# Table of Contents

  * [Introduction](#content1)
  {: .TOC1}
  * [Architecture and Design](#content2)
  {: .TOC2}
  * [The Convolutional Layer](#content3)
  {: .TOC3}
  * [The Pooling Layer](#content4)
  {: .TOC4}
  * [Convolution and Pooling as an Infinitely Strong Prior](#content5)
  {: .TOC5}
  * [Variants of the Basic Convolution Function and Structured Outputs](#content6)
  {: .TOC6}

</div>

***
***


[CNNs in CV](/work_files/research/dl/cnnx)  
[CNNs in NLP](/work_files/research/dl/nlp/cnnsNnlp)  
[CNNs Architectures](/work_files/research/dl/arcts)  
[Convnet Ch.9 Summary (blog)](https://medium.com/inveterate-learner/deep-learning-book-chapter-9-convolutional-networks-45e43bfc718d)  

* [Understanding Deep Convolutional Networks (Paper!!)](https://arxiv.org/pdf/1601.04920.pdf)  

* [Computing Receptive Fields in CNNs (Blog)](https://distill.pub/2019/computing-receptive-fields/)  
* [CNN Explainer - CNNs Visualized in your browser! (Blog!!)](https://poloclub.github.io/cnn-explainer/)  


## Introduction
{: #content1}

1. **CNNs:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}   
    In machine learning, a convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks that has successfully been applied to analyzing visual imagery.  
    In general, it works on data that have _grid-like topology._  
    > E.g. Time-series data (1-d grid w/ samples at regular time intervals), image data (2-d grid of pixels).  

    Convolutional networks are simply neural networks that use convolution in place of general matrix multiplication in at least one of their layers.  


2. **The Big Idea:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}   
    CNNs use a variation of multilayer Perceptrons designed to require minimal preprocessing. In particular, they use the [Convolution Operation](#bodyContents31).   
    The Convolution leverage _three important ideas_ that can help improve a machine learning system:  
    1. __Sparse Interactions/Connectivity/Weights:__  
        Unlike FNNs, where every input unit is connected to every output unit, CNNs have sparse interactions. This is accomplished by making the kernel smaller than the input.  
        __Benefits:__   
        * This means that we need to _store fewer parameters_, which both,  
            * _Reduces the memory requirements_ of the model and  
            * _Improves_ its _statistical efficiency_  
        * Also, Computing the output requires fewer operations  
        * In deep CNNs, the units in the deeper layers interact indirectly with large subsets of the input which allows modelling of complex interactions through sparse connections.  

        > These improvements in efficiency are usually quite large.  
        If there are $$m$$ inputs and $$n$$ outputs, then matrix multiplication requires $$m \times n$$ parameters, and the algorithms used in practice have $$\mathcal{O}(m \times n)$$ runtime (per example). If we limit the number of connections each output may have to $$k$$, then the sparsely connected approach requires only $$k \times n$$ parameters and $$\mathcal{O}(k \times n)$$ runtime.   
        
        <button>Figure: Sparse Connectivity from Below</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/cnn/14.png){: width="70%" hidden=""}  
        <button>Figure: Sparse Connectivity from Above</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/cnn/15.png){: width="70%" hidden=""}  

    2. __Parameter Sharing:__   
        refers to using the same parameter for more than one function in a model.  

        __Benefits:__{: style="color: red"}  
        {: #lst-p}
        * This means that rather than learning a separate set of parameters for every location, we _learn only one set of parameters_.  
            * This does not affect the runtime of forward propagation—it is still $$\mathcal{O}(k \times n)$$  
            * But it does further reduce the storage requirements of the model to $$k$$ parameters ($$k$$ is usually several orders of magnitude smaller than $$m$$)  

        Convolution is thus dramatically more efficient than dense matrix multiplication in terms of the memory requirements and statistical efficiency.  
        <button>Figure: Parameter Sharing</button>{: .showText value="show" onclick="showTextPopHide(event);"}
        ![img](/main_files/dl/cnn/16.png){: width="70%" hidden=""}  

    3. __Equivariant Representations:__  
        For convolutions, the particular form of parameter sharing causes the layer to have a property called __equivariance to translation__.   
        > A function is __equivariant__ means that if the input changes, the output changes in the same way.  
            Specifically, a function $$f(x)$$ is equivariant to a function $$g$$ if $$f(g(x)) = g(f(x))$$.   

        Thus, if we move the object in the input, its representation will move the same amount in the output.  
        
        __Benefits:__{: style="color: red"}  
        {: #lst-p}  
        * It is most useful when we know that some function of a small number of neighboring pixels is useful when applied to multiple input locations (e.g. edge detection)  
        * Shifting the position of an object in the input doesn't confuse the NN  
        * Robustness against translated inputs/images   

        Note: Convolution is __not__ naturally equivariant to some other transformations, such as _changes in the scale_ or _rotation_ of an image.  


    Finally, the convolution provides a means for working with __inputs of variable sizes__ (i.e. data that cannot be processed by neural networks defined by matrix multiplication with a fixed-shape matrix).  

    <button>FC Mat-Mul as a small kernel</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/gifs/nn_matmul.gif){: width="70%" hidden=""}  
    <br>

3. **Inspiration Model:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    Convolutional networks were inspired by biological processes in which the connectivity pattern between neurons is inspired by the organization of the animal visual cortex.  
    Individual cortical neurons respond to stimuli only in a restricted region of the visual field known as the receptive field. The receptive fields of different neurons partially overlap such that they cover the entire visual field. 


***

## Architecture and Design
{: #content2}


0. **Design:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents20}  
    A CNN consists of an input and an output layer, as well as multiple hidden layers.  
    The hidden layers of a CNN typically consist of convolutional layers, pooling layers, fully connected layers and normalization layers.  

1. **Volumes of Neurons:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}   
    Unlike neurons in traditional Feed-Forward networks, the layers of a ConvNet have neurons arranged in 3-dimensions: **width, height, depth**.  
    > Note: __Depth__ here refers to the third dimension of an activation volume, not to the depth of a full Neural Network, which can refer to the total number of layers in a network.  

2. **Connectivity:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}   
    The neurons in a layer will only be connected to a small region of the layer before it, instead of all of the neurons in a fully-connected manner.

3. **Functionality:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}   
    A ConvNet is made up of Layers.  
    Every Layer has a simple API: It transforms an input 3D volume to an output 3D volume with some differentiable function that may or may not have parameters.  
    
    ![img](/main_files/dl/cnn/1.png){: width="100%"}

    
4. **Layers:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}   
    We use three main types of layers to build ConvNet architectures:  
    * Convolutional Layer:  
        * Convolution (Linear Transformation)   
        * Activation (Non-Linear Transformation; e.g. ReLU)  
            > Known as __Detector Stage__  
    * Pooling Layer  
    * Fully-Connected Layer  

41. **Process:**{: style="color: SteelBlue"}{: .bodyContents2  #bodyContents241}  
    :   ConvNets transform the original image layer by layer from the original pixel values to the final class scores. 

5. **Example Architecture (CIFAR-10):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}  
    :   Model: [INPUT - CONV - RELU - POOL - FC]
    :   * **INPUT:** [32x32x3] will hold the raw pixel values of the image, in this case an image of width 32, height 32, and with three color channels R,G,B.   
        * **CONV-Layer** will compute the output of neurons that are connected to local regions in the input, each computing a dot product between their weights and a small region they are connected to in the input volume.    
        This may result in volume such as [$$32\times32\times12$$] if we decided to use 12 filters.  
        * **RELU-Layer:**  will apply an element-wise activation function, thresholding at zero. This leaves the size of the volume unchanged ([$$32\times32\times12$$]).  
        * **POOL-Layer:** will perform a down-sampling operation along the spatial dimensions (width, height), resulting in volume such as [$$16\times16\times12$$].  
        * **Fully-Connected:** will compute the class scores, resulting in volume of size [$$1\times1\times10$$], where each of the 10 numbers correspond to a class score, such as among the 10 categories of CIFAR-10.  
        As with ordinary Neural Networks and as the name implies, each neuron in this layer will be connected to all the numbers in the previous volume.

6. **Fixed Functions VS Hyper-Parameters:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    :   Some layers contain parameters and other don’t.
    :   * **CONV/FC layers** perform transformations that are a function of not only the activations in the input volume, but also of the parameters (the weights and biases of the neurons).
    :   * **RELU/POOL** layers will implement a fixed function. 
    :   > The parameters in the CONV/FC layers will be trained with gradient descent so that the class scores that the ConvNet computes are consistent with the labels in the training set for each image.  

7. **[Summary](http://cs231n.github.io/convolutional-networks/):**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    * A ConvNet architecture is in the simplest case a list of Layers that transform the image volume into an output volume (e.g. holding the class scores)  
    * There are a few distinct types of Layers (e.g. CONV/FC/RELU/POOL are by far the most popular)  
    * Each Layer accepts an input 3D volume and transforms it to an output 3D volume through a differentiable function  
    * Each Layer may or may not have parameters (e.g. CONV/FC do, RELU/POOL don’t)  
    * Each Layer may or may not have additional hyperparameters (e.g. CONV/FC/POOL do, RELU doesn’t)  
> [Click this for Credits](http://cs231n.github.io/convolutional-networks/)  

    ![img](/main_files/dl/cnn/2.png){: width="100%"}


***

## The Convolutional Layer
{: #content3}

![img](https://cdn.mathpix.com/snip/images/7aQe47vYUKI3QSjMCypArdV-ubxClScrkNIpzVxH2go.original.fullsize.png){: width="50%"}  

* [Convolution Arithmetic Visualization (Blog!)](https://github.com/vdumoulin/conv_arithmetic)  

<button>Convolution Operation Arithmetic Visualized</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
<div hidden="" markdown="1"> 
_N.B.: Blue maps are inputs, and cyan maps are outputs._
<table style="width:100%; table-layout:fixed;">
  <tr>
    <td>No padding, no strides</td>
    <td>Arbitrary padding, no strides</td>
    <td>Half padding, no strides</td>
    <td>Full padding, no strides</td>
  </tr>
  <tr>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/no_padding_no_strides.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/arbitrary_padding_no_strides.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/same_padding_no_strides.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/full_padding_no_strides.gif"></td>
  </tr>
  <tr>
    <td>No padding, strides</td>
    <td>Padding, strides</td>
    <td>Padding, strides (odd)</td>
    <td></td>
  </tr>
  <tr>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/no_padding_strides.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/padding_strides.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/padding_strides_odd.gif"></td>
    <td></td>
  </tr>
</table> 
</div>


<button>__Transposed__ Convolution Operation Arithmetic Visualized</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
<div hidden="" markdown="1"> 
<table style="width:100%; table-layout:fixed;">
  <tr>
    <td>No padding, no strides, transposed</td>
    <td>Arbitrary padding, no strides, transposed</td>
    <td>Half padding, no strides, transposed</td>
    <td>Full padding, no strides, transposed</td>
  </tr>
  <tr>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/no_padding_no_strides_transposed.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/arbitrary_padding_no_strides_transposed.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/same_padding_no_strides_transposed.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/full_padding_no_strides_transposed.gif"></td>
  </tr>
  <tr>
    <td>No padding, strides, transposed</td>
    <td>Padding, strides, transposed</td>
    <td>Padding, strides, transposed (odd)</td>
    <td></td>
  </tr>
  <tr>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/no_padding_strides_transposed.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/padding_strides_transposed.gif"></td>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/padding_strides_odd_transposed.gif"></td>
    <td></td>
  </tr>
</table>
</div>

<button>__Dilated__ Convolution Operation Arithmetic Visualized</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
<div hidden="" markdown="1"> 
<table style="width:25%; table-layout:fixed;">
  <tr>
    <td>No padding, no stride, dilation</td>
  </tr>
  <tr>
    <td><img width="150px" src="/main_files/dl/cnn/gifs/dilation.gif"></td>
  </tr>
</table>
</div>

1. **Convolutions:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}   
    In its most general form, the convolution is a __Linear Operation__ on two functions of real-valued arguments.  

    Mathematically, a __Convolution__ is a mathematical operation on two functions ($$f$$ and $$g$$) to produce a third function, that is typically viewed as a modified version of one of the original functions, giving the integral of the point-wise multiplication of the two functions as a function of the amount that one of the original functions is translated.  
    The convolution could be thought of as a __weighting function__ (e.g. for taking the weighted average of a series of numbers/function-outputs).  

    The convolution of the __continuous__ functions $$f$$ and $$g$$:  
    <p>$${\displaystyle {\begin{aligned}(f * g)(t)&\,{\stackrel {\mathrm {def} }{=}}\ \int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau \\&=\int_{-\infty }^{\infty }f(t-\tau )g(\tau )\,d\tau .\end{aligned}}}$$</p>  

    The convolution of the __discreet__ functions f and g: 
    <p>$${\displaystyle {\begin{aligned}(f * g)[n]&=\sum_{m=-\infty }^{\infty }f[m]g[n-m]\\&=\sum_{m=-\infty }^{\infty }f[n-m]g[m].\end{aligned}}} (commutativity)$$</p>  
    In this notation, we refer to:  
    {: #lst-p}
    * The function $$f$$ as the __Input__  
    * The function $$g$$ as the __Kernel/Filter__  
    * The output of the convolution as the __Feature Map__  

    __Commutativity:__  
    <button>On Commutativity</button>{: .showText value="show" onclick="showText_withParent_PopHide(event);"}
    <div hidden="" markdown="1">
    Can be achieved by flipping the kernel with respect to the input; in the sense that as increases, the index into the $$m$$ input increases, but the index into the kernel decreases.  
    While the commutative property is useful for writing proofs, it is not usually an important property of a neural network implementation.  
    Moreover, in a CNN, the convolution is used simultaneously with other functions, and the combination of these functions __does not commute__ regardless of whether the convolution operation flips its kernel or not.  
    Because Convolutional networks usually use multichannel convolution, the linear operations they are based on are not guaranteed to be commutative, even if kernel flipping is used. These multichannel operations are only commutative if each operation has the same number of output channels as input channels.  
    </div>
    <br>

                

2. **Cross-Correlation:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}   
    :   Cross-Correlation is a measure of similarity of two series as a function of the displacement of one relative to the other.
    :   The __continuous__ cross-correlation on continuous functions f and g:  
    :   $$(f\star g)(\tau )\ {\stackrel {\mathrm {def} }{=}}\int_{-\infty }^{\infty }f^{*}(t)\ g(t+\tau )\,dt,$$
    :   The __discrete__ cross-correlation on discreet functions f and g:  
    :   <p>$$(f\star g)[n]\ {\stackrel {\mathrm {def} }{=}}\sum _{m=-\infty }^{\infty }f^{*}[m]\ g[m+n].$$</p>  
    <br>

3. **Convolutions and Cross-Correlation:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}   
    * Convolution is similar to cross-correlation.  
    * _For discrete real valued signals_, they differ only in a time reversal in one of the signals.  
    * _For continuous signals_, the cross-correlation operator is the **adjoint operator** of the convolution operator.  
    <br>

4. **CNNs, Convolutions, and Cross-Correlation:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}   
    The term Convolution in the name "Convolution Neural Network" is unfortunately a __misnomer__.  
    CNNs actually __use Cross-Correlation__ instead as their similarity operator.  
    The term 'convolution' has stuck in the name by convention.  
    <br>


15. **Convolution in DL:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents315}   
    The Convolution operation:  
    <p>$$s(t)=(x * w)(t)=\sum_{a=-\infty}^{\infty} x(a) w(t-a)$$</p>   
    we usually assume that these functions are zero everywhere but in the finite set of points for which we store the values.  
    <br>

16. **Convolution Over Two Axis:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents316}   
    If we use a 2D image $$I$$ as our input, we probably also want to use a two-dimensional kernel $$K$$:  
    <p>$$S(i, j)=(I * K)(i, j)=\sum_{m} \sum_{n} I(m, n) K(i-m, j-n)$$</p>  

    In practice we use the following formula instead (commutativity):  
    <p>$$S(i, j)=(K * I)(i, j)=\sum_{m} \sum_{n} I(i-m, j-n) K(m, n)$$</p>  
    Usually the latter formula is more straightforward to implement in a machine learning library, because there is less variation in the range of valid values of $$m$$ and $$n$$.  


    The Cross-Correlation is usually implemented by ML-libs:  
    <p>$$S(i, j)=(K * I)(i, j)=\sum_{m} \sum_{n} I(i+m, j+n) K(m, n)$$</p>  


17. **The Mathematics of the Convolution Operation:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents317}    
    * The operation can be broken into matrix multiplications using the Toeplitz matrix representation for 1D and block-circulant matrix for 2D convolution:  
        * __Discrete convolution__ can be viewed as __multiplication by a matrix__, but the matrix has several entries constrained to be equal to other entries.  
        > For example, for __univariate discrete convolution__, each row of the matrix is constrained to be equal to the row above shifted by one element. This is known as a *__Toeplitz matrix__*.  
            A __Toeplitz matrix__ has the property that values along all diagonals are constant.  

            <!-- * <button>Figure: Toeplitz Matrix</button>{: .showText value="show" onclick="showTextPopHide(event);"}  
             -->
            ![img](/main_files/dl/cnn/20.png){: width="50%"}  
        * In __two dimensions__, a __doubly block circulant matrix__ corresponds to convolution.  
            > A matrix which is circulant with respect to its sub-matrices is called a __block circulant matrix__. If each of the submatrices is itself circulant, the matrix is called __doubly block-circulant matrix__.  
                <!-- * <button>Figure: Block-Circulant Matrix</button>{: .showText value="show" onclick="showTextPopHide(event);"}   -->
                ![img](/main_files/dl/cnn/21.png){: width="40%"}  
    * Convolution usually corresponds to a __very sparse matrix__ (a matrix whose entries are mostly equal to zero).  
        This is because the kernel is usually much smaller than the input image.  
    * Any neural network algorithm that works with matrix multiplication and does not depend on specific properties of the matrix structure should work with convolution, without requiring any further changes to the neural network.  
    * Typical convolutional neural networks do make use of further specializations in order to deal with large inputs efficiently, but these are not strictly necessary from a theoretical perspective.  
    <br>

5. **The Convolution operation in a CONV Layer:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}   
    * The CONV layer’s __parameters__ consist of __a set of learnable filters__.  
        * Every filter is small spatially (along width and height), but extends through the full depth of the input volume.  
        >  For example, a typical filter on a first layer of a ConvNet might have size 5x5x3 (i.e. 5 pixels width and height, and 3 because images have depth 3, the color channels).  
    * In the __forward pass__, we slide (convolve) each filter across the width and height of the input volume and compute dot products between the entries of the filter and the input at any position.  
        * As we slide the filter over the width and height of the input volume we will produce a 2-dimensional activation map that gives the responses of that filter at every spatial position.  
        > Intuitively, the network will learn filters that activate when they see some type of visual feature such as an edge of some orientation or a blotch of some color on the first layer, or eventually entire honeycomb or wheel-like patterns on higher layers of the network. 
        * Now, we will have an entire set of filters in each CONV layer (e.g. 12 filters), and each of them will produce a separate 2-dimensional activation map.   
        * We will __stack__ these activation maps along the depth dimension and produce the output volume.  

    <p style="color: red">As a result <i>(of what?)</i>, the network learns filters that activate when it detects some specific type of feature at some spatial position in the input. </p>    
    <br>
    
6. **The Brain Perspective:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}  
    Every entry in the 3D output volume can also be interpreted as an output of a neuron that looks at only a small region in the input and shares parameters with all neurons to the left and right spatially.  
    <br>

7. **Local Connectivity:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}  
    * Convolutional networks exploit spatially local correlation by enforcing a local connectivity pattern between neurons of adjacent layers: 
        * Each neuron is connected to only a small region of the input volume.
    * The __Receptive Field__ of the neuron defines the extent of this connectivity as a hyperparameter.  
    >  For example, suppose the input volume has size $$[32\times32\times3]$$ and the receptive field (or the filter size) is $$5\times5$$, then each neuron in the Conv Layer will have weights to a $$[5\times5\times3]$$ region in the input volume, for a total of $$5*5*3 = 75$$ weights (and $$+1$$ bias parameter).  

    <p style="color: red">Such an architecture ensures that the learnt filters produce the strongest response to a spatially local input pattern.</p>  
    <br>

8. **Spatial Arrangement:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}  
    There are __three__ hyperparameters control the size of the output volume:  
    1. __The Depth__ of the output volume is a hyperparameter that corresponds to the number of filters we would like to use (each learning to look for something different in the input).  
    2. __The Stride__ controls how depth columns around the spatial dimensions (width and height) are allocated.  
        > e.g. When the stride is 1 then we move the filters one pixel at a time.  

        * The __Smaller__ the stride, the __more overlapping regions__ exist and the __bigger the volume__.  
        * The __bigger__ the stride, the __less overlapping regions__ exist and the         __smaller the volume__.  

    3. The __Padding__ is a hyperparameter whereby we pad the input volume with zeros around the border.   
        This allows to _control the spatial size_ of _the output_ volumes.  
    <br>

9. **The Spatial Size of the Output Volume:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents29}  
    We compute the spatial size of the output volume as a function of:  
    * **$$W$$**: The input volume size.  
    * **$$F$$**: $$\:$$The receptive field size of the Conv Layer neurons.  
    * **$$S$$**: $$\:$$The stride with which they are applied.  
    * **$$P$$**: $$\:$$The amount of zero padding used on the border.  
    Thus, the __Total Size of the Output__:  
    <p>$$\dfrac{W−F+2P}{S} + 1$$</p>  

    __Potential Issue__: If this number is not an integer, then the strides are set incorrectly and the neurons cannot be tiled to fit across the input volume in a symmetric way.  
    * __Fix__: In general, setting zero padding to be $${\displaystyle P = \dfrac{K-1}{2}}$$ when the stride is $${\displaystyle S = 1}$$ ensures that the input volume and output volume will have the same size spatially.  
    <br>

10. **Calculating the Number of Parameters:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents210}   
    Given:  
    * __Input Volume__:  $$32\times32\times3$$  
    * __Filters__:  $$10\:\:\: (5\times5)$$  
    * __Stride__:  $$1$$  
    * __Pad__:  $$2$$  
    
    The number of parameters equals the number of parameters in each filter $$ = 5*5*3 + 1 = 76$$ (+1 for __bias__) times the number of filters $$ 76 * 10 = 760$$.  
    <br>

11. **The Convolution Layer:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents311}   
    ![img](/main_files/dl/cnn/3.png){: width="70%"}  
    ______  
    ![img](/main_files/dl/cnn/8.png){: width="70%"}  
    ______  

    __The Conv Layer and the Brain:__  
    ![img](/main_files/dl/cnn/10.png){: width="70%"}  
    ______  
    ![img](/main_files/dl/cnn/11.png){: width="70%"}  
    ______  
    ![img](/main_files/dl/cnn/12.png){: width="70%"}  
    ______  
    <br>


12. **From FC-layers to Conv-layers:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents312}   
    ![img](/main_files/dl/cnn/4.png){: width="70%"}  
    ***
    ![img](/main_files/dl/cnn/5.png){: width="70%"}  
    ***
    ![img](/main_files/dl/cnn/6.png){: width="70%"}  
    ***
    <br>


13. **$$1\times1$$ Convolutions:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents313}   
    ![img](/main_files/dl/cnn/9.png){: width="70%"}  
    <br>

0. **Notes:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents30}   
    * __Summary__:  
        * ConvNets stack CONV,POOL,FC layers 
        * Trend towards smaller filters and deeper architectures 
        * Trend towards getting rid of POOL/FC layers (just CONV) 
        * Typical architectures look like [(CONV-RELU) * N-POOL?] * M-(FC-RELU) * K, SOFTMAX  
            where $$N$$ is usually up to \~5, $$M$$ is large, $$0 <= K <= 2$$.  
            But recent advances such as ResNet/GoogLeNet challenge this paradigm 
    * __Effect of Different Biases__:  
        Separating the biases may slightly reduce the statistical efficiency of the model, but it allows the model to correct for differences in the image statistics at different locations. For example, when using implicit zero padding, detector units at the edge of the image receive less total input and may need larger biases.  
    * In the kinds of architectures typically used for classification of a single object in an image, the greatest reduction in the spatial dimensions of the network comes from using pooling layers with large stride.  


***


## The Pooling Layer
{: #content4}

1. **The Pooling Operation/Function:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}   
    The pooling function calculates a __summary statistic__ of the nearby pixels at the point of operation.  
    Some common statistics are _max, mean, weighted average_ and _$$L^2$$ norm_ of a surrounding rectangular window.  
    <br>


2. **The Key Ideas/Properties:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}   
    In all cases, pooling helps to make the representation approximately __invariant to small translations__ of the input.   
    > Invariance to translation means that if we translate the input by a small amount, the values of most of the pooled outputs do not change.  
    Invariance to local translation can be a useful property if we care more about whether some feature is present than exactly where it is.  

    <button>Figure: MaxPooling</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/cnn/17.png){: width="70%" hidden=""}   

    __(Learned) Invariance to other transformations:__  
    Pooling over spatial regions produces invariance to translation, but if we _pool over the outputs of separately parametrized convolutions_, the features can learn which transformations to become invariant to.  
    This property has been used in __Maxout networks__.  
    <button>Figure: Examples of Learned Invariance</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/cnn/18.png){: width="70%" hidden=""}  


    For many tasks, pooling is essential for handling inputs of varying size.  
    > This is usually accomplished by varying the size of an offset between pooling regions so that the classification layer always receives the same number of summary statistics regardless of the input size. For example, the final pooling layer of the network may be defined to output four sets of summary statistics, one for each quadrant of an image, regardless of the image size.  

    One can use fewer pooling units than detector units, since they provide a summary; thus, by reporting summary statistics for pooling regions spaced $$k$$ pixels apart rather than $$1$$ pixel apart, we can improve the computational efficiency of the network because the next layer has roughly $$k$$ times fewer inputs to process.  
    This reduction in the input size can also result in improved statistical efficiency and reduced memory requirements for storing the parameters.  
    <button>Figure: Downsampling</button>{: .showText value="show" onclick="showTextPopHide(event);"}
    ![img](/main_files/dl/cnn/19.png){: width="70%" hidden=""}  
    <br>

3. **Theoretical Guidelines for choosing the pooling function:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}   
    [Link](http://www.di.ens.fr/willow/pdfs/icml2010b.pdf)  
    <br>

4. **Variations:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}   
    __Dynamical Pooling:__  
    It is also possible to dynamically pool features together, for example, by running a clustering algorithm on the locations of interesting features (Boureau et al., 2011) [link](http://yann.lecun.com/exdb/publis/pdf/boureau-iccv-11.pdf). This approach yields a different set of pooling regions for each image.  

    __Learned Pooling:__  
    Another approach is to learn a single pooling structure that is then applied to all images (Jia et al., 2012).  
    <br>

5. **Pooling and Top-Down Architectures:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}   
    Pooling can complicate some kinds of neural network architectures that use top-down information, such as Boltzmann machines and autoencoders.  
    <br>

6. **The Pooling Layer (summary):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}   
    ![img](/main_files/dl/cnn/13.png){: width="100%"}  
    <br>


<!-- 7. **The Pooling Layer (summary):**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}   
    ![img](/main_files/dl/cnn/13.png){: width="100%"}   -->

<!-- 7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  -->

**Notes:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}  
* __Pooling Layer__:  
    * Makes the representations smaller and more manageable
    * Operates over each activation map independently (i.e. preserves depth)  
* You can use the stride instead of the pooling to downsample  

***

## Convolution and Pooling as an Infinitely Strong Prior
{: #content5}
            
1. **A Prior Probability Distribution:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}  
    This is a probability distribution over the parameters of a model that encodes our beliefs about what models are reasonable, before we have seen any data.  
    <br>

2. **What is a weight prior?:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}  
    Assumptions about the weights (before learning) in terms of acceptable values and range are encoded into the prior distribution of the weights.  
    * A __Weak Prior__:  has a high _entropy_, and thus, variance and shows that there is low confidence in the initial value of the weight.  
    * A __Strong Prior__: in turn has low entropy/variance, and shows a narrow range of values about which we are confident before learning begins.  
    * A __Infinitely Strong Prior__: demarkets certain values as forbidden completely, assigning them zero probability.  
    <br>

3. **Convolutional Layer as a FC Layer:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}  
    If we view the conv-layer as a FC-layer, the:  
    * __Convolution__: operation imposes an *__infinitely strong prior__* by making the following restrictions on the weights:  
        * Adjacent units must have the same weight but shifted in space.  
        * Except for a small spatially connected region, all other weights must be zero.  
    * __Pooling__: operation imposes an *__infinitely strong prior__* by:  
        * Requiring features to be __Translation Invariant__.   
    <br>    

4. **Key Insights/Takeaways:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}  
    * Convolution and pooling can cause underfitting if the priors imposed are not suitable for the task. When a task involves incorporating information from very distant locations in the input, then the prior imposed by convolution may be inappropriate.  
    > As an example, consider this scenario. We may want to learn different features for different parts of an input. But the compulsion to used tied weights (enforced by standard convolution) on all parts of an image, forces us to either compromise or use more kernels (extract more features).  

    * Convolutional models should only be compared with other convolutional models. This is because other models which are permutation invariant can learn even when input features are permuted (thus loosing spatial relationships). Such models need to learn these spatial relationships (which are hard-coded in CNNs).


*** 

## Variants of the Basic Convolution Function and Structured Outputs
{: #content6}

1. **Practical Considerations for Implementing the Convolution Function:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}  
    * In general a convolution layer consists of application of *__several different kernels to the input.__* This allows the extraction of several different features at all locations in the input. This means that in each layer, a single kernel (filter) isn’t applied. Multiple kernels (filters), usually a power of 2, are used as different feature detectors.  
    * The _input_ is generally not real-valued but instead *__vector valued__* (e.g. RGB values at each pixel or the feature values computed by the previous layer at each pixel position). Multi-channel convolutions are commutative only if number of output and input channels is the same.  
    * __Strided Convolutions__ are a means to do *__DownSampling__*; they are used to reduce computational cost, by calculating features at a *__coarser level__*. The effect of strided convolution is the same as that of a convolution followed by a downsampling stage. This can be used to reduce the representation size.  
        <p>$$Z_{i, j, k}=c(\mathrm{K}, \mathrm{V}, s)_{i, j, k}=\sum_{l, m, n}\left[V_{l,(j-1) \times s+m,(k-1) \times s+n} K_{i, l, m, n}\right] \tag{9.8}$$</p>  
    * __Zero Padding__ is used to make output dimensions and kernel size independent (i.e. to control the output dimension regardless of the size of the kernel). There are three types:  
        1. __Valid__: The output is computed only at places where the entire kernel lies inside the input. Essentially, _no zero padding_ is performed. For a kernel of size $$k$$ in any dimension, the input shape of $$m$$ in the direction will become $$m-k+1$$ in the output. This shrinkage restricts architecture depth.   
        2. __Same__: The input is zero padded such that the _spatial size of the input and output is **same**_. Essentially, for a dimension where kernel size is $$k$$, the input is padded by $$k-1$$ zeros in that dimension. Since the number of output units connected to border pixels is less than that for center pixels, it may under-represent border pixels.  
        3. __Full__: The input is padded by enough zeros such that _each input pixel is connected to the same number of output units_.  
        > The optimal amount of Zero-Padding usually lies between "valid" and "same" convolution.  

    * __Locally Connected Layers__/__Unshared Convolution__: has the same connectivity graph as a convolution operation, but *__without parameter sharing__* (i.e. each output unit performs a linear operation on its neighbourhood but the parameters are not shared across output units.).  
        This allows models to capture local connectivity while allowing different features to be computed at different spatial locations; at the _expense_ of having _a lot more parameters_.      
        <p>$$Z_{i, j, k}=\sum_{l, m, n}\left[V_{l, j+m-1, k+n-1} w_{i, j, k, l, m, n}\right] \tag{9.9}$$</p>  
        > They're useful when we know that each feature should be a function of a small part of space, but there is no reason to think that the same feature should occur across all of space.  
        For example, if we want to tell if an image is a picture of a face, we only need to look for the mouth in the bottom half of the image.  
    * __Tiled Convolution__: offers a middle ground between Convolution and locally-connected layers. Rather than learning a separate set of weights at _every_ spatial location, it learns/uses a set of kernels that are cycled through as we move through space.  
        This means that immediately neighboring locations will have different filters, as in a locally connected layer, but the memory requirements for storing the parameters will increase only by a factor of the size of this set of kernels, rather than by the size of the entire output feature map.  
        <p>$$Z_{i, j, k}=\sum_{l, m, n} V_{l, j+m-1, k+n-1} K_{i, l, m, n, j \% t+1, k \% t+1} \tag{9.10}$$</p>  
    * __Max-Pooling, and Locally Connected Layers and Tiled Layers__: When max pooling operation is applied to locally connected layer or tiled convolution, the model has the ability to become transformation invariant because adjacent filters have the freedom to learn a transformed version of the same feature.  
    > This essentially similar to the property leveraged by pooling over channels rather than spatially.  
    * __Different Connections__: Besides locally-connected layers and tiled convolution, another extension can be to restrict the kernels to operate on certain input channels. One way to implement this is to connect the first m input channels to the first n output channels, the next m input channels to the next n output channels and so on. This method decreases the number of parameters in the model without decreasing the number of output units.  
    * __Other Operations__: The following three operations—convolution, backprop from output to weights, and backprop from output to inputs—are sufficient to compute all the gradients needed to train any depth of feedforward convolutional network, as well as to train convolutional networks with reconstruction functions based on the transpose of convolution. 
    > See Goodfellow (2010) for a full derivation of the equations in the fully general multidimensional, multiexample case.  
    * __Bias__:  Bias terms can be used in different ways in the convolution stage.  
        * For locally connected layer and tiled convolution, we can use a bias per output unit and kernel respectively.  
        * In case of traditional convolution, a single bias term per output channel is used.  
        * If the _input size is fixed_, a bias per output unit may be used to _counter the effect of regional image statistics and smaller activations at the boundary due to zero padding_.  
        
2. **Structured Outputs:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}  
    Convolutional networks can be trained to output high-dimensional structured output rather than just a classification score.  
    A good example is the task of __image segmentation__ where each pixel needs to be associated with an object class.  
    Here the output is the same size (spatially) as the input. The model outputs a tensor $$S$$  where $$S_{i, j, k}$$ is the probability that pixel $$(j,k)$$ belongs to class $$i$$.  
    * __Problem__: One issue that often comes up is that the output plane can be smaller than the input plane.  
    * __Solutions__:  
        * To produce an output map as the same size as the input map, only same-padded convolutions can be stacked.  
        * Avoid Pooling Completely _(Jain et al. 2007)_  
        * Emit a lower-Resolution grid of labels _(Pinheiro and Collobert, 2014, 2015)_ 
        * __Recurrent-Convolutional Models__: The output of the first labelling stage can be refined successively by another convolutional model. If the models use tied parameters, this gives rise to a type of recursive model.  
        * Another model that has gained popularity for segmentation tasks (especially in the medical imaging community) is the [U-Net](https://arxiv.org/abs/1505.04597). The up-convolution mentioned is just a direct upsampling by repetition followed by a convolution with same padding.  

    The output can be further processed under the assumption that contiguous regions of pixels will tend to belong to the same label. Graphical models can describe this relationship. Alternately, [CNNs can learn to optimize the graphical models training objective](https://www.robots.ox.ac.uk/~vgg/rg/papers/tompson2014.pdf).  


<!-- ## Seven
{: #content7}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents71}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents72}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents73}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents74}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents75}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents76}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents77}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents7 #bodyContents78}

## Eight
{: #content8}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents81}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents82}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents83}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents84}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents85}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents86}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents87}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents8 #bodyContents88}
 -->

***

## Extra
{: #contentx}

<!-- 1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents91}  -->

2. **Image Features:**{: style="color: SteelBlue"}{: .bodyContents9 #bodyContents92} 
    :   are certain quantities that are calculated from the image to _better describe the information in the image_, and to _reduce the size of the input vectors_. 
    :   * Examples:  
            * __Color Histogram__: Compute a (bucket-based) vector of colors with their respective amounts in the image.  
            * __Histogram of Oriented Gradients (HOG)__: we count the occurrences of gradient orientation in localized portions of the image.   
            * __Bag of Words__: a _bag of visual words_ is a vector of occurrence counts of a vocabulary of local image features.  
                > The __visual words__ can be extracted using a clustering algorithm; K-Means.  
