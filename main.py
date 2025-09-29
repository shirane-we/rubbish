import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from load_data import load_raw
from visualize import hourly_heatmap, top_station_bar

if __name__ == "__main__":
    df = load_raw()
    Path("outputs").mkdir(exist_ok=True)
    hourly_heatmap(df, "outputs/hourly_heatmap.png")
    top_station_bar(df, "outputs/top10_bar.png")
    print("✅ 可视化完成，图片已保存至 outputs/")
