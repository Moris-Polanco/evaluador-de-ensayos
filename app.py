import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def evaluar_ensayo(ensayo, tipo):
    # Obtener el número de párrafos en el ensayo
    num_parrafos = ensayo.count("\n")

    # Si el número de párrafos es menor a 5, mostrar un mensaje de error
    if num_parrafos < 5:
        st.error("El ensayo debe tener al menos 5 párrafos.")
        return

    # Si el número de párrafos es 5 o más, continuar con la evaluación del ensayo
    if tipo == "argumentativo":
        prompt = (f"Evaluar la calidad del ensayo argumentativo:\n{ensayo}\n\n"
                  "Criterios de evaluación: estructura, coherencia y argumentación. "
                  "Señalar los aspectos positivos y negativos y dar una calificación.")
    else:
        prompt = (f"Evaluar la calidad del ensayo expositivo:\n{ensayo}\n\n"
                  "Criterios de evaluación: claridad, precisión y coherencia. "
                  "Señalar los aspectos positivos y negativos y dar una calificación.")

    model_engine = "text-davinci-003"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
                                           temperature=0.5)
    respuesta = completions.choices[0].text

    # Devuelve la respuesta de GPT-3
    return respuesta

def main():
    st.title("Evaluador de ensayos con GPT-3")

    tipo = st.selectbox("Selecciona el tipo de ensayo", ["argumentativo", "expositivo"])
    ensayo = st.text_area("Ingresa el ensayo a evaluar. Al finalizar, Ctrl+Enter")
    if ensayo:
        respuesta = evaluar_ensayo(ensayo, tipo)
        st.markdown(respuesta)

if __name__ == "__main__":
  main()
