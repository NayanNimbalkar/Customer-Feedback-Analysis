import os
import re
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Customer Feedback Analysis",
    page_icon="💬",
    layout="centered"
)

# OpenAI API key will be added securely during deployment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key is not configured.")
    st.stop()

client = OpenAI(api_key=api_key)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def classify_review(score):
    if score in [1, 2]:
        return "🔴 Critical"
    return "🟢 Non-Critical"


def generate_customer_response(review):

    prompt = f"""
You are a professional customer support agent.

A customer has submitted the following negative review:

Customer Review:
{review}

Write a short, personalized and empathetic apology email.

Requirements:
- Address the customer's specific complaint.
- Acknowledge the customer's frustration.
- Be professional and empathetic.
- Keep the response concise.
- Do not invent refunds, discounts, compensation, or actions.
- Do not make promises that are not supported by the review.
- Do not mention AI.
- End with a professional customer-support closing.

Return only the email.
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text


# Application title
st.title("💬 Customer Feedback Analysis")

st.subheader(
    "Customer Feedback Analysis and Automated Response"
)

st.write(
    "Analyze customer reviews using rule-based filtering "
    "and generate personalized AI-powered responses."
)

# Customer rating
score = st.selectbox(
    "Customer Rating",
    [1, 2, 3, 4, 5]
)

# Customer review
review = st.text_area(
    "Customer Review",
    height=180,
    placeholder="Enter the customer's review here..."
)

# Analyze button
if st.button("🔍 Analyze Review"):

    if not review.strip():

        st.warning("Please enter a customer review.")

    else:

        cleaned_review = clean_text(review)
        classification = classify_review(score)

        st.divider()

        st.subheader("Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Customer Rating", f"{score} / 5")

        with col2:
            st.write("Review Classification")
            st.write(classification)

        st.subheader("Cleaned Review")
        st.write(cleaned_review)

        # Generate AI response only for critical reviews
        if score in [1, 2]:

            st.subheader("🤖 Automated Customer Response")

            with st.spinner("Generating personalized response..."):

                try:

                    ai_response = generate_customer_response(review)

                    st.success(
                        "AI response generated successfully."
                    )

                    st.text_area(
                        "Generated Response",
                        value=ai_response,
                        height=250
                    )

                except Exception as e:

                    st.error(
                        f"Unable to generate AI response: {str(e)}"
                    )

        else:

            st.info(
                "This review is non-critical. "
                "An automated apology response is not required."
            )