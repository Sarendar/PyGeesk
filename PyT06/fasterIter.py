import os
import pandas as pd
import time

if __name__ == "__main__":

    file_path = os.path.join("predictions.csv")
    df = pd.read_csv(file_path)
    print("Entered in to main: ", len(df))
    B = []

    C = []
    A = time.time()
    for i in range(len(df)):
        C.append(df.loc[i, "close"])
    B.append(time.time() - A)

    C = []
    A = time.time()
    for i, r in df.iterrows():
        C.append((r['Date']))
    B.append(time.time() - A)

    C = []
    A = time.time()
    for ir in df.itertuples():
        C.append((ir[1]))
        #print("ir 11", ir[2])
    B.append(time.time() - A)

    C = []
    A = time.time()
    for r in zip(df['Date']):
        C.append((r[0]))
    B.append(time.time() - A)

    print("TIME CALCULATIONS range(len()), iterrows(), itertuples(), zip()......", B)