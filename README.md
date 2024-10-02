# Customer Satisfaction Prediction

---

## Project Documentation: Customer Satisfaction Prediction (ML Classification Project)

### Table of Contents
1. Introduction
2. Dataset Description
3. Project Objectives
4. Project Structure
5. Data Ingestion
6. Data Transformation
7. Model Training
8. Training Pipeline
9. Prediction Pipeline
10. Flask
11. Logging
12. Exception Handling
13. Utils
14. Conclusion

---

### 1. Introduction
The **Customer Satisfaction Prediction** project aims to classify customer satisfaction levels based on various factors such as service quality, product experience, delivery time, and other relevant metrics. This document provides a detailed overview of the project's structure, processes, and supporting scripts.

---

### 2. Dataset Description
**Dataset Name**: Customer Satisfaction Dataset

**Description**: The dataset contains multiple entries and columns, providing features that help predict customer satisfaction:
The dataset contains 103,904 entries with 25 columns. Below is a brief description of each column:

1. **Unnamed: 0**: Index column, representing the row number.
2. **id**: Unique identifier for each entry.
3. **Gender**: Gender of the customer (Male or Female).
4. **Customer Type**: Whether the customer is a Loyal Customer or a Disloyal Customer.
5. **Age**: Age of the customer.
6. **Type of Travel**: Type of travel (Business travel or Personal travel).
7. **Class**: Travel class (Eco, Eco Plus, Business).
8. **Flight Distance**: Distance traveled by the flight in miles.
9. **Inflight wifi service**: Rating of the inflight Wi-Fi service (1 to 5).
10. **Departure/Arrival time convenient**: Rating of how convenient the departure/arrival time was (1 to 5).
11. **Ease of Online booking**: Rating of the ease of booking online (1 to 5).
12. **Gate location**: Rating of the gate location (1 to 5).
13. **Food and drink**: Rating of the food and drink quality (1 to 5).
14. **Online boarding**: Rating of the online boarding experience (1 to 5).
15. **Seat comfort**: Rating of the seat comfort (1 to 5).
16. **Inflight entertainment**: Rating of the inflight entertainment (1 to 5).
17. **On-board service**: Rating of the on-board service (1 to 5).
18. **Leg room service**: Rating of the legroom service (1 to 5).
19. **Baggage handling**: Rating of the baggage handling (1 to 5).
20. **Checkin service**: Rating of the check-in service (1 to 5).
21. **Inflight service**: Rating of the inflight service (1 to 5).
22. **Cleanliness**: Rating of the cleanliness of the flight (1 to 5).
23. **Departure Delay in Minutes**: Number of minutes the flight was delayed at departure.
24. **Arrival Delay in Minutes**: Number of minutes the flight was delayed at arrival.
25. **Satisfaction**: Whether the customer was satisfied or neutral/dissatisfied with the service.

This dataset is used for predicting customer satisfaction based on various factors related to flight experience.

---

### 3. Project Objectives
- **Data Ingestion**: Load and explore the dataset.
- **Data Transformation**: Clean, preprocess, and transform the dataset for model analysis.
- **Model Training**: Train machine learning models to predict customer satisfaction levels.
- **Pipeline Creation**: Develop pipelines for data ingestion, transformation, and model training.
- **Supporting Scripts**: Provide scripts for setup, logging, exception handling, and utility functions.

---

### 4. Project Structure
```
├── artifacts/
│   ├── (best)model.pkl
│   ├── LogisticRegression.pkl
│   ├── DecisionTreeClassifier.pkl
│   ├── RandomForestClassifier.pkl
│   ├── GradientBoostingClassifier.pkl
│   ├── XGBoostClassifier.pkl
│   ├── KNeighborsClassifier.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│     ├── data/
│     │    └── train.csv
│     └── Customer_Satisfaction_Prediction.ipynb
├── src/
│   ├── __init__.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_training.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   ├── airplane.png
│   └── style.css
│
├── app.py
├── .gitignore
├── requirements.txt
├── README.md
└── setup.py
```

---

### 5. Data Ingestion
The data ingestion module loads the customer satisfaction dataset, splits it into training and testing sets, and saves them for further use. The raw dataset is stored in the `artifacts/` folder.

---

### 6. Data Transformation
The data transformation module preprocesses the dataset, including encoding categorical variables (e.g., Satisfaction level) and scaling numerical features (e.g., Product Quality, Service Quality). The transformed data is stored in the `artifacts/` folder.

---

### 7. Model Training
The model training module trains multiple machine learning classification models, such as:
- **Logistic Regression**
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Gradient Boosting Classifier**
- **XGBoost Classifier**
- **KNeighbors Classifier**

The best-performing model is saved as `best_model.pkl` in the `artifacts/` folder.


![model_accuracy_comparison (1)](https://github.com/user-attachments/assets/55344077-14cd-4289-a2bb-dee159ba0d05)


---

### 8. Training Pipeline
The training pipeline integrates data ingestion, transformation, and model training, ensuring smooth execution of the workflow from loading data to saving the trained model.

---

### 9. Prediction Pipeline
The prediction pipeline uses `best_model.pkl` and `preprocessor.pkl` to predict customer satisfaction levels on new data. It handles preprocessing and model inference seamlessly.

---

### 10. Flask (app.py)
The Flask app provides a web interface to input customer data and predict their satisfaction level. Input fields are handled by `index.html`, and the results are displayed in `results.html`.

![Screenshot 08-01-2024 09 14 02](https://github.com/user-attachments/assets/0a3d4f08-73a9-488d-b784-85c00d332697)

![Screenshot 08-01-2024 09 17 27](https://github.com/user-attachments/assets/75ff3cd1-9b9f-4ca6-a029-ed7c47c69342)

---

### 11. Logging
The `logger.py` file captures logs for various processes such as data ingestion, transformation, and model training, helping to debug and monitor the workflow.

---

### 12. Exception Handling
The `exception.py` file ensures robust error handling by logging and addressing any issues encountered during the project execution.

---

### 13. Utils
The `utils.py` file includes utility functions for tasks like directory creation, file management, and data loading.

---

### 14. Conclusion
This documentation outlines the end-to-end workflow of the **Customer Satisfaction Prediction** project, covering ingestion, transformation, modeling, and deployment. The project is structured to be modular and scalable, facilitating future extensions or adaptations.

--- 
