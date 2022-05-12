---
layout: NotesPage
title: Ping Roadmap
permalink: /work_files/ping_short
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