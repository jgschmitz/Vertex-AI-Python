## Using MongoDB Atlas with Vertex AI for Classification

<img src="https://miro.medium.com/v2/resize:fit:578/1*r-iod_ZxZQLy_dFoay52cA.png" alt="vertex Logo" width="300">

## Objective

This tutorial demonstrates how to use the Vertex AI Python client library to train and deploy a classification model for online prediction, where the data is stored in MongoDB Atlas.

**Note:** Be aware of potential charges for training, prediction, storage, or usage of other Google Cloud products during testing.

## Prerequisites

- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [MongoDB Atlas account](https://www.mongodb.com/cloud/atlas)
- Python and relevant libraries installed

## Steps

###  Set Up MongoDB Atlas

1. Create a MongoDB Atlas account if you don't have one.
2. Set up a cluster and a database to store your data. Note down the connection string.

###  Prepare Data in MongoDB

1. Ensure your data in MongoDB is appropriately structured for classification.
2. Convert MongoDB data into a format suitable for training. You might need to use Python scripts to fetch and preprocess data.

### Install Vertex AI Python Client Library

```
pip install google-cloud-aiplatform
```
So after the above is installed you should be able to do this
```
Python 3.11.7 (main, Dec  4 2023, 18:10:11) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from google.cloud import aiplatform
>>> import vertexai.preview
```
### Authenticate with Google Cloud
```
gcloud auth login
```
### Create a Vertex AI Model Training Job
```
gcloud aiplatform jobs custom-job create \
    --display-name="classification-job" \
    --python-package-path="your_package_path" \
    --python-module="your_module_name" \
    --runtime-version=2.8 \
    --region="your_region" \
    --master-image-uri="gcr.io/cloud-aiplatform/training/tf-cpu.2-8:latest"
```

### Train a Classification Model
Use the Vertex AI Python client library to initiate classification training. Adapt your code to fetch data from MongoDB.
Ensure your model handles non-tabular data appropriately.

### Deploy the Model Resource to a Serving Endpoint Resource
```
gcloud aiplatform models deploy "your_model_name" \
    --region="your_region" \
    --display-name="your_display_name" \
    --machine-type="n1-standard-4" \
    --python-version="3.7" \
    --runtime-version="2.8" \
    --model-uri="your_model_uri"
```

### Make a Prediction by Sending Data
Use the deployed model's endpoint to send data from MongoDB for prediction.
Adapt your code to retrieve data from MongoDB instead of Google Cloud Storage.
 Undeploy the Model Resource
```
gcloud aiplatform models undeploy "your_model_name" --region="your_region"
```
Congratulations! You have successfully trained, deployed, and tested a classification model using Vertex AI with MongoDB Atlas as your data source.

Replace placeholders like "your_package_path," "your_module_name," etc., with your actual information. Adapt the data retrieval and preprocessing steps according to your MongoDB data structure.
