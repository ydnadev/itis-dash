import pandas as pd

df = pd.read_csv('../itisdata/animals_phyla.txt', sep='\t')
df.to_parquet('../data/itis.parquet')
