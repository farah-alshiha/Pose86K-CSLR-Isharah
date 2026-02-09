import os

MODE = "SI"

# INPUT FILES (your raw label files)
TRAIN_RAW = "./annotations_v2/isharah2000/SI/train.txt"
DEV_RAW   = "./annotations_v2/isharah2000/SI/dev.txt"

# OUTPUT FILES (what the baseline will read)
OUT_DIR = f"./annotations_v2/isharah2000/{MODE}"
os.makedirs(OUT_DIR, exist_ok=True)

TRAIN_OUT = os.path.join(OUT_DIR, "train.txt")
DEV_OUT   = os.path.join(OUT_DIR, "dev.txt")


def convert_by_index(in_path, out_path):
    rows = []
    with open(in_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if len(line) < 10:
                continue  # skip malformed lines

            sample_id = line[1:8].strip()
            text      = line[9:].strip()

            if sample_id and text:
                rows.append((sample_id, text))

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("id|text\n")   # HEADER IS REQUIRED
        for sid, txt in rows:
            f.write(f"{sid}|{txt}\n")

    print(f"Wrote {len(rows)} rows → {out_path}")


convert_by_index(TRAIN_RAW, TRAIN_OUT)
convert_by_index(DEV_RAW,   DEV_OUT)

print("Done.")
