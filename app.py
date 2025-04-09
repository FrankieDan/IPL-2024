
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="IPL 2024 Dashboard", layout="wide")

st.title("🏏 IPL 2024 Data Analysis Dashboard")
st.markdown("Upload your IPL 2024 match data CSV file to explore team and player performance.")

uploaded_file = st.file_uploader("Upload IPL 2024 CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data loaded successfully!")

    with st.expander("📋 Show Raw Data"):
        st.dataframe(df, use_container_width=True)

    # Display summary statistics
    st.subheader("📊 Summary Statistics")
    st.dataframe(df.describe(), use_container_width=True)

    # Team-wise analysis
    if 'team' in df.columns:
        st.subheader("🏆 Team Performance")
        team_col = st.selectbox("Select Team Column", options=['team'], index=0)
        fig1, ax1 = plt.subplots()
        df[team_col].value_counts().plot(kind='bar', ax=ax1, color='skyblue')
        ax1.set_ylabel("Matches Played")
        ax1.set_title("Matches Played by Team")
        st.pyplot(fig1)

    # Player performance analysis
    player_cols = [col for col in df.columns if 'player' in col.lower()]
    if player_cols:
        st.subheader("⭐ Player Performance")
        player_col = st.selectbox("Select Player Column", player_cols)
        top_players = df[player_col].value_counts().head(10)
        fig2, ax2 = plt.subplots()
        top_players.plot(kind='barh', ax=ax2, color='orange')
        ax2.invert_yaxis()
        ax2.set_xlabel("Appearances")
        ax2.set_title("Top 10 Players by Match Appearance")
        st.pyplot(fig2)

    # Numeric analysis
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if numeric_cols:
        st.subheader("📈 Numeric Data Visualization")
        selected_num = st.selectbox("Select a Numeric Column", numeric_cols)
        fig3, ax3 = plt.subplots()
        sns.histplot(df[selected_num], kde=True, ax=ax3)
        ax3.set_title(f"Distribution of {selected_num}")
        st.pyplot(fig3)

else:
    st.info("Please upload a CSV file to start the analysis.")
