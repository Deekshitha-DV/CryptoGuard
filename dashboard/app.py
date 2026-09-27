import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CryptoGuard | Blockchain Risk Analytics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "Data"
    / "processed"
    / "cryptoguard_risk_results.csv"
)

MODEL_PERFORMANCE_PATH = (
    BASE_DIR
    / "Data"
    / "processed"
    / "model_performance.csv"
)

SHAP_PATH = (
    BASE_DIR
    / "Data"
    / "processed"
    / "shap_transaction_12661353.csv"
)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():
    risk_data = pd.read_csv(
        DATA_PATH,
        low_memory=False
    )

    model_performance = pd.read_csv(
        MODEL_PERFORMANCE_PATH
    )

    return risk_data, model_performance


@st.cache_data
def load_shap_data():
    return pd.read_csv(SHAP_PATH)


df, model_performance = load_data()
shap_data = load_shap_data()


# ============================================================
# TITLE
# ============================================================

st.title("🛡️ CryptoGuard")

st.subheader(
    "AI-Based Blockchain Transaction Risk and Anomaly Detection System"
)

st.caption(
    "A Machine Learning and Blockchain Analytics Approach "
    "for Identifying Potentially Illicit Cryptocurrency Transactions"
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🛡️ CryptoGuard")

    st.markdown(
        """
        **Project Purpose**

        CryptoGuard analyzes cryptocurrency transaction,
        anomaly, and blockchain network signals to support
        risk-based transaction investigation.
        """
    )

    st.divider()

    st.subheader("🔧 Technology Stack")

    st.markdown(
        """
        - Python
        - Pandas & NumPy
        - Scikit-learn
        - XGBoost
        - Isolation Forest
        - NetworkX
        - SHAP
        - Streamlit
        """
    )

    st.divider()

    st.subheader("🤖 Models")

    st.markdown(
        """
        **Supervised Learning**
        - Logistic Regression
        - Random Forest
        - XGBoost

        **Anomaly Detection**
        - Isolation Forest

        **Network Analysis**
        - NetworkX

        **Explainability**
        - SHAP
        """
    )

    st.divider()

    st.subheader("📊 Risk Methodology")

    st.markdown(
        """
        The investigation framework combines:

        - XGBoost risk score
        - Anomaly score
        - Blockchain network activity

        The resulting investigation score is a
        project-defined analytical score and is **not
        a calibrated probability of illicit activity**.
        """
    )

    st.divider()

    st.warning(
        """
        **Important Disclaimer**

        CryptoGuard is an academic/research prototype.
        A high-risk score does not prove criminal activity
        or illicit behavior. Results should be treated as
        investigation signals requiring further review.
        """
    )


# ============================================================
# DATASET OVERVIEW
# ============================================================

st.header("📊 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Transactions",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "High Risk",
        f"{(df['Risk_Category'] == 'High Risk').sum():,}"
    )

with col3:
    st.metric(
        "Medium Risk",
        f"{(df['Risk_Category'] == 'Medium Risk').sum():,}"
    )

with col4:
    st.metric(
        "Low Risk",
        f"{(df['Risk_Category'] == 'Low Risk').sum():,}"
    )


# ============================================================
# RISK DISTRIBUTION
# ============================================================

st.header("🚦 Risk Distribution")

risk_order = [
    "Low Risk",
    "Medium Risk",
    "High Risk"
]

risk_distribution = (
    df["Risk_Category"]
    .value_counts()
    .reindex(risk_order)
    .fillna(0)
)

st.bar_chart(risk_distribution)


# ============================================================
# INVESTIGATION PRIORITY
# ============================================================

st.header("🔎 Investigation Priority")

priority_order = [
    "Low Priority",
    "Medium Priority",
    "High Priority"
]

priority_distribution = (
    df["Investigation_Priority"]
    .value_counts()
    .reindex(priority_order)
    .fillna(0)
)

st.bar_chart(priority_distribution)


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.header("🤖 Model Performance")

st.caption(
    "Evaluation results from the chronological test set "
    "used during model development."
)

performance_display = model_performance.copy()

performance_display = performance_display.rename(
    columns={
        "F1": "F1 Score",
        "ROC_AUC": "ROC-AUC",
        "PR_AUC": "PR-AUC"
    }
)

metric_columns = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score",
    "ROC-AUC",
    "PR-AUC"
]

performance_display[metric_columns] = (
    performance_display[metric_columns] * 100
)

st.dataframe(
    performance_display.style.format(
        {
            "Accuracy": "{:.2f}%",
            "Precision": "{:.2f}%",
            "Recall": "{:.2f}%",
            "F1 Score": "{:.2f}%",
            "ROC-AUC": "{:.2f}%",
            "PR-AUC": "{:.2f}%"
        }
    ),
    width="stretch",
    hide_index=True
)

st.caption(
    "Metrics are measured on the held-out chronological test period. "
    "They should not be interpreted as guaranteed real-world performance."
)


# ============================================================
# TRANSACTION INVESTIGATION
# ============================================================

st.header("🔍 Transaction Investigation")

search_tx = st.text_input(
    "Enter Transaction ID",
    placeholder="Example: 30157957"
)

if search_tx:

    try:
        search_tx_id = int(search_tx)

        transaction = df[
            df["txId"] == search_tx_id
        ]

        # --------------------------------------------------------
        # TRANSACTION NOT FOUND
        # --------------------------------------------------------

        if len(transaction) == 0:

            if search_tx_id == 12661353:

                st.info(
                    """
                    **Transaction 12661353 is not part of the current
                    risk-investigation dataset.**

                    It is a labeled test transaction used separately
                    for the SHAP model-explainability demonstration
                    below.
                    """
                )

            else:

                st.warning(
                    f"No transaction found with txId `{search_tx_id}`."
                )

        # --------------------------------------------------------
        # TRANSACTION FOUND
        # --------------------------------------------------------

        else:

            row = transaction.iloc[0]

            # ====================================================
            # RISK ASSESSMENT
            # ====================================================

            st.subheader("🎯 Risk Assessment")

            risk_col1, risk_col2, risk_col3 = st.columns(3)

            with risk_col1:

                st.metric(
                    "Risk Category",
                    row["Risk_Category"]
                )

            with risk_col2:

                st.metric(
                    "Combined Risk Score",
                    f"{row['Combined_Risk_Score']:.4f}"
                )

            with risk_col3:

                st.metric(
                    "Investigation Priority",
                    row["Investigation_Priority"]
                )


            # ====================================================
            # ML / ANOMALY SIGNALS
            # ====================================================

            st.subheader("🤖 ML & Anomaly Signals")

            signal_col1, signal_col2, signal_col3 = st.columns(3)

            with signal_col1:

                st.metric(
                    "XGBoost Risk Score",
                    f"{row['XGB_Risk_Score']:.4f}"
                )

            with signal_col2:

                st.metric(
                    "Anomaly Score",
                    f"{row['Anomaly_Score']:.4f}"
                )

            with signal_col3:

                if row["Anomaly_Flag"] == 1:
                    anomaly_status = "Anomaly"
                else:
                    anomaly_status = "Normal"

                st.metric(
                    "Anomaly Status",
                    anomaly_status
                )


            # ====================================================
            # NETWORK ACTIVITY
            # ====================================================

            st.subheader("🌐 Blockchain Network Activity")

            network_col1, network_col2, network_col3 = st.columns(3)

            with network_col1:

                st.metric(
                    "In-Degree",
                    int(row["In_Degree"])
                )

            with network_col2:

                st.metric(
                    "Out-Degree",
                    int(row["Out_Degree"])
                )

            with network_col3:

                st.metric(
                    "Total Degree",
                    int(row["Total_Degree"])
                )

            st.metric(
                "Network Activity Score",
                f"{row['Network_Activity_Score']:.4f}"
            )


            # ====================================================
            # INVESTIGATION SCORE
            # ====================================================

            st.subheader("📌 Investigation Score")

            st.metric(
                "Investigation Score",
                f"{row['Investigation_Score']:.4f}"
            )

            st.progress(
                float(row["Investigation_Score"])
            )

            st.caption(
                "This score combines supervised ML risk, anomaly "
                "signals, and blockchain network activity."
            )


            # ====================================================
            # ANOMALY INFORMATION
            # ====================================================

            st.subheader("⚠️ Anomaly Information")

            anomaly_col1, anomaly_col2 = st.columns(2)

            with anomaly_col1:

                st.metric(
                    "Normalized Anomaly Score",
                    f"{row['Normalized_Anomaly_Score']:.4f}"
                )

            with anomaly_col2:

                st.metric(
                    "Network Degree Bin",
                    row["Network_Degree_Bin"]
                )


    except ValueError:

        st.warning(
            "Please enter a valid numeric transaction ID."
        )


# ============================================================
# SHAP MODEL EXPLAINABILITY
# ============================================================

st.header("🧠 Model Explainability")

st.subheader(
    "SHAP Explanation — Transaction 12661353"
)

st.markdown(
    """
    SHAP (SHapley Additive exPlanations) is used to understand
    which features influenced the XGBoost model's prediction
    for the selected labeled test transaction.
    """
)


# ============================================================
# TOP SHAP FEATURES
# ============================================================

shap_display = shap_data.copy()

shap_display["absolute_shap"] = (
    shap_display["shap_value"].abs()
)

top_shap = (
    shap_display
    .sort_values(
        "absolute_shap",
        ascending=False
    )
    .head(10)
    .copy()
)

st.subheader(
    "Top Features Influencing the Prediction"
)

st.dataframe(
    top_shap[
        [
            "feature",
            "shap_value",
            "feature_value"
        ]
    ].style.format(
        {
            "shap_value": "{:.4f}",
            "feature_value": "{:.6f}"
        }
    ),
    width="stretch",
    hide_index=True
)


# ============================================================
# STRONGEST CONTRIBUTION
# ============================================================

strongest_feature = top_shap.iloc[0]

st.subheader(
    "🎯 Strongest Model Contribution"
)

strong_col1, strong_col2, strong_col3 = st.columns(3)

with strong_col1:

    st.metric(
        "Feature",
        strongest_feature["feature"]
    )

with strong_col2:

    st.metric(
        "SHAP Value",
        f"{strongest_feature['shap_value']:.4f}"
    )

with strong_col3:

    st.metric(
        "Observed Value",
        f"{strongest_feature['feature_value']:.6f}"
    )

if strongest_feature["shap_value"] > 0:

    st.info(
        f"""
        The feature **{strongest_feature['feature']}** had the
        largest positive SHAP contribution among the features
        shown. Its observed value pushed the XGBoost model's
        prediction toward the positive class.
        """
    )

else:

    st.info(
        f"""
        The feature **{strongest_feature['feature']}** had the
        largest absolute SHAP contribution among the features
        shown. Its contribution pushed the model prediction
        away from the positive class.
        """
    )


# ============================================================
# POSITIVE / NEGATIVE CONTRIBUTIONS
# ============================================================

st.subheader(
    "📈 Positive and Negative Contributions"
)

positive_shap = (
    shap_display[
        shap_display["shap_value"] > 0
    ]
    .sort_values(
        "shap_value",
        ascending=False
    )
    .head(5)
)

negative_shap = (
    shap_display[
        shap_display["shap_value"] < 0
    ]
    .sort_values(
        "shap_value",
        ascending=True
    )
    .head(5)
)

positive_col, negative_col = st.columns(2)

with positive_col:

    st.markdown("**Positive Contributions**")

    st.dataframe(
        positive_shap[
            [
                "feature",
                "shap_value",
                "feature_value"
            ]
        ].style.format(
            {
                "shap_value": "{:.4f}",
                "feature_value": "{:.6f}"
            }
        ),
        width="stretch",
        hide_index=True
    )

with negative_col:

    st.markdown("**Negative Contributions**")

    st.dataframe(
        negative_shap[
            [
                "feature",
                "shap_value",
                "feature_value"
            ]
        ].style.format(
            {
                "shap_value": "{:.4f}",
                "feature_value": "{:.6f}"
            }
        ),
        width="stretch",
        hide_index=True
    )

st.caption(
    "SHAP values describe the contribution of model features "
    "to the prediction. They do not establish causation or "
    "the real-world meaning of anonymized dataset features."
)


# ============================================================
# SELECTED TRANSACTION DATA
# ============================================================

st.header("📄 Transaction Data")

if search_tx:

    try:

        searched_id = int(search_tx)

        selected_transaction = df[
            df["txId"] == searched_id
        ]

        if len(selected_transaction) > 0:

            st.dataframe(
                selected_transaction,
                width="stretch",
                hide_index=True
            )

    except ValueError:

        pass


# ============================================================
# SAMPLE RISK RESULTS
# ============================================================

st.header("📋 Sample Risk Results")

sample_columns = [
    "txId",
    "XGB_Risk_Score",
    "Anomaly_Score",
    "Combined_Risk_Score",
    "Risk_Category",
    "Total_Degree",
    "Investigation_Score",
    "Investigation_Priority"
]

st.dataframe(
    df[sample_columns].head(20),
    width="stretch",
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "CryptoGuard | MCA Mini Project | Machine Learning + "
    "Blockchain Analytics + Anomaly Detection"
)

st.caption(
    "For academic and research purposes. Risk scores are "
    "analytical indicators and should not be interpreted as "
    "proof of illicit activity."
)