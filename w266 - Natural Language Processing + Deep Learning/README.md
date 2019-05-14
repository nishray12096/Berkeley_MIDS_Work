# W266 - Natural Language Processing & Deep Learning
Assignments completed:
Introduction to Tensorflow
Text classification using CNN's
Language Modelling
Part of Speech Tagging

Assignment files are withheld to avoid plagiarism.

Final project:
# W266-NLP-Project

# List of documents:
* W266_Automated_Essay_Grading.pdf contains the project report
* Feature_Engineering.ipynb contains the work related to feature extraction [Section 3 of project report]
* Linear_Predictors.ipynb contains the linear models used on the features extracted [Section 4 of project report]
* Visuals.ipynb contains the graphs/visuals of features
* AEG_Deep_Learning_Essay_Classification.ipynb contains the deep learning models on essay set [Section 5 & 7]
* AEG_LSTM_Best_Model.ipynb contains the execution of stacked LSTM on essay set [Section 5] 
* AEG_Deep_Learning_Sentence_Classification.ipynb contains the deep learning models on sentence level [Section 6]

# Project Proposal:
We propose to leverage graded essay datasets to create insights into the quality of writing. Primarily, we will use two datasets provided by the Hewlett Foundation: one of essay length answers (avg 150-550 words) and one of the short answers (avg 50 words). The datasets are limited in size (13,000 and 17,000 respectively) and our goals require model transparency: thus, we anticipate using simpler models. Previous work in this area used such techniques [1]. 

At a high level, our first step is to study literature to identify possible featurizations that could correlate with writing “quality.” After featurizing essays, we will attempt to predict the output grade using transparent ML techniques. If the classifier can achieve reasonable performance, we can identify heavily weighted features as important to the quality of writing. We propose to use the quadratic weighted kappa as our primary performance measure. We would consider the model's inability to differentiate between low and high scoring essays on the basis of text quality measures an interesting finding as well: as it would suggest the need for a new metric. 

Additional goals will include applying these techniques to TED talk transcripts. We will create proxy metrics for TED talk quality using the talk popularity. We are interested in finding if any of the features that correlate with essay score also correlate (either positively or negatively) with TED talk popularity.

The primary challenge of this exercise is identifying reasonable and informative text featurizations when considering essay quality. Our literature review to date has suggested the following possibilities:

* Length Features: the average sentence length in words and word length [2]
* Occurrence Features: use of linguistic phenomena (e.g. punctuation marks) [1,2]
* Syntax Features: syntactic variation, proportion of special clauses [1, 2]
* Style Features: quality of vocabulary, variety of vocabulary, word frequency [2, 3,4]
* Cohesion Features: occurence of connective words or phrases [1,2]
* Coherence Features: topical overlap between adjacent sentences [2]
* Error Features: grammatical or spelling errors [2,5]
* Readability Features: counts of words/letters/syllables that impact readability [2,3] 

We will be capturing some of these feature categories with multiple features, so the question of aggregation remains open. Some initial research suggests that a model with aggregated features (combining micro features from a category into an aggregate score) and the micro features themselves outperforms models with either just the micro features  or just the aggregate features [6]. Our hope is that the aggregate 

Additional goals will include applying these techniques to TED talk transcripts. We will create proxy metrics for TED talk quality using the talk popularity. We are interested in finding if any of the features that correlate with essay score also correlate (either positively or negatively) with TED talk popularity.


References: 
Automated Scoring Using A Hybrid Feature Identification Technique (1998)
Task-Independent Features for Automated Essay Grading (2015) 
Real-Time Web Text Classification and Analysis of Reading Difficulty (2008) 
Thank “Goodness”! A Way to Measure Style in Student Essays (2018) 
How Far are We from Fully Automatic High Quality Grammatical Error Correction? (2015)
To Aggregate or Not? Linguistic Features in Automatic Essay Scoring and Feedback Systems (2015)
