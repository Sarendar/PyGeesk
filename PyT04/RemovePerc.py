import os
import pandas as pd

if __name__ == "__main__":
    print("Entered.............")
    # read csv file
    path = os.path.join("predictions.csv")
    df = pd.read_csv(path)
    print("DFFFFFFF data..",df)
    df["tpv"] = df["tpv"].replace("%","",regex=True).astype("float")

    print("After removed % DF",df,df['tpv'][11],type(df['tpv'][11]))
