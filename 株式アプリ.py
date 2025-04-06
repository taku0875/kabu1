import streamlit as st
import pandas as pd

# --- アプリ設定 ---
st.set_page_config(page_title="会社別セクター表示", page_icon="🏢", layout="centered")

# --- タイトル ---
st.markdown("## 🏢 会社を選んでセクターを確認")
st.caption("※ データはSQLiteから取得しています")

# --- SQLiteに接続 ---
conn = st.connection("sqlite", type="sql")

# --- データ取得 ---
df = conn.query(
    "SELECT CompanyName, SectorName FROM kabu WHERE CompanyName IS NOT NULL AND SectorName IS NOT NULL",
    ttl=600
)

# --- 会社名リスト作成 ---
companies = sorted(df["CompanyName"].unique())
selected_company = st.selectbox("会社を選択してください", companies)

# --- 結果表示 ---
if selected_company:
    sector = df[df["CompanyName"] == selected_company]["SectorName"].iloc[0]
    
    with st.container():
        st.markdown("---")
        st.markdown(f"### 📊 セクター")
        st.success(f"**{selected_company}** の属するセクターは **「{sector}」** です。", icon="🏷️")