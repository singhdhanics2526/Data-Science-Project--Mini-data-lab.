import numpy as np


def summary(df):
    return df.describe()


def mean(df, column):
    return np.mean(df[column].values)


def std(df, column):
    return np.std(df[column].values)


def correlation(df):
    numeric = df.select_dtypes(include=[np.number])
    return numeric.corr()


def print_stats(df, name):
    print(f"\n{name} — df.describe()")
    print(summary(df))
    print(f"\n{name} — correlation matrix")
    print(correlation(df))
