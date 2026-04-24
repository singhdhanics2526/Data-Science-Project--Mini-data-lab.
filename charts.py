import matplotlib.pyplot as plt


def bar_chart(df, x_col, y_cols, title):
    ax = df.plot(x=x_col, y=y_cols, kind="bar", figsize=(10, 5), title=title)
    ax.set_xlabel(x_col)
    ax.set_ylabel("Value")
    plt.tight_layout()
    plt.show()


def line_chart(df, x_col, y_cols, title):
    ax = df.plot(x=x_col, y=y_cols, kind="line", figsize=(10, 5), title=title, marker="o")
    ax.set_xlabel(x_col)
    ax.set_ylabel("Value")
    plt.tight_layout()
    plt.show()


def histogram(df, column, title):
    df[column].plot(kind="hist", bins=10, figsize=(8, 5), title=title, edgecolor="black")
    plt.xlabel(column)
    plt.tight_layout()
    plt.show()
