```bash
# 1. 克隆（或手动建文件夹）
git clone https://github.com/yourname/subway-flow.git
cd subway-flow

# 2. 建虚拟环境
python -m venv venv
source venv/bin/activate      # Windows 用 venv\Scripts\activate

# 3. 装依赖
pip install -r requirements.txt

# 4. 跑
python -m src                 # 自动生成 outputs/ 两张 png
jupyter lab notebook/eda.ipynb # 想交互再跑
```
