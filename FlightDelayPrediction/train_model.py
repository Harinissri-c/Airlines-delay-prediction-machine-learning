import pandas as pd
import numpy as np
import pickle
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import os

warnings.simplefilter('ignore')

def train():
    print("Loading dataset...")
    # Path to the dataset
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'C:\\Users\\HARINI SSRI\\OneDrive\\Documents\\project\\DelayedFlights.csv (2)\\DelayedFlights.csv\\DelayedFlights.csv')
    
    # Reading a subset to speed up training
    df = pd.read_csv(data_path, nrows=200000)
    
    print("Pre-processing data...")
    # Drop rows with missing target values
    df = df.dropna(subset=['ArrDelay'])
    
    # Create target: 1 if Delay > 15 mins, else 0
    df['IsDelayed'] = (df['ArrDelay'] > 15).astype(int)
    
    # Select features
    features = ['Month', 'DayofMonth', 'DayOfWeek', 'CRSDepTime', 'UniqueCarrier', 'Origin', 'Dest', 'Distance']
    X = df[features]
    y = df['IsDelayed']
    
    # Handling categorical features
    le_carrier = LabelEncoder()
    X['UniqueCarrier'] = le_carrier.fit_transform(X['UniqueCarrier'])
    
    le_origin = LabelEncoder()
    X['Origin'] = le_origin.fit_transform(X['Origin'])
    
    le_dest = LabelEncoder()
    X['Dest'] = le_dest.fit_transform(X['Dest'])
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))
    
    print("Saving model and encoders...")
    model_dir = os.path.join(os.path.dirname(__file__), 'model')
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        
    with open(os.path.join(model_dir, 'flight_delay_model.pkl'), 'wb') as f:
        pickle.dump((model, le_carrier, le_origin, le_dest), f)
    
    print("Training complete and model saved.")

if __name__ == '__main__':
    train()
