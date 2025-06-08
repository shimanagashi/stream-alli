# アライ販売 事前問診票

このリポジトリには、ストリームリットで実装した簡単な Web アプリケーションが含まれています。体重、身長、腹囲、性別を入力すると BMI を計算し、アライ(オルリスタット)を販売できるかどうかを判定します。また、結果をテキストファイルとしてダウンロードすることもできます。

## セットアップ

1. 依存パッケージをインストールします。
   ```bash
   pip install -r requirements.txt
   ```
2. アプリを起動します。
   ```bash
   streamlit run src/main.py
   ```

## Docker での実行例

Docker を使用してアプリを実行する場合は次のようにします。
```bash
docker build -t stream-alli .
docker run -p 8501:8501 stream-alli streamlit run src/main.py
```

## ファイル構成
- `src/main.py` : Streamlit アプリ本体
- `requirements.txt` : 必要な Python パッケージ
- `Dockerfile` : Docker イメージ作成用の設定

このアプリは検証用の簡易ツールであり、実際の医療判断には利用できません。
