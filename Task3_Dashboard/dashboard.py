import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Titanic Survival Dashboard",
    page_icon="🚢",
    layout="wide"
)

# Dashboard title
st.title("🚢 Titanic Survival Analysis Dashboard")
st.markdown(
    "Explore passenger survival patterns by gender, age group, and passenger class."
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Task1_Data_Cleaning/Titanic_cleaned.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

gender_options = ["All"] + sorted(df["Sex"].dropna().unique().tolist())
selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

class_options = ["All"] + sorted(df["Pclass"].dropna().unique().tolist())
selected_class = st.sidebar.selectbox(
    "Select Passenger Class", class_options
)

# Apply filters
filtered_df = df.copy()

if selected_gender != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == selected_gender]

if selected_class != "All":
    filtered_df = filtered_df[filtered_df["Pclass"] == selected_class]

# KPI calculations
total_passengers = len(filtered_df)
survivors = int(filtered_df["Survived"].sum())
deceased = total_passengers - survivors

survival_rate = (
    survivors / total_passengers * 100
    if total_passengers > 0 else 0
)

# KPI cards
st.subheader("📊 Key Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Passengers", total_passengers)
col2.metric("Survivors", survivors)
col3.metric("Deceased", deceased)
col4.metric("Survival Rate", f"{survival_rate:.1f}%")

st.divider()

# Survival distribution chart
st.subheader("1. Survival Distribution")

if not filtered_df.empty:
    survival_counts = filtered_df["Survived"].value_counts().reindex(
        [0, 1], fill_value=0
    )
    survival_counts.index = ["Did Not Survive", "Survived"]

    fig1, ax1 = plt.subplots()
    survival_counts.plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Passenger Outcome")
    ax1.set_ylabel("Number of Passengers")
    ax1.set_title("Passenger Survival Distribution")
    ax1.tick_params(axis="x", rotation=0)
    fig1.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

    # Survival by gender
    st.subheader("2. Survival Rate by Gender")

    gender_survival = (
        filtered_df.groupby("Sex")["Survived"].mean() * 100
    )

    fig2, ax2 = plt.subplots()
    gender_survival.plot(kind="bar", ax=ax2)
    ax2.set_xlabel("Gender")
    ax2.set_ylabel("Survival Rate (%)")
    ax2.set_title("Survival Rate by Gender")
    ax2.tick_params(axis="x", rotation=0)
    fig2.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

    # Survival by passenger class
    st.subheader("3. Survival Rate by Passenger Class")

    class_survival = (
        filtered_df.groupby("Pclass")["Survived"].mean() * 100
    )

    fig3, ax3 = plt.subplots()
    class_survival.plot(kind="bar", ax=ax3)
    ax3.set_xlabel("Passenger Class")
    ax3.set_ylabel("Survival Rate (%)")
    ax3.set_title("Survival Rate by Passenger Class")
    ax3.tick_params(axis="x", rotation=0)
    fig3.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)

    # Survival by age group
    st.subheader("4. Survival Rate by Age Group")

    age_df = filtered_df.dropna(subset=["Age"]).copy()

    age_df["AgeGroup"] = pd.cut(
        age_df["Age"],
        bins=[0, 12, 18, 35, 60, 100],
        labels=["Child", "Teenager", "Young Adult", "Adult", "Senior"],
        include_lowest=True
    )

    age_survival = (
        age_df.groupby("AgeGroup", observed=False)["Survived"].mean() * 100
    )

    fig4, ax4 = plt.subplots()
    age_survival.plot(kind="bar", ax=ax4)
    ax4.set_xlabel("Age Group")
    ax4.set_ylabel("Survival Rate (%)")
    ax4.set_title("Survival Rate by Age Group")
    ax4.tick_params(axis="x", rotation=0)
    fig4.tight_layout()
    st.pyplot(fig4)
    plt.close(fig4)

    # Filtered data table
    with st.expander("View Passenger Data"):
        st.dataframe(filtered_df, use_container_width=True)

else:
    st.warning("No passengers match the selected filters.")

# Footer
st.divider()
st.caption("CodSoft Internship | Task 3: Data Visualization Dashboard")