# Hospital Readmission Risk Prediction & Healthcare Analytics

This project predicts 30-day hospital readmission using structured synthetic healthcare data.

FINAL XGBOOST TEST RESULTS
Accuracy: 0.7871
Precision: 0.5248
Recall: 0.1027
F1-score: 0.1718
ROC-AUC: 0.6691

The final model is saved at models/readmission_xgboost.joblib and is used directly by the Streamlit dashboard.

IMPORTANT: The dataset is synthetic and the model is for portfolio/educational use only. It is not a clinical decision-support system.

Run:
pip install -r requirements.txt
streamlit run app/app.py
