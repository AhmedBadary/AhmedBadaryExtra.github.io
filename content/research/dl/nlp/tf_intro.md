---
layout: NotesPage
title: TensorFlow 
permalink: /work_files/research/dl/nlp/tf_intro
prevLink: /work_files/research/dl/nlp.html
---


## Introduction
{: #content1}

1. **Big Idea:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents11}  
    :   Express a numeric computation as a __graph__.

2. **Main Components:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents12}
    :   * __Graph Nodes__:  
            are __*Operations*__ which have any number of Inputs and Outputs
        * __Graph Edges__:  
            are __*Tensors*__ which flow between nodes   

3. **Example:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents13}  
    :   $$h = \text{ReLU}(Wx+b) \\ 
            \rightarrow$$  
        ![img](/main_files/dl/nlp/t_f/1.png){: width="20%"}  

4. **Components of the Graph:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents14}  
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

5. **Sample Code:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents15}  
    :   ```python
        import tensorflow as tf
        b = tf.Variable(tf.zeros((100,)))
        W = tf.Variable(tf.random_uniform((784, 100) -1, 1))
        x = tf.placeholder(tf.float32, (100, 784))  
        h = tf.nn.relu(tf.matmul(x, W) + b)
        ```

6. **Running the Graph:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents16}  
    :   After defining a graph, we can __deploy__ the graph with a  
        __Session__: a binding to a particular execution context  
        > i.e. the Execution Environment  
    :   * CPU  
        or  
        * GPU

7. **Getting the Output:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents17}  
    :   * Create the _session_ object
        * Run the _session_ object on:  
            * __Fetches__: List of graph nodes.  
              Returns the outputs of these nodes. 
            * __Feeds__: Dictionary mapping from graph nodes to concrete values.  
              Specifies the value of each graph node given in the dictionary.   
    :   * CODE:  
            ```python
            sess = tf.Session()
            sess.run(tf.initialize_all_variables())
            sess.run(h, {x: np.random.random(100, 784)})
            ```

8. **Defining the Loss:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents18}  
    :   * Use __placeholder__ for __labels__
        * Build loss node using __labels__ and __prediction__
    :   * CODE:  
            ```python
            prediction = tf.nn.softmax(...) # output of neural-net
            label = tf.placeholder(tf.float32, [100, 10])
            cross_entropy = -tf.reduce_sum(label * tf.log(prediction), axis=1)
            ```

9. **Computing the Gradients:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents19}  
    :   * We have an __Optimizer Object__:  
        ```tf.train.GradientDescentOptimizaer```
        * We, then, add __Optimization Operation__ to computation graph:  
        ```tf.train.GradientDescentOptimizer(lr).minimize(cross_entropy)```
    :   * CODE:  
            ```python
            train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
            ```

10. **Training the Model:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents110}  
    :   ```python
        sess = tf.Session()
        sess.run(tf.initialize_all_variables())

        for i in range(1000):
            batch_x, batch_label = data.next_batch()
            sess.run(train_step, feed_dict={x: batch_x, label: batch_label})  
        ```

11. **Variable Scope:**{: style="color: SteelBlue"}{: .bodyContents1 #bodyContents111}  
    :   ![img](/main_files/dl/nlp/t_f/5.png){: width="100%"}

***

## THIRD
{: #content3}

1. **Introduction and Definitions:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents31}  
    :   * Hierarchy:  
            ![img](/main_files/dl/nlp/t_f/6.png){: width="80%"}  
    :   * __Input Function__:  
            An input function is a function that returns a tf.data.Dataset object which outputs the following two-element tuple:  
            * features - A python dict in which:  
                * Each key is the name of a feature
                * Each value is an array containing all of that features values
            * label - An array containing the values of the label for every example.  
            ```python
            def train_input_fn(features, labels, batch_size):
                """An input function for training"""
                # Convert the inputs to a Dataset.
                dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
                # Shuffle, repeat, and batch the examples.
                return dataset.shuffle(1000).repeat().batch(batch_size)
            ```  

2. **Import and Parse the data sets:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents32}  
    :   e.g. Iris DataSet with KERAS
    :   ```python
        TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
        TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"
        # Train
        train_path = tf.keras.utils.get_file(fname=TRAIN_URL.split('/')[-1], origin=TRAIN_URL)
        train = pd.read_csv(filepath_or_buffer=train_path, names=CSV_COLUMN_NAMES)
        train_features, train_label = train, train.pop(label_name)
        # Test
        test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)
        test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
        test_features, test_label = test, test.pop(label_name)
        ```


3. **Describe the data:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents33}  
    :   Creating features.  
        E.g. Numeric
    :   ```python
        my_feature_columns = []
        for key in train_x.keys():
            my_feature_columns.append(tf.feature_column.numeric_column(key=key))
        ```

4. **Select the type of model:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents34}  
    :   To specify a model type, instantiate an Estimator class:  
        * Pre-made 
        * Custom
    :   E.g. DNNClassifier
    :   ```python
        classifier = tf.estimator.DNNClassifier(feature_columns=my_feature_columns, hidden_units=[10, 10], n_classes=3, optimizer='SGD')
        ```

5. **Train the model:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents35}  
    :   Instantiating a tf.Estimator.DNNClassifier creates a framework for learning the model. Basically, we've wired a network but haven't yet let data flow through it.
    :   To __train__ the neural network, call the Estimator object's __train method__:  
    :   ```python
        classifier.train(
        input_fn=lambda:train_input_fn(train_feature, train_label, args.batch_size),
        steps=args.train_steps)
        ```
    :   * The steps argument tells train to stop training after the specified number of iterations.
        * The __input_fn__ parameter identifies the function that supplies the training data. The call to the train method indicates that the train_input_fn function will supply the training data with signature:  
        ```def train_input_fn(features, labels, batch_size):```   
        The following call converts the input features and labels into a tf.data.Dataset object, which is the base class of the Dataset API:  
        ```python
        dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
        # Modifying the data
            dataset = dataset.shuffle(buffer_size=1000).repeat(count=None).batch(batch_size)
        ```  
        > Setting the buffer_size to a value larger than the number of examples (120) ensures that the data will be well shuffled  


6. **Evaluate the model:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents36}  
    :   To evaluate a model's effectiveness, each Estimator provides an evaluate method:  
    :   ```python
        # Evaluate the model.
eval_result = classifier.evaluate(
    input_fn=lambda:eval_input_fn(test_x, test_y, args.batch_size))
        print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))
        ```
    :   The call to classifier.evaluate is similar to the call to classifier.train. The biggest difference is that classifier.evaluate must get its examples from the test set rather than the training set

7. **Predicting:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents37}  
    :   Every Estimator provides a predict method, which premade_estimator.py calls as follows:
    :   ```python
    predictions = classifier.predict(
    input_fn=lambda:eval_input_fn(predict_x,labels=None, batch_size=args.batch_size))
        ```

8. **JIRA:**{: style="color: SteelBlue"}{: .bodyContents3 #bodyContents38}  
    :   __Project__:  
        * A JIRA Project is a collection of issues 
        * Every issue belongs to a Project 
        * Each project is identified by a Name and Key 
        * Project Key is appended to each issue associated with the 
        project 
        * Example: 
            * Name of Project: Social Media Site 
            * Project Key: SM 
            * Issue: SM 24 Add a new friend 
    :   __Issue:__ 
        * Issue is the building block of the project 
        * Depending on how your organization is using JIRA, an issue could represent: 
            * a software bug 
            * a project task 
            * a helpdesk ticket 
            * a product improvement 
            * a leave request from client 
    :   __Components__:   
        * Components are sub-sections of a project 
        * Components are used to group issues within a project to smaller parts  
        ![img](/main_files/dl/nlp/t_f/10.png){: width="80%"}  
    :   __Workflow:__   
        * A JIRA workflow is the set of statuses and transitions that an issue goes through during its lifecycle. 
        * Workflows typically represent business processes. 
        * JIRA comes with default workflow and it can be customized to fit your organization  
    :   __Workflow Status and Transitions:__   
        ![img](/main_files/dl/nlp/t_f/11.png){: width="80%"}  




***

## FOURTH
{: #content4}

1. **To write a TF program based on pre-made Estimator:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents41}
    * Create one or more input function
    * Define the models feature columns 
    * Instantiate an Estimator, specifying the feature columns and various hyperparameters.
    * Call one or more methods on the Estimator object, passing the appropriate input function as the source of the data. 

2. **Checkpoint:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents42}  
    :   are saved automatically and are restored automatically after training.  
    :   Save by specifying which ```model_dir``` to save into:  
    :   ```python
        classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns, hidden_units=[10, 10], n_classes=3, model_dir='models/iris')
        ```

3. **Feature Column:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents43}  
:   [check this page for the feature column functions](https://www.tensorflow.org/get_started/feature_columns)  

4. **Custom Estimator:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents44}  
:   Basically, you need to write a __model function__ (```model_fn```) which implements the ML algo.
:   * Write an Input Function (same)
    * Create feature columns (same) 
    * Write a Model Function:  
        ```python 
        def my_model_fn(
   features, # This is batch_features from input_fn
   labels,   # This is batch_labels from input_fn
   mode,     # An instance of tf.estimator.ModeKeys
   params):  # Additional configuration
        ```  
        > The mode argument indicates whether the caller is requesting training, predicting, or evaluation.  
    * Create the estimator:  
        ```python
        classifier = tf.estimator.Estimator(
    model_fn=my_model,
    params={
        'feature_columns': my_feature_columns,
        # Two hidden layers of 10 nodes each.
        'hidden_units': [10, 10],
        # The model must choose between 3 classes.
        'n_classes': 3,
    })
        ```

5. **Writing Model Function:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents45}  
:   You need to do:  
    * Define the Model
    * Specify additional calculations: 
        * Predict
        * Evaluate
        * Train
:   __Define the Model:__  
    * __The Input Layer__:  
        convert the feature dictionary and feature_columns into input for your model  
        ```python
            # Use `input_layer` to apply the feature columns.
    net = tf.feature_column.input_layer(features, params['feature_columns'])
        ```
    * __Hidden Layer__:  
        The Layers API provides a rich set of functions to define all types of hidden layers.  
        ```python
            # Build the hidden layers, sized according to the 'hidden_units' param.
    for units in params['hidden_units']:
        net = tf.layers.dense(net, units=units, activation=tf.nn.relu)
        ```  
        The variable __net__ here signifies the current top layer of the network. During the first iteration, __net__ signifies the input layer.  
        On each loop iteration tf.layers.dense creates a new layer, which takes the previous layer's output as its input, using the variable net.  
    * __Output Layer__:  
        Define the output layer by calling ```tf.layer.dense``` 
        ~~~ python
        # Compute logits (1 per class).
    logits = tf.layers.dense(net, params['n_classes'], activation=None)
        ~~~  
        When defining an output layer, the units parameter specifies the number of outputs. So, by setting units to params['n_classes'], the model produces one output value per class.
:   __Predict:__ 
    ```python
    # Compute predictions.
predicted_classes = tf.argmax(logits, 1)
if mode == tf.estimator.ModeKeys.PREDICT:
    predictions = {
        'class_ids': predicted_classes[:, tf.newaxis],
        'probabilities': tf.nn.softmax(logits),
        'logits': logits,
    }
    return tf.estimator.EstimatorSpec(mode, predictions=predictions)
    ```

6. **Embeddings:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents46}  
    :   An __embedding__ is a mapping from discrete objects, such as words, to vectors of real numbers.  


7. **Saving Params:**{: style="color: SteelBlue"}{: .bodyContents4 #bodyContents47}  
    :   ```python
        saver = tf.train.Saver() # before 'with'
        saver.save(sess, './checkpoints/generator.ckpt') # After (within) first for-loop
        # To restore
        saver.restore(sess, tf.train.latest_checkpoint('checkpoints')) # after 'with'
        


***

## Complete Training Example (Low-Level)
{: #content5}

1. **Computational Graph:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents51}
    :   * __Operations__: the nodes of the graph.  
            They __take in__ *__tensors__* and __produce__ *__tensors__*.  
        * __Tensors__: the edges in the graph.  
            They are the __values__ flowing through the graph.  

2. **Tensorboard:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents52}
    :   * First, save the computation graph to a tensorboard summary file:  

        ```writer = tf.summary.FileWriter('.')
        writer.add_graph(tf.get_default_graph())```   
            This will produce an __event__ file in the current directory.  
        * Launch Tensorboard:  
            ```tensorboard --logdir```  

3. **Session:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents53}
    :   To evaluate tensors, instantiate a tf.Session object, informally known as a session.   
        A session encapsulates the state of the TensorFlow runtime, and runs TensorFlow operations.
    :   * First, create a session:  
            ```sess = tf.Session()```
        * Run the session:  
            ```sess.run()```  
            It takes a dict of any tuples or any tensor.  
            It evaluates the tensor.  
    :   Some TensorFlow functions return tf.Operations instead of tf.Tensors. The result of calling run on an Operation is None. You run an operation to cause a side-effect, not to retrieve a value. Examples of this include the initialization, and training ops demonstrated later.

4. **Feeding:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents54}
    :   ```python
        x = tf.placeholder(tf.float32)
        y = tf.placeholder(tf.float32)
        z = x + y
        ```
    :   ```python
        print(sess.run(z, feed_dict={x: 3, y: 4.5}))
        print(sess.run(z, feed_dict={x: [1, 3], y: [2, 4]}))
        ```

5. **Datasets:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents55}
    :   The preferred method of streaming data into a model instead of __placeholders__.  
    :   To get a runnable tf.Tensor from a Dataset you must first convert it to a tf.data.Iterator, and then call the Iterator's get_next method.
    :   Create the Iterator:  
        ```python
        slices = tf.data.Dataset.from_tensor_slices(my_data)
        next_item = slices.make_one_shot_iterator().get_next()
        # Then pass as follows  
        while True:
          try:
            print(sess.run(next_item))
          except tf.errors.OutOfRangeError:
            break
        ```
    :   If the Dataset depends on stateful operations (e.g. random value) you may need to initialize the iterator before using it, as shown below:  
        ```python
        iterator = dataset.make_initializable_iterator()
        next_row = iterator.get_next()
        ```

6. **Layers:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents56}
    :   A trainable model must modify the values in the graph to get new outputs with the same input. Layers are the preferred way to add trainable parameters to a graph.
    :   Layers package together both the variables and the operations that act on them.  
        The connection weights and biases are managed by the layer object.  
        > E.g. a densely-connected layer performs a weighted sum across all inputs for each output and applies an optional activation function.  
    :   __Creating Layers__:  
        ```python
        x = tf.placeholder(tf.float32, shape=[None, 3])
        linear_model = tf.layers.Dense(units=1)
        y = linear_model(x)
        ```
    :   __Initializing Layers:__  
        The layer contains variables that must be initialized before they can be used.  
        ```python
        init = tf.global_variables_initializer()
        sess.run(init)
        ```
    :   __Executing Layers:__  
        ```python
        print(sess.run(y, {x: [[1, 2, 3],[4, 5, 6]]}))
        ```
    :   __Layer Function shortcuts__:  
        For each layer class (like tf.layers.Dense) TensorFlow also supplies a shortcut function (like tf.layers.dense).  
        The only difference is that the shortcut function versions create and run the layer in a single call.  
    :   ```python 
        x = tf.placeholder(tf.float32, shape=[None, 3])
        y = tf.layers.dense(x, units=1)
        # Is Equivalent to:  
        x = tf.placeholder(tf.float32, shape=[None, 3])
        linear_model = tf.layers.Dense(units=1)
        y = linear_model(x)
        ```  
        > While convenient, this approach allows no access to the tf.layers.Layer object. This makes introspection and debugging more difficult, and layer reuse impossible.

7. **Example:**{: style="color: SteelBlue"}{: .bodyContents5 #bodyContents57}
    :   ```python
        x = tf.constant([[1], [2], [3], [4]], dtype=tf.float32)
        y_true = tf.constant([[0], [-1], [-2], [-3]], dtype=tf.float32)

        linear_model = tf.layers.Dense(units=1)

        y_pred = linear_model(x)
        loss = tf.losses.mean_squared_error(labels=y_true, predictions=y_pred)

        optimizer = tf.train.GradientDescentOptimizer(0.01)
        train = optimizer.minimize(loss)

        init = tf.global_variables_initializer()

        sess = tf.Session()
        sess.run(init)
        for i in range(5000):
          _, loss_value = sess.run((train, loss))
          print(loss_value)

        print(sess.run(y_pred))
        ```
