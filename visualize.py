import matplotlib.pyplot as plt
import seaborn as sns
from preprocess import add_features, station_flow

def hourly_heatmap(df, save_path=None):
    """全天 24h 进出站热力图"""
    df = add_features(df)
    heat = (df.pivot_table(index="station_name", columns="hour",
                           values="type", aggfunc="count",
                           fill_value=0))
    plt.figure(figsize=(12, 6))
    sns.heatmap(heat.iloc[:20], cmap="YlGnBu")
    plt.title("Top20 站点 24h 客流热力图")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def top_station_bar(df, save_path=None):
    """TOP10 站点柱状图"""
    flow = station_flow(df)
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=flow, x="total", y="station_name", ax=ax,
                palette="viridis")
    ax.set_title("2023.5 日均客流 TOP10 站点")
    if save_path:
        fig.savefig(save_path, dpi=300)
    plt.show()

if __name__ == "__main__":
    from load_data import load_raw
    df = load_raw()
    hourly_heatmap(df, save_path="outputs/hourly_heatmap.png")
    top_station_bar(df, save_path="outputs/top10_bar.png")
