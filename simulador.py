import random
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class RuletaIA:
    def __init__(self):
        self.historial = []
        self.modelo = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
        self.scaler = StandardScaler()
        self.entrenado = False

    def generar_resultado(self):
        colores = ['rojo']*18 + ['negro']*18 + ['verde']
        return {'color': random.choice(colores)}

    def preparar_datos(self):
        if len(self.historial) < 6:
            return None, None
        X, y = [], []
        for i in range(5, len(self.historial)):
            muestra = self.historial[i-5:i]
            colores = [1 if x['color'] == 'rojo' else -1 if x['color'] == 'negro' else 0 for x in muestra]
            X.append(colores)
            y.append(self.historial[i]['color'])
        return X, y

    def entrenar_modelo(self):
        X, y = self.preparar_datos()
        if X is None: return
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
        X_scaled = self.scaler.fit_transform(X_train)
        self.modelo.fit(X_scaled, y_train)
        self.entrenado = True

    def predecir(self):
        if not self.entrenado or len(self.historial) < 5:
            return random.choice(['rojo', 'negro'])
        muestra = self.historial[-5:]
        colores = [1 if x['color'] == 'rojo' else -1 if x['color'] == 'negro' else 0 for x in muestra]
        X_scaled = self.scaler.transform([colores])
        return self.modelo.predict(X_scaled)[0]

def estrategia_martingala(exito, estado):
    if exito:
        estado['apuesta'] = estado['apuesta_base']
        estado['racha'] = 0
    else:
        estado['racha'] += 1
        estado['apuesta'] *= 2
    return estado

def simular(capital_inicial=50, rondas=100):
    resultados = []
    ruleta = RuletaIA()
    capital = capital_inicial
    estado = {'apuesta_base': 2, 'apuesta': 2, 'racha': 0}
    for ronda in range(rondas):
        if capital <= 0:
            break
        if ronda % 50 == 0:
            ruleta.entrenar_modelo()
        pred = ruleta.predecir()
        res = ruleta.generar_resultado()
        ruleta.historial.append(res)
        exito = (pred == res['color'])
        capital += estado['apuesta'] if exito else -estado['apuesta']
        estado = estrategia_martingala(exito, estado)
        resultados.append({
            'ronda': ronda + 1,
            'prediccion': pred,
            'real': res['color'],
            'ganado': exito,
            'apuesta': estado['apuesta'],
            'capital': capital
        })
    return pd.DataFrame(resultados)
