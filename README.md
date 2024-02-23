# Voyage Analytics: Integrating MLOps for Predictive and Recommender Systems in Travel

## Project Overview

This project aims to revolutionize travel experiences through the integration of machine learning and data analytics. By utilizing datasets on users, flights, and hotels, we develop sophisticated machine learning models to enhance travel-related decision-making and master the art of MLOps. It also uses version control to ensure that the development is logged and can be reviewed

### Objectives

- Develop a regression model to predict flight prices.
- Deploy a REST API for real-time flight price predictions.
- Containerize the flight price prediction model using Docker.
- Scale the deployment using Kubernetes.
- Automate workflows with Apache Airflow.
- Implement a CI/CD pipeline using Jenkins.
- Track and manage model versions with MLFlow.
- Classify user gender and provide hotel recommendations.

## Repository Structure

.
├── models
│   ├── flight_price_model.pkl
│   ├── gender_classification_model.pkl
│   └── hotel_recommendation_model.pkl
├── encoders_scalers
│   ├── encoder.pkl
│   ├── scaler.pkl
│   ├── company_encoder.pkl
│   ├── age_scaler.pkl
│   ├── gender_encoder.pkl
│   ├── hotel_encoder.pkl
│   └── user_encoder.pkl
├── notebooks
│   ├── Flight_Price_Prediction_Model.ipynb
│   ├── Gender_Classification_Model.ipynb
│   ├── Travel_Recommendation_Model.ipynb
│   └── Voyage_Analytics.ipynb
├── api
│   ├── flask_app.py (for flight price prediction)
├── web_app
│   ├── streamlit_app.py (for travel recommendations)
├── docker
│   ├── Dockerfile
├── kubernetes
│   ├── deployment.yml
├── airflow
│   ├── dag_files
│       └── example_dag.py
├── mlflow
│   ├── tracking_code.py (for model tracking)
├── requirements.txt
└── README.md

## Setup Instructions

Detailed setup instructions for running the Flask API, Streamlit web application, deploying with Docker and Kubernetes, scheduling with Airflow, and setting up the CI/CD pipeline with Jenkins are provided in the corresponding directories. 

### Prerequisites

- Docker
- Kubernetes
- Apache Airflow
- Jenkins
- MLFlow

### Installation

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Follow the setup instructions in each directory.

## Usage

- **Flight Price Prediction API**: Navigate to the `api` directory and follow the instructions to run the Flask app.
- **Travel Recommendation Web App**: Go to the `web_app` directory for details on launching the Streamlit application.
- **Containerization and Deployment**: Check the `docker` and `kubernetes` directories for deployment guides.
- **Workflow Automation**: The `airflow` directory contains DAGs for automating ML workflows.
- **Model Tracking**: Instructions for using MLFlow for model versioning are in the `mlflow` directory.

## Contact
Github: https://github.com/taslimmirza/Voyage-Analytics
