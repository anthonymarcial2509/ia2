from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Simulador conectado con éxito"}

@app.post("/simular")
def ejecutar_simulacion(capital: int = 50, rondas: int = 200):
    df = simular(capital, rondas)
    return df.to_dict(orient="records")
