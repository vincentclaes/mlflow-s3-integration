import mlflow
from mlflow.store.artifact.s3_artifact_repo import S3ArtifactRepository
# fetch model from local running service with sqlite and s3 as backend
# check the notebook for more info
mlflow.tracking.set_tracking_uri(uri="http://127.0.0.1:5000")

# fetch some logged model
logged_model = 'runs:/1cd9275a9f9b4da18d72863afd210d89/dummy_classifier'
model = mlflow.sklearn.load_model(model_uri=logged_model)
model