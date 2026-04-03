#  Bengaluru House Price Predictor
**A professional Machine Learning valuation engine for the Bengaluru real estate market.**

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://real-estate-price-prediction-rqhv.onrender.com)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)

---

##  Overview
This project is an end-to-end Data Science and Machine Learning application designed to provide institutional-grade property estimates. It utilizes a refined Linear Regression model trained on over **13,000 localized datapoints** from the Bengaluru housing market.

The application features a **modern, professional UI** that allows users to instantly calculate property values based on location, square footage, and BHK configuration.

### **[Explore the Live App](https://real-estate-price-prediction-rqhv.onrender.com)**
<img width="1824" height="992" alt="image" src="https://github.com/user-attachments/assets/c2ee4936-225a-462c-b92a-1a4ead781801" />

---

##  Key Features
*   **Precision Modeling:** removal of BHK, Price-per-Sqft, and Bathroom outliers for high accuracy (~84% R²).
*   **Professional UI:** Minimalist, data-forward design with a "Market Insights" dashboard.
*   **Smart Search:** Integrated location search with autocompletion for 240+ Bengaluru localities.
*   **Cloud Ready:** Fully optimized for production deployment with Gunicorn and dynamic port handling.

---

##  Tech Stack
*   **Core Logic:** Python 3.13, Pandas, NumPy
*   **Machine Learning:** Scikit-Learn (Linear Regression, GridSearchCV, K-Fold Cross Validation)
*   **Backend:** Flask, Gunicorn (WSGI)
*   **Frontend:** HTML5, CSS3 (Modern Minimalist Design), JavaScript (Vanilla)

---

##  Project Structure
*   `apps.py`: Main Flask application with production server logic.
*   `real estate project.ipynb`: Comprehensive Data Science pipeline (Cleaning, EDA, Outlier Removal).
*   `templates/`: Contains the professional UI refactor (`index.html`).
*   `banglore_home_prices_model.pickle`: Optimized serialized ML model.
*   `columns.json`: Feature mapping for One-Hot Encoding.
*   `requirements.txt`: System dependencies.
*   `Procfile`: Deployment configuration for Render/Heroku.

---

##  Data Science Workflow
This project follows a rigorous data cleaning and modeling process:
1.  **Data Cleaning:** Handling null values and normalizing complex strings (e.g., area ranges).
2.  **Feature Engineering:** Dimensionality reduction for locations and synthesizing BHK attributes.
3.  **Outlier Removal:** 
    *   Business logic filters (e.g., 300 sqft/BHK minimum).
    *   Statistical standard deviation filters for Price-per-Sqft.
    *   Consistency checks (ensuring 3BHK prices align with 2BHK in the same area).
4.  **Model Selection:** Evaluated Linear Regression, Lasso, and Decision Trees using `GridSearchCV`.

---

##  Local Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/malikparth05/Real-Estate-Price-prediction.git
    cd Real-Estate-Price-prediction
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the Server**
    ```bash
    # Development mode
    python apps.py

    # Production mode (Gunicorn)
    gunicorn apps:app
    ```

4.  **Access the Dashboard**
    Open `http://127.0.0.1:5006` in your browser.

---

##  Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/malikparth05/Real-Estate-Price-prediction/issues).

---
*Created by Parth Malik*
