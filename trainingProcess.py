from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data(data):
    # Example: Convert categorical labels to numerical using LabelEncoder
    label_encoder = LabelEncoder()
    data['label'] = label_encoder.fit_transform(data['label'])
    
    # Example: Split data into features and labels
    X = data.drop(columns=['label'])
    y = data['label']
    
    # Example: Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test
