# 🛡️ CryptoGuard

### AI-Based Blockchain Transaction Risk & Anomaly Detection System

**A Machine Learning and Blockchain Analytics Approach for Identifying Potentially Illicit Cryptocurrency Transactions**

CryptoGuard is an end-to-end **machine learning and blockchain analytics project** designed to identify cryptocurrency transactions that exhibit patterns associated with potentially illicit or anomalous activity.

The system combines:

* 🤖 Supervised Machine Learning
* 🔎 Anomaly Detection
* 🌐 Blockchain Network Analysis
* 🧠 Model Explainability
* 📊 Risk Scoring
* 📈 Interactive Streamlit Dashboard

> **Important:** CryptoGuard does not determine whether a transaction is criminal or definitively illicit. It produces analytical risk and investigation signals that can support further human review.

---

## 🎯 Problem Statement

Cryptocurrency transactions generate large volumes of interconnected transaction data. Identifying potentially suspicious activity manually can be difficult because:

* Blockchain transaction networks can contain millions of relationships.
* Illicit transactions may represent only a small proportion of labelled data.
* Unusual transaction behaviour may not always have a known label.
* A transaction can appear risky because of its individual characteristics, unusual behaviour, or network structure.
* Machine-learning predictions can be difficult for analysts to interpret without explainability.

### The problem

> **How can machine learning and blockchain network analytics be combined to identify potentially high-risk cryptocurrency transactions and prioritize them for further investigation?**

---

# 💡 Proposed Solution

CryptoGuard processes cryptocurrency transaction data through multiple analytical layers.

```text
Blockchain Transaction Data
          ↓
Data Understanding & Cleaning
          ↓
Feature Engineering
          ↓
Supervised Machine Learning
          ↓
Anomaly Detection
          ↓
Blockchain Network Analysis
          ↓
Risk Scoring
          ↓
Model Explainability
          ↓
Investigation Prioritization
          ↓
Streamlit Dashboard
```

The system does not rely on a single signal.

Instead, it combines:

**Transaction prediction + unusual behaviour + network activity**

to create an investigation-oriented risk score.

---

# 📌 What CryptoGuard Produces

The final system generates:

### 1. Transaction Risk Score

An XGBoost model estimates the likelihood that a labelled transaction belongs to the potentially illicit class.

### 2. Anomaly Score

Isolation Forest identifies unusual patterns among previously unknown transactions.

### 3. Network Activity Score

NetworkX analyses transaction relationships using graph-based connectivity measures.

### 4. Combined Risk Score

Multiple analytical signals are combined into an investigation-oriented score.

### 5. Risk Category

Transactions are grouped into:

* 🟢 Low Risk
* 🟡 Medium Risk
* 🔴 High Risk

### 6. Investigation Priority

Transactions can additionally be prioritized as:

* Low Priority
* Medium Priority
* High Priority

### 7. Explainable Predictions

SHAP is used to investigate which features contributed most strongly to an individual model prediction.

---

# 📊 Dataset

CryptoGuard uses the **Elliptic++ cryptocurrency transaction dataset**.

Dataset repository:

**EllipticPlusPlus — git-disl**

The dataset contains transaction features, transaction relationships, and class information.

### Dataset dimensions

| Dataset              |    Rows | Columns |
| -------------------- | ------: | ------: |
| Transaction features | 203,769 |     184 |
| Transaction classes  | 203,769 |       2 |
| Transaction edges    | 234,355 |       2 |

### Class distribution

| Class   | Meaning used in project | Transactions |
| ------- | ----------------------- | -----------: |
| Class 1 | Potentially illicit     |        4,545 |
| Class 2 | Licit                   |       42,019 |
| Class 3 | Unknown / unlabeled     |      157,205 |

The unknown class is **not treated as illicit**.

Instead, these transactions are analysed using anomaly detection, network analysis, and risk scoring.

---

# 🧹 Data Preprocessing

The dataset was examined for:

* Missing values
* Duplicate transactions
* Duplicate transaction IDs
* Infinite values
* Constant features
* Class imbalance
* Feature consistency
* Transaction ID consistency

### Results

* Duplicate transaction IDs: **0**
* Duplicate rows: **0**
* Feature/class transaction ID mismatch: **0**
* Infinite values after preprocessing: **0**
* Constant features: **0**

The dataset contained missing values in several transaction/network-related features.

Median imputation was fitted **only on the training data** and then applied to the test data to avoid information leakage.

---

# ⏱️ Time-Aware Machine Learning Evaluation

Instead of randomly shuffling transactions, CryptoGuard uses a chronological split.

```text
Time Steps 1–40  → Training
Time Steps 41–49 → Testing
```

### Training set

**36,591 transactions**

* Potentially illicit: 4,021
* Licit: 32,570

### Test set

**9,973 transactions**

* Potentially illicit: 524
* Licit: 9,449

This approach is intended to provide a more realistic evaluation of how a model trained on earlier transaction periods performs on later periods.

---

# 🤖 Machine Learning Models

Three supervised models were evaluated:

1. Logistic Regression
2. Random Forest
3. XGBoost

## Model Performance

| Model               | Accuracy | Precision | Recall |     F1 | ROC-AUC | PR-AUC |
| ------------------- | -------: | --------: | -----: | -----: | ------: | -----: |
| Logistic Regression |   0.8176 |    0.1886 | 0.7481 | 0.3012 |  0.8898 | 0.4331 |
| Random Forest       |   0.9762 |    0.9527 | 0.5763 | 0.7182 |  0.9578 | 0.7494 |
| XGBoost             |   0.9706 |    0.7516 | 0.6584 | 0.7019 |  0.9620 | 0.7848 |

Because the dataset is imbalanced, **PR-AUC, precision, recall and F1** are considered alongside accuracy.

---

# 🚀 Primary Model — XGBoost

XGBoost was selected as the primary downstream transaction-risk model.

### Test-set performance

* Accuracy: **97.06%**
* Precision: **75.16%**
* Recall: **65.84%**
* F1 Score: **70.19%**
* ROC-AUC: **96.20%**
* PR-AUC: **78.48%**

### Why PR-AUC matters

Only a relatively small portion of the labelled dataset belongs to the potentially illicit class.

Therefore, accuracy alone does not provide a complete picture of model performance.

PR-AUC provides additional information about the model's behaviour on the positive class under class imbalance.

---

# 🔎 Anomaly Detection

A major challenge is the **157,205 transactions with unknown class labels**.

These transactions cannot simply be treated as licit or illicit.

CryptoGuard therefore applies **Isolation Forest** to identify transactions with unusual patterns.

### Method

```text
Known labelled transactions
          ↓
Model training
          ↓
Isolation Forest
          ↓
Unknown transactions
          ↓
Anomaly score
          ↓
High-anomaly candidates
```

A **99th-percentile anomaly threshold** was used as an initial project-defined investigation threshold.

This identified:

**1,573 high-anomaly transactions**

The threshold is an analytical choice for investigation prioritization and should not be interpreted as proof of illicit behaviour.

---

# 🌐 Blockchain Network Analysis

Cryptocurrency transactions can also be represented as a directed graph.

```text
Transaction A
      ↓
Transaction B
      ↓
Transaction C
      ↓
Transaction D
```

CryptoGuard uses **NetworkX** to construct the transaction graph.

### Graph statistics

* Nodes: **203,769**
* Edges: **234,355**

For each transaction, the system calculates:

* In-Degree
* Out-Degree
* Total Degree
* Network Activity Score

### Important observation

High connectivity does **not automatically mean high risk**.

For example, one transaction with a total degree of **121** had an XGBoost risk score of approximately **0.0022**.

Another transaction with a total degree of **109** had an XGBoost risk score of approximately **0.9891**.

This demonstrates why network connectivity is treated as **one analytical signal rather than a standalone risk indicator**.

---

# 🧮 Investigation Score

CryptoGuard combines three analytical signals:

```text
Investigation Score =
    0.60 × XGBoost Risk
  + 0.20 × Normalized Anomaly Score
  + 0.20 × Network Activity Score
```

The score is a **project-defined analytical heuristic**.

It is not a calibrated probability and does not represent a verified AML scoring standard.

---

# 📈 Investigation Prioritization

The investigation score is used to categorize the unknown transactions.

| Category | Transactions |
| -------- | -----------: |
| Low      |      149,344 |
| Medium   |        6,288 |
| High     |        1,573 |

These thresholds are based on project-defined percentile boundaries.

They are intended to help demonstrate **how an analyst could prioritize a large transaction population for review**.

---

# 🧠 Model Explainability with SHAP

CryptoGuard uses **SHAP (SHapley Additive exPlanations)** to investigate individual XGBoost predictions.

For example:

### Transaction

`12661353`

### Actual class

Potentially illicit

### Model prediction

**99.74% predicted probability**

The SHAP analysis identified the features that contributed most strongly toward the model's prediction.

For this transaction:

| Feature                | SHAP contribution |
| ---------------------- | ----------------: |
| `size`                 |         +2.501198 |
| `Local_feature_53`     |         +0.757184 |
| `Aggregate_feature_68` |         +0.707354 |
| `Local_feature_90`     |         +0.644511 |
| `Aggregate_feature_70` |         +0.481809 |

The largest positive SHAP contribution was from:

`size`

Because the dataset contains anonymized feature names, the project does **not** assign unsupported real-world meanings to features such as `Local_feature_53`.

Feature importance and SHAP contribution indicate model behaviour; they do not establish causation.

---

# 🧪 Example Investigation

One example from the unknown transaction population is:

### Transaction ID

`30157957`

| Signal                   |         Value |
| ------------------------ | ------------: |
| XGBoost Risk Score       |      0.996910 |
| Anomaly Score            |     -0.027111 |
| Normalized Anomaly Score |      0.415177 |
| Combined Risk Score      |      0.822390 |
| In-Degree                |            43 |
| Out-Degree               |             0 |
| Total Degree             |            43 |
| Network Activity Score   |      0.999472 |
| Investigation Score      |      0.881076 |
| Risk Category            |     High Risk |
| Investigation Priority   | High Priority |

This transaction is therefore surfaced as a **high-priority analytical candidate**.

It should not be interpreted as proof that the transaction is illegal or criminal.

---

# 📊 Visual Analytics

The project is designed to communicate results visually rather than relying only on raw model output.

Planned/created project visualisations include:

### Risk Funnel

```text
Unknown Transactions
       ↓
157,205
       ↓
High-anomaly candidates
       ↓
1,573
       ↓
High-priority investigation candidates
```

### Transaction DNA

A compact visual representation of an individual transaction's:

* ML risk
* Network activity
* Investigation score
* Degree
* Risk category

### SHAP Feature Impact

A visual explanation showing which features pushed a model prediction toward or away from the potentially illicit class.

### Model Scorecard

A compact comparison of the evaluated machine-learning models using:

* Precision
* Recall
* F1
* ROC-AUC
* PR-AUC

---

# 🖥️ Streamlit Dashboard

CryptoGuard includes an interactive Streamlit dashboard for transaction investigation.

The dashboard provides:

### Dataset Overview

* Total transactions
* Labelled transactions
* Unknown transactions
* Network statistics

### Risk Distribution

* Low Risk
* Medium Risk
* High Risk

### Investigation Priority

* Low Priority
* Medium Priority
* High Priority

### Transaction Investigation

Users can search for a transaction ID and inspect its available analytical signals.

### Transaction Data

The dashboard exposes the underlying risk-analysis results for further inspection.

---

## 📷 Dashboard Preview

Add the dashboard screenshot here:

```text
reports/figures/dashboard.png
```

Example Markdown:

```markdown
![CryptoGuard Dashboard](reports/figures/dashboard.png)
```

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │ Elliptic++ Dataset  │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Data Preprocessing  │
                    └──────────┬──────────┘
                               ↓
              ┌────────────────┴────────────────┐
              ↓                                 ↓
     ┌──────────────────┐             ┌──────────────────┐
     │ Supervised ML    │             │ Anomaly Detection│
     │ XGBoost          │             │ Isolation Forest │
     └────────┬─────────┘             └────────┬─────────┘
              │                                │
              └────────────────┬───────────────┘
                               ↓
                    ┌─────────────────────┐
                    │ NetworkX Analysis   │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Investigation Score │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ SHAP Explainability │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Streamlit Dashboard │
                    └─────────────────────┘
```

---

# 🛠️ Technology Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost

### Anomaly Detection

* Isolation Forest

### Blockchain Network Analysis

* NetworkX

### Explainable AI

* SHAP

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
│   │   ├── txs_features.txt
│   │   ├── txs_classes.txt
│   │   └── txs_edgelist.txt
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
│   └── figures/
│
├── .gitignore
├── README.md
└── requirements.txt
```

> Large raw datasets and trained model files are excluded from the Git repository through `.gitignore`.

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

# ▶️ Running the Dashboard

From the project root:

```bash
streamlit run .\dashboard\app.py
```

The Streamlit dashboard will open in your browser.

---

# 📓 Notebook

The main analysis notebook is:

```text
notebook/01_data_understanding.ipynb
```

It contains the project's data exploration, preprocessing, modelling and analytical workflow.

---

# 🔐 Responsible Use

CryptoGuard is an **academic and analytical prototype**.

A high-risk score does not prove:

* Criminal activity
* Money laundering
* Fraud
* Illicit ownership
* Intentional wrongdoing

The system should be used to **prioritize transactions for human investigation**, not to automatically make legal or financial decisions.

Any real-world deployment would require additional validation, domain expertise, regulatory controls, monitoring, and human review.

---

# ⚠️ Limitations

The current project has several limitations:

1. The dataset contains anonymized features.
2. Unknown transactions do not have confirmed ground-truth labels.
3. Investigation-score weights are project-defined heuristics.
4. The model has been evaluated on a specific dataset rather than live blockchain data.
5. Model performance may change when applied to other cryptocurrency networks or time periods.
6. Anomaly detection identifies unusual behaviour, not confirmed illicit behaviour.
7. Network connectivity alone is not sufficient to establish transaction risk.
8. The current dashboard is a research/academic prototype rather than a production AML platform.

---

# 🚀 Future Improvements

Potential future development includes:

* Real-time blockchain transaction ingestion
* Streaming transaction analysis
* More advanced graph neural networks
* Temporal graph analysis
* Graph embeddings
* Advanced anomaly detection
* Model calibration
* Threshold optimization
* SHAP-based dashboard explanations
* Automated investigation reports
* Alert management
* Transaction relationship visualization
* Cross-network blockchain analytics
* Production API deployment
* Model monitoring and drift detection

---

# 🎓 Academic & Career Relevance

CryptoGuard combines several areas of my MCA specialization:

**Data Analysis**

→ Exploratory data analysis, feature analysis and visualization

**Data Science**

→ Machine learning, evaluation and risk modelling

**Machine Learning with Python**

→ Logistic Regression, Random Forest, XGBoost and Isolation Forest

**Crypto Security**

→ Transaction risk analysis and suspicious-pattern investigation

**Blockchain Analysis**

→ Transaction graph construction and network analytics

This project demonstrates how **data science and blockchain analytics can be combined into a practical investigation-oriented system**.

---

# ⭐ Key Takeaways

CryptoGuard demonstrates an end-to-end approach to cryptocurrency transaction analysis:

```text
203,769
Transactions analysed
        ↓
46,564
Labelled transactions
        ↓
XGBoost
97.06% Accuracy
78.48% PR-AUC
        ↓
157,205
Unknown transactions analysed
        ↓
1,573
High-anomaly / high-priority candidates
        ↓
NetworkX
203,769 nodes
234,355 edges
        ↓
SHAP
Explainable model predictions
        ↓
Streamlit
Interactive investigation dashboard
```

The central idea is simple:

> **Use multiple analytical signals to help investigators identify which cryptocurrency transactions deserve closer examination.**

---

# 👩‍💻 Author

**Deekshitha D V**

MCA Student | Data Science | Machine Learning | Blockchain Analytics | Crypto Security

GitHub:
https://github.com/Deekshitha-DV

LinkedIn:
https://www.linkedin.com/in/deekshithadv/

---

# 📄 Disclaimer

CryptoGuard is developed for **academic, research and educational purposes**.

The risk scores, anomaly scores and investigation priorities generated by this project are analytical outputs and should not be interpreted as definitive evidence of criminal or illicit activity.

Any real-world financial-crime or AML application would require appropriate validation, regulatory compliance, domain expertise and human oversight.
