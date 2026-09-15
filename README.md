# Bank Loan Approval Prediction

## Project Overview

This project predicts whether a bank loan application will be approved or not using Machine Learning.

The project uses applicant information such as income, credit history, education, marital status, dependents, and property area to make the prediction.

## Objective

The main objective of this project is to build a classification model that can predict loan approval based on applicant details.

## Dataset

The dataset contains information about loan applicants, including:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area
- Loan Status

## Data Preprocessing

The following preprocessing steps were performed:

- Handled missing values
- Removed the `Loan_ID` column
- Converted categorical variables into numerical values using One-Hot Encoding
- Divided the data into training and testing sets

## Machine Learning Model

### Random Forest Classifier

A Random Forest Classifier was used to train the model and predict whether a loan application will be approved.

## Model Evaluation

The model was evaluated using a **Confusion Matrix** to compare actual loan approval results with predicted results.

## Streamlit Application

A Streamlit web application was created where users can enter applicant details and get a loan approval prediction.

### Prediction Results

The application displays:

- **Loan Approved ✅**
- **Loan Not Approved ❌**

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

## Project Files

- `loan_approval_prediction.ipynb` — Machine Learning notebook
- `app.py` — Streamlit application
- `loan_model.pkl` — Trained Random Forest model
- `train_u6lujuX_CVtuZ9i (1).csv` — Dataset

## How to Run

Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```
Run the Streamlit application:

```bash
streamlit run app.py
```
## Conclusion

The project demonstrates a practical classification problem where Machine Learning is used to predict whether a loan application can be approved based on applicant information.