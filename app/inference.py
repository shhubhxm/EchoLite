import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class SentimentModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        self.model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")
        self.model.eval()

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        return torch.nn.functional.softmax(outputs.logits, dim=1).tolist()

# --- app/ray_serve_deployment.py ---
from ray import serve
from fastapi import FastAPI
from app.inference import SentimentModel

model = SentimentModel()
app = FastAPI()

@serve.deployment(route_prefix="/predict")
@serve.ingress(app)
class ModelDeployment:
    @app.post("/")
    async def predict(self, request: dict):
        text = request.get("text", "")
        return {"probabilities": model.predict(text)}

ModelDeployment.deploy()