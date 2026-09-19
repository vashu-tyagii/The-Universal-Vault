import sys
from pathlib import Path
import pandas as pd  # type:ignore

# Automatic root folder dhoondh kar sys.path mein jodna
current_dir = Path(__file__).resolve()
for parent in [current_dir] + list(current_dir.parents):
    if parent.name == "The-Universal-Vault":
        sys.path.append(str(parent))
        break

# Config se engine import karo
# # fmt: off
from config.sql_connect import engine # type:ignore
# # fmt: on


query = 'select * from employees ;'
print(pd.read_sql(query, con=engine))
