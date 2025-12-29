#  Bengaluru House Price Predictor

##  Overview
This project is an end-to-end Machine Learning web application that predicts real estate prices in Bengaluru, India. 

The application allows users to enter the property's **location**, **total square footage**, **number of bathrooms**, and **BHK (Bedrooms, Hall, Kitchen)** to get an estimated price in Lakhs. The model was trained on a dataset of Bengaluru housing prices, processed to remove outliers, and deployed using a Flask server with a responsive HTML/CSS frontend.



## 🛠️ Tech Stack
* **Python**: Core programming language.
* **Pandas & NumPy**: For data manipulation and cleaning.
* **Matplotlib**: For data visualization and EDA.
* **Scikit-Learn**: For building and tuning the machine learning model.
* **Flask**: For the backend web server.
* **HTML/CSS**: For the user interface.

##  Project Workflow

### 1. Data Cleaning & EDA (Jupyter Notebook)
The data processing was done in `real estate project.ipynb`:
* **Data Cleaning:** Handled missing values and dropped unnecessary columns (`area_type`, `availability`, etc.).
* **Feature Engineering:** * Converted `total_sqft` ranges (e.g., "1133 - 1384") into average numbers.
    * Created a `bhk` column from the `size` feature.
    * Dimensionality Reduction: Grouped locations with fewer than 10 data points into an "other" category to reduce the number of features (One Hot Encoding).
* **Outlier Removal:** * Removed properties where `sqft` per bedroom was less than 300.
    * Removed properties where the number of bathrooms exceeded `bhk + 2`.
    * Removed price per sqft outliers using Mean and Standard Deviation.

### 2. Model Building
I used **GridSearchCV** to find the best model and parameters. I compared:
* **Linear Regression** (Best Accuracy: ~84%)
* Lasso Regression
* Decision Tree Regressor

**Linear Regression** was selected as the final model.

### 3. Deployment
* Exported the trained model to a pickle file (`banglore_home_prices_model.pickle`).
* Exported column structure to `columns.json`.
* Built a **Flask** server (`apps.py`) to handle HTTP requests.
* Designed a clean frontend (`index.html`) where users select locations from a dropdown (populated dynamically) and get predictions.

##  How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    Create a `requirements.txt` file (or install manually):
    ```bash
    pip install flask pandas scikit-learn numpy matplotlib
    ```

3.  **Run the application:**
    ```bash
    python apps.py
    ```

4.  **Open in Browser:**
    The app runs on port 5006. Open your browser and go to:
    `http://127.0.0.1:5006`

## 📂 Repository Structure
* `apps.py`: Main Flask application file.
* `templates/index.html`: The frontend user interface.
* `real estate project.ipynb`: Notebook containing Data cleaning, EDA, and Model selection.
* `banglore_home_prices_model.pickle`: The serialized Machine Learning model.
* `columns.json`: List of columns used by the model (required for One Hot Encoding).

##  Future Improvements
* Deploy the application to the cloud (AWS/Heroku/Render).
* Add more features like "Carpet Area" or "Age of Property".
* Improve the UI with a modern framework like React.
