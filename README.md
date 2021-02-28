# COVID-analysis
NLP based text summarization and clustering of COVID-related research.

### Motivation
The world is grappling with one of the deadliest pandemics in history. Each day I receive news about a new COVID-19 research and its findings. I was interested in keeping myself informed with the latest research on coronaviruses and I decided to analyze research papers to understand the different topics being discussed. I was also interested in summarizing these papers to quickly understand the content of the papers without having to read it fully. 

### Dataset
[CORD-19: The Covid-19 Open Research Dataset](https://allenai.org/data/cord-19)
CORD-19 is a free resource of tens of thousands of scholarly articles about COVID-19, SARS-CoV-2, and related coronaviruses for use by the global research community.
The data was pulled in August 2020 and has ~19,000 research papers.

### Analysis

#### Clustering and Topic Modelling
Identify the optimal number of clusters for this dataset using k-means clustering. Then perform topic modelling for the number of clusters from clustering analysis. 

#### Abstractive summarization
Build abstractive summaries on papers using [BertAbs](https://github.com/nlpyang/PreSumm) and BERT-Base uncased model.

### Code
1. extract_data - Preprocess raw papers and store it in json format for ease of accessibility.
2. covid_analysis - exploratory analysis on extractive summarization and abstracts of papers.
3. covid_clustering - Analyze papers using K-means clustering nd topic modelling.
4. covid_bert - Generate abstractive summarization on papers using BERTAbs and BERT-Base uncased model.






