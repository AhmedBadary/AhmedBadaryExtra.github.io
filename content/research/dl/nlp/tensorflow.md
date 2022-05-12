---
layout: NotesPage
title: TensorFlow 
permalink: /work_files/research/dl/nlp/tf_intro_2
prevLink: /work_files/research/dl/nlp.html
---


## Introduction and Definitions
{: #content1}

1. **Computational Graph:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
:   __Main Components:__  
    * __Graph Nodes__:  
        are __*Operations*__ which have any number of Inputs and Outputs.  
        They __take in__ *__tensors__* and __produce__ *__tensors__*.  
    * __Graph Edges__:  
        are __*Tensors*__ (values) which flow between nodes.     
:   

2. **Components of the Graph::**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}
    :   * __Variables__: are stateful nodes which output their current value.  
            ![img](/main_files/dl/nlp/t_f/2.png){: width="20%"}         
            * State is retained across multiple executions of a graph.  
            * It is easy to restore saved values to variables  
            * They can be saved to the disk, during and after training  
            * Gradient updates, by default, will apply over all the variables in the graph  
            * Variables are, still, by "definition" __operations__
            * They constitute mostly, __Parameters__    
        * __Placeholders__: are nodes whose value is fed in at execution time.  
            ![img](/main_files/dl/nlp/t_f/3.png){: width="20%"}  
            * They do __not__ have initial values
            * They are assigned a:  
                * data-type  
                * shape of a tensor 
            * They constitute mostly, __Inputs__ and __labels__   
        * __Mathematical Operations__:   
            ![img](/main_files/dl/nlp/t_f/4.png){: width="20%"}  

3. **Example:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   $$h = \text{ReLU}(Wx+b) \\ 
            \rightarrow$$  
        ![img](/main_files/dl/nlp/t_f/1.png){: width="20%"}  

***

## Estimators
{: #content2}

1. **Input Function:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents21}  
    :   An input function is a function that returns a tf.data.Dataset object which outputs the following two-element tuple:  
        * __features__ - A python dict in which:  
            * Each key is the name of a feature
            * Each value is an array containing all of that features values
        * __label__ - An array containing the values of the label for every example.  
        ```python
        def train_input_fn(features, labels, batch_size):
            """An input function for training"""
            # Convert the inputs to a Dataset.
            dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
            # Shuffle, repeat, and batch the examples.
            return dataset.shuffle(1000).repeat().batch(batch_size)
        ```  
    :   The job of the input function is to create the TF operations that generate data for the model

2. **Model Function:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents22}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents23}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents24}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents25}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents26}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents27}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents2 #bodyContents28}

***

## 
{: #content3}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}

***

## FOURTH
{: #content4}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents48}

***

## 
{: #content5}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents57}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents58}

*** 

## Commands and Notes
{: #content6}

1. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents61}

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents62}

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents63}

4. **TensorBoard:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents64}  
    :   ```File_writer  = tf.summary.FileWriter('log_simple_graph', sess.graph)```  
        ```tensorboard --logdir="path"```

5. **Testing if GPU works:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents65}  
    :   ```import tensorflow as tf
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c)) ```

6. **GPU Usage:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents66}  
    :   ```!nvidia-smi ```

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents67}

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents6 #bodyContents68

***

## Ten
{: #content10}

1. **Session:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents101}  
    :   To evaluate tensors, instantiate a tf.Session object, informally known as a session.   
        A session encapsulates the state of the TensorFlow runtime, and runs TensorFlow operations.
    :   * First, create a session:  
            ```sess = tf.Session()```
        * Run the session:  
            ```sess.run()```  
            It takes a dict of any tuples or any tensor.  
            It evaluates the tensor.  
    :   Some TensorFlow functions return tf.Operations instead of tf.Tensors. The result of calling run on an Operation is None. You run an operation to cause a side-effect, not to retrieve a value. Examples of this include the initialization, and training ops demonstrated later.

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents102}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents103}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents104}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents105}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents106}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents107}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents10 #bodyContents108}  
    :   


***
***


## Tips and Tricks
{: #content11}


1. **Saving the model:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents111}  
:   * After the model is run, it uses the most recent checkpoint
    * To run a different model with different architecture, use a different branch  

2. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents112}  
    :   

3. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents113}  
    :   

4. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents114}  
    :   

5. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents115}  
    :   

6. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents116}  
    :   

7. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents117}  
    :   

8. **Asynchronous:**{: style="color: SteelBlue"}{: .bodyContents11 #bodyContents118}  
    :   
