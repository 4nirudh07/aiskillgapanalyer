import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import warnings

# Suppress annoying logistic regression warnings
warnings.filterwarnings('ignore')

def get_best_model(models_dict, X_train, X_test, y_train, y_test, metric_func, task_name):
    print(f"\n--- Evaluating models for {task_name} ---")
    best_score = -float('inf')
    best_model = None
    best_name = ""
    
    for name, model in models_dict.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        score = metric_func(y_test, preds)
        print(f"  {name} score: {score:.4f}")
        
        if score > best_score:
            best_score = score
            best_model = model
            best_name = name
            
    print(f"-> Selected {best_name} as the best model for {task_name} (Score: {best_score:.4f})")
    
    # Retrain the best model on the entire dataset for maximum data utilization
    X_full = pd.concat([X_train, X_test])
    y_full = pd.concat([y_train, y_test])
    best_model.fit(X_full, y_full)
    
    return best_model

def train_and_save_model(csv_path="dataset.csv", model_dir="backend/app/ml/models"):
    print("Loading dataset...")
    df = pd.read_csv(csv_path)

    # Features (X)
    feature_cols = [
        'technical_skills_score', 'programming_skills_score', 
        'problem_solving_score', 'projects_score', 
        'communication_score', 'education_score', 'experience_score'
    ]
    X = df[feature_cols]

    print("Encoding categorical labels...")
    le_strongest = LabelEncoder()
    le_missing = LabelEncoder()
    
    y_match = df['skill_match_percentage']
    y_readiness = df['job_readiness_percentage']
    y_strongest = pd.Series(le_strongest.fit_transform(df['strongest_skill']))
    y_missing = pd.Series(le_missing.fit_transform(df['missing_skill']))

    # Split data into 80% train and 20% test for evaluation
    X_train, X_test, y_match_tr, y_match_te = train_test_split(X, y_match, test_size=0.2, random_state=42)
    _, _, y_read_tr, y_read_te = train_test_split(X, y_readiness, test_size=0.2, random_state=42)
    _, _, y_str_tr, y_str_te = train_test_split(X, y_strongest, test_size=0.2, random_state=42)
    _, _, y_mis_tr, y_mis_te = train_test_split(X, y_missing, test_size=0.2, random_state=42)

    # Define our 3 candidate models for regression (predicting percentages)
    regressors = {
        "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
        "GradientBoosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
        "LinearRegression": LinearRegression()
    }
    
    # Define our 3 candidate models for classification (predicting distinct skill names)
    classifiers = {
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
        "GradientBoosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
        "LogisticRegression": LogisticRegression(max_iter=2000)
    }

    # Evaluate all 3 models for each of the 4 tasks and select the best one
    model_match = get_best_model(regressors, X_train, X_test, y_match_tr, y_match_te, r2_score, "Skill Match Percentage")
    model_readiness = get_best_model(regressors, X_train, X_test, y_read_tr, y_read_te, r2_score, "Job Readiness Percentage")
    
    model_strongest = get_best_model(classifiers, X_train, X_test, y_str_tr, y_str_te, accuracy_score, "Strongest Skill Identification")
    model_missing = get_best_model(classifiers, X_train, X_test, y_mis_tr, y_mis_te, accuracy_score, "Missing Skill Identification")

    # Save the winning models
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model_match, os.path.join(model_dir, 'model_match.pkl'))
    joblib.dump(model_readiness, os.path.join(model_dir, 'model_readiness.pkl'))
    joblib.dump(model_strongest, os.path.join(model_dir, 'model_strongest.pkl'))
    joblib.dump(model_missing, os.path.join(model_dir, 'model_missing.pkl'))
    
    joblib.dump(le_strongest, os.path.join(model_dir, 'le_strongest.pkl'))
    joblib.dump(le_missing, os.path.join(model_dir, 'le_missing.pkl'))
    
    print(f"\nWinner Models trained and saved successfully in {model_dir}!")

if __name__ == "__main__":
    dataset_path = "../../../dataset.csv" if not os.path.exists("dataset.csv") else "dataset.csv"
    train_and_save_model(dataset_path, "backend/app/ml/models")
