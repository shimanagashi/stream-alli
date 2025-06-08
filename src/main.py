import streamlit as st

st.title("アライ販売 事前問診票")

# 入力欄（すべて手入力）
weight = st.number_input("体重（kg）", value=65)
height = st.number_input("身長（cm）", value=160)
waist = st.number_input("腹囲（cm）", value=90)
sex = st.radio("性別", options=["female", "male"])

# 判定関数
def check_arai(weight, height, waist, sex):
    normalized_height = height / 100
    bmi = weight / (normalized_height ** 2)

    if sex == "female":
        if waist >= 90 and 25 <= bmi < 35:
            return "ok"
        else:
            return "no"
    elif sex == "male":
        if waist >= 85 and 25 <= bmi < 35:
            return "ok"
        else:
            return "no"
    else:
        return "不明な性別"

# 判定 & ダウンロード
if st.button("判定とダウンロード"):
    result = check_arai(weight, height, waist, sex)
    bmi = weight / ((height / 100) ** 2)

    # 表示
    st.write(f"判定結果: {result}")
    st.write(f"BMI: {bmi:.1f}")

    # ダウンロード用テキストを作成
    report = f"""【アライ販売 事前問診票】
性別: {sex}
体重: {weight} kg
身長: {height} cm
腹囲: {waist} cm
BMI: {bmi:.1f}
判定結果: {result}
"""

    st.download_button(
        label="問診票をダウンロード（.txt）",
        data=report,
        file_name="arai_monsin.txt",
        mime="text/plain"
    )
