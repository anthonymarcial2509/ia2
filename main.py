from fastapi import FastAPI
from simulador import simular

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Simulador activo"}

@app.post("/simular")
def ejecutar_simulacion(capital: int = 50, rondas: int = 200):
    df = simular(capital, rondas)
    return df.to_dict(orient="records")
