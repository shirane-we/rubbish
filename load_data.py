import pandas as pd
from config import RAW_FILE

def load_raw():
    """返回原始刷卡数据"""
    return pd.read_csv(RAW_FILE, parse_dates=["time"])

if __name__ == "__main__":
    df = load_raw()
    print(df.head())
