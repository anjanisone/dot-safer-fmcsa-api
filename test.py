import os
from tqdm import tqdm


for i in tqdm(range(1000000, 3000000)):
    os.system(f"./dot.py --query '{i}' > files/{i}.txt")
    with open(f"files/{i}.txt") as file:
        data = file.read()
        if len(data) == 0:
            os.system(f"rm -rf files/{i}.txt")
        if "an error occurred" in data:
            os.system(f"rm -rf files/{i}.txt")