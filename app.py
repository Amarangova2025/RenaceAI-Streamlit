import streamlit as st
import joblib
import os

st.set_page_config(page_title="Renace AI - Detector Emocional", layout="centered")
st.title("💖 Renace AI - Tu Asistente Emocional")
st.subheader("Escribe lo que sientes y descubre tu emoción con una respuesta empática.")

modelo_path = "modelo_entrenado.pkl"

if not os.path.exists(modelo_path):
    st.error("🚫 No se encontró el modelo entrenado. Asegúrate de subir 'modelo_entrenado.pkl'.")
    st.stop()

modelo = joblib.load(modelo_path)

respuestas_empaticas = {
    "culpa": "Recuerda que mereces perdonarte. Todos estamos en proceso de crecimiento. 💛",
    "ansiedad": "Respira hondo. Estás haciendo lo mejor que puedes, un paso a la vez. 🌿",
    "tristeza": "No estás sola. Tus lágrimas son parte del proceso de sanación. 🤍",
    "confusión": "Tómate tu tiempo. La claridad llegará cuando estés lista. 🌈"
}

texto_usuario = st.text_area("✍️ Escribe aquí tu pensamiento o sentimiento:", height=150)

if st.button("🔍 Analizar emoción"):
    if texto_usuario.strip() == "":
        st.warning("Por favor, escribe algo antes de analizar.")
    else:# Transformar el texto con el vectorizer antes de predecir
        texto_vectorizado = vectorizer.transform([texto_usuario])
        emocion_detectada = modelo.predict(texto_vectorizado)[0]
        st.success(f"🧠 Emoción detectada: **{emocion_detectada.capitalize()}**")
        respuesta = respuestas_empaticas.get(emocion_detectada.lower(),
                    "Estamos aquí para ti. 💜 Cada emoción es válida y merece atención.")
        st.info(f"💬 Respuesta empática: {respuesta}")
