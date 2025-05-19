from ray import serve
from fastapi import FastAPI, Request
from app.inference import SentimentModel
from app.config import Settings

settings = Settings()
model = SentimentModel()
app = FastAPI()

@serve.deployment(route_prefix=settings.route_prefix)
@serve.ingress(app)
class ModelDeployment:
    @app.post("/")
    async def predict(self, request: Request):
        data = await request.json()
        text = data.get("text", "")
        return {"probabilities": model.predict(text)}