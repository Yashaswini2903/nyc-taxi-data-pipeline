import pandas as pd

def ingest_data():
    df = pd.read_csv('data/sample_data.csv')
    print("Data Ingested Successfully")
    print(df.head())

if __name__ == "__main__":
    ingest_data()
