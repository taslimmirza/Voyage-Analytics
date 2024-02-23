import mlflow
from sklearn.metrics import mean_squared_error, r2_score

def log_model(model, X_train, y_train, X_test, y_test):
    with mlflow.start_run():
        # Train model
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        
        # Log parameters, metrics, and model
        mlflow.log_param("model_type", str(type(model)))
        mlflow.log_metric("rmse", mean_squared_error(y_test, y_pred, squared=False))
        mlflow.log_metric("r2", r2_score(y_test, y_pred))
        
        mlflow.sklearn.log_model(model, "model")

if __name__ == "__main__":
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    import pandas as pd
    
    # Load and prepare your data here
    df = pd.read_csv(...)
    # X_train, X_test, y_train, y_test = train_test_split(...)
    
    model = LinearRegression()
    log_model(model, X_train, y_train, X_test, y_test)
