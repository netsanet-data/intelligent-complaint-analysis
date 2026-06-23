import re
import pandas as pd


TARGET_PRODUCTS = [
    "Credit Card",
    "Personal Loan",
    "Savings Account",
    "Money Transfer"
]


def load_data(file_path):
    """
    Load the complaints dataset.
    """
    if not file_path:
        raise FileNotFoundError("Dataset path is missing.")

    return pd.read_csv(file_path)


def filter_products(df):
    """
    Keep only the four required product categories.
    """
    return df[df["product_category"].isin(TARGET_PRODUCTS)].copy()


def remove_empty_narratives(df):
    """
    Remove rows without complaint narratives.
    """
    return df.dropna(subset=["consumer_complaint_narrative"]).copy()


def clean_text(text):
    """
    Basic text cleaning.
    """
    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-z0-9\s]", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


def preprocess_dataframe(df):

    df = filter_products(df)

    df = remove_empty_narratives(df)

    df["cleaned_text"] = df["consumer_complaint_narrative"].apply(clean_text)

    return df