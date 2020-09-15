import os
import pandas as pd


def movingColumns():

    path = os.path.join("predictions.csv")
    df = pd.read_csv(path)
    print("Data frame..........", list(df.columns))
    cols = list(df.columns)

    # Moving last column to first
    move_cols = [cols[-1]] + cols[:-1]
    df = df[move_cols]

    print("Moved last column to first: ",list(df.columns))

    # Moving first column to last
    move_cols = cols[1:] + [cols[0]]
    df =df[move_cols]
    print("Moved first column to last :",list(df.columns))

if __name__ == "__main__":
    print("Reading CSV file")

    movingColumns()


