import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    print(f"Missing values:\n{df.isnull().sum()[df.isnull().sum() > 0]}\n")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["director"].fillna("Unknown", inplace=True)
    df["cast"].fillna("Unknown", inplace=True)
    df["country"].fillna("Unknown", inplace=True)
    df["rating"].fillna(df["rating"].mode()[0], inplace=True)
    df["duration"].fillna("Unknown", inplace=True)

    df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    df["year_added"] = df["year_added"].fillna(df["year_added"].median())

    df["duration_value"] = df["duration"].str.extract(r"(\d+)").astype(float)
    df["main_genre"] = df["listed_in"].str.split(", ").str[0]
    df["primary_country"] = df["country"].str.split(", ").str[0]

    return df


def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["is_movie"] = (df["type"] == "Movie").astype(int)

    df_encoded = pd.get_dummies(
        df[["primary_country", "rating", "main_genre", "is_movie"]],
        drop_first=True
    )
    return df_encoded