# UAnalyze Online Reviews to Identify Pain points
## Goal: Identify West Elm customers pain points by analyzing 1 & 2 star reviews 
Our CCIP team's client is West Elm, and we're trying to identify issues with the company. There are online articles that address West Elm's issues with late deliveries. However, to substantiate these claims and decide whether West Elm's delivery is truly a problem to customer, I decided to use Python to find the most discussed topics in negative online reviews, and compare the results with West Elm's competitors (Ikea and Wayfair).
## Process:
1. Scrape online reviews from ConsumerAffairs using Octoparse
2. Use Natural Language Processing to Preprocess and Clean Reviews (Tokenize sentences, Remove stop words, Normalize words)
3. Visualize most commonly used words with Matplotlib

# Result: Most commonly used words in 700 negative West Elm reviews:
From the graph, it can be concluded that the most mentioned issues in West Elm's online reviews are delivery (650 times) and customer service (400 times)
![alt text](https://github.com/nct1906/review-analysis/blob/main/West%20Elm%20consumer%20affair%20700.png?raw=true)
