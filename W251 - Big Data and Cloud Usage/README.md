# W251 - Big Data, Cloud, IOT

AzureML:
One responsibility was to track new offerings in the cloud DS space. I presented on AzureML capabilities.
Files:
•	Discussion_AzureML_Deployment.pptx

Assignment 1: "The Mumbler"
Here, we used n-grams calculated by google books to create an algorithm that would input a word and a sentence length and output sentence of specified length. The challenge was that the n-gram data to be used was too large to fit on any one machine in the cluster: thus, we optimized to reduce network traffic and calculate n-grams as quickly as possible.

Files:
•	Mumbler.py – runs the mumbler
•	Download_file_loop*.sh – scripts to download files from google books, split out so I could download in parallel
•	Inputprocessing.sh – takes the individual zipped files, unzips and aggregates one by one to reduce size
•	SearchNode*.sh – uses grep and awk to find records relevant to the word being searched
•	mumblerNode.sh – adds node related file endings to each csv for separation of tasks by node

HW2: Introduction to Spark
In this assignment, we processed the book "Moby Dick" and answered several basic questions using Spark.
Files:
•	Hw6JavaCode.java - code to process Moby Dick using RDDs

HW3: Streaming Data
In this assignment, I calculated the most popular tags and authors on twitter using two windows of differing length in Scala. The shorter window would continuously output results for the duration of the longer window. I also took in a number of popular topics: this number of topics would be presented in outputs.
Files
•	twitter_popularity.scala - all code required to open twitter stream, calculate window RDDs, and output results

Final Project - Streaming stock data + related tweets, providing reporting, and making short-term stock price predictions
In our final project, we streamed stock data every 5 minutes and aggregated twitter data for Fortune 100 companies. We built a pair of VM clusters: one to stream from twitter and stock price repositories, one to store processed data using MongoDB. We also built Kibana dashboards for sentiment visualizations by company and stock price reporting as well as RNN-based stock price predictions.
Files:
•	parseAndStoreStockPrices.scala - stream stock data every 5 minutes
•	SentimentUtils.scala - using StanfordCoreNLP to tag each tweet related to a Fortune 100 company with some sentiment
•	TrainSentiment_RNN.py - using aggregated sentiment for sequence stock price prediction. Allows variable windows & lookback
•	pophashtag.scala - code to stream tweets and manage sentiment calculation





