from io import StringIO
import requests
import polars as pl

IRIS = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def main():
    result = analyze(dataframe_from(iris_data()))
    print(result)


def iris_data(url: str = IRIS) -> str:
    return requests.get(url).text


def dataframe_from(csv_data: str) -> pl.DataFrame:
    return pl.read_csv(StringIO(csv_data))


def analyze(df: pl.DataFrame) -> pl.DataFrame:
    return df.filter(pl.col("sepal_length") > 5).group_by("species").agg(pl.all().sum())


if __name__ == "__main__":
    main()
