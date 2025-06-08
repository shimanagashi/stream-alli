FROM python:3.12.10-bullseye

# 必要パッケージのインストール
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの作成
WORKDIR /app

# Python パッケージのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
