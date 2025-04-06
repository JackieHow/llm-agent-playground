# 创建环境
conda env create -f environment.yml

# 激活环境
conda activate your_env_name

# 生成并安装 pip 依赖
pipreqs . --force
pip install -r requirements.txt

# 安装其他依赖（如果有）
# conda install package_name