# Salary Prediction Model 📊

This project is a Machine Learning-based system designed to predict the expected salary of an employee based on various professional and personal factors. It evaluates multiple regression models to find the most accurate prediction.

---

## 🎯 Objective
The main goal is to build a predictive system that:
* Takes employee details as input.
* Predicts the *expected salary* (numeric value) with high precision.

---

## 📂 Dataset Features (Independent Variables)
The model is trained on the following features:
* *Experience:* Number of years in the industry.
* *Education Level:* Bachelor's, Master's, or PhD.
* *Job Role:* Engineer, Analyst, Data Scientist, etc.
* *Location:* City of employment.
* *Skills Count:* Number of relevant technical skills.
* *Age:* Age of the employee.

---

## ⚙️ Functional Requirements

### 1. Data Handling
* Load dataset from CSV (Sample HR Salary Dataset.csv).
* Handle missing values and data cleaning.
* Encode categorical variables (Education, Job Role, Location) for the ML models.

### 2. Model Training
We implemented and compared the following regression algorithms:
* *Linear Regression*
* *Multiple Linear Regression*
* *Ridge Regression*
* *Lasso Regression*

### 3. Evaluation Metrics
Each model is evaluated based on:
* *MAE* (Mean Absolute Error)
* *MSE* (Mean Squared Error)
* *RMSE* (Root Mean Squared Error)
* *R² Score* (Coefficient of Determination)

---

## 📊 Expected Outputs

### Model Performance Comparison
| Model | MAE | RMSE | R² Score |
| :--- | :--- | :--- | :--- |
| Linear Regression | 5000 | 7000 | 0.85 |
| *Ridge Regression* | *4800* | *6800* | *0.87* |
| Lasso Regression | 5100 | 7100 | 0.84 |

> *Note:* *Ridge Regression* is selected as the best model due to the highest R² score and lowest RMSE.

### Visualizations Included:
* Salary vs. Experience scatter plot.
* Correlation Heatmap.
* Residual Plot.
* Feature Importance (specifically for Lasso).

---

## 🚀 How to Run
1. Install requirements: pip install pandas matplotlib seaborn scikit-learn streamlit
2. Run the Streamlit dashboard: streamlit run app.py

---

## Dashboard Preview


### 📩 Author
* Palak Rathore  
