# Customer Feedback Analysis and Automated Response

## Project Overview

This project analyzes customer reviews to identify critical negative feedback and automate personalized customer-support responses using Generative AI.

The project combines Python-based data analysis, rule-based filtering, text analysis, and Generative AI to help a customer-support team prioritize important reviews and reduce the manual effort required to draft responses.

## Business Problem

A company receives a large number of customer reviews and support feedback. Manually identifying critical negative reviews and preparing individual responses can be time-consuming.

This project aims to:

- Identify critical negative reviews using customer ratings.
- Analyze frequently mentioned topics in critical reviews.
- Select the most critical and detailed reviews.
- Generate personalized and empathetic customer-support responses using Generative AI.

## Project Objectives

1. Clean and prepare the customer review dataset.
2. Handle missing values and clean review text.
3. Identify critical reviews using a rule-based approach.
4. Analyze frequently mentioned complaint keywords.
5. Select three detailed critical reviews.
6. Generate personalized responses using the OpenAI API.
7. Provide business insights based on the analysis.

## Dataset

The dataset contains customer reviews and related information such as:

- Customer name
- Review content
- Rating/score
- Helpful votes
- Review version
- Review date
- Company response
- Response date
- Application ID

## Data Cleaning

The following data-cleaning steps were performed:

- Removed unnecessary columns.
- Checked missing values.
- Converted date columns into datetime format.
- Converted review text to lowercase.
- Removed unnecessary special characters.
- Created a separate `clean_content` column for text analysis.
- Removed reviews that became empty after text cleaning.
- Checked and removed duplicate records.
- Created a `review_length` column to measure review length.

The original review text was retained for Generative AI processing, while the cleaned text was used for keyword analysis.

## Rule-Based Critical Review Filtering

Critical reviews were identified using customer ratings.

```python
critical_reviews = df[df['score'].isin([1, 2])].copy()