# 🛡️ CryptoGuard

## AI-Based Blockchain Transaction Risk & Anomaly Detection System

**CryptoGuard** is a machine-learning and blockchain analytics system designed to identify **potentially high-risk cryptocurrency transactions** and prioritize them for further investigation.

The project combines:

* 🤖 Supervised Machine Learning
* 🚨 Anomaly Detection
* 🕸️ Blockchain Transaction-Network Analysis
* 🧠 Explainable AI
* 📊 Risk Scoring
* 🖥️ Interactive Data Visualization

> **CryptoGuard does not determine criminality. It produces analytical signals that can help prioritize transactions for human investigation.**

---

# 🎯 Problem Statement

Cryptocurrency transactions generate large volumes of interconnected blockchain data. Manually examining this activity is difficult because transaction behaviour can be complex, highly imbalanced, and distributed across transaction networks.

Traditional transaction-level analysis may also miss unusual behaviour when a transaction does not have a known label.

### The problem addressed by CryptoGuard is:

> **How can machine learning, anomaly detection, and blockchain network analysis be combined to identify potentially high-risk cryptocurrency transactions and prioritize them for further investigation?**

CryptoGuard addresses this by combining predictive modelling with unsupervised anomaly detection and transaction-network activity.

---

# 💡 Proposed Solution

CryptoGuard follows a multi-signal analytical approach.

```text
                BLOCKCHAIN TRANSACTION DATA
                           │
                           ▼
                Data Understanding
                           │
                           ▼
                  Data Preprocessing
                           │
                           ▼
                  Feature Engineering
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
     Supervised ML                 Anomaly Detection
     XGBoost / RF / LR              Isolation Forest
             │                           │
             └─────────────┬─────────────┘
                           ▼
                 Blockchain Network
                      Analysis
                           │
                           ▼
                  Risk & Investigation
                       Scoring
                           │
                           ▼
                   Explainable AI
                        SHAP
                           │
                           ▼
                Streamlit Dashboard
                           │
                           ▼
                 Analyst Investigation
```

---

# 🔎 What CryptoGuard Produces

For an analysed transaction, the system can generate:

| Output                     | Purpose                                                         |
| -------------------------- | --------------------------------------------------------------- |
| **XGBoost Risk Score**     | Model-based risk signal                                         |
| **Anomaly Score**          | Measures unusual transaction behaviour                          |
| **Anomaly Flag**           | Identifies transactions crossing the selected anomaly threshold |
| **Combined Risk Score**    | Combines predictive and anomaly signals                         |
| **Risk Category**          | Low / Medium / High                                             |
| **In-Degree**              | Incoming transaction relationships                              |
| **Out-Degree**             | Outgoing transaction relationships                              |
| **Total Degree**           | Overall transaction connectivity                                |
| **Network Activity Score** | Relative network activity                                       |
| **Investigation Score**    | Combined investigation-prioritisation signal                    |
| **Investigation Priority** | Low / Medium / High priority                                    |

These outputs are intended to **support investigation prioritisation**, not replace human judgement.

---

# 📊 Dataset

CryptoGuard uses the **Elliptic++ cryptocurrency transaction dataset**.

The project works with three main components:

* Transaction features
* Transaction class information
* Transaction relationships / edges

### Dataset overview

| Dataset component          | Records |
| -------------------------- | ------: |
| Transaction features       | 203,769 |
| Class records              | 203,769 |
| Transaction relationships  | 234,355 |
| Labelled transactions      |  46,564 |
| Unknown-class transactions | 157,205 |

### Class distribution

| Class               | Transactions | Percentage |
| ------------------- | -----------: | ---------: |
| Potentially illicit |        4,545 |      2.23% |
| Licit               |       42,019 |     20.62% |
| Unknown             |      157,205 |     77.15% |

The large unknown-class population is not used as labelled ground truth. Instead, it is analysed using anomaly detection, machine-learning risk signals, and network activity.

---

# 🧹 Data Preprocessing

The preprocessing pipeline includes:

* Dataset loading
* Transaction-ID consistency validation
* Duplicate detection
* Missing-value analysis
* Feature-group identification
* Class filtering
* Infinite-value validation
* Constant-feature checks
* Median imputation
* Chronological train/test splitting

### Missing-value handling

Missing values were concentrated in 17 transaction/network-related fields.

Median imputation was fitted **only on the training data** and then applied to the test data to avoid information leakage.

---

# ⏳ Time-Aware Model Evaluation

Instead of randomly shuffling the labelled transactions, CryptoGuard uses a chronological split.

```text
Time Steps 1–40
       │
       ▼
    TRAINING
    36,591
       │
       │
       ▼
Time Steps 41–49
       │
       ▼
     TESTING
      9,973
```

This allows the model to be evaluated on a later time period rather than simply mixing earlier and later observations.

The data also exhibits a change in class proportions between the training and test periods, making time-aware evaluation particularly relevant.

---

# 🤖 Machine Learning Models

Three supervised classification models were evaluated:

### Logistic Regression

A linear baseline model used to establish a reference point.

### Random Forest

An ensemble tree-based model capable of capturing nonlinear relationships.

### XGBoost

A gradient-boosted decision-tree model used as the primary predictive model for the downstream CryptoGuard risk-analysis pipeline.

---

# 📈 Model Performance

The following results were obtained on the chronological test set.

| Model               | Accuracy | Precision | Recall |     F1 | ROC-AUC | PR-AUC |
| ------------------- | -------: | --------: | -----: | -----: | ------: | -----: |
| Logistic Regression |   0.8176 |    0.1886 | 0.7481 | 0.3012 |  0.8898 | 0.4331 |
| Random Forest       |   0.9762 |    0.9527 | 0.5763 | 0.7182 |  0.9578 | 0.7494 |
| XGBoost             |   0.9706 |    0.7516 | 0.6584 | 0.7019 |  0.9620 | 0.7848 |

Because the labelled dataset is highly imbalanced, accuracy alone is not sufficient for interpreting model performance. Precision, recall, F1, ROC-AUC and particularly PR-AUC are considered together.

### XGBoost test-set results

```text
Accuracy       97.06%
Precision      75.16%
Recall         65.84%
F1 Score       70.19%
ROC-AUC        96.20%
PR-AUC         78.48%
```

XGBoost is subsequently used as the primary predictive model in the risk-analysis pipeline.

---

# 🚨 Anomaly Detection

A large portion of the dataset has an unknown class.

Instead of ignoring these transactions, CryptoGuard analyses them using **Isolation Forest**.

### Why?

A transaction can be unusual even when there is no confirmed label available.

The anomaly-detection pipeline:

```text
Unknown Transactions
        ↓
Isolation Forest
        ↓
Anomaly Score
        ↓
Percentile Analysis
        ↓
High-Anomaly Transactions
```

An initial operational threshold was selected at the **99th percentile** of the anomaly-score distribution.

This identified:

### **1,573 high-anomaly transactions**

This threshold is a project-defined analytical choice and does **not** mean that these transactions are illicit.

---

# 🕸️ Blockchain Network Analysis

CryptoGuard represents transaction relationships as a directed graph using **NetworkX**.

### Network metrics

**In-Degree**

Number of transaction relationships entering a transaction/node.

**Out-Degree**

Number of transaction relationships leaving a transaction/node.

**Total Degree**

Combined incoming and outgoing connectivity.

**Network Activity Score**

A percentile-based representation of network activity.

### Network statistics

| Metric               |  Result |
| -------------------- | ------: |
| Graph nodes          | 203,769 |
| Graph edges          | 234,355 |
| Maximum in-degree    |     212 |
| Maximum out-degree   |     122 |
| Maximum total degree |     212 |

### Important observation

Network connectivity is **not treated as a standalone risk indicator**.

A highly connected transaction can have a low machine-learning risk signal, while another highly connected transaction can have a high risk signal.

Therefore, network activity is used as **additional context** rather than proof of suspicious activity.

---

# 🎯 Investigation Scoring

CryptoGuard combines three analytical signals into an investigation score:

```text
Investigation Score
=
0.60 × XGBoost Risk Score
+
0.20 × Normalized Anomaly Score
+
0.20 × Network Activity Score
```

The weights are **project-defined heuristic values** and have not been presented as validated AML/compliance weights.

### Investigation priorities

The resulting scores are grouped into:

```text
LOW PRIORITY
      ↓
MEDIUM PRIORITY
      ↓
HIGH PRIORITY
```

The project uses percentile-based thresholds to create these investigation categories.

For the generated unknown-transaction risk dataset:

| Priority / Risk Category | Transactions |
| ------------------------ | -----------: |
| Low                      |      149,344 |
| Medium                   |        6,288 |
| High                     |        1,573 |

These categories are intended for **analytical prioritisation**, not probability estimates or legal classifications.

---

# 🔍 Example Transaction Investigation

One of the transactions investigated through the Streamlit dashboard was:

## Transaction `30157957`

| Signal                   |            Result |
| ------------------------ | ----------------: |
| XGBoost Risk Score       |        **0.9969** |
| Anomaly Score            |       **-0.0271** |
| Normalized Anomaly Score |        **0.4152** |
| Combined Risk Score      |        **0.8224** |
| Risk Category            |     **High Risk** |
| In-Degree                |            **43** |
| Out-Degree               |             **0** |
| Total Degree             |            **43** |
| Network Activity Score   |        **0.9995** |
| Investigation Score      |        **0.8811** |
| Investigation Priority   | **High Priority** |

### Interpretation

The transaction received a high investigation score because multiple analytical signals contributed to the result:

```text
High XGBoost Risk
        +
High Network Activity
        +
Anomaly Signal
        ↓
High Investigation Score
        ↓
High Investigation Priority
```

This means the transaction is **prioritised for further investigation**.

It does not establish that the transaction is criminal or illicit.

---

# 🧠 Explainable AI with SHAP

CryptoGuard uses **SHAP** to understand individual XGBoost predictions.

For an analysed labelled transaction:

```text
Transaction ID: 12661353

Predicted probability:
≈ 99.74%
```

SHAP identifies the features that contributed toward or away from the model prediction.

### Example

For transaction `12661353`, the `size` feature produced the largest positive SHAP contribution among the analysed features.

The model's SHAP explanation can therefore be expressed as:

```text
Transaction
     ↓
XGBoost Prediction
     ↓
SHAP Analysis
     ↓
Feature Contributions
     ↓
Human-Readable Investigation Context
```

Because many Elliptic++ variables are anonymised, CryptoGuard does **not** assign unsupported real-world meanings to `Local_feature_*` or `Aggregate_feature_*` variables.

> Feature importance and SHAP contribution describe model behaviour; they do not establish causation.

---

# 🖥️ Streamlit Dashboard

CryptoGuard provides an interactive Streamlit dashboard for exploring the generated investigation results.

### Dashboard sections

* Dataset Overview
* Risk Distribution
* Investigation Priority
* Transaction Investigation
* Transaction Data

### Investigation workflow

```text
Enter Transaction ID
        ↓
Retrieve Transaction
        ↓
View ML Risk Signal
        ↓
View Anomaly Signal
        ↓
View Network Activity
        ↓
View Investigation Score
        ↓
View Investigation Priority
```

The dashboard allows an analyst to move from a large transaction dataset to an individual transaction-level investigation view.

---

# 📸 Dashboard Preview

> Add your actual Streamlit dashboard screenshot here.

```text
docs/
└── dashboard-preview.png
```

Once the screenshot is added to the repository, display it in this section using:

```markdown
![CryptoGuard Dashboard](docs/dashboard-preview.png)
```

---

# 📊 Project Visualisations

The final repository should include selected project-generated figures rather than every notebook plot.

Recommended figures:

```text
reports/
└── figures/
    ├── class_distribution.png
    ├── model_performance.png
    ├── anomaly_distribution.png
    ├── risk_distribution.png
    ├── network_analysis.png
    └── shap_explanation.png
```

Suggested README presentation:

### Class Distribution

Show the severe imbalance between labelled classes and the unknown population.

### Model Comparison

Show Accuracy, Precision, Recall, F1, ROC-AUC and PR-AUC.

### Risk Distribution

Show how the unknown transactions are distributed across investigation categories.

### Anomaly Detection

Show the anomaly-score distribution and selected threshold.

### Network Analysis

Show transaction connectivity or network-degree distribution.

### SHAP Explanation

Show the actual SHAP explanation for transaction `12661353`.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │  Elliptic++ Dataset  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Data Preprocessing   │
                    │ & Validation         │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
          ┌──────────┐  ┌────────────┐  ┌─────────────┐
          │ XGBoost  │  │ Isolation  │  │  NetworkX   │
          │ Model    │  │  Forest    │  │  Graph      │
          └────┬─────┘  └─────┬──────┘  └──────┬──────┘
               │              │                │
               └──────────────┼────────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Investigation Score  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ SHAP Explainability  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    └──────────────────────┘
```

---

# 🧰 Technology Stack

| Category          | Technologies                |
| ----------------- | --------------------------- |
| Language          | Python                      |
| Data Processing   | Pandas, NumPy               |
| Machine Learning  | Scikit-learn, XGBoost       |
| Anomaly Detection | Isolation Forest            |
| Network Analysis  | NetworkX                    |
| Explainable AI    | SHAP                        |
| Visualisation     | Matplotlib, Seaborn, Plotly |
| Dashboard         | Streamlit                   |
| Development       | Jupyter Notebook, VS Code   |
| Version Control   | Git, GitHub                 |

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
│   └── figures/
│
├── .gitignore
├── README.md
└── requirements.txt
```

> Large datasets, generated processed data, trained model binaries, and virtual-environment files are excluded from the public Git repository through `.gitignore`.

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

```powershell
pip install -r requirements.txt
```

---

# ▶️ Run the Dashboard

From the project root:

```powershell
streamlit run .\dashboard\app.py
```

The dashboard will open in your browser.

---

# 📓 Notebook

The main analysis notebook is:

```text
notebook/01_data_understanding.ipynb
```

It contains the data-understanding and modelling workflow developed for the project.

---

# 🔐 Responsible Use

CryptoGuard is an **academic and research prototype**.

A high-risk score, anomaly flag, or high investigation priority:

* does not prove criminal behaviour
* does not prove illicit activity
* does not identify a criminal
* should not be treated as a legal conclusion
* should not replace professional AML/compliance investigation

The system is designed to identify **transactions that may warrant additional analytical review**.

---

# ⚠️ Limitations

### Dataset Generalisation

Results are based on the Elliptic++ dataset and should not automatically be assumed to generalise to every blockchain or cryptocurrency ecosystem.

### Class Imbalance

The labelled dataset contains a strong imbalance between the available classes.

### Temporal Distribution Shift

The class distribution changes between the training and later test periods, which can affect model performance.

### Anomaly Detection

An unusual transaction is not necessarily an illicit transaction.

### Heuristic Risk Scoring

The combined investigation score uses project-defined weights and is not a calibrated probability.

### Feature Semantics

Anonymised dataset features cannot reliably be assigned real-world meanings without additional information.

### Operational Deployment

The current implementation is a research/academic prototype rather than a production AML or financial-crime detection platform.

---

# 🚀 Future Improvements

Potential future development includes:

* Probability calibration
* Threshold optimisation
* Temporal drift monitoring
* Graph-based machine learning
* Graph embeddings
* Advanced anomaly-detection methods
* Model monitoring
* Analyst feedback mechanisms
* REST API deployment
* Docker containerisation
* Cloud deployment
* Automated testing
* CI/CD integration
* Support for additional blockchain datasets
* More detailed transaction-level explanations

---

# 🎓 Academic & Career Relevance

CryptoGuard combines several areas of modern technology:

```text
Data Science
      +
Machine Learning
      +
Blockchain Analytics
      +
Cybersecurity
      +
Network Analysis
      +
Explainable AI
      +
Financial Risk Analytics
```

The project demonstrates practical experience with:

* Real-world dataset analysis
* Data preprocessing
* Imbalanced classification
* Time-aware evaluation
* Ensemble machine learning
* Anomaly detection
* Graph analytics
* Explainable AI
* Risk scoring
* Interactive dashboard development
* Git/GitHub project organisation

---

# 📌 Key Takeaways

CryptoGuard demonstrates that blockchain transaction analysis can be approached using **multiple complementary signals** rather than relying on a single model.

The project combines:

```text
Predictive Signal
       +
Anomaly Signal
       +
Network Signal
       ↓
Investigation Priority
```

The final system converts large-scale blockchain transaction data into an **interactive investigation workflow**.

---

# 👩‍💻 Author

## Deekshitha D V

**MCA | Data Science | Data Analytics | Blockchain & Crypto Security**

Areas of interest:

* Data Science
* Data Analytics
* Machine Learning
* Blockchain Analytics
* Crypto Risk Analysis
* Explainable AI

### Profiles

* [GitHub](https://github.com/Deekshitha-DV)
* [LinkedIn](https://www.linkedin.com/in/deekshithadv/)

---

# 📄 Project Disclaimer

CryptoGuard is developed for **academic, research, and educational purposes**.

The system generates analytical risk and anomaly signals for investigation prioritisation. It does not establish criminality, legal liability, or definitive illicit activity.

Any real-world financial, compliance, or investigative decision should involve appropriate human review, additional evidence, domain expertise, and applicable legal and regulatory procedures.
