<<<<<<< HEAD
# 🛡️ CryptoGuard
=======
# CryptoGuard
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

## AI-Based Blockchain Transaction Risk and Anomaly Detection System

**CryptoGuard** is a machine learning and blockchain analytics project designed to identify cryptocurrency transactions that may require further investigation.

The system combines **supervised machine learning, anomaly detection, blockchain network analysis, explainable AI (SHAP), and an interactive Streamlit dashboard** to generate transaction-level risk and investigation signals.

> **Important:** CryptoGuard identifies potentially high-risk or unusual transaction patterns. A high-risk score does **not** prove criminality, illicit activity, or wrongdoing. The results are intended as analytical signals that may support further investigation.

---

<<<<<<< HEAD
## 🎯 Project Objective
=======
## Project Overview
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

Cryptocurrency transaction networks can contain large volumes of transactions, making manual identification of unusual or potentially illicit patterns difficult.

<<<<<<< HEAD
* Analyze cryptocurrency transaction data
* Detect potentially illicit transaction patterns
* Handle highly imbalanced transaction classes
* Identify unusual transactions using anomaly detection
* Analyze transaction connectivity using graph-based features
* Combine multiple risk signals into an investigation-priority score
* Explain machine-learning predictions using SHAP
* Present analytical results through an interactive Streamlit dashboard

---

## 🧠 Methodology
=======
CryptoGuard addresses this problem by combining multiple analytical signals:
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

```text
Blockchain Transaction Data
          ↓
Data Preprocessing
          ↓
Feature Engineering
          ↓
Supervised Machine Learning
          ↓
Anomaly Detection
          ↓
Blockchain Network Analysis
          ↓
Risk & Investigation Scoring
          ↓
SHAP Explainability
          ↓
Interactive Streamlit Dashboard
```

<<<<<<< HEAD
---

## 📊 Dataset

CryptoGuard uses the **Elliptic++ cryptocurrency transaction dataset**, containing transaction features, class labels, and transaction relationships.

The dataset contains three class categories:

| Class | Description | Records |
| ----- | ----------- | ------: |
| 1     | Illicit     |   4,545 |
| 2     | Licit       |  42,019 |
| 3     | Unknown     | 157,205 |

For supervised learning, Classes 1 and 2 were used because they contain known labels.

Class 3 was kept separately for **anomaly detection and investigation-oriented analysis**.

The raw dataset is intentionally **not included in this repository** because of its large size.

---

## 🔍 Data Analysis
=======
The system is designed as a **research and analytical prototype** for exploring how machine learning and blockchain graph analytics can be combined for transaction-risk investigation.

---

## Key Features
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

* Cryptocurrency transaction classification using machine learning
* Chronological train/test splitting to reduce temporal leakage
* Logistic Regression, Random Forest and XGBoost comparison
* XGBoost-based transaction risk scoring
* Isolation Forest-based anomaly detection
* Blockchain transaction network analysis using NetworkX
* Transaction-level investigation scoring
* Risk categorization into Low, Medium and High Risk
* SHAP-based model explainability
* Interactive Streamlit dashboard
* Transaction search and investigation interface
* Model performance comparison
* Network activity analysis using transaction graph connections

---

## Dataset

CryptoGuard uses the **Elliptic++ cryptocurrency transaction dataset**.

The dataset contains:

* Transaction features
* Transaction classes
* Transaction relationships/edges
* Temporal information
* Local and aggregate transaction features
* Transaction and network-level attributes

### Dataset characteristics used in this project

| Dataset Component          | Records |
| -------------------------- | ------: |
| Transaction features       | 203,769 |
| Transaction classes        | 203,769 |
| Transaction edges          | 234,355 |
| Labeled transactions       |  46,564 |
| Unknown-class transactions | 157,205 |

The original raw dataset is **not included in this repository** because of its large size. It is excluded through `.gitignore`.

---

## Class Distribution

The dataset contains three classes:

| Class   | Meaning |   Count | Percentage |
| ------- | ------- | ------: | ---------: |
| Class 1 | Illicit |   4,545 |      2.23% |
| Class 2 | Licit   |  42,019 |     20.62% |
| Class 3 | Unknown | 157,205 |     77.15% |

For supervised binary classification, Classes 1 and 2 were used.

The **unknown class** was kept separate and used for anomaly detection and transaction-risk investigation.

---

## Machine Learning Approach

### 1. Data preprocessing

The preprocessing pipeline includes:

* Transaction ID validation
* Duplicate checking
* Missing-value analysis
* Median imputation
* Feature validation
* Infinite-value checking
* Constant-feature checking
* Chronological train/test splitting

The train/test split was based on the dataset's time-step information rather than random shuffling.

### 2. Supervised classification

<<<<<<< HEAD
The labeled subset contains **46,564 transactions**.

---

## 🤖 Machine Learning

Three supervised machine-learning models were evaluated:
=======
Three classification models were evaluated:
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

* Logistic Regression
* Random Forest
* XGBoost

The primary downstream risk-scoring model is **XGBoost**.

### 3. Anomaly detection

An **Isolation Forest** was trained to identify unusual patterns among transactions belonging to the unknown class.

The anomaly signal is treated as an investigation indicator rather than evidence of illicit behavior.

### 4. Blockchain network analysis

The transaction relationships were represented as a directed graph using **NetworkX**.

<<<<<<< HEAD
XGBoost was selected as the primary supervised model for the downstream risk-scoring pipeline.

---

## 🚨 Anomaly Detection

CryptoGuard uses **Isolation Forest** to identify unusual transactions among the previously unknown transactions.

The anomaly-detection stage provides an additional signal independent of the supervised classification model.

An initial **99th-percentile anomaly threshold** was used to identify transactions requiring additional investigation.

This threshold is a project-defined analytical threshold and **does not represent a legal or regulatory definition of illicit activity**.

---

## 🕸️ Blockchain Network Analysis

Transaction relationships were represented using a directed graph with **NetworkX**.

The graph contains:

* **203,769 nodes**
* **234,355 edges**

Network features include:
=======
Network-level signals include:
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

* In-degree
* Out-degree
* Total degree
* Network activity score

These signals help provide additional context around transaction connectivity.

### 5. Risk and investigation scoring

CryptoGuard combines multiple signals to prioritize transactions for investigation.

<<<<<<< HEAD
## 📈 Risk & Investigation Scoring

CryptoGuard combines multiple analytical signals:

```text
Supervised ML Risk
        +
Anomaly Detection
        +
Network Activity
        ↓
Investigation Score
```

The investigation score is a **project-defined heuristic** designed to prioritize transactions for further analysis.

It is **not a calibrated probability of illicit activity** and should not be interpreted as proof of criminal behavior.

---

## 💡 Explainable AI

CryptoGuard uses **SHAP (SHapley Additive exPlanations)** to examine which features contributed to individual model predictions.

Example analysis included:

* Global feature contribution analysis
* Individual transaction explanations
* SHAP-based feature importance
* Investigation of true-positive predictions

Because the dataset contains anonymized feature names such as `Local_feature_3` and `Aggregate_feature_70`, the project does not assign unsupported real-world meanings to these features.

Feature importance indicates model behavior; it does **not establish causation**.

---

## 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit dashboard designed to support transaction investigation.

Planned dashboard components include:

* Risk overview
* Transaction search
* ML risk score
* Anomaly score
=======
The project uses defined analytical scoring formulas combining:

* XGBoost risk
* Anomaly signal
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833
* Network activity

These scores are **project-defined analytical heuristics and are not calibrated probabilities or validated AML risk models**.

---

## Model Performance

The models were evaluated using a chronological test set.

| Model               | Accuracy | Precision | Recall |     F1 | ROC-AUC |     PR-AUC |
| ------------------- | -------: | --------: | -----: | -----: | ------: | ---------: |
| Logistic Regression |   81.76% |    18.86% | 74.81% | 30.12% |  0.8898 |     0.4331 |
| Random Forest       |   97.62% |    95.27% | 57.63% | 71.82% |  0.9578 |     0.7494 |
| XGBoost             |   97.06% |    75.16% | 65.84% | 70.19% |  0.9620 | **0.7848** |

Because the positive class is imbalanced, metrics such as **precision, recall, F1 and PR-AUC** are important alongside accuracy.

XGBoost was selected as the primary model for the downstream risk-scoring pipeline.

---

## Explainable AI

CryptoGuard uses **SHAP (SHapley Additive exPlanations)** to investigate why the XGBoost model produced a particular prediction.

For example, transaction `12661353` was analyzed using SHAP.

The largest positive contribution in the saved explanation was:

```text
Feature: size
SHAP value: 2.501198
Feature value: 192
```

This means that, for this specific transaction, the observed `size` value pushed the model prediction toward the positive class more strongly than the other features shown in the explanation.

The dataset contains anonymized feature names such as:

```text
Local_feature_53
Local_feature_90
Aggregate_feature_68
Aggregate_feature_70
```

Their real-world meanings are not inferred from their names.

---

## Risk Investigation

The unknown-class transactions were analyzed using multiple signals.

The final investigation dataset contains:

```text
157,205 transactions
14 analytical columns
0 missing values
```

Current investigation categories:

| Category    | Transactions |
| ----------- | -----------: |
| Low Risk    |      149,344 |
| Medium Risk |        6,288 |
| High Risk   |        1,573 |

These categories are **project-defined investigation bands based on score thresholds**. They should not be interpreted as probabilities or confirmed classifications.

---

## Streamlit Dashboard

CryptoGuard includes an interactive Streamlit dashboard for transaction investigation.

The dashboard provides:

* Dataset overview
* Risk distribution
* Investigation priority distribution
* Transaction search
* Transaction-level risk information
* Network activity information
* Investigation score
* Model performance information
* Model explainability information

Example investigation fields include:

```text
Transaction ID
XGBoost Risk Score
Anomaly Score
Network Activity Score
Investigation Score
Risk Category
Investigation Priority
In-Degree
Out-Degree
Total Degree
```

---

<<<<<<< HEAD
## 🛠️ Technology Stack
=======
## Technology Stack
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

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

<<<<<<< HEAD
## 📁 Project Structure
=======
## Project Structure
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

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
│   ├── logistic_regression_model.pkl
│   ├── random_forest_model.pkl
│   ├── xgboost_model.pkl
│   ├── isolation_forest_model.pkl
│   └── standard_scaler.pkl
│
├── notebook/
│   └── 01_data_understanding.ipynb
│
├── reports/
│
├── .gitignore
├── requirements.txt
└── README.md
```

Large datasets, processed data files, trained model artifacts and local environments are excluded from version control through `.gitignore`.

---

<<<<<<< HEAD
## ⚙️ Installation
=======
## Installation
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

Clone the repository and create a virtual environment:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd CryptoGuard

python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Dashboard

After preparing the required local data and model artifacts:

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser.

---

<<<<<<< HEAD
## ⚠️ Limitations
=======
## Reproducibility
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

The project uses a chronological train/test split and training-only preprocessing for the supervised model pipeline.

The project also stores generated artifacts locally, while large and generated files are excluded from GitHub using `.gitignore`.

To reproduce the complete analysis, the required Elliptic++ dataset must be obtained separately and placed in the expected local data directory.

---

## Limitations

CryptoGuard is a **research and academic prototype**, not a production AML/compliance system.

Important limitations include:

1. The risk scores are project-defined analytical scores.
2. They are not calibrated probabilities.
3. High-risk transactions are not automatically illicit.
4. Anomaly detection identifies unusual patterns, not criminal activity.
5. Network connectivity alone does not establish transaction risk.
6. The dataset contains anonymized features whose meanings should not be inferred without documentation.
7. The model has been evaluated on the available dataset and should be independently validated before real-world deployment.
8. Real financial investigations require additional contextual, regulatory and human-review information.
9. Production deployment would require monitoring for data drift, model drift, threshold changes and false positives.

---

<<<<<<< HEAD
## 🚀 Future Improvements
=======
## Future Improvements
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

Potential future development includes:

* Real-time blockchain transaction ingestion
* Additional blockchain graph features
* Temporal graph analysis
* Advanced graph neural networks
* Calibrated risk probabilities
* Model drift monitoring
* Automated investigation reports
* SHAP-based dashboard explanations
* Real-time alerting
* Multi-chain transaction analysis
* Integration with blockchain explorer APIs
* Analyst feedback loops for model improvement

---

<<<<<<< HEAD
## 🎓 Academic Context
=======
## Academic / Career Relevance
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

CryptoGuard combines several areas of the MCA specialization:

* Data Analysis
* Data Science
* Machine Learning with Python
* Blockchain Analytics
* Crypto Security
* Network Analysis
* Explainable AI

The project demonstrates an end-to-end workflow from **raw blockchain transaction data to machine-learning-based investigation signals and an interactive analytical dashboard**.

It is intended to demonstrate practical skills relevant to roles such as:

* Data Analyst
* Data Science Analyst
* Junior Data Scientist
* Blockchain Analyst
* Crypto Research Analyst
* Blockchain Risk Analyst
* AML / Transaction Monitoring Analyst

---

<<<<<<< HEAD
## 📌 Disclaimer
=======
## Disclaimer
>>>>>>> 301260053cc9b9f952a79dcc290d93abe348e833

CryptoGuard is developed for **academic, research and educational purposes**.

The system's predictions and scores should be treated as analytical signals for further investigation and **not as proof of criminality, illicit behavior or wrongdoing**.

---

## Author

**Deekshitha D V**

MCA | Data Science | Blockchain Analytics | Machine Learning

GitHub: **Deekshitha-DV**

LinkedIn: **Deekshitha D V**
