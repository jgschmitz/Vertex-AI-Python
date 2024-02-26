def send_data_for_prediction(endpoint, data):
    # Adapt this function based on the specific requirements of the deployed model
    # For example, you might need to convert your data to JSON or a specific format
    
    response = endpoint.predict(instances=data)
    predictions = response.predictions
    
    return predictions
