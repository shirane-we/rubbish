import pandas as pd
from load_data import load_raw

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """新增小时、星期、是否节假日"""
    df = df.copy()
    df["hour"] = df["time"].dt.hour
    df["weekday"] = df["time"].dt.dayofweek      # 0=周一
    df["is_holiday"] = df["time"].dt.date.isin(holiday_list())
    return df

def holiday_list():
    """2023 年五一假期手工表，可再扩"""
    from datetime import date
    return [date(2023, 4, 29), date(2023, 4, 30),
            date(2023, 5, 1),  date(2023, 5, 2), date(2023, 5, 3)]

def station_flow(df: pd.DataFrame, top_n: int = 10):
    """计算站点日均进出站量"""
    flow = (df.groupby(["station_id", "station_name", "type"])
              .size()
              .unstack(fill_value=0)
              .reset_index())
    flow["total"] = flow["in"] + flow["out"]
    return flow.nlargest(top_n, "total")

if __name__ == "__main__":
    df = load_raw()
    df = add_features(df)
    print(station_flow(df))
