!pip install kagglehub pandas mido

import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "Kepler_lightcurve_statistics.csv"

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "nikitamanaenkov/kepler-452b-exoplanet-datasets",
    file_path,
)

print("First 5 records:", df.head())
print("Available columns:", df.columns.tolist())
