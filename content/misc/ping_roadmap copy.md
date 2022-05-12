---
layout: NotesPage
title: Ping Technical Specifications
permalink: /work_files/ping
prevLink: /
---

### __TASKS__  
* __Automatic Timesheet Completion/Filling:__{: style="color: SteelBlue"}    
    * __Description:__ Making tools that make sound guesses at what a user would want to do in filling out a timesheet and do it for them  
    * __Current Stack__:  
        * __Gradient-Boosted Models (GBMs)__: model per data source (1 UK firm, 1 US firm)  
    * __Desiderata:__  
        * __Mitigating the "Cold-Start" Problem:__{: style="color: DarkRed"}     
            * __Description:__ We also could use ways of limiting cold start effects when we deploy at a new site.  
        * __Feature Importance (aka Timeseries Entry Ranking):__{: style="color: DarkRed"}     
            * __Description:__ For the __time entries we can’t quite predict with confidence__, can we at least <span>__predict the likelihood that the user will actually *bill* for that time entry__</span>{: style="color: purple"}?  
                * That way we can put the important stuff at the top of their time entry lists.  
        * __Generalized Modeling + Transfer Learning:__{: style="color: DarkRed"}  
            * __Description:__ How quickly can we get away from a model for every customer?  
        * __Feature Engineering:__{: style="color: DarkRed"}       
            * __Description:__ Create other metrics/features to track and collect as part of data collection.  
        * __User-level Models:__{: style="color: DarkRed"}       
            * __Description:__ Create Personalized Models per/user that attends to there characteristics
        * An accurate __NER__ system that may be fine-tuned on the domain of legal documents.  
            * __Description:__  
* __Data Anonymization:__{: style="color: SteelBlue"}  
    * __Description:__ Anonymize customer data meeting security standards.  
    * __Current Stack__:  
        * __Locality-based Hash:__ Replace all _proper nouns_ in the document titles and bodies.  
* __Activity Segmentation:__{: style="color: SteelBlue"}  
    * __Description:__ Since we collect the user’s activity in too much detail, we need to help them <span>__group several activities__ together as a __single billable unit__</span>{: style="color: purple"}.  
    * __Notes__:  
        * Most clustering algos want to know _how many clusters to make_ and don’t like leaving things out of clusters.  
            So this requires some creativity or research.  
* __Timesheet Summarization (aka Narrative Generation):__{: style="color: SteelBlue"}  
    * __Notes__:  
        * I also think that __narrative generation__ should be driven by <span>__completion tries__</span>{: style="color: purple"}.  
            We all know the theory behind those, but when you get into it, there are lots of fun implementation details (fast serialization/deserialization, how much to send, how quickly can we update it).  
* __Activity-Type Classification:__{: style="color: SteelBlue"}  
    * __Description__: We also need a model that weeds out personal vs work emails and web sessions.  
* __Topic Modeling (aka Document-Type Classifier):__{: style="color: SteelBlue"}  
    * __Description:__ Can we build a <span>__generic document type classifier__</span>{: style="color: purple"}?  
    * __Notes__:  
        * Each firm will have their own templates that they use for documents they create, so those should be easy.  
        * They will also get documents through email from other firms that would be great to identify.  
        * I personally think if we can figure out the document types, we can make an excellent advancement on narratives, phase/task codes and matter categorization for users.  
* (*__Long-Term__*) __Time-Series Analytics:__{: style="color: SteelBlue"}   
    * __Description:__ In time, we expect to show law firms analytics that help them understand how their lawyers are working, and how long cases of different types take.  

***

### __DATA__  
* __Input:__ User Activity  
    * __User Activities:__  
        * Document Type (worked on) / Activity Type (e.g. phone call)  
        * Document Title  
        * Time-Period of Work (Total + Work-Intervals)  
        * First 8K of the Document  
        * Past Behavior    
* __Output:__ Timesheets  
    * __Timesheet Entry:__  
        * __Case Number:__ i.e. related matter/subject   
        * __Phase/Task code:__ Discovery - Depositions (see UTBMS in wikipedia for details)  
        * __Narrative__: short summary of the (case?)  
* __Data-Collection__: Engineering tracks a users activity and we use the data they scraped to fill in the entries  
* __Sources__: 1 UK firm + 1 US firm  
* __Notes__:  
    * <span>Labeled Targets Exist (labeled time-sheets)</span>{: style="color: green"}   
    * <span>Input Features are _limited_</span>{: style="color: red"}  

***

### __COMPLICATIONS__  
* Limited Data Resources (quantity, variety)  
* Different Countries have different documents $$\implies$$ different datasets have different targets:  
    __Notes:__ The US and UK have separate phase/task code systems, so we may always have two models.  
* Single-Tenancy implies no <span>data sharing</span>{: style="color: purple"}  
* __Long-term storage__ of client Data requires <span>__full Anonymization__</span>{: style="color: purple"}  
    * Current __NER__ is, _possibly_, too "aggressive"  



__Notes:__{: style="color: red"}  
{: #lst-p}
* Right now we have matter categorization (which case), phase task code prediction, and NER scrubbing in production.  
* I'm finishing a microservice that will make cleaner narratives.  
* Gilles is finishing the first gen entry grouper.  
* A toy model built on Enron data exists in demo only to detect personal emails vs work.  
* I'm not thrilled with any of them, but the customers seem happy with getting some assistance over none.  
    It is a start, and get better from here.  
* A feature I forgot is the included parties on an email or phone call.  
* 30% of all work is email based.   
* Three primary high-dollar adjustment categories for attorney invoices are 1) inadequate description of work; 2) unreasonable time spent on the activity; and 3) lack or prior authorization for the activity.  
    Is the description adequate? Was the time reasonable? Was authorization actually given?  
    In other words, humans are required to evaluate and analyze what the software has flagged, and then to make a judgement about whether to adjust the line item or leave it alone.  
* litigation code classification - [Bert for lcc](https://www.mishcon.com/upload/files/Pre-trained_Contextual_Embeddings_for_Litigation_Code_Classification.Bartolo_etal.pdf)  


***
***
***

## Resources  

* __Entity Extraction:__  
    * [Accuracy Metrics For Entity Extraction](https://www.rosoka.com/sites/default/files/accuracyMetricsForEntityExtraction.pdf)  
    * [sberbank-ai/ner-bert: BERT-NER (nert-bert) with google bert https://github.com/google-research.](https://github.com/sberbank-ai/ner-bert)
    * [Joint NER and Classification (Papers With Code)](https://paperswithcode.com/task/joint-ner-and-classification)  
    * [Multitask learning for biomedical named entity recognition with cross-sharing structure \| BMC Bioinformatics \| Full Text](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-3000-5)

* __Text Classification (few-shot)__:  
    * [When Low Resource NLP Meets Unsupervised Language Model: Meta-pretraining Then Meta-learning for Few-shot Text Classification](https://arxiv.org/abs/1908.08788)
    * [ATTENTIVE TASK-AGNOSTIC META-LEARNING FOR FEW-SHOT TEXT CLASSIFICATION](https://openreview.net/pdf?id=SyxMWh09KX)  

* __Transfer Learning__:  
    * [A Tutorial to Fine-Tuning BERT with Fast AI \| Machine Learning Explained](http://mlexplained.com/2019/05/13/a-tutorial-to-fine-tuning-bert-with-fast-ai/)  
    * [Multi-label Text Classification using BERT – The Mighty Transformer](https://medium.com/huggingface/multi-label-text-classification-using-bert-the-mighty-transformer-69714fa3fb3d)  

* __Text/Document Clustering__:   
    * [Text Clustering (Papers With Code)](https://paperswithcode.com/task/text-clustering)
    * [(14) StatQuest: Hierarchical Clustering - YouTube](https://www.youtube.com/watch?v=7xHsRkOdVwo&t=0s)

* __Topic Modeling__:   
    * [echen/sarah-palin-lda: Topic Modeling the Sarah Palin emails.](https://github.com/echen/sarah-palin-lda) 

* __Summarization__:  
    * [Abstractive Sentence Compression: Differentiable Sequence-to-Sequence-to-Sequence Autoencoder for Unsupervised Abstractive Sentence Compression"](https://github.com/cbaziotis/seq3)
    * [Unsupervised Sentence Compression (Papers With Code)](https://paperswithcode.com/task/unsupervised-abstractive-sentence-compression)

* __Time-Series Clustering & Processing__:  
    * [Time Series Clustering (Papers with Code)](https://paperswithcode.com/task/time-series-clustering)  
    * [Temporal Processing \| NLP-progress](https://nlpprogress.com/english/temporal_processing.html)

* __Knowledge Graphs & Graph Theory__:  
    * [Salesforce Research: Knowledge graphs and machine learning to power Einstein \| ZDNet](https://www.zdnet.com/article/*alesforce-research-knowledge-graphs-and-machine-learning-to-power-einstein/)
    * [Populating a GRAKN.AI Knowledge Graph with the World](https://www.kdnuggets.com/2017/07/populating-grakn-ai-knowledge-graph.html)
    * [GRAKN.AI - Wikipedia](https://en.wikipedia.org/wiki/GRAKN.AI)
    * [echen/information-propagation: Information Propagation in a Social Network](https://github.com/echen/information-propagation)

* __Calendar Modeling & Event Extraction & Time Tracking__: 
    * [Natural Language Processing — Event Extraction - Towards Data Science](https://towardsdatascience.com/*atural-language-processing-event-extraction-f20d634661d3)
    * [Understanding Events with Artificial Intelligence - Towards Data Science](https://towardsdatascience.com/*nderstanding-events-with-artificial-intelligence-12e1ec3c5c9)
    * [Learning User Preferences and Understanding Calendar Contexts for Event Scheduling](https://arxiv.org/pdf/1809.01316.pdf)
    * [Supercharging Scoro with Machine Learning \| Scoro](https://www.scoro.com/blog/supercharging-scoro-with-machine-learning)
    * [Using Machine Learning to Predict and Explain Employee Attrition](https://www.kdnuggets.com/2017/10/*achine-learning-predict-employee-attrition.html)
    * [Smart task logging : Prediction of tasks for timesheets with machine learning](http://www.diva-portal.org/smash/record.jsf?pid=diva2%3A1220634&dswid=8525)
    * [Smart task logging (Thesis)](http://www.diva-portal.org/smash/get/diva2:1220634/FULLTEXT01.pdf)
    * [Leverage AI to transform time tracking into time intelligence - YouTube](https://www.youtube.com/watch?v=GylT44CUOBI&t=1553s)
    * [Memory AI - Fully automatic time tracking powered by deep learning \| Product Hunt](https://www.producthunt.com/posts/memory-ai)
    * [6 Features Any Smart Timesheet App Needs. Does Yours Have Them?](https://zistemo.com/blog/6-features-smart-timesheet-app-needs/)
    * [Using employee time series data to predict employee turnover (Binary Prediction using Time Series Data) : MLQuestions](https://www.reddit.com/r/MLQuestions/comments/a1qsnz/using_employee_time_series_data_to_predict/). 

* __Data Labeling:__  
    * [Data Turks](https://dataturks.com/)
    * [Prodigy · An annotation tool for AI, Machine Learning & NLP](https://prodi.gy/)

* __Security and Data Privacy__:  
    * [Deep Learning with Differential Privacy (paper)](https://arxiv.org/pdf/1607.00133.pdf)  

* __Resources__:  
    * [Text Matching: (NTMC-Community/MatchZoo: Facilitating the design, comparison and sharing of deep text matching models)](https://github.com/NTMC-Community/MatchZoo)
    * [lda2vec](https://github.com/cemoody/lda2vec)  
    * [Anomaly Detection in Keras with AutoEncoders (14.3) - YouTube](https://www.youtube.com/watch?v=1ySn6h2A68I&t=0s)  
    * [Relationship Extraction (Distant Supervised) (Papers With Code)](https://paperswithcode.com/task/relationship-extraction-distant-supervised)
    * [5hirish/adam\_qas: ADAM - A Question Answering System. Inspired from IBM Watson](https://github.com/5hirish/adam_qas)
    * [machine learning smart timesheet - Google Search](https://www.google.com/search?q=machine+learning+smart+timesheet&rlz=1C5CHFA_enUS78*US785&sxsrf=ACYBGNTEWbybI3F0iFyNSqX67r6qltb2Fg:1572128131533&ei=g8W0XfufII-0swXK87_4AQ&start=30&sa=N&ved=0ahUKEwi77cjW-brlAhUP2qwKHcr5Dx84FBDy0wMIdg&biw=1920&bih=969)
    * [Memory AI: About \| LinkedIn](https://www.linkedin.com/company/memory-ai/about/)
    * [Semi-supervised Sequence Learning](https://arxiv.org/abs/1511.01432)
    * [EMNLP-2019-Papers: Statistics and Accepted paper list with arXiv link of EMNLP-IJCNLP 2019](https://github.com/roomylee/EMNLP-2019-Papers)