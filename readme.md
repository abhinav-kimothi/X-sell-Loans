# Thera Bank Loan Cross Sell Eligibility Modeling
![Thera Bank Loan Predictor](static/TB%20Header.png)
---

Welcome to the Thera Bank Loan Cross Sell Eligibility Modeling repository! This project focuses on utilizing machine learning techniques to predict cross-sell eligibility for personal loans in Thera Bank, a fictitious financial institution. 

## Machine Learning for Cross-Sell Eligibility

In the realm of banking, cross-selling involves offering existing customers additional products or services. Predictive modeling, powered by machine learning algorithms, becomes a valuable tool for identifying customers who are most eligible for cross-sell offers.

## Application Overview

### User Interface

The application includes a Flask web app that allows users to input information and receive predictions on whether a customer is eligible for a personal loan cross sell. Here's a sneak peek at the user interface:

![Thera Bank Loan Predictor](static/TB%20UI.png)

#### Positive Response

If a customer is deemed eligible, the user will receive a positive response:

![Positive Response](static/TB%20Approve.png)

#### Negative Response

For customers who are not eligible, a negative response is provided:

![Negative Response](static/TB%20Deny.png)

## Repository Structure

The repository is organized as follows:

- **Data:** Contains the dataset used for modeling (`Bank_Personal_Loan_Modelling.csv`) and a zip code database (`zip_code_database.csv`).

- **Model_Objects:** Houses the trained machine learning model (`pl_prediction_model.pkl`) and the scaler object used for preprocessing (`scaler.pkl`).

- **Notebooks:** Includes Jupyter notebooks for exploratory data analysis (`ML_Trials.ipynb`) and model training (`Model_Training.ipynb`).

    `ML_Trials.ipynb` includes extensive EDA & Trials of different classification techniques

    ![](static/Model%20Trials.png)


- **Static:** Contains images used in the Flask web app, such as favicons (`favicon-16x16.png`, `favicon-32x32.png`).

- **Templates:** Holds the HTML template for the Flask app (`index.html`).

- **app.py:** Python code for the Flask web app.

- **loan_predictor.py:** Function for predicting cross-sell response.

- **requirements.txt:** Lists the required dependencies for running the application.

## How to Install and Run the App

To get started with the Thera Bank Loan Predictor, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/thera-bank-loan-predictor.git
   ```
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the Flask App***
    ```bash 
    python app.py
    ```
4. **Access the App**

    Open your web browser and go to http://localhost:5000.

5. **Use the Loan Predictor**
    Fill in the required information on the web page and click the "Predict" button to see the cross-sell eligibility response.


**Note**: This is a fictitious project created for demonstration purposes only. The data and model used are not based on real-world information.




