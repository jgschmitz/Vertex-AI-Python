from google.cloud import aiplatform

def deploy_model(project, model_display_name, model_uri):
    aiplatform.init(project=project)
    
    model = aiplatform.Model(display_name=model_display_name)
    
    endpoint = model.deploy(
        machine_type="n1-standard-4",
        sync=True,
        traffic_split={"0": 100}
    )
    
    return endpoint
