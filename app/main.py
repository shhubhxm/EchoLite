import ray
from app.ray_serve_deployment import ModelDeployment

ray.init()
serve.start()
ModelDeployment.deploy()