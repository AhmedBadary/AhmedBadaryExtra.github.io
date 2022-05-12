---
layout: NotesPage
title: Ping! <br> Roadmap
permalink: /work_files/ping2
prevLink: /
---


* __Tasks:__{: style="color: SteelBlue"}  
    * __Automatic Timesheet Completion__  
        __Description:__ Making tools that make sound guesses at what a user would want to do in filling out a timesheet and do it for them  
* __Data:__{: style="color: SteelBlue"}  
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
* __Complications:__{: style="color: SteelBlue"}  
    * Limited Data Resources (quantity, variety)  
    * Different Countries have different documents $$\implies$$ different datasets have different targets:  
        __Notes:__ The US and UK have separate phase/task code systems, so we may always have two models.  
    * Single-Tenancy implies no <span>data sharing</span>{: style="color: purple"}  
    * __Long-term storage__ of client Data requires <span>__full Anonymization__</span>{: style="color: purple"}  
        * Current __NER__ is, _possibly_, too "aggressive"  
            * Does it do us any good to store endless documents and emails if every 5th word is replaced with a tag?  (I have deep concerns over this.)  
            * Tags eliminate the ability for any large transformer to track semantic relationships between subjects and objects.  
                Does that matter (I presume it does, but haven’t tested the effect)?  


* __Current Stack:__{: style="color: SteelBlue"}  
    * __Automated Time-Sheet Completion__:  
        * __Model:__ Gradient-Boosted Models (GBMs)  
            Model for each data source (1 UK firm, 1 US firm)  
    * __Data Anonymization__:  
        * __Model:__ Locality-based Hash  
            Replace all _proper nouns_ in the document titles and bodies.  



* __Desiderata:__{: style="color: SteelBlue"}  
    * How quickly can we get away from a model for every customer.  
    * Anonymize customer data meeting security standards.  
    * Create other metrics/features to track and collect as part of data collection.  
    * Create Personalized Models per/user that attends to there characteristics  
    * An accurate __NER__ system that may be fine-tuned on the domain of legal documents.
