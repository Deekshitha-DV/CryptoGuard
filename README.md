# 🛡️ CryptoGuard

### AI-Based Blockchain Transaction Risk & Anomaly Detection System

> **Turning blockchain transaction data into explainable investigation signals.**

CryptoGuard is a machine-learning and blockchain analytics project designed to identify **potentially high-risk cryptocurrency transactions** by combining supervised machine learning, anomaly detection, and transaction-network analysis.

Rather than treating a transaction as simply *“licit”* or *“illicit”*, CryptoGuard produces an **investigation-oriented risk signal** that helps an analyst understand which transactions may deserve further examination.

---

## 🔎 Why CryptoGuard?

Blockchain transactions are transparent, but transparency does not automatically make transaction activity easy to investigate.

Large transaction datasets can contain:

* highly imbalanced classes
* unusual transaction behaviour
* complex transaction relationships
* hidden patterns across multiple features
* large volumes of transactions requiring prioritisation

CryptoGuard explores how machine learning and graph-based analytics can be combined to reduce this complexity.

### The core idea

```text
Blockchain Transaction Data
          ↓
Data Understanding & Cleaning
          ↓
Feature Engineering
          ↓
Machine Learning
          ↓
Anomaly Detection
          ↓
Blockchain Network Analysis
          ↓
Risk & Investigation Scoring
          ↓
Explainable Results
          ↓
Interactive Streamlit Dashboard
```

---

## 🎯 Project Objective

The objective of CryptoGuard is to build an analytical system that can:

1. Analyse cryptocurrency transaction behaviour.
2. Detect patterns associated with potentially illicit transactions.
3. Identify unusual transactions that differ from learned normal patterns.
4. Incorporate transaction-network activity into investigation prioritisation.
5. Provide model-based explanations for individual predictions.
6. Present the results through an interactive dashboard.

CryptoGuard is an **academic and analytical project** and is not intended to determine criminality or replace professional AML/compliance investigation.

---

## 🧠 What Makes CryptoGuard Different?

CryptoGuard combines three complementary analytical signals:

### 1. 🤖 Supervised Machine Learning

The labelled portion of the dataset is used to train classification models capable of distinguishing between the available labelled transaction classes.

Models explored:

* Logistic Regression
* Random Forest
* XGBoost

XGBoost is used as the primary predictive model for the downstream risk-analysis pipeline.

### 2. 🚨 Anomaly Detection

An **Isolation Forest** is applied to transactions without known class labels.

This allows CryptoGuard to investigate transactions that may exhibit unusual patterns even when a confirmed label is unavailable.

> An anomaly is **not automatically an illicit transaction**.

### 3. 🕸️ Blockchain Network Analysis

Transactions are represented as a directed graph using NetworkX.

CryptoGuard analyses:

* In-degree
* Out-degree
* Total degree
* Network activity

This provides additional context about how a transaction participates in the transaction network.

---

# 📊 Dataset

CryptoGuard uses the **Elliptic++** cryptocurrency transaction dataset.

The dataset contains transaction features, transaction relationships, and class information.

### Dataset dimensions used in the project

| Component                  | Records |
| -------------------------- | ------: |
| Transaction features       | 203,769 |
| Class records              | 203,769 |
| Transaction relationships  | 234,355 |
| Labelled transactions      |  46,564 |
| Unknown-class transactions | 157,205 |

The labelled data contains two known classes, while the large unknown-class population is retained for anomaly and risk investigation.

### Class distribution

| Class               | Transactions |  Share |
| ------------------- | -----------: | -----: |
| Potentially illicit |        4,545 |  2.23% |
| Licit               |       42,019 | 20.62% |
| Unknown             |      157,205 | 77.15% |

The strong class imbalance is an important consideration when evaluating the classification models.

---

# 🧪 Machine Learning Pipeline

CryptoGuard uses a chronological train/test strategy rather than randomly shuffling transactions.

```text
Labelled Transactions
        │
        ├── Time Steps 1–40
        │       ↓
        │    Training
        │
        └── Time Steps 41–49
                ↓
              Testing
```

This approach provides a more realistic experiment by evaluating the model on a later time period.

### Preprocessing

The pipeline includes:

* transaction ID separation
* class filtering
* feature selection
* missing-value analysis
* training-set median imputation
* validation of infinite values
* constant-feature checks
* chronological train/test splitting

---

# 📈 Model Performance

The following results were obtained on the chronological test set.

| Model               | Accuracy | Precision | Recall |     F1 | ROC-AUC | PR-AUC |
| ------------------- | -------: | --------: | -----: | -----: | ------: | -----: |
| Logistic Regression |   0.8176 |    0.1886 | 0.7481 | 0.3012 |  0.8898 | 0.4331 |
| Random Forest       |   0.9762 |    0.9527 | 0.5763 | 0.7182 |  0.9578 | 0.7494 |
| XGBoost             |   0.9706 |    0.7516 | 0.6584 | 0.7019 |  0.9620 | 0.7848 |

Because the dataset is highly imbalanced, **PR-AUC, recall, precision and F1** are considered alongside accuracy rather than relying on accuracy alone.

XGBoost is used as the primary model in the downstream CryptoGuard risk-analysis pipeline.

---

# 🔬 Explainable AI

A risk score is more useful when an analyst can investigate **why** the model produced it.

CryptoGuard uses **SHAP (SHapley Additive exPlanations)** to examine individual model predictions.

For example, for an analysed transaction:

```text
Transaction ID
12661353

Predicted risk probability
≈ 99.74%
```

The SHAP analysis identifies which features contributed most strongly toward or away from the model's prediction.

One important example was the `size` feature, which produced the largest positive SHAP contribution for this transaction.

Because the Elliptic++ feature names are anonymised, CryptoGuard deliberately avoids assigning unsupported real-world meanings to individual `Local_feature_*` or `Aggregate_feature_*` variables.

### Why this matters

```text
Model Prediction
      ↓
"What happened?"
      ↓
SHAP Explanation
      ↓
"Which features influenced this prediction?"
```

This makes the system more suitable for **analytical investigation and model interpretation**.

---

# 🚨 Anomaly Detection

The unknown-class transactions are analysed separately using Isolation Forest.

CryptoGuard calculates an anomaly signal and identifies transactions located toward the extreme end of the anomaly-score distribution.

An initial operational threshold was selected at the **99th percentile** of the anomaly-score distribution.

This produced:

**1,573 high-anomaly transactions**

The threshold is a project-defined analytical choice and should not be interpreted as proof of illicit behaviour.

---

# 🕸️ Blockchain Network Analysis

CryptoGuard converts the transaction relationship data into a directed NetworkX graph.

### Network metrics

**In-Degree**

Number of transaction relationships entering a node.

**Out-Degree**

Number of transaction relationships leaving a node.

**Total Degree**

Combined transaction connectivity.

**Network Activity Score**

A percentile-based representation of network activity.

### Important analytical observation

A highly connected transaction is **not automatically high risk**.

Network connectivity is therefore treated as an additional analytical signal rather than a standalone risk indicator.

---

# 🎯 Investigation Scoring

CryptoGuard combines multiple signals into an investigation-oriented score:

```text
Investigation Score
=
0.60 × XGBoost Risk
+
0.20 × Normalized Anomaly Signal
+
0.20 × Network Activity
```

The resulting score is used to prioritise transactions for further analytical investigation.

### Investigation categories

| Category | Purpose                       |
| -------- | ----------------------------- |
| Low      | Lower investigation priority  |
| Medium   | Requires additional review    |
| High     | Higher investigation priority |

These categories are **project-defined analytical groupings**, not calibrated probabilities or legal classifications.

---

# 🖥️ Interactive Dashboard

CryptoGuard includes a Streamlit dashboard for exploring the generated risk results.

### Dashboard capabilities

* Dataset overview
* Risk-category distribution
* Investigation-priority distribution
* Transaction search
* Individual transaction risk information
* Anomaly information
* Blockchain network activity
* Investigation score
* Transaction-level investigation data

Example investigation workflow:

```text
Search Transaction ID
        ↓
Risk Profile
        ↓
ML Risk Signal
        ↓
Anomaly Signal
        ↓
Network Activity
        ↓
Investigation Priority
```

---

# 🧰 Technology Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost

### Explainable AI

* SHAP

### Blockchain / Network Analytics

* NetworkX

### Visualization

* Matplotlib
* Seaborn
* Plotly

### Dashboard

* Streamlit

### Development

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# 📁 Project Structure

```text
CryptoGuard/
│
├── dashboard/
│   └── app.py
│
├── Data/
│   ├── raw/
│   │   └── Elliptic++ dataset files
│   │
│   └── processed/
│       ├── cryptoguard_risk_results.csv
│       ├── model_performance.csv
│       └── shap_transaction_12661353.csv
│
├── models/
│   ├── isolation_forest_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── random_forest_model.pkl
│   ├── standard_scaler.pkl
│   └── xgboost_model.pkl
│
├── notebook/
│   └── 01_data_understanding.ipynb
│
├── reports/
│
├── .gitignore
├── README.md
└── requirements.txt
```

> Large datasets and trained model binaries are intentionally excluded from version control.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Deekshitha-DV/CryptoGuard.git
cd CryptoGuard
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Dashboard

From the project root:

```powershell
streamlit run .\dashboard\app.py
```

The Streamlit application will open in your browser.

---

# 🔁 Reproducibility

The project follows a structured analytical workflow:

```text
Raw Dataset
    ↓
Data Understanding
    ↓
Preprocessing
    ↓
Chronological Split
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Anomaly Detection
    ↓
Network Analysis
    ↓
Risk Scoring
    ↓
Explainability
    ↓
Dashboard
```

The trained models and generated analytical datasets are maintained separately from the public source-code repository because of their size and reproducibility considerations.

---

# ⚠️ Limitations

CryptoGuard has several important limitations.

### Dataset limitations

The system is evaluated using the available Elliptic++ dataset and therefore should not automatically be assumed to generalise to every blockchain, exchange, wallet population, or time period.

### Class imbalance

The labelled data is strongly imbalanced, which affects the interpretation of classification metrics.

### Anomaly detection

Anomalous behaviour does not necessarily indicate illicit behaviour.

### Risk scoring

The combined investigation score uses project-defined weights and is **not a calibrated probability of illicit activity**.

### Feature interpretability

Several dataset variables are anonymised. Their statistical contribution can be analysed, but their real-world semantic meaning should not be invented.

### Operational use

CryptoGuard is an academic prototype and should not be used as an autonomous AML, law-enforcement, compliance, or criminal-risk decision system.

---

# 🚀 Future Improvements

Potential future development includes:

* model calibration
* threshold optimisation
* temporal drift monitoring
* graph-based machine learning
* advanced graph embeddings
* additional anomaly-detection algorithms
* automated model monitoring
* richer transaction-level explanations
* analyst feedback loops
* API-based deployment
* containerisation
* cloud deployment
* testing and CI/CD
* support for additional blockchain datasets

---

# 🎓 Academic & Career Relevance

CryptoGuard brings together several areas of modern data and financial technology:

```text
Data Science
     +
Machine Learning
     +
Blockchain Analytics
     +
Cybersecurity
     +
Explainable AI
     +
Network Analysis
     +
Financial Risk Investigation
```

The project demonstrates practical experience with:

* real-world data preprocessing
* imbalanced classification
* time-aware model evaluation
* ensemble machine learning
* anomaly detection
* graph analytics
* explainable AI
* interactive data applications
* reproducible project organisation

This makes CryptoGuard suitable as an **MCA academic project and portfolio project for data science, analytics, blockchain analytics, and crypto-risk roles**.

---

# 🔐 Responsible Use

CryptoGuard produces **analytical investigation signals**, not accusations.

A high-risk or anomalous transaction should be interpreted as a reason for **further investigation**, not as evidence that a person or entity committed an illegal act.

Human review, additional evidence, domain expertise, and appropriate legal/compliance procedures are required for real-world decisions.

---

# 👩‍💻 Author

**Deekshitha D V**

MCA | Data Science | Data Analytics | Blockchain & Crypto Security

Interested in:

* Data Science
* Data Analytics
* Blockchain Analytics
* Crypto Risk Analysis
* Machine Learning
* Explainable AI

### Connect

* **LinkedIn:** [Deekshitha D V](https://www.linkedin.com/in/deekshithadv/)
* **GitHub:** [Deekshitha-DV](https://github.com/Deekshitha-DV)

---

## ⭐ Project Status

**Current stage:** Functional academic prototype

The core pipeline includes data analysis, supervised machine learning, anomaly detection, blockchain network analysis, explainability, risk scoring, and an interactive Streamlit dashboard.

Further work is focused on documentation, validation, testing, reproducibility, and future deployment improvements.

---

### 📌 Disclaimer

CryptoGuard is developed for **academic, research, and educational purposes**.

It does not establish criminality, legal liability, or definitive illicit activity. Risk scores and anomaly signals should be treated as analytical indicators requiring appropriate human investigation.
