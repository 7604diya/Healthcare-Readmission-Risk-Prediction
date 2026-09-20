# 🏥 Hospital Readmission Risk Prediction & Healthcare Analytics

A machine learning project for predicting **30-day hospital readmission risk** using structured healthcare data, XGBoost, SQL analytics, and an interactive Streamlit dashboard.

> **Note:** This project uses a **synthetic healthcare dataset containing 12,000 patient records**. It is intended for educational and portfolio purposes and is **not a clinical decision-support system**.

---

## 📌 Project Overview

Hospital readmissions are an important healthcare analytics problem because identifying patients at higher risk of returning to the hospital can help healthcare teams better understand patient-level risk patterns and healthcare utilization.

This project builds an end-to-end machine learning pipeline to:

* Analyze structured patient and hospitalization data
* Perform exploratory data analysis (EDA)
* Prepare healthcare features for machine learning
* Predict 30-day hospital readmission risk
* Evaluate classification performance using multiple metrics
* Perform SQL-based healthcare analytics
* Generate patient-level risk predictions
* Provide an interactive Streamlit interface for prediction and analysis

---

## 🎯 Problem Statement

The objective is to predict whether a patient is likely to experience a **hospital readmission within 30 days** based on demographic, clinical, hospitalization, and healthcare-utilization characteristics.

### Target Variable

`readmitted_30_days`

| Value | Meaning                       |
| ----- | ----------------------------- |
| `0`   | No readmission within 30 days |
| `1`   | Readmitted within 30 days     |

---

## 📊 Dataset

The project uses a **synthetically generated structured healthcare dataset** containing:

* **12,000 patient records**
* Demographic information
* Clinical measurements
* Hospitalization information
* Previous healthcare utilization
* Medication-related information
* Comorbidity-related features
* Healthcare encounter information
* Readmission outcome

The dataset was created specifically for this portfolio project and does not represent real patient records.

---

## 🔎 Exploratory Data Analysis

The analysis investigates relationships between patient characteristics, healthcare utilization, and readmission outcomes.

Key analysis areas include:

* Readmission class distribution
* Patient demographics
* Length of hospital stay
* Previous hospital visits
* Emergency visits
* Chronic conditions
* Medication counts
* Clinical measurements
* Healthcare utilization patterns
* Feature relationships and correlations

Visualizations were created using:

* Matplotlib
* Seaborn
* Plotly

---

## 🤖 Machine Learning

### Model

The primary classification model used in this project is:

**XGBoost Classifier**

The machine learning workflow includes:

1. Data loading
2. Data validation
3. Missing-value handling
4. Feature preprocessing
5. Train-test split
6. Model training
7. Probability prediction
8. Classification thresholding
9. Model evaluation
10. Patient-level risk prediction

### Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

These metrics provide a broader view of model performance than accuracy alone, particularly for classification problems where the classes may not be evenly distributed.

---

## 📈 Model Evaluation

Initial model evaluation produced approximately:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 78.71% |
| Precision | 52.48% |
| Recall    | 10.27% |
| F1-score  | 17.18% |
| ROC-AUC   | 0.6691 |

These results are treated as a **baseline model evaluation** rather than a claim of clinical-grade performance.

The project also explores classification thresholds and the trade-off between precision and recall.

---

## 🎚️ Classification Threshold

The model generates a probability representing the estimated likelihood of readmission.

A classification threshold is then used to convert this probability into a binary prediction.

For example:

```text
Predicted probability ≥ threshold
        ↓
Readmission = 1

Predicted probability < threshold
        ↓
Readmission = 0
```

Threshold selection can affect the balance between:

* Precision
* Recall
* False positives
* False negatives

This is particularly important in healthcare classification problems where different types of prediction errors can have different implications.

---

## 🧮 SQL Healthcare Analytics

SQL is used alongside machine learning to perform structured healthcare analysis.

Example analytical tasks include:

* Identifying high-risk patients
* Aggregating readmission statistics
* Analyzing hospital utilization
* Comparing patient groups
* Calculating readmission rates
* Filtering patients based on clinical and utilization attributes
* Generating summary statistics

SQL scripts are available in the:

```text
sql/
```

directory.

---

## 🖥️ Streamlit Dashboard

The project includes an interactive **Streamlit application** that allows users to interact with the trained model.

The application supports:

* Patient feature input
* Readmission risk prediction
* Model probability output
* Risk interpretation
* Interactive healthcare analytics

### Run the application

Clone the repository:

```bash
git clone https://github.com/7604diya/Healthcare-Readmission-Risk-Prediction.git
```

Navigate to the project:

```bash
cd Healthcare-Readmission-Risk-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app\app.py
```

The application will open in your browser.

---

## 🗂️ Project Structure

```text
Healthcare-Readmission-Risk-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   ├── healthcare_readmission.csv
│   └── model_predictions.csv
│
├── models/
│   ├── readmission_xgboost.joblib
│   └── metrics.json
│
├── notebooks/
│   └── Model development and analysis notebooks
│
├── sql/
│   └── Healthcare analytics SQL queries
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Technology Stack

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-learn
* XGBoost
* Joblib

### Database & Analytics

* SQL

### Deployment / Interface

* Streamlit

### Development

* Jupyter Notebook
* Git
* GitHub

---

## 🔄 End-to-End Workflow

```text
Synthetic Healthcare Dataset
            ↓
     Data Preprocessing
            ↓
  Exploratory Data Analysis
            ↓
    Feature Preparation
            ↓
     XGBoost Classifier
            ↓
  Probability Prediction
            ↓
 Classification Threshold
            ↓
   Readmission Prediction
            ↓
 ┌──────────┴──────────┐
 ↓                     ↓
SQL Analytics      Streamlit App
```

---

## 💡 Key Learning Outcomes

This project demonstrates practical experience with:

* End-to-end machine learning workflows
* Structured healthcare data analysis
* Classification problems
* Feature preprocessing
* XGBoost
* Model evaluation
* Precision-recall trade-offs
* Classification thresholds
* SQL analytics
* Model serialization using Joblib
* Streamlit application development
* Git/GitHub project management

---

## ⚠️ Limitations

This project has several important limitations:

1. The dataset is **synthetic** and does not represent real hospital or patient data.
2. The model has not been clinically validated.
3. The baseline model's recall is relatively low.
4. The predictions should not be used for medical diagnosis or treatment decisions.
5. Real-world deployment would require external validation, appropriate healthcare datasets, privacy safeguards, and clinical evaluation.

---

## 🚀 Future Improvements

Potential extensions include:

* Testing additional classification algorithms
* Hyperparameter optimization
* Class-imbalance handling
* Threshold optimization using validation data
* Precision-recall curve analysis
* SHAP-based model explainability
* Model monitoring
* More extensive SQL analytics
* Integration with a real publicly available healthcare dataset
* Improved Streamlit visualizations
* Model versioning and deployment

---

## 📁 Repository

**GitHub:**
https://github.com/7604diya/Healthcare-Readmission-Risk-Prediction

---

## 👩‍💻 Author

**Sarodiya Pal**
MSc Mathematics & Scientific Computing
National Institute of Technology, Warangal

---

### ⭐ Disclaimer

This project is developed for **educational, portfolio, and machine-learning demonstration purposes only**. The dataset is synthetic, and the model should not be used for clinical decision-making.
