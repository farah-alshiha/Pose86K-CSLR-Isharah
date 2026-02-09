import pandas as pd

PATH1 = "./annotations_v2/isharah2000/SI/train.txt"
PATH2 = "./annotations_v2/isharah2000/SI/dev.txt"

# Read as pipe-delimited
df1 = pd.read_csv(PATH1, delimiter="|")
df2 = pd.read_csv(PATH2, delimiter="|")

# Remove ALL double quotes from the text column
df1["text"] = df1["text"].astype(str).str.replace('"', '', regex=False)
df2["text"] = df2["text"].astype(str).str.replace('"', '', regex=False)

# Overwrite the file (same format)
df1.to_csv(PATH1, sep="|", index=False)
df2.to_csv(PATH2, sep="|", index=False)

print("Fixed quotes in:", PATH1)
print("Fixed quotes in:", PATH2)

print(df1.head())
print(df2.head())

