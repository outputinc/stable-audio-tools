from pathlib import Path
import pandas as pd

loops_df = pd.read_csv("loops.csv")

loopid_to_name = dict(zip(loops_df["loop_id"], loops_df["name"]))

def get_custom_metadata(info, audio):
    loopid = Path(info["relpath"]).parent
    name = loopid_to_name.get(str(loopid), "")
    return {"prompt": name}