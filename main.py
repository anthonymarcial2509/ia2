from fastapi import FastAPI
from simulador import simular

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API del simulador de ruleta está activa"}

@app.post("/simular")
def ejecutar_simulacion(capital: int = 50, rondas: int = 200):
    df = simular(capital, rondas)
    return df.to_dict(orient="records")
