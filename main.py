import streamlit as st
from simulador import simular

def mostrar_dashboard():
    st.title("🎰 Simulador de Ruleta con IA y Estrategias")
    capital = st.slider("Capital Inicial", min_value=10, max_value=500, value=50, step=10)
    rondas = st.slider("Número de Rondas", min_value=50, max_value=1000, value=200, step=50)

    if st.button("Iniciar Simulación"):
        df = simular(capital, rondas)
        st.success("¡Simulación completada!")

        st.subheader("📊 Resultados por Estrategia")
        for estrategia in df['estrategia'].unique():
            datos = df[df['estrategia'] == estrategia]
            st.write(f"### Estrategia: {estrategia}")
            st.line_chart(datos[['ronda', 'capital']].set_index('ronda'))

        st.subheader("📋 Opciones por Ronda")
        for estrategia in df['estrategia'].unique():
            datos = df[df['estrategia'] == estrategia][['ronda', 'prediccion', 'real', 'apuesta', 'capital']]
            st.write(f"### Estrategia: {estrategia}")
            st.dataframe(datos)

        st.subheader("🔎 Tabla Resumen")
        resumen = df.groupby('estrategia').agg(
            Inicial=("capital", "first"),
            Final=("capital", "last"),
            Aciertos=("ganado", "sum"),
            Promedio_Apuesta=("apuesta", "mean"),
            Porc_Acierto=("ganado", "mean"),
        )
        resumen["ROI (%)"] = (resumen["Final"] - resumen["Inicial"]) / resumen["Inicial"] * 100
        resumen["Porcentaje Acierto (%)"] = resumen.pop("Porc_Acierto") * 100
        st.dataframe(resumen)

if __name__ == "__main__":
    mostrar_dashboard()
