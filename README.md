# A basic python flask app which is deployed using k8s deployments and also with Helm

 - initiate virtual environment: python3 -m venv python-ms
 - Activate virtual environment: source python-ms/bin/activate

 - Create a basic flask app
 - freeze the python packages by pip freeze > requirements.txt

 - Create Dockerfile
 - Docker compose can be used.

 - For kubernetes:
  - Create a deployment.yaml and services.yaml
  - deploy them.

 - Using helm:
 commands-
  - Create a helm chart by - helm create webapp(chart name)
  - Edit deployment.yaml, services.yaml, values.yaml as required
  - render the helm chart by - helm template webapp
  - install helm chart by - helm install chart-version chart-name
    
